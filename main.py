# coding: utf-8

# ===== import =====
# built-in
from time import sleep
from threading import Thread

# 3rd-party
import hvicorn
import yaml

# folder
from utils import Bot, log

# ===== init =====

with open('config.yaml', 'r', encoding='utf-8') as f:
    c: dict = yaml.safe_load(f)
    f.close()

# ----- patch to support custom server address -----

import hvicorn.bot.sync_client
import hvicorn.bot
hvicorn.bot.sync_client.WS_ADDRESS = c.get('server', 'wss://hack.chat/chat-ws')

# ===== functions =====


def run_bot(nick: str, channel: str, password: str | None = None):
    bot = Bot(
        nick=nick,
        channel=channel
    )
    bot.log(f'Starting bot as {nick} on {channel}')
    client = hvicorn.Bot(
        nick=nick,
        channel=channel,
        password=password
    )
    client.register_global_function(bot.global_listener)
    while True:
        try:
            client.run(ignore_self=False)
            client.join()
        except Exception as e:
            bot.log(f'Error: {e}, reconnecting in 5s...')
            sleep(5)

# ===== start =====
if __name__ == '__main__':
    try:
        threads: list[Thread] = []
        clients = c.get('clients', {})
        if not clients:
            log('Empty clients setting, exiting.')
            raise EnvironmentError
        for i in clients:
            th = Thread(target=run_bot, daemon=True, args=(
                i['nick'],
                i['channel'],
                i['password']
            ))
            th.start()
            threads.append(th)
            sleep(1)
        log('All Started!')
        while True:
            sleep(114514)
    except KeyboardInterrupt:
        log(f'Received ^C, quitting')
    except EnvironmentError:
        exit(1)
    except Exception as e:
        log(f'Main Error: {e}')
    finally:
        exit(0)
