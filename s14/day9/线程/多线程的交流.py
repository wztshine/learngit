import threading
import time

number = 0

def run(num):
    global number
    number += 1
    print('Num: %s'% number)
    time.sleep(3)



for i in range(100):
    # 创建线程，target:目标函数，args:函数的参数，使用元组的形式
    t = threading.Thread(target=run,args=(i,))
    # 开始线程活动
    t.start()

time.sleep(0.01)
print('Main thread is finished.')
print('Current Thread:',threading.activeCount())