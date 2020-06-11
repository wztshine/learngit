import select
import socket
import queue

# 生成socket对象
server = socket.socket()
# 设置非阻塞模式
server.setblocking(False)

# 绑定地址，设置监听
server.bind(('localhost',9999))
server.listen(1000)

inputs = [server,]
outputs = []
msg_queue = {}

while True:
    '''
    select的三个参数：
    rlist -- wait until ready for reading
    wlist -- wait until ready for writing
    xlist -- wait for an ``exceptional condition'
    
    下面这句话的意思是：
    监视 inputs 列表中的文件描述符（简称fd），如果有 fd 准备好 reading 了，就将这些准备好的 fd 返回到 rlist 列表中。
    监视 outputs 列表中的fd，如果有fd准备好 writing 了，就将这些 fd 返回到 wlist 列表中。
    监视 inputs 列表中的fd，如果有fd 出错了，就将这些 fd 返回到elist列表中。
    
    针对socket可读可写的判断，可以参考博客：https://www.cnblogs.com/chenyang920/p/5086458.html
    '''

    rlist,wlist,elist = select.select(inputs,outputs,inputs)  # 没有fd就绪，此处就一直阻塞
    for r in rlist:                             # rlist中有值了，说明inoputs列表中有fd可以准备读取了
        if r is server:                         # 如果可读的 fd 是 server，说明有 客户端 连接过来了
            conn, addr = server.accept()
            conn.setblocking(False)             # 不要阻塞客户端
            inputs.append(conn)                 # 将这个客户端添加到受监视的inputs中，以便下次循环时去检测它
            msg_queue[conn] = queue.Queue()     # 接收到客户端连接后，可以放到队列中，之后再返回给客户端数据
            print('Server is ...')

        else:                                   # 不是服务器可读，说明是客户端可读，也就是客户端发数据过来等待读取
            data = r.recv(1024)
            if data:
                print('Recv Data:',data.decode())
                msg_queue[r].put(data)
                if r not in outputs:      # 不在 outputs 里面，就将它添加进去（因为受到数据后，就可以准备去发送数据了）
                    outputs.append(r)
            else:     # 没有data，说明客户端断开了，就从监视的列表中删除
                print('客户端断开了')
                if r in outputs:
                    outputs.remove(r)
                inputs.remove(r)
                del msg_queue[r]

    for w in wlist:          # 可写的列表
        try:  # 获取队列消息
            msg = msg_queue[w].get_nowait()
        except:
            outputs.remove(w)  # 队列为空，说明没啥消息需要返回给客户端，就从outputs里面删掉
        else:
            w.send(msg)

    for e in elist:
        e.close()
        print('Error occured.')
        inputs.remove(e)
        if e in outputs:
            outputs.remove(e)
        del msg_queue[e]




