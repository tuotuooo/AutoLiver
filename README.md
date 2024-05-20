```
        GGGGGGGGGGGGG                                                       hhhhhhh               iiii                    
     GGG::::::::::::G                                                       h:::::h              i::::i                   
   GG:::::::::::::::G                                                       h:::::h               iiii                    
  G:::::GGGGGGGG::::G                                                       h:::::h                                       
 G:::::G       GGGGGG    eeeeeeeeeeee    nnnn  nnnnnnnn        ssssssssss    h::::h hhhhh       iiiiiii nnnn  nnnnnnnn
G:::::G                ee::::::::::::ee  n:::nn::::::::nn    ss::::::::::s   h::::hh:::::hhh    i:::::i n:::nn::::::::nn  
G:::::G               e::::::eeeee:::::een::::::::::::::nn ss:::::::::::::s  h::::::::::::::hh   i::::i n::::::::::::::nn 
G:::::G    GGGGGGGGGGe::::::e     e:::::enn:::::::::::::::ns::::::ssss:::::s h:::::::hhh::::::h  i::::i nn:::::::::::::::n
G:::::G    G::::::::Ge:::::::eeeee::::::e  n:::::nnnn:::::n s:::::s  ssssss  h::::::h   h::::::h i::::i   n:::::nnnn:::::n
G:::::G    GGGGG::::Ge:::::::::::::::::e   n::::n    n::::n   s::::::s       h:::::h     h:::::h i::::i   n::::n    n::::n
G:::::G        G::::Ge::::::eeeeeeeeeee    n::::n    n::::n      s::::::s    h:::::h     h:::::h i::::i   n::::n    n::::n
 G:::::G       G::::Ge:::::::e             n::::n    n::::nssssss   s:::::s  h:::::h     h:::::h i::::i   n::::n    n::::n
  G:::::GGGGGGGG::::Ge::::::::e            n::::n    n::::ns:::::ssss::::::s h:::::h     h:::::hi::::::i  n::::n    n::::n
   GG:::::::::::::::G e::::::::eeeeeeee    n::::n    n::::ns::::::::::::::s  h:::::h     h:::::hi::::::i  n::::n    n::::n
     GGG::::::GGG:::G  ee:::::::::::::e    n::::n    n::::n s:::::::::::ss   h:::::h     h:::::hi::::::i  n::::n    n::::n
        GGGGGG   GGGG    eeeeeeeeeeeeee    nnnnnn    nnnnnn  sssssssssss     hhhhhhh     hhhhhhhiiiiiiii  nnnnnn    nnnnn
```


## 🏪项目介绍
&emsp;&emsp;致`肝疼`的朋友🍻    

## 🏗️护肝宝典
- [x] 1. 米游社-游戏（原神、星穹轨道、崩坏3、未定事件薄）-每日签到奖励
- [x] 2. 云原神-游玩时长-每日签到奖励（15min）

## ☠️BUG
> `X-Rpc-Device_id`

- 此参数绑定的是登录设备的信息。即设备信息=`X-Rpc-Device_id`
- 此参数在程序启动时，已经生成完毕

| 生成原理 | 影响 |备注|
|:------:|:------:|:------:|
| UUID | 1and2 |🔓️绕过 |

> 绕过方法：登录`https://user.mihoyo.com/#/login/captcha`关闭在新设备登录时需短信验证功能
