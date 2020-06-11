import threading
import time

num = 0
lock = threading.Lock()  # 互斥锁，因为多个线程要对num进行修改，防止出现错误。

class MyThread(threading.Thread):
    def __init__(self):
        super().__init__() # 写了__init__，就一定要继承父类的构造方法。父类的__init__的参数是默认参数，故可以不用重写父类的参数。

    def task(self):  # 自定义的函数
        global num
        if lock.acquire():  # 如果上锁成功，则执行：
            num+=1
            print(f'{self.name}, Num is : {num}')
            lock.release()   # 释放锁，供其他线程使用
            time.sleep(1)


    def task2(self):
        time.sleep(0.1)
        print(f'{self.name}','Task2 is being called.')
        time.sleep(1)

    def run(self):  # 重写父类的run方法。每个单独的线程控制中，start()会自动调用 run()方法。
        self.task()
        self.task2()


for i in range(10):
    T = MyThread() # 针对每个线程对象，start()最多只能调用一次，否则会抛出错误。所以才每循环一次，在循环内部重新生成一个对象
    T.start()