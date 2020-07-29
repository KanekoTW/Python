import socket


with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.connect(('192.168.0.57', 50007))
    #メッセージ
    s.sendall(b'Sensor Connected')
    data = s.recv(1024)
    print(repr(data))
