import configparser
import requests
import datetime
import sys

def eee(gameId, serverId, roleId, userId, reqMonth, token):
    url = "https://api.kurobbs.com/encourage/signIn/v2"
    headers = {
      "Host": "api.kurobbs.com",
      "user-agent": "Mozilla/5.0 (Linux; Android 9; TAS-AL00 Build/PQ3A.190605.05081124; WV)AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.114 Safari/537.36Kuro/2.2.0 KuroGameBox/2.2.0",
      "devcode": "",
      "token": token,
      "content-type": "application/x-www-form-urlencoded",
      "origin": "https://web-static.kurobbs.com",
      "x-requested-with": "com.kurogame.kjq",
      "sec-fetch-site": "same-site",
      "sec-fetch-mode": "cors",
      "sec-fetch-dest": "empty",
      "accept-encoding": "gzip, deflate",
      "accept-language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
      "source": "android",
      "pragma": "no-cache",
      "cache-control": "no-cache"
    }
    data = {
        'gameId': gameId,
        'serverId': serverId,
        'roleId': roleId,
        'userId': userId,
        'reqMonth': reqMonth
    }
    response = requests.post(url, headers=headers, data=data)
    return response.text

def main():
    gameId = sys.argv[1]
    serverId = sys.argv[2]
    roleId = sys.argv[3]
    now = datetime.datetime.now()
    month = str(now.month).zfill(2)
    config = configparser.ConfigParser()
    config.read('kjq.cfg', encoding='utf-8')
    userId = config['user']['kjq_userId']
    token = config['user']['token']
    fdsf = eee(gameId, serverId, roleId, userId, month, token)
    print(fdsf)
if __name__ == '__main__':
    main()
