# hack-chat-bot

一个基于 [Hack.Chat](https://hack.chat) & [hvicorn](https://github.com/Hiyoteam/hvicorn) 制作的**轻量**聊天* (记录)* Bot!

## 功能

*+ hvicorn:*
- [x] 记录频道日志 & 聊天消息
- [x] 一次启动多个频道
- [ ] 进群自动打招呼

*+ requests:*
- [ ] Discord Webhook 推送新消息

*+ flask:*
- [ ] 网页查看聊天消息记录 *(比较简陋)*
- [ ] ~~聊天代理 (可发送消息 / 指定频道 / 查看历史记录)~~

## 使用

安装依赖:

```sh
pip install -r requirements.txt
```

进行配置: [`config.example.yaml`](./config.example.yaml)

启动:

```sh
python3 main.py
```

## 起因

<details>
<summary>点击展开</summary>

在考古某位 B 站 up 的视频时发现了一个野生聊天室 (点进去竟然还有人)!

但 hack.chat 不保存用户的聊天记录，导致我们看不见之前人发的消息，挺悲伤的（bushi

所以，我尝试寻找 hack.chat 的官方 github repo，并惊喜地发现它竟然有一众 [第三方 SDK](https://github.com/hack-chat/3rd-party-software-list)!!!

于是我飞速开了本地仓库，并在几个小时内做好了基础的记录功能，上传到 github，就有了你现在看到的这个 repo

</details>

<details>

<summary>Link</summary>

https://bilibili.com/video/BV1jb411v7pk (`BV1jb411v7pk`)

</details>

> [!TIP]
> 欢迎 Issue / PR~ <br/>
> **想催更? 欢迎访问 [此处](https://siiway.top/about/contact) 获取 *(团队)* 的联系方式** <br/>
> *可能大概应该也许不会有人的吧...*