'''
迭代对象：能用for循环进行遍历的对象，都是迭代对象，可迭代的
迭代器：  凡是能用next调用的对象，才是迭代器,所以生成器是迭代器，但是迭代器不一定非得是生成器
'''
from collections.abc import Iterable
from collections.abc import Iterator

# 判断是否可迭代
print(isinstance('aaaa',Iterable))
print(isinstance([1,2,3],Iterable))
print(isinstance({1:2,3:4},Iterable))
print(isinstance((1,2,3),Iterable))

# 判断是否是迭代器
print(isinstance('aaaa',Iterator))
print(isinstance([1,2,3],Iterator))
print(isinstance({1:2,3:4},Iterator))
print(isinstance((1,2,3),Iterator))
print(isinstance((x*1 for x in range(10)),Iterator))

# 转换成迭代器
a = iter([1,2,3,4,5])
print(next(a))
print(next(a))
