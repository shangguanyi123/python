import pymysql

class MySQLHelper:
    def __init__(self):
        #连接mysql
        self.connection = pymysql.connect(
            host= '221.226.240.154',
            port= 3307,
            user= 'root',
            password= '******',
            database= 'qso_erp',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )
    #执行查询语句，并返回查询结果
    def execute_query(self, query):
        result = None
        try:
            with self.connection.cursor() as cursor: #获取游标对象
                cursor.execute(query) #执行查询
                result = cursor.fetchall() #获取当前结果
        finally:
            self.connection.commit() #提交事务，返回查询结果
            return result
    #执行更新语句（包括修改和删除操作）
    def execute_update(self, query):
        try:
            with self.connection.cursor() as cursor: #获取游标对象
                cursor.execute(query) #执行更新
        finally:
            self.connection.commit() #提交事务
    #关闭数据库连接
    def close_connection(self):
        self.connection.close() #关闭连接

