# 位置参数和默认参数
def test(x,y,z = 3):   # x,y,z 形参; 其中x,y是位置参数，z是默认参数
    print(x,y,z)
test(1,2)             # 1,2 实参
test(y =2 ,x=1, z=5)  # 关键字参数，直接赋值
test(1, y = 2,z = 5)   # 关键参数必须放在位置参数之后


# 非固定参数，可变参数
def test2(x,y,z=3,*args):
    print(x,y,z,args)
test2(1,2,3,4,5,6)      # 注意此时的3赋值给了z，后面的才是可变参数的值

def test3(x,y,z=3,*args,**kwargs):  # **kwargs接受关键字参数，作为键值对存入字典
    print(x,y,z,args,kwargs)

test3(1,2,3,4,5,6,name = '1',age = 22)  # 此处的关键字参数作为键值对，存入**kwargs
list1 = ['a',1,1,1]
dict1 = {'name':'Wang','age':22}
test3(1,2,*list1)      # 把一个列表传递给*args，需要加*，注意，此处的列表的第一个元素依然给了z,当成了默认参数的值
test3(1,2,**dict1)     # 把一个字典直接传递给**kwargs，需要加**