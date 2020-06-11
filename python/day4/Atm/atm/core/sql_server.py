import mysql.connector
from atm.config import settings

class Sql():
    def __init__(self):
        self.config = settings.config
        self.conn = mysql.connector.connect(**self.config)
        self.cursor = self.conn.cursor()

    def createTable(self):
        # 创建表
        try:
            # 创建user表:
            self.cursor.execute('create table user (id int(10) NOT NULL AUTO_INCREMENT primary key, '
                           'name varchar(20), password varchar(20),balance int(10),debt int(10))')
            self.conn.commit()
        except mysql.connector.errors.ProgrammingError as e:
            # print('Table is already exists.')
            pass


    def searchUser(self,name):
        user_exist = False
        # 运行查询:
        self.cursor.execute('select * from user where name = %s', (name,))   # 固定格式，必须加,
        # 获取第一行数据
        # row_1 = self.cursor.fetchone()
        # 获取前n行数据
        # row_2 = self.cursor.fetchmany(3)
        # 获取所有数据
        values = self.cursor.fetchall()
        if len(values) > 0:
            user_exist = True
            return user_exist
        else:
            return user_exist

    def addUser(self,name,password,balance,debt):
        # 先查询看是否存在user，如果存在，则不添加
        user_exist = self.searchUser(name)
        if user_exist == False:
            # 添加user
            # 插入一行记录，注意MySQL的占位符是%s,占位使用，所有的类型如数字也用%s传递:
            # 上面创建的表id是自增的，因此不用传递id参数
            self.cursor.execute('insert into user (name,password,balance,debt) values ( %s, %s,%s,%s)', [name,password,balance,debt])
            self.cursor.rowcount
            # 提交事务:
            self.conn.commit()
        else:
            print('User has already exists.')

    def getUserInfo(self,name):
        self.cursor.execute('select * from user where name = %s', (name,))  # 固定格式，必须加,确保是元组类型
        values = self.cursor.fetchone()
        # print(values)
        return values

    def update(self,command,argu):
        # command,argu的格式："UPDATE user SET debt=%s,balance=%s WHERE name=%s",(debt,balance,name)
        self.cursor.execute(command,argu)
        self.conn.commit()

    def close(self):
        self.conn.close()
        self.cursor.close()

# sql = Sql()
# sql.createTable()
# sql.addUser('Wang','1234',15000,0)
# sql.close()




