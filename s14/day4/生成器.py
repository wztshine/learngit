gen = (i for i in range(1000))  # 简单的生成器，也就是迭代器的一种，尽管这里写了range(1000),但是迭代器是数据流，
                                # 没有长度，只能通过计算获取下一个值
print(gen)


def fib(num):           # 生成器
    n,a,b = 0,0,1
    while n<num:
        yield b            # 每次调用，执行到yeild就停止，相当于return b，
                            # 下一次调用__next__方法时，从yield的下一行开始执行
        a,b = b,a+b
        n+=1
    return 'done.'       '''注意，for循环遍历迭代器无法执行到这一句代码，必须通过异常处理捕获，
                            因为生成器是实时计算的，没有长度，除非抛出异常，否则不会执行return'''


f = fib(10)
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())
print('------------')

# 遍历迭代器的内容:方法一，无法获取返回值
# for i in f:
#     print(i)

# 遍历迭代器的内容:方法二，通过捕获异常获取返回值
while True:
    try:
        x = next(f)  # 等同于 f.__next__()
        print(x)
    except StopIteration as e:  # 通过异常处理获取返回值
        print(e.value)          # e的内容是return的内容
        break

