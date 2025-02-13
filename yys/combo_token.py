import requests
import json
import configparser


def login(uni_web_token,cookie_token_v2,mid,uid,ltoken_v2,cookie_token,ltoken):
    url = 'https://hk4e-sdk.mihoyo.com/hk4e_cn/combo/granter/login/webLogin'

    headers = {
        'Host': 'hk4e-sdk.mihoyo.com',
        'Cookie': 'uni_web_token='+uni_web_token+'; cookie_token_v2='+cookie_token_v2+'; account_mid_v2='+mid+'; account_id_v2='+uid+'; ltoken_v2='+ltoken_v2+'; ltmid_v2='+mid+'; ltuid_v2='+uid+'; cookie_token='+cookie_token+'; account_id='+uid+'; ltoken='+ltoken+'; ltuid='+uid,
        'Sec-Ch-Ua': '"Chromium";v="124", "Microsoft Edge";v="124", "Not-A.Brand";v="99"',
        'X-Rpc-Device_model': 'Microsoft%20Edge%20124.0.0.0',
        'X-Rpc-Channel_id': '1',
        'X-Rpc-Device_os': 'Windows%2010%2064-bit',
        'X-Rpc-Mdk_version': '2.24.0',
        'X-Rpc-Device_name': 'Microsoft%20Edge',
        'X-Rpc-Device_fp': '38d7fa4137750',
        'X-Rpc-Client_type': '22',
        'Sec-Ch-Ua-Platform': '"Windows"',
        'X-Rpc-Language': 'zh-cn',
        'X-Rpc-Game_biz': 'hk4e_cn',
        'Sec-Ch-Ua-Mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0',
        'X-Rpc-Device_id': '003b5c8a-ae14-40c9-8b56-fa7d956d4802',
        'Content-Type': 'application/json',
        'Accept': 'application/json, text/plain, */*',
        'Origin': 'https://ys.mihoyo.com',
        'Sec-Fetch-Site': 'same-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://ys.mihoyo.com/',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Priority': 'u=1, i',
        'Connection': 'close'
    }

    data = {"app_id": 4, "channel_id": 1}

    response = requests.post(url, headers=headers, json=data)
    data = response.text
    response_data = json.loads(data)
    combo_token = response_data['data']['combo_token']
    return combo_token

def main():
    config = configparser.ConfigParser()
    config.read('cnm.cfg',encoding='utf-8')
    uni_web_token = config['cs']['uni_web_token']
    cookie_token_v2 = config['cs']['cookie_token_v2']
    ltoken_v2 = config['cs']['ltoken_v2']
    cookie_token = config['cs']['cookie_token']
    ltoken = config['cs']['ltoken']
    mid = config['cs']['account_mid_v2']
    uid = config['yx']['uid']
    y = 'combo_token'
    x = login(uni_web_token, cookie_token_v2, mid, uid, ltoken_v2, cookie_token, ltoken)
    config.set('cs', y, x)
    with open('cnm.cfg', 'w') as configfile:
        config.write(configfile)
if __name__ == "__main__":
    main()
