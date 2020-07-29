import socket
import subprocess

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(('192.168.0.57', 50007))#IPアドレス
    s.listen(1)
    while True:
        conn, addr = s.accept()
        with conn:
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                print('data : {}, addr: {}'.format(data, addr))
                KK = subprocess.check_output( ["i2cdetect", "-y", "1" ] ) 
                KS = KK == b'     0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f\n00:          -- -- -- -- -- -- -- -- -- -- -- -- -- \n10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- \n20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- \n30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- \n40: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- \n50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- \n60: -- -- -- -- -- -- -- -- 68 -- -- -- -- -- -- -- \n70: -- -- -- -- -- -- -- --                         \n'
                if KS == False:
                    conn.sendall(b'Received: ')#パイソンに返す部分
                else:
                    conn.sendall(b'Received: ' + data)#接続されているときの
