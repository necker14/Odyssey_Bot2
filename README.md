这是Odyssey emby公益服社区的专用telegram机器人（已开发票房推送功能）
=================
*注：本机器人基于Python编写，需要用户自行配置Python3.7环境*

票房信息机器人使用指南：   

1.创建一个新的机器人，获取你创建好的机器人TOKEN，将机器人设为目标chat管理员。并通过@getidsbot机器人获取你的目标Chat_ID.

2.将源代码拉取到本地:

    git clone https://github.com/necker14/Odyssey_Bot2.git

3.安装依赖:

```pip install -r requirements.txt```

4.修改config.py进行配置，TOKEN 为 Bot 的 API:

```TOKEN = 'Your TOKEN'```

5.修改tt.py进行配置，odyssey_id为目标Chat_ID:

```odyssey_id = 'YOUR CHAT_ID'```

6.运行机器人：

```nohup /usr/bin/python3 /root/Odyssey_Bot2/src/tt.py &```

7.使用机器人(请把机器人私有化，切勿让他人使用)

向机器人输入指令:```/list_USA```,即可向目标Chat推送北美票房排行榜

向机器人输入指令:```/list_China```,即可向目标Chat推送大陆票房排行榜
