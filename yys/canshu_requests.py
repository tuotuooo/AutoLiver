import requests
import configparser
import re
def login(x,y):
    url = 'https://passport-api.mihoyo.com/account/ma-cn-passport/web/loginByPassword'

    headers = {
        'Host': 'passport-api.mihoyo.com',
        'Sec-Ch-Ua': '"Chromium";v="124", "Microsoft Edge";v="124", "Not-A.Brand";v="99"',
        'X-Rpc-Device_model': 'Microsoft%20Edge%20124.0.0.0',
        'X-Rpc-Lifecycle_id': '3431892fb5',
        'X-Rpc-Device_os': 'Windows%2010%2064-bit',
        'X-Rpc-Sdk_version': '2.26.0',
        'X-Rpc-Device_name': 'Microsoft%20Edge',
        'X-Rpc-Device_fp': '38d7fa4137750',
        'X-Rpc-Client_type': '22',
        'Sec-Ch-Ua-Platform': '"Windows"',
        'X-Rpc-Game_biz': 'hk4e_cn',
        'Sec-Ch-Ua-Mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0',
        'Content-Type': 'application/json',
        'X-Rpc-Device_id': '003b5c8a-ae14-40c9-8b56-fa7d956d4802',
        'Accept': 'application/json, text/plain, /',
        'X-Rpc-Source': 'v2.webLogin',
        'X-Rpc-App_id': 'c76ync6mutq8'
    }

    data = {
        "account": x,
        "password": y
    }

    response = requests.post(url, headers=headers, json=data)
    data = response.headers['Set-Cookie']
    canshu = ['uni_web_token', 'cookie_token_v2', 'ltoken_v2', 'cookie_token', 'ltoken']
    cfg = {}
    for key in canshu:
        match = re.search(rf'{key}=([^;]+)', data)
        if match:
            cfg[key] = match.group(1)
    return cfg

def main():
    config = configparser.ConfigParser()
    config.read('cnm.cfg')
    account = config['credentials']['account']
    password = config['credentials']['password']
    q = login(account, password)
    for key, value in q.items():
        config.set('cs', key, value)
    with open('cnm.cfg', 'w') as configfile:
        config.write(configfile)


if __name__ == "__main__":
    main()
