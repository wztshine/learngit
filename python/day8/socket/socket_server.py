import socket
import os
import hashlib
import threading

def tcplink(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    while True:         # 和每个接入的客户端，进行多次数据通信
        data = sock.recv(1024)  # 接收客户端数据
        if not data or data.decode('utf-8') == 'exit':  # 如果客户端不发送数据或者发送了exit
            print('client disconnected.')
            break
        oper,filename = data.decode('utf-8').split()  # 对接收的数据按照空格分割
        if oper == 'get':
            m = hashlib.md5()
            if os.path.isfile(filename):
                size = os.stat(filename).st_size   # 获取文件大小
                print('Send size:',size)
                sock.send(str(size).encode('utf-8'))  # 发送文件大小
                recv = sock.recv(1024)              # 接收客户端确认信息(因为上下文两个send是连着的，所以为了防止粘包，接收一次信息)
                f = open(filename,'rb')
                for line in f:
                    sock.send(line)   #读取文件，发送给客户端
                    m.update(line)
                # print('Send finished.',m.hexdigest())   # 打印md5的值
                sock.send(m.hexdigest().encode('utf-8'))  # 把md5的值发送给客户端
    sock.close()
    print('Connection from %s:%s closed.' % addr)


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 监听端口:
s.bind(('127.0.0.1', 9999))
s.listen(3)
print('Waiting for connection...')

while True:
    # 接受一个新连接:
    sock, addr = s.accept()
    # 创建新线程来处理TCP连接:
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()




