import threading
import time

def run(num):
    print('Num: %s'% num)
    time.sleep(3)

    if num == 4:
        print('Thread is finished.')

for i in range(5):
    # 创建线程，target:目标函数，args:函数的参数，使用元组的形式
    t = threading.Thread(target=run,args=(i,))
    # 开始线程活动
    t.start()

time.sleep(0.01)
print('Main thread is finished.')