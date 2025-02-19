import requests
import json
import configparser


def HQtokenAlogin_ticket(x,y,u):
    url = "https://passport-api.mihoyo.com/account/ma-cn-passport/app/loginByPassword"
    headers = {
        "Accept": "application/json",
        "x-rpc-app_id": "d47umitaylmo",
        "x-rpc-client_type": "8",
        "x-rpc-device_id": u,
        "x-rpc-device_name": "LI0-AN00",
        "x-rpc-device_model": "LIO-AN00",
        "x-rpc-sys_version": "9",
        "x-rpc-game_biz": "nap_cn",
        "x-rpc-app_version": "1.5.0",
        "x-rpc-sdk version": "2.31.0",
        "x-rpc-account_version": "2.31.0",
        "x-rpc-aigis": "",
        "Content-Type": "application/json",
        "Host": "passport-api.mihoyo.com",
        "Connection": "Keep-Alive",
        "Accept-Encoding": "gzip",
        "User-Agent": "okhttp/4.10.0"
    }
    json_data = {
        "account": x,
        "password": y
    }

    response = requests.post(url, headers=headers, json=json_data)
    data = response.text
    print(data)
    parsed_data = json.loads(data)
    token = parsed_data['data']['token']['token']
    mid = parsed_data['data']['user_info']['mid']
    return token,mid

def main():
    canshu = {}
    config = configparser.ConfigParser()
    config.read('cnm.cfg',encoding='utf-8')
    account = config['credentials']['account']
    password = config['credentials']['password']
    ttt = config['credentials']['id']
    q = HQtokenAlogin_ticket(account,password,ttt)
    canshu['token'] = q[0]
    canshu['mid'] = q[1]
    for key, value in canshu.items():
        config.set('cs', key, value)
    with open('cnm.cfg', 'w') as configfile:
        config.write(configfile)

if __name__ == "__main__":
    main()
