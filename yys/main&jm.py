import hmac
import hashlib
import configparser
import requests

def generate_hmac_sha256(x,uid):
    ey = "d0d3a7342df2026a70f650b907800111"
    key = bytes(ey, 'utf-8')
    message = "app_id=4&channel_id=1&combo_token=" + x + "&open_id=" + uid
    message = bytes(message, 'utf-8')
    hmac_obj = hmac.new(key, message, hashlib.sha256)
    hmac_digest = hmac_obj.digest()
    return hmac_digest.hex()

def request(uid,x,y):
    url = 'https://api-cloudgame.mihoyo.com/hk4e_cg_cn/wallet/wallet/get'

    headers = {
        'X-Rpc-Combo_token': 'ai=4;ci=1;oi='+uid+';ct='+x+';si='+y+';bi=hk4e_cn'
    }
    response = requests.get(url, headers=headers)
    data = response.text
    return data

def main():
    config = configparser.ConfigParser()
    config.read('cnm.cfg')
    x = config['cs']['combo_token']
    uid = config['yx']['uid']
    y = generate_hmac_sha256(x,uid)
    print(request(uid,x,y))
if __name__ == "__main__":
    main()