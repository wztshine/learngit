a = dict(name = 'wang')
b = [1,2,3]
try:                # 尝试着执行try里面的代码
    print(a)
    print(a['age'])
    print(b[100])
except (NameError,) as e:  # 遇到NameError的错误，则抛出（可以将多个错误写在一行，用括号括起来，逗号隔开）
    print(e)
except KeyError as e:     # keyError
    print('key_error',e)
except Exception as e:    # 所有能抛出的异常都可以抛出
    print('未知错误。')
else:
    print('没有错误,才执行此句。可以省略')
finally:
    print('总会执行此句。可以省略')



# 自定义 异常
class NumError(Exception):    # 创建一个异常类，继承自Exception
    def __init__(self,info):
        super().__init__(self)   # 继承父类的方法
        self.info = info
    def __str__(self):       # __str__方法，打印对象即可直接打印返回值
        return self.info

num = [1,2,3,4,5]
try:
    if len(num)<100:
        raise NumError('Length Error')  # 通过raise主动抛出异常
except NumError as e:
    print(e)