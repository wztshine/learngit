import socket
import os
import threading

def tcplink(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    while True:         # 和每个接入的客户端，进行多次数据通信
        data = sock.recv(1024)  # 接收客户端数据
        if not data or data.decode('utf-8') == 'exit':  # 如果客户端不发送数据或者发送了exit
            print('client disconnected.')
            break
        content = os.popen(data.decode('utf-8')).read() # 对发送来的数据执行cmd命令，获取结果
        if len(content) == 0:           #如果执行的命令结果为空的，就手动造一个结果。因为如果为空数据，会挂起，无法正常发送。
            content = 'cmd not exists.'
        sock.send(str(len(content.encode('utf-8'))).encode('utf-8')) # 发送数据的长度
        print('send length:', (len(content.encode('utf-8'))))
        # print('content,', content.encode('utf-8'))
        recv = sock.recv(1024)  # 因为上下都有一个send连在一起，可能发生粘包现象，为了防止这种情况，可以让客户端重新应答一下
        print('Answer:',recv.decode('utf-8'))
        sock.send(content.encode('utf-8'))        # 发送数据
        print('send finished.')
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




