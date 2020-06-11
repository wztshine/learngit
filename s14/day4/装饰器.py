'''装饰器其实是一个函数，作用是装饰其他函数
装饰器的特点：1. 不改变被装饰的函数的源代码的情况下添加函数的功能
             2. 不改变被装饰的函数的调用方式
装饰器的组成方式：高阶函数+嵌套函数'''

'''python的内存分配机制:
1. 普通变量内存分配，例如：x=1  y=x
    在这个例子中，x相当于一个门牌号,是一个内存地址，可以看做一个门牌号，内存里面放着1，
    而y=x相当于这个内存加了一个门牌号：y ，它俩实际上指向一个内存地址，
    当x，y都不再调用1时，这个内存才会被定期的内存刷新清理掉
2. 函数的内存分配：例如 def get():
                            pass
   这个例子中，函数名get是一个内存地址，内存里存的是函数的内容，只是字符串，这里就是pass,
   所以print(get)得到的是一个内存地址，而get()才是真的执行了函数的内容'''


import time
from time import sleep

def timer(func):   # 高阶函数：以函数作为参数
    def deco(*args,**kwargs):    # 嵌套函数，在函数内部以 def 声明一个函数,接受 被装饰函数的所有参数
        time1 = time.time()
        func(*args,**kwargs)
        time2 = time.time()
        print('func elapsed %s' %(time2-time1))
    return deco    # 注意，返回的函数没有加括号！所以返回的是一个内存地址，而不是函数的返回值

@timer   # 装饰器，放在被装饰函数的顶部，等同于： test1 = timer(test1) = deco
def test1(name):
    print('test1 is running, will sleep 1 seconds...')
    sleep(1)
    print('test1 is over.',name)

test1('wwwww')


'''对上面的代码进行断点调试，运行的步骤是：
1. 执行19行的timer，相当于timer = ‘函数体’，也就是将函数体作为字符串赋值给了timer，函数体不会被执行
2. 所以第2步就跳到了27行的@timer，等同于： test1 = timer(test1) = deco， 这里才开始执行timer函数，所以程序跳转到了20行
3. 因为timer是一个嵌套函数，里面的函数没有被调用，所以不会被执行，直接执行timer的返回值，25行
4. 第3步执行完以后，28行的test1函数没有执行！直接执行33行的test1(). 
   不知道为什么，估计是装饰器的问题，可能默认就不执行被装饰函数
5. 根据第2步，test1= timer的返回值，也就是deco，所以test1()相当于deco()，程序也就跳到了21行
6. deco一步步运行，知道22行的func()，因为func是一个参数，也就是def 的test1，所以程序调到29行，真正执行test1函数'''
