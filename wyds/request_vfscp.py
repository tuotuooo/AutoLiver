import requests
import json
import configparser
import subprocess

def requesturl(y):
    url = 'https://dl.reg.163.com/dl/wxdl/yd/vfscp'

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
    id = config['ini']['id']
    cap = config['check']['validate']
    ppp = config['phone']['num']
    xxx = '{"pd":"godlike_wyds_xcx","pkid":"VYoLaWc","pkht":"ds.163.com","channel":102,"id":"' +id+'","cap":"'+cap+'","un":"'+ppp+'"}'
    result = subprocess.run(['node', 'sm4jm.js', str(xxx)], capture_output=True, text=True)
    output = result.stdout
    # print(output)
    www = requesturl(output)
    www = json.loads(www)
    print(www)

if __name__ == "__main__":
    main()
