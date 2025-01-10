import requests
import json
import configparser
import subprocess

def requesturl(x, y):
    url = x

    data = {
        'encParams': y
    }

    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        'Host': 'dl.reg.163.com',
        'Referer': 'https://servicewechat.com/wx53eacbe0d8a7a95a/186/page-frame.html',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'cross-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090a13) XWEB/8555',
        'xweb_xhr': '1'
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))
    return response.text

def main():
    config = configparser.ConfigParser()
    config.read('canshu.cfg',encoding='utf-8')
    account = config['ini']['requestone']
    url = config['ini']['url']
    result = subprocess.run(['node', './js/jm.js', str(account)], capture_output=True, text=True)
    output = result.stdout
    www = requesturl(url, output)
    www = json.loads(www)
    combo_token = www['id']
    combo_token1 = www['capId']
    config.set('ini', 'id', combo_token)
    config.set('ini', 'capId', combo_token1)
    with open('canshu.cfg', 'w') as configfile:
        config.write(configfile)

if __name__ == "__main__":
    main()
