import requests
import socket

# 此处填写用户名，必须在引号内填写
# 例如 
# user = "2018" 
user = ""
# 此处填写密码，必须在引号内填写
# 例如
# password = "mima"
password = ""

def getSession():
    import json
    s = requests.Session()
    redirectUrl = "http://10.16.0.21:80/?usermac="+getWinMac()+"&userip="+getIp()+"&nasip=10.100.0.1"
    data =  json.load(open("up.txt"))
    data.update({"redirectUrl": redirectUrl})
    
    s.headers.update({"Content-type": "application/json", "Host": "10.16.0.21"})
    resp = s.post("http://10.16.0.21/portal/api/v2/online", json=data)
    print(resp.status_code)    

def getWinMac():
    import subprocess
    for line in subprocess.check_output("getmac").decode().split("\r\n"):
        if "Device" in line:
            return line[:17]

def getIp():
    import socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    s.close()
    return ip
        

if __name__ == "__main__":
    getSession()
    import os
    os.system("pause")
