import pymysql

class MySQLHelper:
    def __init__(self):
        #����mysql
        self.connection = pymysql.connect(
            host= '192.168.10.215',
            port= 3307,
            user= 'root',
            password= 'Nj@qs1234',
            database= 'qso_datasite',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )
    #ִ�в�ѯ��䣬�����ز�ѯ���
    def execute_query(self, query):
        result = None
        try:
            with self.connection.cursor() as cursor: #��ȡ�α����
                cursor.execute(query) #ִ�в�ѯ
                result = cursor.fetchall() #��ȡ��ǰ���
        finally:
            self.connection.commit() #�ύ���񣬷��ز�ѯ���
            return result
    #ִ�и�����䣨�����޸ĺ�ɾ��������
    def execute_update(self, query):
        try:
            with self.connection.cursor() as cursor: #��ȡ�α����
                cursor.execute(query) #ִ�и���
        finally:
            self.connection.commit() #�ύ����
    #ִ�в������
    def execute_insert(self, table, data):
        keys = ', '.join(data.keys()) #���� ͨ��data.keys()��ȡ���������ݵļ��б�Ȼ��ʹ��', '.join(data.keys())�����б����ӳ��ַ���
        values = ', '.join(['%s'] * len(data)) #ʹ��', '.join(['%s'] * len(data))����һ�������Ӧ������ռλ���ַ���
        query = f"INSERT INTO {table} ({keys}) VALUES ({values})" #({values})��һ��ռλ�������ᱻ����values��ֵ�滻
        try:
            with self.connection.cursor() as cursor: #��ȡ�α����
                cursor.execute(query, list(data.values())) #ִ�в���
        finally:
            self.connection.commit() #�ύ���񣬷��ز�ѯ���
    #ִ��ɾ�����
    def execute_delete(self, table, condition):
        query = f"DELETE FROM {table} WHERE {condition}"
        try:
            with self.connection.cursor() as cursor: #��ȡ�α����
                cursor.execute(query) #ִ��ɾ��
        finally:
            self.connection.commit() #�ύ����
    #�ر����ݿ�����
    def close_connection(self):
        self.connection.close() #�ر�����
