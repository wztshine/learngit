import time
import threading
import queue

# 设置队列大小的上限 10
q = queue.Queue(maxsize=10)

def teacher(name):
    for i in range(20):
        q.put(1)   # 阻塞的方法，如果队列达到上限10，则等待着队列被其他线程get出队后再put
        print(f'{name} 发了一张试卷')
        time.sleep(2)
    print('-----------等待剩余试卷被做完...------------')
    q.join()  # 阻塞的方法，直到队列中的所有任务都被task_done
    print('全做完了！')


def studnet(name):
    while True:
        q.get()  # 出队一个任务，如果队列为空，则等待着，直到队列有值再取出
        print(f'{name} 做了一张试卷，还剩{q.qsize()}')
        time.sleep(5)
        q.task_done()  # 对出队的任务进行task_done

t = threading.Thread(target=teacher,args=('王老师',))

# threading.Timer(time,func,args,kwargs) 对一个线程延迟一个时间后再执行。
s = threading.Timer(3,studnet,args=('小明',))
s1 = threading.Timer(3,studnet,args=('小洪',))

t.start()
s.start()
s1.start()
