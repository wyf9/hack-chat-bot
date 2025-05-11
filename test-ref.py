# 消息参考
from hvicorn import OnlineSetPackage, User, UncatchedPackage, ChatPackage

OnlineSetPackage(
    cmd='onlineSet',
    channel='kt1j8rpc',
    nicks=['awa_ya', 'wyf9', 'wyf9test'],
    time=1746951131205,
    users=[
        User(channel='kt1j8rpc', color='6a5eed', hash='LmZU1EIVlYpAomk', isBot=False, isme=False, level=100, nick='awa_ya', trip='mounge', uType='user', userid=5508803711310),
        User(channel='kt1j8rpc', color='ed655e', hash='hJyjlI9T9GTzOz5', isBot=False, isme=False, level=100, nick='wyf9', trip='', uType='user', userid=8721167322191),
        User(channel='kt1j8rpc', color='edbf5e', hash='7EjQkvszJ5jCZHH', isBot=False, isme=True, level=100, nick='wyf9test', trip='', uType='user', userid=6190830067142)
    ]
)

UncatchedPackage(
    rawjson={
        'cmd': 'session',
        'restored': False,
        'token': 'eyJhbGciOiJIUzxxxxxxxxxx',
        'channels': ['kt1j8rpc'],
        'time': 1746951131206
    }
)

ChatPackage(
    cmd='chat',
    channel='kt1j8rpc',
    color='ed655e',
    level=100,
    nick='wyf9',
    text=':thinking:',
    time=1746951154651,
    trip=None,
    uType='user',
    userid=8721167322191,
    customId=None
)
