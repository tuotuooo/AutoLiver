import requests
import json
import configparser
import subprocess

def requesturl(x, y):
    url = 'https://webzjcaptcha.reg.163.com/api/v2/mp/get'
    params = {
        'id': y,
        'https': 'true', # 暂时固定
        'type': '', # 暂时固定
        'version': '1.1.4', # 暂时固定
        'drp': '1', # 暂时固定
        'dev': '2', # 暂时固定
        'cb': x,
        'width': '240', # 暂时固定
        'runEnv': '40' # 暂时固定
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

    response = requests.get(url, params=params, headers=headers)
    return response.text

def main():
    config = configparser.ConfigParser()
    config.read('canshu.cfg', encoding='utf-8')
    account = config['ini']['capid']
    result = subprocess.run(['node', './js/1111.js'], capture_output=True, text=True).stdout.strip()
    www = requesturl(result, account)
    www = json.loads(www)
    combo_token = www['data']['token']
    config.set('get', 'token', combo_token)
    with open('canshu.cfg', 'w') as configfile:
        config.write(configfile)

if __name__ == "__main__":
    main()
