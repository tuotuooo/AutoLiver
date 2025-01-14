import requests
import json
import configparser
import subprocess
import ast

def requesturl(x, y, cb, ss):
    url = 'https://webzjcaptcha.reg.163.com/api/v2/mp/check'
    data = {
        'id': x,
        'extraData': '',
        'token': y,
        'type': 5,
        'version': '1.1.4',
        'cb': cb,
        'runEnv': 40,
        'width': 240,
        'data': json.dumps(ss)
    }

    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Host': 'webzjcaptcha.reg.163.com',
        'Referer': 'https://servicewechat.com/wx53eacbe0d8a7a95a/188/page-frame.html',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'cross-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090a13) XWEB/8555',
        'xweb_xhr': '1',
        'YD_ZONEID': 'CN31'
    }

    response = requests.post(url, data=data, headers=headers)
    return response.text

def main():
    config = configparser.ConfigParser()
    config.read('canshu.cfg', encoding='utf-8')
    account = config['ini']['capid']
    result1 = config['get']['token']
    result = subprocess.run(['node', 'mpext.js', str(result1)], capture_output=True, text=True).stdout.strip()
    result = ast.literal_eval(result)
    data11 = {"d":"","m":result[1],"p":result[2],"ext":result[3]}
    www = requesturl(account, result1, result[0], data11)
    www = json.loads(www)
    print(www)
    combo_token = www['data']['validate']
    config.set('check', 'validate', combo_token)
    with open('canshu.cfg', 'w') as configfile:
        config.write(configfile)

if __name__ == "__main__":
    main()
