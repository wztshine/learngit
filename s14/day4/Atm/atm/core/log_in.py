from atm.core.sql_server import Sql

user_data = {
    'account_name':None,
    'is_authenticated':False,
}

# 带参数的装饰器
def authen(user):
    def auth1(func):
        def deco(*args,**kwargs):
            if user['is_authenticated'] == False:
                print('------------User is not authenticated.--------------')
            else:
                print('-------------User is authenticated.----------------')
                func(*args,**kwargs)
        return deco
    return auth1

def log_in():
    name = input('Input Username:')
    password = input('Input Password:')
    sql = Sql()
    if sql.searchUser(name) == False:
        print('User is not exists,please sign up.')
    else:
        if sql.getUserInfo(name)[2] == password:
            print('Login success.')
            user_data['account_name'] = name
            user_data['is_authenticated'] = True
            return name
        else:
            print('Password is wrong.')
    sql.close()

