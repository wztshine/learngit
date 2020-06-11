import threading
import time

def run(num):
    print('Num: %s'% num)
    time.sleep(3)

    if num == 4:
        print('Thread is finished.')

Tlist = []
for i in range(5):
    # 创建线程，target:目标函数，args:函数的参数，使用元组的形式
    t = threading.Thread(target=run,args=(i,))
    # 开始线程活动
    t.start()
    Tlist.append(t)

for t in Tlist:  # 针对每个子线程，等待子线程执行一段时间，再继续往下执行主线程。
    # t.join(0.1)  # 针对每个子线程，等待0.1秒，如果超时还未执行完毕，则不管子线程的状态，继续往下执行主线程。
    t.join()   # 没写时间，则默认等待子线程执行完毕，才继续往下执行主线程。

time.sleep(0.01)
print('Main thread is finished.')