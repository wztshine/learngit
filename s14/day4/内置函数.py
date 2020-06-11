# import itertools
#
# con = itertools.chain('abc','def')
# for c in con:
#     print(c)
#
# print('-'.ljust(50,'-'))
#
# com = itertools.chain.from_iterable(['abc','def'])
# for c in com:
#     print(c)

# all() 一个可迭代对象的所有元素如果都为True，则True，否则false
print(all(['1',2,3]))

# any()
print(any([12,3,40,0]))

# ascii() 转换成string
x = [1,2,3]
print(ascii(x))

# bin()  # 把十进制的数字转换成二进制
print(bin(2))

print(oct(26))  # 把十进制转成8进制

# hex  把十进制的数字转换成16进制
print('16进制',hex(24))

# bytes()
a = bytes('abcde',encoding='utf-8')   # 转换成字节，不可更改。string等类型都是不可更改的，不像list
print(a,type(a))

#bytearray()
b = bytearray('abcde',encoding='utf-8') # 转换成字节数组，可以对数组中的元素更改
b[0] = 100
print(b)

# callable() 是否可调用
print(callable('a'))

# chr()  Unicode的数字转成string
print(chr(99))
print(ord('A'))

# exec()  执行python语句，没有返回值
exec("print('这是python语句')")

namespace = {}
com = '''
print('第二个')
x=3
'''
exec(com,namespace)
print(namespace["x"])

# eval() 执行表达式，有返回值
print(eval('1+2+3'))

# dir() 获取一个参数的可以调用的方法
a= 'xx'
print(dir(a))

# divmod() 获取除数和被除数的商和余数
print(divmod(5,1))

# enumerate() 获取可迭代对象的元素的下标，返回元组
print(list(enumerate([1,2,3])))

# lambda 匿名函数，最多只能进行三元运算
cal = lambda x : x if x >10 else x+1
print(cal(5))

# filter 过滤一个可迭代对象True的值，所以作为参数的函数的返回值要是bool类型的
f= filter(lambda x:x >5 ,[1,2,3,4,5,6,7,8,9])
print(list(f))

# map() 对可迭代对象的每一个值执行前一个函数，返回可迭代对象
f = map(lambda x:x+5,range(10))
print(list(f))


# reduce() 对一个序列从左到右进行累计，最后把序列变成一个值
import functools
f = functools.reduce(lambda x,y:x+y ,[1,2,3,4,5])
# 上面代码等同于 ((((1+2)+3)+4)+5)
print(f)

f = frozenset([1,2,3,3,3,3])  # 生成一个冻结的集合，不可添加删除等

print(globals())  # 打印当前文件所有的全局变量名和值，作为字典。
print(locals())   # 打印当前文件的局部变量，例如函数内部的变量

# 打印最大的值，不能跨类型，要么全是字符串，要么全是数字
print(max(['a','lsdf','lasdiofwosdklfwe']))
print(min([1,2,3,3,3,67]))

print(pow(2,8))  # 2的8次方

print(round(1.4234,2))   # 保留几位小数


# sorted(iterable, *, key=None, reverse=False)  key是一个函数
a = {1:23,99:2,28:72,3:83,72:222}
print(sorted(a))     # 对字典按照key排序，打印key
print(sorted(a.items()))   # 对字典按照key排序，打印键值对元组
print(sorted(a.items(),key=lambda x:x[1],reverse=True))   # 对字典按照value排序，打印键值对元组

print(sum([1,2,2,3,8]))  # 列表求和


a = [1,2,3,4,5]
b = ['a','b','c','d']
for i in zip(a,b):
    print(i)
