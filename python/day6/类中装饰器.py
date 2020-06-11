class A():
    '''this is class A's doc'''
    n = 1
    def __init__(self,name):
        self.name = name

    @staticmethod  # 静态方法，不能调用类变量和实例变量。相当于把一个普通的方法放在类里面而已。如果想调用实例变量，需要传入实例。
    def time(self,hour):
        print('%s has spent %s hours'%(self.name,hour))

    @classmethod  # 类方法，只能调用类变量，不能调用实例变量。
    def num(cls):
        print('n = %s' % cls.n )

    @property     # 属性方法，把一个方法变成一个属性，调用时不能加括号
    def abc(self):
        print('%s is running' %self.name)
    @abc.setter   # 属性方法的修改
    def abc(self,arg):
        print('%s change to %s' % (self.name,arg))
    @abc.deleter  # 属性方法的删除
    def abc(self):
        print('deleted.')

a = A('Wang') # 实例化
# a.time(a,1)   #静态方法的调用
# a.num()       # 类方法的调用
# a.abc         # 属性方法的调用
# a.abc='Li'    # 属性方法的修改
# del a.abc     # 属性方法的删除

print(a.__doc__)

