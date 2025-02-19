import requests
import json
import configparser
import hmac
import hashlib

def generate_hmac_sha256(message: str, secret_key: str) -> str:
    """
    生成HMAC-SHA256签名
    :param message: 需要签名的消息（字符串）
    :param secret_key: 密钥（字符串）
    :return: HMAC-SHA256签名（十六进制字符串）
    """
    # 将密钥和消息转换为字节类型
    secret_key_bytes = secret_key.encode('utf-8')
    message_bytes = message.encode('utf-8')

    # 使用HMAC和SHA256算法生成签名
    hmac_signature = hmac.new(secret_key_bytes, message_bytes, hashlib.sha256).hexdigest()
    return hmac_signature

def login(i, t, ii):
    url = 'https://nap-sdk.mihoyo.com/nap_cn/combo/granter/login/v2/login'

    ssss = 'app_id=12&channel_id=1&data={"uid":"'+i+'","token":"'+t+'","guest":false,"is_new_register":false}&device='+ii
    # 密钥
    secret_key = "8844b676f3268c082a56021d9f47a206"

    # 示例消息（可以根据需要替换）
    message = ssss

    # 生成HMAC-SHA256签名
    hmac_signature = generate_hmac_sha256(message, secret_key)

    headers = {
        "Accept-Encoding": "gzip",
        "x-rpc-channel_version": "2.31.12",
        "x-rpc-combo_version": "2.31.12",
        "x-rpc-mdk_version": "2.31.12",
        "x-rpc-game_biz": "nap_cn",
        "x-rpc-account_version": "2.31.0",
        "x-rpc-channel_id": "1",
        "x-rpc-payment_version": "2.31.1",
        "x-rpc-sys_version": "9",
        "x-rpc-client_type": "8",
        "x-rpc-language": "zh-cn",
        "x-rpc-device_model": "LIO-AN00",
        "x-rpc-device_name": "LIO-AN00",
        "Content-Type": "application/json;charset=UTF-8",
        "Host": "nap-sdk.mihoyo.com",
        "Connection": "Keep-Alive",
        "User-Agent": "okhttp/4.10.0"
    }
    t = t.replace('=', '\\u003d')
    x0 = r'{"data":"{\"uid\":\"'
    x1 = r'\",\"token\":\"'
    x2 = r'\",\"guest\":false,\"is_new_register\":false}","sign":"'
    x3 = r'","app_id":12,"channel_id":1,"device":"'
    x4 = r'"}'
    x5 = x0 + i + x1 + t + x2 + hmac_signature + x3 + ii + x4
    print(x5)
    response = requests.post(url, headers=headers, data=x5)
    data1 = response.text
    response_data = json.loads(data1)
    print(data1)
    combo_token = response_data['data']['combo_token']
    return combo_token

def main():
    config = configparser.ConfigParser()
    config.read('cnm.cfg',encoding='utf-8')
    ltoken = config['cs']['token']
    uid = config['yx']['uid']
    y = 'combo_token'
    fefe = config['credentials']['id']
    x = login(uid, ltoken, fefe)
    config.set('cs', y, x)
    with open('cnm.cfg', 'w') as configfile:
        config.write(configfile)
if __name__ == "__main__":
    main()
