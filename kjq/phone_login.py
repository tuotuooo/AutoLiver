import configparser
import json
import random
import requests

def eee(phone, code, hex_string):
    url = "https://api.kurobbs.com/user/sdkLogin"
    headers = {
        "Host": "api.kurobbs.com",
        "osversion": "Android",
        "countrycode": "CN",
        "model": "TAS-AL00",
        "source": "android",
        "lang": "zh-Hans",
        "version": "2.2.0",
        "versioncode": "2200",
        "channelid": "2",
        "content-type": "application/x-www-form-urlencoded",
        "accept-encoding": "gzip",
        "user-agent": "okhttp/3.11.0"
    }
    data = {
        "mobile": phone,
        "code": code,
        "devCode": hex_string
    }
    response = requests.post(url, headers=headers, data=data)
    weraw = response.text
    parsed_data = json.loads(weraw)
    token = parsed_data['data']['token']
    return token

def main():
    canshu = {}
    config = configparser.ConfigParser()
    config.read('kjq.cfg', encoding='utf-8')
    phone = config['user']['phone']
    code = config['user']['code']
    characters = '0123456789ABCDEF'
    hex_string = ''.join(random.choice(characters) for _ in range(40))
    fdsf = eee(phone, code, hex_string)
    print(fdsf)
    canshu['token'] = fdsf
    for key, value in canshu.items():
        config.set('user', key, value)
    with open('kjq.cfg', 'w') as configfile:
        config.write(configfile)

if __name__ == '__main__':
    main()
