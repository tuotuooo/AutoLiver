> [!Important]
> 🈲使用此项目进行任何违法违规活动。
> 
> It is prohibited to use this project for any illegal activities.

## Introduction
致"肝疼"的朋友🍻

To friends with liver pain🍻

`(,,´•ω•)ノ"(´っω•｀。)`

## Function
- [x] 1. 米游社-游戏（原神、星穹轨道、崩坏3、未定事件薄、绝区零）-每日签到奖励
- [x] 2. 云原神-游玩时长-每日签到奖励
- [x] 3. 云绝区零-游玩时长-每日签到奖励
- [x] 4. 库街区-游戏（鸣潮、战双帕弥什）-每日签到奖励
- [ ] 5. 网易大神-游戏-每日签到奖励
      
## BUG
> `X-Rpc-Device_id`

参数介绍：用UUID与用户的设备信息绑定；影响`1` `2` `3`

绕过方法：登录`https://user.mihoyo.com/#/login/captcha`关闭`在新设备登录时需短信验证`功能

## Deployments
> `yys`

^(*￣(oo)￣)^：食用前请先查阅BUG

cnm.cfg：配置文件需要填写的参数介绍如下

|account|password|uid|
| :----:  | :----:  | :----:  |
|账号|密码|米游社的UID|

脚本运行顺序如下，依次执行

1. jm.py 用于加密账号和密码
2. canshu_requests.py 发送加密后的账号密码获取参数1
3. combo_token.py 发送参数1到服务器获取参数2
4. main&jm.py 对参数2进行签名等处理再发送到服务器完成签到

> `yjql`

^(*￣(oo)￣)^：食用前请先查阅BUG

cnm.cfg：配置文件需要填写的参数介绍如下

|account|password|uid|
| :----:  | :----:  | :----:  |
|账号|密码|米游社的UID|

脚本运行顺序如下，依次执行

1. jm.py 用于加密账号和密码
2. canshu_requests.py 发送加密后的账号密码获取参数1
3. combo_token.py 对参数1进行签名等处理再发送到服务器获取参数2
4. main&jm.py 对参数2进行签名等处理再发送到服务器完成签到
