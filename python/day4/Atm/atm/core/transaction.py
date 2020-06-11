from atm.core.sql_server import Sql
from atm.core.log_in import authen,user_data

@authen(user=user_data)
def account_info(name):
    sql = Sql()
    info = sql.getUserInfo(name)
    # print(info)
    print('''UserID  : %s
Username: %s
Balance : %s
Debt    : %s'''%(info[0],info[1],info[3],info[4]))
    sql.close()

def pay_check():
    pass


def transfer():
    pass

def logout():
    pass

@authen(user=user_data)
def repay(name):
    '''还款功能'''
    sql = Sql()
    vlues = sql.getUserInfo(name)
    print(vlues)
    if vlues[4] == 0:
        print('Your debt is 0, No need to repay.')
    else:
        money = int(input('How much do you want to repay: '))
        if money > abs(vlues[4]):
            print('Too much !')
        else:
            balance = vlues[3]-money
            debt = vlues[4]+money
            sql.update("UPDATE user SET debt=%s,balance=%s WHERE name=%s",(debt,balance,name))
    sql.close()
    account_info(name)

def withdraw():
    pass

def next_step(name):
    menu = '''
-------  Bank info ---------
1.  账户信息
2.  还款(功能已实现)
3.  取款(功能已实现)
4.  转账
5.  账单
6.  退出
'''
    print(menu)
    num = input('What do you want to do? Input number:')
    menu_dic = {
        '1': account_info,
        '2': repay,
        '3': withdraw,
        '4': transfer,
        '5': pay_check,
        '6': logout,
    }
    menu_dic[num](name)

