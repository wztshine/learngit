# 类变量：修改、增加、删除
# 实例变量：增加、删除、修改

# 析构函数 __del__
# 私有变量、私有方法：前面加 __

class Car():
    region = 'China'                 # 类变量，公有变量，每个实例化的对象都可以访问
    def __init__(self,brand,price):  # 构造方法，实例化
        self.brand = brand
        self.price = price
        self.__mile = 100              # 私有变量，只能内部访问，无法通过实例化的对象进行外部访问
    def __modifyMiles(self,mile):    # 私有方法，只能内部调用
        self.__mile += mile
    def getMiles(self):
        return self.__mile
    def __del__(self):              # 析构方法，销毁对象时自动执行的方法（如程序运行结束、主动删除对象）
        # print('destroy obj.')
        pass
    @staticmethod  # @staticmethod是把函数嵌入到类中的一种方式，函数属于类，但是和类没有什么直接关系
    def car_run(obj):  # 接受一个对象作为参数，调用这个参数的方法
        obj.run()

car = Car('奔驰',300000)
car.getMiles()
car.owner = 'LaoWang'  # 实例化的对象也可以在外面直接添加变量
print(car.region)
car.region = 'Beijing' # 相当于重新声明了一个实例化变量
print(car.owner,car.region) # 当类变量和实例化变量同时存在，首先访问实例变量
del car.owner
del car.region
print(Car.region)

class CC():
    pass

class EleCar(Car,CC):  # 多继承，子类继承父类Car,CC；子类不能直接调用父类的私有变量和私有方法，可以调用父类的调用了私有方法的方法
    def __init__(self,brand,price,battery): # 要写父类的参数
        # 三种继承方法，推荐最后一种
        # Car.__init__(self,brand,price)
        # super(EleCar,self).__init__(brand,price)
        super().__init__(brand,price)    # 继承父类，初始化父类的属性（只初始化一个父类，按继承的顺序从左到右查找，遇到的第一个带有__init__方法的父类停止），不管多少个父类，只写一遍即可。
        self.battery = battery
    def run(self):
        print('%s is running.' % self.brand)

class Bike(Car):
    def __init__(self,brand,price):
        super().__init__(brand,price)
    def run(self):
        print('%s is running.' % self.brand)

bike = Bike('永久',300)
bike.run()

print('--------')
ec = EleCar('宝马',300000,'asdf')
# print(ec.getMiles())
ec.run()

print('多态：一个接口，多种实现')
Car.car_run(ec)
Car.car_run(bike)
