import socket

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
        s.send(b'Ready to receive...')    # 发送接收命令
        length = int(length.decode('utf-8'))
        print('receive len:', length)
        data_len = 0
        data_recv = b''
        while data_len < length:    # 已经接收的信息的长度，如果小于总长度
            data = s.recv(1024)     # 从服务器接收数据
            data_recv += data
            data_len += len(data)
        print(data_recv.decode('utf-8'))  # 打印返回的数据。




