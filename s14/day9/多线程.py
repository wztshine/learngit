import threading
import time

num = 0

lock = threading.Lock()

def run(name):
    global num
    print(name,num)
    lock.acquire()
    num+=1
    lock.release()
    time.sleep(2)

start_time = time.time()
taskList = []
for i in range(10):
    task = threading.Thread(target=run,args=('Task-%s'%i,))   # 创建线程，target目标函数，args函数的参数，使用元组的形式
    # task.setDaemon(True)    # 将线程设为守护线程，即只要主线程结束，子线程也就跟着结束了，不设置则主线程等待子线程结束才结束
    task.start()                                            # 启动线程
    taskList.append(task)

# for t in taskList:     # 针对列表中的每个线程，执行join方法
#     t.join(1)   # 不写等待时间，则等待线程完成。写了时间，则等待相应的秒数。如果上面设置了守护线程，超时后则杀掉线程，否则不杀掉。

spend_time =time.time() - start_time

print('主线程执行到最后一行了：用时 %s' %spend_time ,threading.currentThread(),
      '当前线程数量：%s' %threading.activeCount())
