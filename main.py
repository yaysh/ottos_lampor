
def loadIPAddress():
    f = open("ipaddress.txt", "r")
    line = f.read()
    return line.strip()


def main():
    ip_address = loadIPAddress()
    print(ip_address)
    

if __name__ == "__main__":
    main()