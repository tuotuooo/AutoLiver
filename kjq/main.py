import subprocess
import configparser


def zs():
    gameId = config['zs']['gameid']
    serverId = config['zs']['serverid']
    roleId = config['zs']['roleid']
    subprocess.call(["python", "zsqd.py", gameId, serverId,roleId])

def mc():
    gameId = config['zs']['gameidmc']
    serverId = config['zs']['serveridmc']
    roleId = config['zs']['roleidmc']
    subprocess.call(["python", "zsqd.py", gameId, serverId,roleId])

def main():
    print("战双签到中")
    zs()
    print("鸣潮签到中")
    mc()
if __name__ == "__main__":
    config = configparser.ConfigParser()
    config.read('kjq.cfg',encoding='utf-8')
    main()
