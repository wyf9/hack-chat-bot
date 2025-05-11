# coding: utf-8

from datetime import datetime
import hvicorn
from json import dumps


def log(*log: str):
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] [main] ", *log)


class Bot:
    nick: str
    channel: str

    def __init__(self, nick: str, channel: str):
        self.nick = nick
        self.channel = channel

    def log(self, *log: str):
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] [{self.nick}@{self.channel}]", *log)

    def write(self, log: str):
        try:
            now = datetime.now()
            with open(f'logs/{self.nick}@{self.channel}@{now.year}-{now.month}-{now.day}.log', 'a+', encoding='utf-8') as f:
                f.write(f'[{now.strftime("%Y-%m-%d %H:%M:%S")}] {log}\n')
                f.close()
        except Exception as e:
            self.log(f'Writing log error: {e}')

    def global_listener(self, *params):
        for i in params:
            if isinstance(i, hvicorn.ChatPackage):
                Type = 'CHAT'
                Log = f"{f'<{i.trip}> ' if i.trip else ''}{i.nick}{f' [{i.customId}]' if i.customId else ''} ({i.userid}):\n{i.text}"
            elif isinstance(i, hvicorn.OnlineSetPackage):
                Type = 'ONLINE'
                Log = f'Online Count: {len(i.nicks)}\nUsers: {", ".join(i.nicks)}'
            elif isinstance(i, hvicorn.UncatchedPackage):
                if i.rawjson.get('token'):
                    return
                Type = 'RAW'
                Log = dumps(i.rawjson, ensure_ascii=False)
            else:
                Type = 'OTHERS'
                Log = f'{type(i)} {i}'
        self.log(f'({Type})\n{Log}')
        self.write(f'({Type})\n{Log}')
