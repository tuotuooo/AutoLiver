import requests
import json
import configparser
import sys

def qiandaorequest(headers,game_uid,url,hdid,region):
    data = {
        "act_id": hdid,
        "region": region,
        "uid": game_uid,
        "lang": "zh-cn"
    }
    response1 = requests.post(url, headers=headers, data=json.dumps(data))
    data1 = response1.text
    parsed_data1 = json.loads(data1)
    try:
        if parsed_data1["data"]["gt"] == "":
            return data1
        else:
            challenge = parsed_data1['data']['challenge']
            headers['x-rpc-challenge'] = challenge
            response = requests.post(url, headers=headers, data=json.dumps(data))
            return response.text
    except:
        return data1

def main():
    game_uid = sys.argv[1]
    hdid = sys.argv[2]
    region = sys.argv[3]
    dh = sys.argv[4]
    url = sys.argv[5]
    config = configparser.ConfigParser()
    config.read('canshu.cfg',encoding='utf-8')
    login_ticket = config['cs']['login_ticket']
    ltoken = config['cs']['ltoken']
    cookie_token = config['cs']['cookie_token']
    mys_id = config['yx']['mys_id']

    headers = {
        'x-rpc-signgame': dh,
        'Cookie':
            'login_ticket=' + login_ticket + ';' + \
            'account_id=' + mys_id + ';' + \
            'ltoken=' + ltoken + ';' + \
            'cookie_token=' + cookie_token + ';'
    }
    print(qiandaorequest(headers,game_uid,url,hdid,region))

if __name__ == "__main__":
    main()
