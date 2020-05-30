import os


def loadIPAddress():
    f = open(os.path.abspath('../') + "/app/static/ipaddress.txt", "r")
    line = f.read()
    return str(line.strip())


def start():
    ip_address = loadIPAddress()
    print(ip_address)
    

if __name__ == "__main__":
    start()