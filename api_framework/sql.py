#encoding=utf-8
import pymysql

class MySQLHelper:
    def __init__(self):
        #连接mysql
        self.connection = pymysql.connect(
            host= '221.226.240.154',
            port= 3307,
            user= 'root',
            password= '*********',
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
    #执行插入语句
    def execute_insert(self, table, data):
        keys = ', '.join(data.keys()) #列名 通过data.keys()获取待插入数据的键列表，然后使用', '.join(data.keys())将键列表连接成字符串
        values = ', '.join(['%s'] * len(data)) #使用', '.join(['%s'] * len(data))生成一个与键对应数量的占位符字符串
        query = f"INSERT INTO {table} ({keys}) VALUES ({values})" #({values})是一个占位符，将会被变量values的值替换
        try:
            with self.connection.cursor() as cursor: #获取游标对象
                cursor.execute(query, list(data.values())) #执行插入
        finally:
            self.connection.commit() #提交事务，返回查询结果
    #执行删除语句
    def execute_delete(self, table, condition):
        query = f"DELETE FROM {table} WHERE {condition}"
        try:
            with self.connection.cursor() as cursor: #获取游标对象
                cursor.execute(query) #执行删除
        finally:
            self.connection.commit() #提交事务
    #关闭数据库连接
    def close_connection(self):
        self.connection.close() #关闭连接
