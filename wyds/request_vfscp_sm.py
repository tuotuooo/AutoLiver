import requests
import json
import configparser
import subprocess

def requesturl(x, y):
    url = x

    data = json.dumps({
        'encParams': y
    })

    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        'Host': 'dl.reg.163.com',
        'Referer': 'https://servicewechat.com/wx53eacbe0d8a7a95a/188/page-frame.html',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'cross-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090a13) XWEB/8555',
        'xweb_xhr': '1'
    }

    response = requests.post(url, headers=headers, data=data)
    return response.text

def main():
    x = 'https://dl.reg.163.com/dl/wxdl/yd/vfscp'
    w = 'https://dl.reg.163.com/dl/wxdl/dlzc/yd/sms/sm'
    config = configparser.ConfigParser()
    config.read('canshu.cfg',encoding='utf-8')
    id = config['ini']['id']
    cap = config['check']['validate']
    ppp = config['phone']['num']
    result = subprocess.run(['node', 'CN31_.js', str(cap)], capture_output=True, text=True)
    cap = result.stdout.replace("\n", "")
    xxx = '{"pd":"godlike_wyds_xcx","pkid":"VYoLaWc","pkht":"ds.163.com","channel":102,"id":"' +id+'","cap":"'+cap+'","un":"'+ppp+'"}'
    result = subprocess.run(['node', 'sm4jm.js', str(xxx)], capture_output=True, text=True)
    output2 = result.stdout.replace("\n", "")
    r = requesturl(x, output2)
    sss = '{"pd":"godlike_wyds_xcx","pkid":"VYoLaWc","pkht":"ds.163.com","channel":102,"id":"' + id + '","un":"' + ppp + '"}'
    result = subprocess.run(['node', 'sm4jm.js', str(sss)], capture_output=True, text=True)
    output = result.stdout.replace("\n", "")
    f = requesturl(w, output)
    print(f)
if __name__ == "__main__":
    main()
