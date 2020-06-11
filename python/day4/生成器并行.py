import time
import random
def consumer(name):
    print('%s来吃包子了！'% name)
    while True:
        baozi = yield
        print('%s包子被%s吃了！'%(baozi,name))

# c = consumer('Wang')
# c.__next__()   # 第一次执行迭代器,执行到yield停止
# c.send('1个')  # 给yield传递值，并继续上次停止的地方开始执行

def maker(name):
    A = consumer('A')
    B = consumer('B')
    next(A)   # A.__next__()
    next(B)
    print('%s开始做包子了！'%name)
    for i in range(5):
        time.sleep(0.7)
        print('%s第%s笼做了10个包子！' %(name,i+1))
        A.send('5个')
        B.send('5个')

maker('Wang')
