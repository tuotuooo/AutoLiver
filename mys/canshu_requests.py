import requests
import json
import configparser

def HQtokenAlogin_ticket(x,y):
    url = "https://passport-api.mihoyo.com/account/ma-cn-passport/app/loginByPassword"
    headers = {
        'Accept': 'application/json',
        'x-rpc-app_id': 'bll8iq97cem8',
        'x-rpc-client_type': '2',
        'x-rpc-device_id': '2892ab834db5dafc',
        'x-rpc-device_fp': '38d7f86f2c07e',
        'x-rpc-device_name': 'NX627J',
        'x-rpc-device_model': 'NX627J',
        'x-rpC-sys_version': '9',
        'x-rpc-game_biz': 'bbs_cn',
        'x-rpc-app_version': '2.69.1',
        'x-rpc-sdk_version': '2.20.2',
        'x-rpc-lifecycle_id': '829012ac-f4f1-4e3a-8309-456922e9252a',
        'x-rpc-account_version': '2.20.2',
        'Host': 'passport-api.mihoyo.com',
        'Accept-Encoding': 'gzip',
        'User-Agent': 'okhttp/4.9.3'
    }
    json_data = {
        "account": x,
        "password": y
    }

    response = requests.post(url, headers=headers, json=json_data)
    data = response.text
    parsed_data = json.loads(data)
    token = parsed_data['data']['token']['token']
    mid = parsed_data['data']['user_info']['mid']
    login_ticket = parsed_data['data']['login_ticket']
    return token,mid,login_ticket

def HQcookie_token(token,mid):
    url = "https://passport-api.mihoyo.com/account/auth/api/getCookieAccountInfoBySToken"
    url1 = 'https://passport-api.mihoyo.com/account/auth/api/getLTokenBySToken'
    headers = {
        'Accept': 'application/json',
        'x-rpc-app_id': 'bll8iq97cem8',
        'x-rpc-client_type': '2',
        'x-rpc-device_id': '2892ab834db5dafc',
        'x-rpc-device_fp': '38d7f86f2c07e',
        'x-rpc-device_name': 'NX627J',
        'x-rpc-device_model': 'NX627J',
        'x-rpc-sys_version': '9',
        'x-rpc-game_biz': 'bbs_cn',
        'x-rpc-app_version': '2.69.1',
        'x-rpc-sdk_version': '2.20.2',
        'x-rpc-lifecycle_id': '944d2d5e-a3f8-4bf3-ac39-53acac38b4ee',
        'x-rpc-account_version': '2.20.2',
        'Cookie': 'stoken=' + token + ';mid=' + mid,
        'Content-Type': 'application/json',
        'Host': 'passport-api.mihoyo.com',
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip',
        'User-Agent': 'okhttp/4.9.3'
    }

    response = requests.get(url, headers=headers)
    data = response.text
    parsed_data = json.loads(data)
    cookie_token = parsed_data['data']['cookie_token']
    response = requests.get(url1, headers=headers)
    data = response.text
    parsed_data = json.loads(data)
    ltoken = parsed_data['data']['ltoken']
    return cookie_token,ltoken

def main():
    canshu = {}
    config = configparser.ConfigParser()
    config.read('canshu.cfg')
    account = config['credentials']['account']
    password = config['credentials']['password']
    q = HQtokenAlogin_ticket(account,password)
    canshu['token'] = q[0]
    canshu['mid'] = q[1]
    canshu['login_ticket'] = q[2]
    w = HQcookie_token(q[0], q[1])
    canshu['cookie_token'] = w[0]
    canshu['ltoken'] = w[1]
    for key, value in canshu.items():
        config.set('cs', key, value)
    with open('canshu.cfg', 'w') as configfile:
        config.write(configfile)

if __name__ == "__main__":
    main()
