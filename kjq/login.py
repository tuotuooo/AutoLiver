import configparser
import re
import requests

def eee(phone, code):
    url = "https://api.kurobbs.com/user/sdkLoginForH5"
    headers = {
        "Version": "2.2.0",
        "Source": "h5",
        "Sec-Ch-Ua-Mobile": "?0",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
        "Accept": "application/json, text/plain, */*",
        "Sec-Ch-Ua-Platform": "Windows",
        "Origin": "https://www.kurobbs.com",
        "Sec-Fetch-Site": "same-site",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://www.kurobbs.com/",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Priority": "u=1, i"
    }
    data = {
        "mobile": phone,
        "code": code
    }
    response = requests.post(url, headers=headers, data=data)
    weraw = str(response.headers)
    match = re.search(r'user_token=(.*?);', weraw)
    user_token = match.group(1)
    return user_token

def main():
    canshu = {}
    config = configparser.ConfigParser()
    config.read('kjq.cfg', encoding='utf-8')
    phone = config['user']['phone']
    code = config['user']['code']
    fdsf = eee(phone, code)
    canshu['token'] = fdsf
    for key, value in canshu.items():
        config.set('user', key, value)
    with open('kjq.cfg', 'w') as configfile:
        config.write(configfile)
      
if __name__ == '__main__':
    main()
