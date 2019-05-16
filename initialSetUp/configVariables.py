import socket

class initialSetUp:
    def __init__(self):
        self.ui_IP_Address = '192.168.11.5'
        self.raspberryPiAddr = '192.168.11.252'

def my_IpAddress():
    return((([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")] or [[(s.connect(("8.8.8.8", 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]]) + ["no IP found"])[0])

