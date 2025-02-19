import hmac
import hashlib
import configparser
import requests


def generate_hmac_sha256(x,uid):
    ey = "8844b676f3268c082a56021d9f47a206"
    key = bytes(ey, 'utf-8')
    message = "app_id=12&channel_id=1&combo_token=" + x + "&open_id=" + uid
    message = bytes(message, 'utf-8')
    hmac_obj = hmac.new(key, message, hashlib.sha256)
    hmac_digest = hmac_obj.digest()
    return hmac_digest.hex()

def request(uid,x,y):
    url = 'https://cg-nap-api.mihoyo.com/nap_cn/cg/wallet/wallet/get?cost_method=0'

    headers = {
        'x-rpc-combo_token': 'ai=12;ci=1;oi='+uid+';ct='+x+';si='+y+';bi=nap_cn'
    }
    print(headers)
    response = requests.get(url, headers=headers)
    data = response.text
    return data


def main():
    config = configparser.ConfigParser()
    config.read('cnm.cfg',encoding='utf-8')
    x = config['cs']['combo_token']
    uid = config['yx']['uid']
    y = generate_hmac_sha256(x,uid)
    print(request(uid,x,y))
if __name__ == "__main__":
    main()
