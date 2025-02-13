import subprocess
import configparser


def xqgd():
    arg1 = config['yx']['xqgd_uid']
    arg2 = config['yx']['xqgd-hdid']
    arg3 = config['yx']['xqgd-region']
    arg4 = ""
    arg5 = config['api']['url']
    subprocess.call(["python", "qd_requests.py", arg1, arg2,arg3,arg4,arg5])

def ys():
    arg1 = config['yx']['ys_uid']
    arg2 = config['yx']['ys-hdid']
    arg3 = config['yx']['ys-region']
    arg4 = config['yx']['dh']
    arg5 = config['api']['url']
    subprocess.call(["python", "qd_requests.py", arg1, arg2,arg3,arg4,arg5])

def bh3():
    arg1 = config['yx']['bh3_uid']
    arg2 = config['yx']['bh3-hdid']
    arg3 = config['yx']['bh3-region']
    arg4 = ""
    arg5 = config['api']['url']
    subprocess.call(["python", "qd_requests.py", arg1, arg2,arg3,arg4,arg5])

def wdsjb():
    arg1 = config['yx']['wdsjb_uid']
    arg2 = config['yx']['wdsjb-hdid']
    arg3 = config['yx']['wdsjb-region']
    arg4 = ""
    arg5 = config['api']['url']
    subprocess.call(["python", "qd_requests.py", arg1, arg2,arg3,arg4,arg5])

def jql():
    arg1 = config['yx']['zzz_uid']
    arg2 = config['yx']['zzz-hdid']
    arg3 = config['yx']['zzz-region']
    arg4 = config['yx']['dh-zzz']
    arg5 = config['api']['url-zzz']
    subprocess.call(["python", "qd_requests.py", arg1, arg2,arg3,arg4,arg5])

def main():
    print("原神签到中")
    ys()
    print("星穹轨道签到中")
    xqgd()
    print("崩坏3签到中")
    bh3()
    print("未定事件薄签到中")
    wdsjb()
    print("绝区零签到中")
    jql()
if __name__ == "__main__":
    config = configparser.ConfigParser()
    config.read('canshu.cfg',encoding='utf-8')
    main()
