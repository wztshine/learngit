import socket
import hashlib

# AF_INET 代表ipv4，SOCK_STREAM 代表TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)     # 确定网络协议，生成对象
s.connect(('127.0.0.1',9999)) # 连接服务器的地址和端口，元组的形式。
while True:
    msg = input('>>:').strip()
    if len(msg) != 0:                  # 如果消息为空，会一直挂起，所以不能为空
        if msg =='exit':
            s.close()                     # 关闭连接
            print('Connection closed.')
            break
        s.send(msg.encode('utf-8'))       # 给服务器发送数据，必须是二进制的
        length = s.recv(1024)            # 首先接收服务器返回的将要接收的数据的长度信息。
        s.send(b'Ready to receive...')    # 发送接收确认命令
        length = int(length.decode('utf-8'))
        print('Recv size:', length)
        data_len = 0
        data_recv = b''
        # 新文件名
        fileName = msg.split()[-1].split('.')[0]
        fileExt =  msg.split()[-1].split('.')[-1]
        newFile = fileName+'-1.'+fileExt
        f = open(newFile,'wb')  # 打开文件，准备写入服务器发过来的文件
        m = hashlib.md5()
        while data_len < length:    # 已经接收的信息的长度，如果小于总长度
            size = length - data_len  
            if size > 1024:      # 如果剩下的信息长度大于1024，即不能一次性发完。
                size = 1024
            else:        # 如果能一次性发完，就只收剩下的信息。目的是准确的接收文件的大小，把可能粘连的send的数据留给下一次recv
                size = length-data_len
            data = s.recv(size)     # 从服务器接收数据
            f.write(data)
            m.update(data)
            data_len += len(data)
        f.close()
        print('recv_md5:',m.hexdigest())  # 打印返回的数据。
        recv = s.recv(1024)      # 接收下一次send的数据，即md5的值。
        print('orig_md5:',recv.decode())

