import requests
import hashlib
import json
from urllib.parse import urlparse
import time
import hmac
import configparser

'''
copy HaneRo大佬的代码并略加修改( •̀ ω •́ )y

https://github.com/HaneRo/skland_arknights_checkin
'''

config = configparser.ConfigParser()
config.read('skd.cfg', encoding='utf-8')
content = config['c']['content']

command_header = {
    "User-Agent": "Skland/1.5.1 (com.hypergryph.skland; build:100501001; Android 34; ) Okhttp/4.11.0",
    'Accept-Encoding': 'gzip',
    'Connection': 'close'
}

sign_header = {
    'platform': '1',
    'timestamp': '',
    'dId': '',
    'vName': '1.5.1'
}


def generate_signature(token, uri, data=None):
    timestamp = str(int(time.time()))
    headers = sign_header.copy()
    headers['timestamp'] = timestamp

    url_parts = urlparse(uri)
    path = url_parts.path
    query = url_parts.query

    data_str = json.dumps(data) if data else ''

    header_ca_str = json.dumps(headers, separators=(',', ':'))
    s = f"{path}{query}{data_str}{timestamp}{header_ca_str}"

    hex_s = hmac.new(token.encode('utf-8'), s.encode('utf-8'), hashlib.sha256).hexdigest()
    md5 = hashlib.md5(hex_s.encode('utf-8')).hexdigest().encode('utf-8').decode('utf-8')
    return md5, headers


def checkin(nickName, uid, gameId):
    url = "https://zonai.skland.com/api/v1/game/attendance"
    json = {
        "uid": uid,
        "gameId": gameId
    }
    sign, headers = generate_signature(token, url, json)
    headers = {**headers, 'sign': sign, 'cred': cred, 'Content-Type': 'application/json;charset=utf-8',
               **command_header}

    response = requests.post(url, headers=headers, json=json)
    test2 = response.json()
    print(test2)
    if response.json()['code'] == 0:
        for award in response.json().get('data', {}).get('awards', []):
            count = award.get('count', None)
            name = award.get('resource', {}).get('name', None)
            print(f'{nickName}签到成功，获得了{name}×{count}\n')
    else:
        print(f"{nickName}签到失败:", response.status_code, response.reason, f'{response.json()["message"]}')


def isCheckined(uid, gameId):
    url = f"https://zonai.skland.com/api/v1/game/attendance?gameId={gameId}&uid={uid}"
    sign, headers = generate_signature(token, url)
    headers = {**command_header, **headers, "sign": sign, "cred": cred}
    response = requests.get(url, headers=headers)
    # 检查"data"和"calendar"键是否存在，并获取"calendar"列表
    if "data" in response.json() and "calendar" in response.json()["data"]:
        calendar_list = response.json()["data"]["calendar"]

        # 遍历"calendar"列表，检查是否有"available"为True的项
        for item in calendar_list:
            if item.get("available", False):
                return True
        else:
            return False
    else:
        print("ERROR 未获取到签到记录")
        return False


def get_bindingList(cred, token):
    url = "https://zonai.skland.com/api/v1/game/player/binding"
    sign, headers = generate_signature(token, url)
    headers = {**command_header, **headers, "sign": sign, "cred": cred}
    response = requests.get(url, headers=headers)
    if response.json()['code'] == 0:
        for i in response.json()['data']['list']:
            if i['appCode'] == 'arknights':
                return i['bindingList']

    else:
        print(f"请求角色列表出现问题：{response.json()['message']}")
        if response.json()['message'] == '用户未登录':
            print(f'用户登录可能失效了，请更新cred！')


def get_code(token):
    url = "https://as.hypergryph.com/user/oauth2/v2/grant"

    data = {
        "appCode": '4ca99fa6b56cc2ba',
        "token": token,
        "type": 0
    }

    response = requests.post(url, headers=command_header, json=data)
    if response.json()['status'] == 0:
        return response.json()['data']['code']
    else:
        raise


def get_cred(code):
    url = "https://zonai.skland.com/api/v1/user/auth/generate_cred_by_code"

    data = {
        "code": code,
        "kind": 1
    }

    headers = {**command_header, "Content-Type": "application/json; charset=utf-8"}
    response = requests.post(url, headers=headers, json=data)
    if response.json()['code'] == 0:
        return response.json()['data']['cred'], response.json()['data']['token']
    else:
        raise


code = get_code(content)
cred, token = get_cred(code)
bindingList = get_bindingList(cred, token)
for i in bindingList:
    if isCheckined(i["uid"], i["channelMasterId"]):
        checkin(i["nickName"], i["uid"], i["channelMasterId"])
    else:
        print(f'{i["nickName"]}已签到')
