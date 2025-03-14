import requests
import asyncio
import re
import random
import json
from ddddocr import DdddOcr
from datetime import datetime, timedelta, timezone
import hashlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
import configparser
import binascii


# 获取发送图标点选验证码所需的参数
def erf():
    headers = {
        "Referer": "https://www.kurobbs.com/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
    }
    url = 'https://gcaptcha4.geetest.com/load'
    params = {
        'captcha_id': 'ec4aa4174277d822d73f2442a165a2cd',
    }
    response = requests.get(url, headers=headers, params=params)
    data = response.text
    return data


# 筛选参数
def split_string(data):
    length = len(data)
    middle = length // 2
    first_half, second_half = data[:middle], data[middle + 1:] if length % 2 else data[middle:]
    lot_number_pattern = r'"lot_number":\s*"([^"]*)"'
    lot_number_match = re.search(lot_number_pattern, first_half)
    lot_number = lot_number_match.group(1) if lot_number_match else None

    target_image_pattern = r'"imgs":\s*"([^"]*)"'
    target_image_match = re.search(target_image_pattern, first_half)
    target_image = target_image_match.group(1) if target_image_match else None

    payload_pattern = r'"payload":\s*"([^"]*)"'
    payload_match = re.search(payload_pattern, data)  # payload 处于两部分之间
    payload = payload_match.group(1) if payload_match else None

    ques_list_pattern = r'"ques":\s*\[(.*?)\]'
    ques_list_match = re.search(ques_list_pattern, data)
    ques = ques_list_match.group(1).split(',') if ques_list_match else None

    process_token_pattern = r'"process_token":\s*"([^"]*)"'
    process_token_match = re.search(process_token_pattern, second_half)
    process_token = process_token_match.group(1) if process_token_match else None

    return lot_number, target_image, ques, payload, process_token


# 生成随机数
def generate_random_string():
    randomStr = ''
    for i in range(4):
        random_number = int(65536 * (1 + random.random()))
        hex_string = hex(random_number)[3:]
        randomStr += hex_string
    return randomStr


# 对生成的用户操作信息进行AES加密
def aesooo(qq, ww, ee, rr, tt, yy, sjs):
    data = {
        "setLeft": qq,
        "passtime": ww,
        "userresponse": ee,
        "device_id": "",
        "lot_number": rr,
        "pow_msg": tt,
        "pow_sign": yy,
        "geetest": "captcha",
        "lang": "zh",
        "ep": "123",
        "biht": "1426265548",
        "XX42": "F7RV",
        "em": {
            "ph": 0,
            "cp": 0,
            "ek": "11",
            "wd": 1,
            "nt": 0,
            "si": 0,
            "sc": 0
        }
    }
    plaintext = str(data).replace(" ", "").replace("'", '"')
    key = sjs.encode()
    iv = b'0000000000000000'
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_data = pad(plaintext.encode(), AES.block_size)
    ciphertext = cipher.encrypt(padded_data)
    return ciphertext.hex()


# 生成用户操作信息
async def huakuai(url1, url2):
    def generate_distance(slice_url, bg_url):
        slide = DdddOcr(det=False, ocr=False, show_ad=False)
        slice_image = requests.get(slice_url).content
        bg_image = requests.get(bg_url).content
        result = slide.slide_match(slice_image, bg_image, simple_target=True)
        return result['target'][0]

    def generate_track(distance):
        def __ease_out_expo(step):
            return 1 if step == 1 else 1 - pow(2, -10 * step)

        tracks = [[random.randint(20, 60), random.randint(10, 40), 0]]
        count = 30 + int(distance / 2)
        _x, _y = 0, 0
        for item in range(1, count + 1):
            x = round(__ease_out_expo(item / count) * distance)
            t = random.randint(10, 20)
            if x == _x:
                continue
            tracks.append([x - _x, _y, t])
            _x = x
        tracks.append([0, 0, random.randint(200, 300)])
        times = sum([track[2] for track in tracks])
        return tracks, times

    distance = generate_distance(url1, url2)
    tracks, total_time = generate_track(distance)
    return distance, total_time, distance / (0.8876 * 340 / 300)


# RSA加密AES的密钥
async def rsaooo(z):
    with open("1.pem", "rb") as key_file:
        pem_public_key = key_file.read()
    public_key = serialization.load_pem_public_key(pem_public_key)
    message_bytes = z.encode('utf-8')
    ciphertext = public_key.encrypt(
        message_bytes,
        padding.PKCS1v15()
    )
    hex_encoded = binascii.hexlify(ciphertext)
    return hex_encoded.decode('utf-8')


# 生成pow_msg  作为AES加密的原始材料
async def aes_time(x, u):
    offset = timedelta(hours=8)
    utc_8 = timezone(offset)
    now = datetime.now()
    now_utc_8 = now.replace(tzinfo=utc_8)
    timestamp = now_utc_8.isoformat()
    pow_msg = f"1|0|md5|{timestamp}|{u}|{x}||{generate_random_string()}"

    md5_object = hashlib.md5()
    md5_object.update(pow_msg.encode())
    encrypted_string = md5_object.hexdigest()

    return pow_msg, encrypted_string


# 拼接参数 异步控制函数
async def e(lot_number, slice_image, bg_image, captcha_id):
    url_a = 'https://static.geetest.com/'
    url_b = f'{url_a}{slice_image}'
    url_c = f'{url_a}{bg_image}'
    sjs = generate_random_string()
    tuo = [huakuai(url_b, url_c), rsaooo(sjs), aes_time(lot_number, captcha_id)]
    nnn = await asyncio.gather(*tuo)
    x = aesooo(nnn[0][0], nnn[0][1], nnn[0][2], lot_number, nnn[2][0], nnn[2][1], sjs)
    y = nnn[1]
    wer = x + y
    return wer


# 发送滑块验证码验证请求
def veve(vc, vx, vm):
    headers = {
        "Host": "gcaptcha4.geetest.com",
        "Referer": "https://www.kurobbs.com/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    }
    url = 'https://gcaptcha4.geetest.com/verify'
    params = {
        'captcha_id': vc,
        'lot_number': vx,
        'w': vm
    }
    response = requests.get(url, headers=headers, params=params)
    data = response.text
    return data


# 筛选参数
def veve_d(data):
    length = len(data)
    middle = length // 2
    first_half, second_half = data[:middle], data[middle + 1:] if length % 2 else data[middle:]
    captcha_output_pattern = r'"captcha_output":\s*"([^"]*)"'
    captcha_output_match = re.search(captcha_output_pattern, first_half)
    captcha_output = captcha_output_match.group(1) if captcha_output_match else None

    first_half, second_half = data[:middle], data[middle + 1:] if length % 2 else data[middle:]
    gen_time_pattern = r'"gen_time":\s*"([^"]*)"'
    gen_time_match = re.search(gen_time_pattern, first_half)
    gen_time = gen_time_match.group(1) if gen_time_match else None

    first_half, second_half = data[:middle], data[middle + 1:] if length % 2 else data[middle:]
    pass_token_pattern = r'"pass_token":\s*"([^"]*)"'
    pass_token_match = re.search(pass_token_pattern, first_half)
    pass_token = pass_token_match.group(1) if pass_token_match else None

    return captcha_output, gen_time, pass_token


# 发送登录请求
def last(phone, captcha_id, captcha_output, lot_number, gen_time, pass_token):
    url = 'https://api.kurobbs.com/user/getSmsCodeForH5'
    headers = {
        'Host': 'api.kurobbs.com',
        'Sec-Ch-Ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
        'Version': '2.2.0',
        'Source': 'h5',
        'Sec-Ch-Ua-Mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
        'Accept': 'application/json, text/plain, */*',
        'Sec-Ch-Ua-Platform': '"Windows"',
        'Origin': 'https://www.kurobbs.com',
        'Sec-Fetch-Site': 'same-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://www.kurobbs.com/',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
    }
    data = {
        'mobile': phone,
        'geeTestData': json.dumps({
            'captcha_id': captcha_id,
            'captcha_output': captcha_output,
            'lot_number': lot_number,
            'gen_time': gen_time,
            'pass_token': pass_token
        })
    }
    response = requests.post(url, headers=headers, data=data)
    return print(f"{response.text}")


def main():
    config = configparser.ConfigParser()
    config.read('kjq.cfg', encoding='utf-8')
    captcha_id = config['captcha']['captcha_id']
    phone = config['user']['phone']
    x = erf()
    y = split_string(x)
    csc = asyncio.run(e(y[0], y[1], y[2], captcha_id))
    dd = veve(captcha_id, y[0], csc)
    cxv = veve_d(dd)
    last(phone, captcha_id, cxv[0], y[0], cxv[1], cxv[2])


if __name__ == '__main__':
    main()
