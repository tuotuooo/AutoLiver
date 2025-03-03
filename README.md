> [!Important]
> 禁止使用此项目进行任何违法违规活动，本项目仅供学习用途。
> 
> It is strictly prohibited to use this project for any illegal or non-compliant activities. This project is solely for learning purposes.

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

> [!Note]
> 目前仅支持国内官服
> 
> 以下为首次执行过程，后续只需执行最终的签到请求即可

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

> `kjq`

^(*￣(oo)￣)^：安心食用

kjq.cfg：配置文件需要填写的参数介绍如下

|phone|code|kjq_userid|roleid|roleidmc|
| :----:  | :----:  | :----:  | :----:  | :----:  |
|手机号|短信验证码|库街区的UID|战双ID|鸣潮ID|

脚本运行顺序如下，依次执行

1. dxyzm.py 用于获取短信验证码，填入kjq.cfg
2. phone_login.py 获取token
3. main.py 控制签到，默认发送战双和鸣潮的签到请求；若不需要同时签到所有，可以注释掉对应的函数

> `mys`

^(*￣(oo)￣)^：食用前请先查阅BUG

canshu.cfg：配置文件需要填写的参数介绍如下

|account|password|mys_id|ys_uid|xqgd_uid|bh3_uid|wdsjb_uid|zzz_uid|
| :----:  | :----:  | :----:  | :----:  | :----:  | :----:  | :----:  | :----:  |
|账号|密码|米游社的UID|原神UID|星穹轨道UID|崩坏3的UID|未来事件薄的UID|绝区零的UID|

脚本运行顺序如下，依次执行

1. jm.py 用于加密账号和密码
2. canshu_requests.py 发送加密后的账号密码获取参数1
3. main.py 控制签到，默认发送原神、星穹轨道、崩坏3、未来事件薄、绝区零的签到请求；若不需要同时签到所有，可以注释掉对应的函数

