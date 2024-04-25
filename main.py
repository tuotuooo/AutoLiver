import subprocess
import configparser

def xqgd():
    arg1 = config['yx']['xqgd_uid']
    arg2 = config['yx']['xqgd-hdid']
    arg3 = config['yx']['xqgd-region']
    arg4 = ""
    subprocess.call(["python", "qd_requests.py", arg1, arg2,arg3,arg4])

def ys():
    arg1 = config['yx']['ys_uid']
    arg2 = config['yx']['ys-hdid']
    arg3 = config['yx']['ys-region']
    arg4 = config['yx']['dh']
    subprocess.call(["python", "qd_requests.py", arg1, arg2,arg3,arg4])

def bh3():
    arg1 = config['yx']['bh3_uid']
    arg2 = config['yx']['bh3-hdid']
    arg3 = config['yx']['bh3-region']
    arg4 = ""
    subprocess.call(["python", "qd_requests.py", arg1, arg2,arg3,arg4])

def wdsjb():
    arg1 = config['yx']['wdsjb_uid']
    arg2 = config['yx']['wdsjb-hdid']
    arg3 = config['yx']['wdsjb-region']
    arg4 = ""
    subprocess.call(["python", "qd_requests.py", arg1, arg2,arg3,arg4])

def main():
    print("原神签到中")
    ys()
    print("星穹轨道签到中")
    xqgd()
    print("崩坏3签到中")
    bh3()
    print("未定事件薄签到中")
    wdsjb()
if __name__ == "__main__":
    config = configparser.ConfigParser()
    config.read('canshu.cfg')
    main()