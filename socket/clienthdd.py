import socket
import psutil 

dsk = psutil.disk_usage('/')
F = dsk.free   #Fに空き容量を代入
FM = F/1000000 #1000000で割ってmbの値にして代入

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.connect(('192.168.0.57', 50007))
    #メッセージ
    s.sendall(b'Sensor Connected')
    data = s.recv(1024)
    print(repr(data))
    print("空き容量(mb)", +FM)
