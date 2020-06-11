import time
from time import sleep

user,passwd = 'alex','123'

def auth(log_type):
    print(log_type)
    def outwrapper(func):
        def wrapper(*args,**kwargs):
            username = input('username:')
            password = input('password:')
            if username == user and password == passwd:
                res = func(*args,**kwargs)
                return res
            else:
                print('username or Password is wrong.')
        return wrapper
    return outwrapper
'''
正常的装饰器不带括号: @auth 等同于 index = auth(index) 
而如果加了括号（此处带了一个关键字参数）,则执行此装饰器（本质是函数），将被装饰函数作为参数传递给里层的函数
'''
@auth(log_type = 'local')  # index = auth(log_type='local') = outwrapper(index) =  wrapper
def index():
    print('welcome to index page.')
    return 1

# @auth(log_type = 'remote')
# def home():
#     print('welcome to home page.')

index()
# home()

