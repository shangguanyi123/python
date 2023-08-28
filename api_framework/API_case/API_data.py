#coding=gbk
import json
import time

cookies = ''

authorization = 'Bearer 7075|yZ3UW12l4GM9G3OcrknNiUVLwpTmEIKJdV8M03Cy'

class Config:
    api_host = "http://192.168.10.198:90"
    headers = {
    'Authorization': authorization,
    #'Cookie': cookies
    }
    headers_json = {
    'Authorization': authorization,
    #'Cookie': cookies,
    'Content-Type': 'application/json'
    }
    headers_biaodan = {
        'Authorization': authorization,
        # 'Cookie': cookies,
        'Content-Type': 'application/x-www-form-urlencoded'
    }


class Data_API1():
    #新增采购订单
    def add_user(self,bianhao,user,phone,status):
        data = {
            "username": user,
            "user_no": bianhao,
            "name": user,
            "password": "123456",
            "org_ids": 1, #所在部门
            "phone": phone,
            "user_type": 2,
            "status": status, #启用1停用0
            "role_ids": [
                6 #所属角色
            ],
            "email": {
                "user_name": "jws6443@163.com",
                "auth_code": "CEGZGOTVOFLMLVMV",
                "port": "465",
                "smtp": 'smtp.163.com'
            }
        }
        return data
    def update_user(self,username,user_no,name,org_ids,phone,user_type,status,role_ids,id):
        data = {
            "username": username,#用户编号
            "user_no": user_no,#登录名
            "name": name,#用户姓名
            "org_ids": org_ids,#部门
            "phone": phone,
            "user_type": user_type,#用户类型
            "status": status,#状态
            "role_ids": [
                role_ids#所属角色
            ],
            "id": id,
            "email": {}
        }
        return data
    def del_user(self,user_id):
        data = {
            "ids": [
                user_id
            ]
        }
        return data
    def update_user_status(self,user_id,status):
        data = {
            "ids": user_id,
            "status": status
        }
        return data
    def add_juese(self,name,status,role_id=None):
        data1 = {
            "name": name,
            "status": status
        }
        data2 = {
            "role_id": role_id,
            "permission_ids": [
                118,
                120,
                119,
                121,
                122,
                123,
                124,
                125,
                126,
                127,
                128,
                129,
                130,
                131,
                132,
                133,
                134,
                135,
                136,
                137,
                138,
                139,
                140,
                141,
                142,
                143,
                144
            ],
            "data_permissions": []
        }
        return data1,data2
    def insert_uesrt(self,user_id,role_id):
        data ={
            "role_id": role_id,
            "user_ids": [
                user_id
            ]
        }
        return data
    def del_user_juese(self,user_id,role_id):
        data =[{
            "user_ids": [
                user_id
            ],
            "role_id": role_id
        }]
        return data
    def del_juese(self,id):
        data = {
            "ids": [
                id
            ]
        }
        return data
    def add_danwei(self,classes,name,status,type=None,base=None,rate=None):
        a = int(time.time())
        if classes == 1:
            data = {
                "code": f"DW{a}",
                "name": name,
                "classes": "measure",  # 计量单位
                "status": status,
                "type": type,  #weight length area volume number_of_packages time other
                "base": base,  # 基本纲0否1是
                "rate": rate  # 转化率
            }
            return data
        elif classes == 0:
            data = {
                "code": f"DW{a}",
                "name": name,
                "classes": "package",  # 包装单位
                "status": status,
                "base": 0
            }
            return data
    def update_danwei(self,classes,name,status,id,code,type=None,base=None,rate=None):
        if classes == 1:
            data = {
                "code": code,
                "name": name,
                "classes": "measure",  # 计量单位
                "status": status,
                "type": type,  #weight length area volume number_of_packages time other
                "base": base,  # 基本纲0否1是
                "rate": rate,  # 转化率
                "id":id,
            }
            return data
        elif classes == 0:
            data = {
                "code": code,
                "name": name,
                "classes": "package",  # 包装单位
                "status": status,
                "base": 0,
                "id":id
            }
            return data
    def del_danwei(self,id):
        data = {
            "ids": [id]
        }
        return data
    def add_danjushenhe(self,danjuleixing,shenheguize,price=None):
        data = {
            "business_document_values": danjuleixing,
            "option_value": shenheguize,
            "price": price
        }
        return data
    def update_danjushenhe(self,id,danjuleixing,shenheguize,price=None):
        data = {
            "id": id,
            "business_document_values": danjuleixing,
            "option_value": shenheguize,
            "price": price
        }
        return data
    def del_danjushenhe(self,id):
        data = {
            "ids": [
                id
            ]
        }
        return data
    def gonggongcanshu_email(self):
        data = {
            "smtp": "smtp.163.com",
            "port": 465,
            "user_name": "jws6443@163.com",
            "auth_code": "CEGZGOTVOFLMLVMV",
            "from_name": "江苏华信有限公司",
            "from_address": "jws6443@163.com",
            "smtp_secure": "ssl",
            "sms_ak": "1",
            "sms_as": "2"
        }
        return data
    def add_diqu(self,status,qu):
        data = {
            "province_name": "测试省",
            "city_name": "测试市",
            "county_name": qu,
            "status": status,
            "country_id": 1 #国家
        }
        return data
    def update_diqu(self,status,qu,id):
        data = {
            "province_name": "测试省",
            "city_name": "测试市",
            "county_name": qu,
            "status": status,
            "id": id
        }
        return data
    def del_diqu(self,id):
        data = {
            "ids": [
                id
            ]
        }
        return data
    def update_biaohao_guize(self,number):
        dqsj = time.strftime("%Y%m%d")
        if number == 1:
            data1 = {
            "id": 2,
            "number": 1,
            "rules_name": "产品编号",
            "rules": [
                {
                    "item": "serial_number",
                    "format": "000001",
                    "length": 6,
                    "item_name": None
                }
            ],
            "demo": "000001",
            "edit_or_not": 0,
            "note": None
        }
            return data1
        elif number == 2:
            data2 = {
            "id": 2,
            "number": 2,
            "rules_name": "产品编号",
            "rules": [
                {
                    "item": "custom",
                    "format": "CP",
                    "length": None,
                    "item_name": "自定义"
                },
                {
                    "item": "serial_number",
                    "format": "000001",
                    "length": 6,
                    "item_name": None
                }
            ],
            "demo": "CP000001",
            "edit_or_not": 0,
            "note": None
        }
            return data2
        elif number == 3:
            data3 = {
            "id": 2,
            "number": 3,
            "rules_name": "产品编号",
            "rules": [
                {
                    "item": "custom",
                    "format": "CP",
                    "length": None,
                    "item_name": "自定义"
                },
                {
                    "item": "date",
                    "format": "YYYYMMDD",
                    "length": 10,
                    "item_name": "日期"
                },
                {
                    "item": "serial_number",
                    "format": "000001",
                    "length": 6,
                    "item_name": None
                }
            ],
            "demo": f"CP{dqsj}000001",
            "edit_or_not": 0,
            "note": None
        }
            return data3
        elif number == 4:
            data4 = {
            "id": 2,
            "number": 1,
            "rules_name": "产品编号",
            "rules": [
                {
                    "item": "custom",
                    "format": "CP",
                    "length": None,
                    "item_name": "自定义"
                }
            ],
            "demo": "CP",
            "edit_or_not": 0,
            "note": None
        }
            return data4
        elif number == 5:
            data5 = {
            "id": 2,
            "number": 2,
            "rules_name": "产品编号",
            "rules": [
                {
                    "item": "custom",
                    "format": "CP",
                    "length": None,
                    "item_name": "自定义"
                },
                {
                    "item": "date",
                    "format": "YYYYMMDD",
                    "length": 10,
                    "item_name": "日期"
                }
            ],
            "demo": f"CP{dqsj}",
            "edit_or_not": 0,
            "note": None
        }
            return data5
    def add_fuzhuziliao_feilei(self,name):
        data = {
            "title": name
        }
        return data
    def update_fuzhuziliao_fenlei(self,id,name):
        data = {
            "title": name,
            "id": id
        }
        return data
    def add_fuzhuziliao_mingcheng(self,key,name,status):
        data = {
            "key": key,
            "name": name,
            "status": status
        }
        return data
    def update_fuzhuziliao_mingcheng(self,id,key,name,status):
        data = {
            "id": id,
            "key": key,
            "name": name,
            "status": status,
            "note": ""
        }
        return data
    def del_fuzhuziliao_mingcheng(self,id):
        data = {
            "ids": [
                id
            ]
        }
        return data
    def del_fuzhuziliao_fenlei(self,id):
        data = {
            "ids": [
                id
            ]
        }
        return data
    def add_fuzhushuxing(self,name,data_type,status,length=None):#varchar int timestamp auxiliary_category
        if data_type == 'varchar':
            data = {
                "show_name": name,
                "table_name": "prods",
                "data_type": "varchar",
                "status": status,
                "is_null": None,
                "length": length
            }
            return data
        if data_type == 'int':
            data = {
                "show_name": name,
                "table_name": "prods",
                "data_type": "int",
                "status": status,
                "is_null": None,
                "length": length
            }
            return data
        elif data_type == 'timestamp':
            data = {
                "show_name": name,
                "table_name": "prods",
                "data_type": "timestamp",
                "status": status,
                "is_null": None,
                "default_timestamp": 1
            }
            return data
        elif data_type == 'auxiliary_category':
            data = {
                "show_name": name,
                "table_name": "prods",
                "data_type": "auxiliary_category",
                "status": status,
                "is_null": None,
                "enum_key": "customer_type"
            }
            return data
    def update_fuzhushuxing(self,id,name,data_type,status,length=None):
        if data_type == 'varchar':
            data = {
                'id': id,
                "show_name": name,
                "table_name": "prods",
                "data_type": "varchar",
                "status": status,
                "is_null": 0, #是否必填
                "length": length
            }
            return data
        elif data_type == 'int':
            data = {
                'id': id,
                "show_name": name,
                "table_name": "prods",
                "data_type": "int",
                "status": status,
                "is_null": 0, #是否必填
                "length": length
            }
            return data
        elif data_type == 'timestamp':
            data = {
                'id': id,
                "show_name": name,
                "table_name": "prods",
                "data_type": "timestamp",
                "status": status,
                "is_null": 0,
                "default_timestamp": 1
            }
            return data
        elif data_type == 'auxiliary_category':
            data = {
                'id': id,
                "show_name": name,
                "table_name": "prods",
                "data_type": "auxiliary_category",
                "status": status,
                "is_null": 0,
                "enum_key": "customer_type"
            }
            return data
    def del_fuzhushuxing(self,id):
        data = {
            "ids": [
                id
            ]
        }
        return data








