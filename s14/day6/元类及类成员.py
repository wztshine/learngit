# 类方法
class T(object):
    '''this is doc'''
    def __new__(cls, *args, **kwargs):
        print('this is new func')
        return super().__new__(cls)

    def __init__(self,name):
        self.name = name

    def getname(self):
        print(self.name)

    def __getitem__(self, item):
        print('getitem:',item)

    def __setitem__(self, key, value):
        print('setitem:',key,value)

    def __delitem__(self, key):
        print('delitem:',key)

    def __call__(self, *args, **kwargs):
        print('this is call, you should add bracket')

    def __str__(self):
        return 'you are print obj'

    def __del__(self):
        print('When obj is been destroyed,this func would execution automatically.')


t=T('Wang')       # # T是一个类，它是由type创建的（type是所有类的类，它可以创建类对象，然后类对象可以创建实例）。而type里面定义了一个__call__函数，所以才能使用 'T()'
print(T.__doc__)  # 打印类的文档注释
print(t.__module__)# 打印对象所处的模块名
print(t.__class__) # 打印对象的类
print(t.__dict__)  # 打印对象的变量
print(T.__dict__)  # 打印类的变量
print(t)           # 打印对象，打印__str__方法的返回值（没有str方法，则打印对象的内存地址)
t()         # 对象直接加括号，调用__call__方法
val = t['1']  # __getitem__
t['1'] = 1    # __setitem__
del t['1']    # __delitem__
del t         # __del__
print('\n------------------------\n')



# # 一个类其实也是一个对象，类是由type方法创建的
# # i.e.
# class A(object):
#     a = 5
#     def abc(self,name):
#         self.name = name
#     def getname(self):
#         print(self.name)

#  使用type创建一个类，和上面的类一模一样
def init(self, name):
    self.name = name
def getname(self):
    print(self.name)
A = type('A',(object,),{'a':5,'__init__':init,'getname':getname})
# type第一个参数：类名
# type第二个参数：当前类的基类
# type第三个参数：类的成员

aa = A('Wang')
aa.getname()
print(aa.a)


print('=====================')


class MyType(type):                     # 创建元类，父类需要传入type
    def __new__(cls,name,bases,attrs):   # 第一步，元类的操作都在__new__中完成，第一个参数是将创建的类。name,将要创建的类。bases，将要创建的类的父类。attrs，类的方法和属性的字典
        print("Mytype __new__",name,bases,attrs,sep=' / ')
        print('cls',cls)
        return type.__new__(cls, name,bases,attrs) # 如果返回一个已经存在的实例或者不返回任何值，则init不会被调用

    def __init__(self,*args,**kwargs):  # 第二步，init
        print("Mytype __init__",*args,**kwargs)

    def __call__(self, *args, **kwargs):  # 第三步，创建的类实例化时才执行。类实例化时需要加括号对吧，这个括号就是__call__方法赋予的。
        print("Mytype __call__", *args, **kwargs)
        obj = self.__new__(self)          # Foo类的new方法
        print("obj.... ",obj,*args, **kwargs)
        print(self)
        self.__init__(obj,*args, **kwargs)
        return obj

print('-------------------------------------')

class Foo(object,metaclass=MyType):
    def __new__(cls, *args, **kwargs):
        print("Foo __new__",cls, *args, **kwargs)
        return object.__new__(cls)

    def __init__(self,name):
        self.name = name
        print("Foo __init__")

    def getname(self):
        print('name is ',self.name)

f = Foo("Wang")
print("f",f)
print("fname",f.name)


'''
metaclass的类中的call方法，调用的是子类的new、init方法，
__call__ --->  __new__ ---> __init__
先执行new，创建构造实例，然后init来实例化
'''


class Meta(type):      # 元类
    def __new__(cls, name,bases,attrs):  # name，类名。attrs，类的所有方法属性的字典。
        attrs[name] = 'Hello, %s' % name  # 创建一个 类名 的变量，值为 ‘Hello， 类名’
        print(attrs)                  # 打印一下类的方法和属性的字典。
        return type.__new__(cls,name,bases,attrs)

class People(object,metaclass=Meta): # 使用元类来创建类
    age = 22

peo = People()
print(peo.People)