
class A(object):
    age = 22
    def __init__(self,name):
        self.name = name
    def getname(self):
        print(self.name)

a = A('wang')
print(hasattr(a,'age')) # True 判断对象中是否有字符串形式的方法或属性名字。

setattr(a,'sex','man')  # 给a对象设置一个属性：sex = 'man'
print(a.sex)

func = getattr(a,'getname',None) # 获取a对象的一个方法：getname；如果没有这个方法，则为None
func()

delattr(a,'name')  # 删除a对象的age属性
try:
    print(a.name)
except:
    print('name is not exists any more')



# https://blog.csdn.net/xie_0723/article/details/78004649
# a  # 文件夹
# │a.py
# │__init__.py
# b  # 文件夹
# │b.py
# │__init__.py
# ├─c  # 文件夹
# │c.py
# │__init__.py
#
# # c.py 中内容
# args = {'a': 1}
# class C:
#     def c(self):
#         pass

# a.py导入c.py
import importlib
pa1 = importlib.import_module('b.c.c')  # 绝对导入
pa2 = importlib.import_module('.c.c',package='b') # 相对导入
pa1.args # 提取变量
pa1.C    # 提取class C
pa1.C.c  # 提取class C的c方法