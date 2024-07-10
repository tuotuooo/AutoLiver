import requests
import configparser
import json

def e(x,y):
    url = 'https://as.hypergryph.com/user/auth/v1/token_by_phone_password'

    headers = {
        'Content-Type': 'application/json;charset=UTF-8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'
    }
    data = {
        'phone': x,
        'password': y
    }

    response = requests.post(url, headers=headers, json=data)
    response_json = json.loads(response.text)
    data = response_json['data']['token']
    return data

def main():
    config = configparser.ConfigParser()
    config.read('skd.cfg',encoding='utf-8')
    phone = config['q']['phone']
    password = config['q']['password']
    x = e(phone,password)
    config.set('c', 'content', x)
    with open('skd.cfg', 'w') as configfile:
        config.write(configfile)

if __name__ == "__main__":
    main()
