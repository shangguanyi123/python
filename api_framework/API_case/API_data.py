#encoding=utf-8
import json
import os
import time

authorization = 'Bearer 7537|45AXV0IDH2hhKBMSRCJEaGrONRge7Hb0zF0Ot6FQ'

class Config:
    api_host = "http://192.168.10.198:90"
    headers = {
    'Authorization': authorization,
    }
    headers_json = {
    'Authorization': authorization,
    'Content-Type': 'application/json'
    }
    headers_biaodan = {
        'Authorization': authorization,
        'Content-Type': 'application/x-www-form-urlencoded'
    }


class Data_xitong():
    #新增采购订单
    def add_user(self,bianhao,user,org_ids,role_ids,phone,status):
        data = {
            "username": user,
            "user_no": bianhao,
            "name": user,
            "password": "123456",
            "org_ids": org_ids, #所在部门
            "phone": phone,
            "user_type": 2,#1系统管理员，2普通用户
            "status": status, #启用1停用0
            "role_ids": [
                role_ids #所属角色
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
                #"code": f"DW{a}",
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
                #"code": f"DW{a}",
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
    def sel_fuzhushuxing(self,name='',type='',status=''):
        params = {
            'page': '1',
            'page_size': '10',
            'title': name,
            'status': status,
            'key': type
        }
        return params
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
                "is_None": None,
                "length": length
            }
            return data
        if data_type == 'int':
            data = {
                "show_name": name,
                "table_name": "prods",
                "data_type": "int",
                "status": status,
                "is_None": None,
                "length": length
            }
            return data
        elif data_type == 'timestamp':
            data = {
                "show_name": name,
                "table_name": "prods",
                "data_type": "timestamp",
                "status": status,
                "is_None": None,
                "default_timestamp": 1
            }
            return data
        elif data_type == 'auxiliary_category':
            data = {
                "show_name": name,
                "table_name": "prods",
                "data_type": "auxiliary_category",
                "status": status,
                "is_None": None,
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
                "is_None": 0, #是否必填
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
                "is_None": 0, #是否必填
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
                "is_None": 0,
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
                "is_None": 0,
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
class Data_chanpin():
    def add_chanpinfenlei(self,fenlei,bianhao,mingcehng,paixv,zhuangtai,shangjifenlei=None):
        if fenlei == 0:
            data = {
                "pid": 0,
                "brand_no": bianhao,#编号
                "name": mingcehng,
                "rank": paixv,#排序
                "status": zhuangtai,#状态
                "note": "备注"
            }
            return data
        elif fenlei == 1:
            data = {
                "pid": shangjifenlei,
                "brand_no": bianhao,
                "name": mingcehng,
                "rank": paixv,
                "status": zhuangtai,
                "note": "备注"
            }
            return data
    def update_chanpinfenlei(self,yijifenlei_id,erjifenlei_id,bianhao,mingcheng,paixv,zhaungtai):
        return {
            "id": erjifenlei_id,
            "pid": yijifenlei_id,
            "brand_no": bianhao,
            "name": mingcheng,
            "rank": paixv,
            "status": zhaungtai,
            "note": "beizhu"
        }
    def del_chanpinfenlei(self,id):
        return {
            "ids": [
                id
            ]
        }
    def add_pinpai(self,mingcheng,caigou_zhekou,xiaoshou_zhekou,paixu):
        return {
            "name": mingcheng,
            "sales_discount": xiaoshou_zhekou,
            "purchase_discount": caigou_zhekou,
            "rank": paixu,
            "note": "备注"
        }
    def update_pinpai(self,id,mingcheng,caigou_zhekou,xiaoshou_zhekou,paixu):
        return {
            "id": id,
            "name": mingcheng,
            "sales_discount": xiaoshou_zhekou,
            "purchase_discount": caigou_zhekou,
            "rank": paixu,
            "note": "备注"
        }
    def del_pinpai(self,id):
        return {
            "ids": [
                id
            ]
        }
    def add_cas(self,cas,name,bieming,fenzijiegou,fenzishi,fenziliang,mdl,einecs,weixianbiaoshi,imgid,filename,img_show):
        return {
            "density": "100",
            "density_nu": "g",
            "density_de": "μl",
            "cas": cas,
            "name_en": name,
            "name_en_alias": bieming,
            "smiles": fenzijiegou,
            "formula": fenzishi,
            "molecular_weight": fenziliang,
            "mdl": mdl,
            "einecs": einecs,
            "dangerous_label": [
                weixianbiaoshi
            ],
            "security_terminology": "具有毒害、腐蚀、爆炸、燃烧、助燃等性质，对人体、设施、环境具有危害的剧毒化学品和其他化学品",
            "precautionary_statement": "1. 实验前，应了解所用化学品的毒性及相应防护措施。  2. 操作有毒气体(如H₂S、Cl₂、Br₂、NO₂、浓HCl和HF等)应在通风橱内进行。  3. 苯、四氯化碳、乙醚、硝基苯等的蒸气会引起中毒。它们有特殊气味，久嗅会使人嗅觉减弱，所以应在通风良好的情况下使用。  4. 有些化学品(如苯、有机溶剂、汞等)能透过皮肤进入人体，应避免与皮肤直接接触。  5. 氰化物、高汞盐(HgCl₂等)、可溶性钡盐(BaCl₂)、重金属盐(如镉、铅盐)等剧毒化学品，应妥善保管，使用时要特别小心。  6. 禁止在实验室内喝水、吃东西。饮食用具不可带进实验室，以防毒物污染，离开实验室前要洗净双手。",
            "structure_img": [{
                "id": imgid,
                "filename": filename,
                "img_show": img_show
            }]
        }
    def update_cas(self,id,cas,name,bieming,fenzijiegou,fenzishi,fenziliang,mdl,einecs,weixianbiaoshi,imgid,filename,img_show):
        return {
            "id": id,
            "density": "100",
            "density_nu": "g",
            "density_de": "μl",
            "cas": cas,
            "name_en": name,
            "name_en_alias": bieming,
            "smiles": fenzijiegou,
            "formula": fenzishi,
            "molecular_weight": fenziliang,
            "mdl": mdl,
            "einecs": einecs,
            "dangerous_label": [
                weixianbiaoshi
            ],
            "security_terminology": "具有毒害、腐蚀、爆炸、燃烧、助燃等性质，对人体、设施、环境具有危害的剧毒化学品和其他化学品",
            "precautionary_statement": "1. 实验前，应了解所用化学品的毒性及相应防护措施。  2. 操作有毒气体(如H₂S、Cl₂、Br₂、NO₂、浓HCl和HF等)应在通风橱内进行。  3. 苯、四氯化碳、乙醚、硝基苯等的蒸气会引起中毒。它们有特殊气味，久嗅会使人嗅觉减弱，所以应在通风良好的情况下使用。  4. 有些化学品(如苯、有机溶剂、汞等)能透过皮肤进入人体，应避免与皮肤直接接触。  5. 氰化物、高汞盐(HgCl₂等)、可溶性钡盐(BaCl₂)、重金属盐(如镉、铅盐)等剧毒化学品，应妥善保管，使用时要特别小心。  6. 禁止在实验室内喝水、吃东西。饮食用具不可带进实验室，以防毒物污染，离开实验室前要洗净双手。",
            "structure_img": [{
                "id": imgid,
                "filename": filename,
                "img_show": img_show
            }]
        }
    def del_cas(self,id):
        return {
            "ids": [
                id
            ]
        }
    def cas_shangchuan_mol(self,path):
        file_name = os.path.basename(path)
        file = [
            ('file', (file_name, open(path, 'rb'), 'application/octet-stream'))
        ]
        return file
    def cas_shangchuan_tupian(self,path):
        file_name = os.path.basename(path)
        file = [
            ('file[]', (file_name, open(path, 'rb'), 'application/octet-stream'))
        ]
        return file
    def add_chanin(self,bianhao,cas,name,fenlei,leixing,chucuntiaojian,weixianpin_biaoqian,fuzhushuxing,img_id,img_filename,img_img_show,guige_bianhao,chundu,pinpai_name,pinpai_id,baozhuang_id,baozhaung_name,jiliang_id,jiliang_name,danweizhaunhuan,baozhuang,jiage,huoqi):
        data = {
            "prod_no": bianhao,
            "cas": cas,
            "name_en": name,
            "prod_category": [
                fenlei
            ],
            "prod_type": leixing,
            "storage_condition": chucuntiaojian,
            "dangerous_label": [
                weixianpin_biaoqian
            ],
            "density": None,
            "density_nu": None,
            "density_de": None,
            "status": 1,
            #辅助属性,传字典
            "data": fuzhushuxing,
            #上传文件
            "structure_img": [
                {
                    "id": img_id,
                    "filename": img_filename,
                    "img_show": img_img_show,
                    "is_default": 1
                }
            ],
            #规格信息
            "prod_has_skus": [
                {
                    "sku_no": guige_bianhao,
                    "purity_specification": chundu,
                    "brand_label": {
                        "value": pinpai_id,
                        "label": pinpai_name
                    },
                    "packing_unit_label": {
                        "value": baozhuang_id,
                        "label": baozhaung_name
                    },
                    "unit_conversion": danweizhaunhuan,
                    "packing": baozhuang,
                    "measuring_unit_label": {
                        "value": jiliang_id,
                        "label": jiliang_name
                    },
                    "price": jiage,
                    "delivery_time": huoqi,
                    "data": {
                        "field_MiTzdL": ""
                    }
                }
            ],
            #产品详情
            "prod_has_infos": {
                "info_cn": "",
                "info_en": ""
            },
            #产品附件
            "prod_has_materials": {
                "msds": [],
                "coa": [],
                "hnmr": [],
                "cnmr": [],
                "ms": [],
                "lc/gc": [],
                "lc-ms": [],
                "hplc": []
            },
            #seo设置
            "prod_has_seo": {
                "title": "标题",
                "title_en": "标题",
                "keywords": "标题",
                "keywords_en": "挑剔"
            }
        }
        return data
    def update_chanin(self,cp_id,chanpin_bianhao,cas,name_en,chanpinfenlei_id,chanpinleixing,chucuntiaojian,weixianpin_id,zhuangtai,fuzhushuxing,
                      img1_id,img1_filename,img1_img_show,img2_id,img2_filename,img2_img_show,
                      guige_id1,guige_bianhao1,chundu1,pinpai_id1,pinpaimingcheng1,banzhuang_id1,baozhuang_name1,danweizhuanhuan1,jiliang_id1,jiliang_name1,baozhaung1,jiage1,huoqi1,
                      guige_bianhao2,chundu2,pinpai_id2,pinpaimingcheng2,banzhuang_id2,baozhuang_name2,danweizhuanhuan2,jiliang_id2,jiliang_name2,baozhaung2,jiage2,huoqi2):
        data = {
            "id": cp_id,
            "prod_no": chanpin_bianhao,
            "cas": cas,
            "name_en": name_en,
            "prod_category": [
                chanpinfenlei_id
            ],
            "prod_type": chanpinleixing,
            "storage_condition": chucuntiaojian,
            "dangerous_label": [
                weixianpin_id
            ],
            "product_feature": None,
            "density": None,
            "density_nu": None,
            "density_de": None,
            "status": zhuangtai,
            "data": fuzhushuxing,
            "structure_img": [
                {
                    "id": img1_id,
                    "filename": img1_filename,
                    "img_show": img1_img_show,
                    "is_default": 0
                },
                {
                    "id": img2_id,
                    "filename": img2_filename,
                    "img_show": img2_img_show,
                    "is_default": 1
                }
            ],
            "prod_has_skus": [
                {
                    "id": guige_id1,
                    "sku_no": guige_bianhao1,
                    "purity_specification": chundu1,
                    "brand_label": {
                        "label": pinpaimingcheng1,
                        "value": pinpai_id1
                    },
                    "packing_unit_label": {
                        "label": baozhuang_name1,
                        "value": banzhuang_id1
                    },
                    "unit_conversion": danweizhuanhuan1,
                    "measuring_unit_label": {
                        "label": jiliang_name1,
                        "value": jiliang_id1
                    },
                    "packing": baozhaung1,
                    "price": jiage1,
                    "delivery_time": huoqi1,
                    "note": None,
                    "data": {
                        "field_MiTzdL": ""
                    }
                },
                {
                    "sku_no": guige_bianhao2,
                    "purity_specification": chundu2,
                    "brand_label": {
                        "label": pinpaimingcheng2,
                        "value": pinpai_id2
                    },
                    "packing_unit_label": {
                        "label": baozhuang_name2,
                        "value": banzhuang_id2
                    },
                    "unit_conversion": danweizhuanhuan2,
                    "measuring_unit_label": {
                        "label": jiliang_name2,
                        "value": jiliang_id2
                    },
                    "packing": baozhaung2,
                    "price": jiage2,
                    "delivery_time": huoqi2,
                    "note": None,
                    "data": {
                        "field_MiTzdL": ""
                    }
                }
            ],
            "prod_has_infos": {
                "info_cn": "<p>丁二酰亚胺是无色针状结晶或具有淡褐色光泽的薄片，味甜。易溶于水、醇或氢氧化钠溶液，不溶于醚、氯仿。熔点126.5 ℃，沸点288 ℃，闪点201 ℃。具有刺激性。避免吸入，避免与皮肤接触。</p>",
                "info_en": "<p>Succinimide is a colorless needle-like crystal or a thin sheet with a light brown sheen that has a sweet taste. Soluble in water, alcohol or sodium hydroxide solution, insoluble in ether, chloroform. The melting point is 126.5 &deg;C, the boiling point is 288 &deg;C, and the flash point is 201 &deg;C. It is irritating. Avoid inhalation and avoid contact with skin.</p>"
            },
            "prod_has_materials": {
                "msds": [],
                "coa": [],
                "hnmr": [],
                "cnmr": [],
                "ms": [],
                "lc/gc": [],
                "lc-ms": [],
                "hplc": []
            },
            "prod_has_seo": {
                "title": "标题",
                "title_en": "标题",
                "keywords": "标题",
                "keywords_en": "挑剔",
                "description": None,
                "description_en": None
            }
        }
        return data
    def sel_chanpin(self, cas='', prod_no='', name_cn='', name_en='', sku_no='', fenzishi='', zhuangtai='',
                    weixianpinbiaoqian_id='', pinpai_id='', cangku_id='', kuwei_id=''):
        params = {
            'page': 1,
            'page_size': 10,
            'search[0][cas]': cas,
            'search[0][prod_no]': prod_no,
            'search[0][name_cn]': name_cn,
            'search[0][name_en]': name_en,
            'search[0][sku_no]': sku_no,
            'search[0][formula]': fenzishi,
            'status': zhuangtai,
            'dangerous_label[]': weixianpinbiaoqian_id,
            'brand_id': pinpai_id,
            'warehouse[warehouse_id]': cangku_id,
            'warehouse[warehouse_location_id]': kuwei_id,
            'cas': cas,
            'prod_no': prod_no,
            'name_cn': name_cn,
            'name_en': name_en,
            'sku_no': sku_no,
            'formula': fenzishi
        }
        return params
    def del_chanpin(self,id):
        return {
            "ids": [
                id
            ]
        }
    def add_coa(self,prod_id,sku_id,kucun,cangku_id,cangkukuwei_id,pihao,jiancejieguo='',jianyanriqi='',yuanshipihao='',shengchanriqi='',shixiaoriqi=''):
        data = {
            "prod_id": prod_id,
            "sku_id": sku_id,
            "inventory_num": kucun,
            "attachment": [
                {
                    "id": 743,
                    "filename": "0/default/20231214/sqSDsCWJI2JwDxKrJeCgu0zXND8j2Py3mkGAqWxC_104.gif",
                    "origin": "157159616923482548.gif",
                    "showFileDel": False
                }
            ],
            "warehouse_location_id": cangku_id,
            "warehouse_id": cangkukuwei_id,
            "storage_condition": "冷冻",
            "test_purity": "98",
            "physical_character": "粉末",
            "test_result": jiancejieguo, #qualified unqualified
            "inspector": "admin",
            "inspection_date": jianyanriqi,
            "inspection_specification": "没茅台",
            "coa_info": [
                {
                    "test_item_cn": "密度",
                    "test_item_en": "density",
                    "test_item_index": "100",
                    "test_item_result": "合格"
                },
                {
                    "test_item_cn": "熔点",
                    "test_item_en": "melting point",
                    "test_item_index": "100",
                    "test_item_result": "合格"
                }
            ],
            "batch_no": pihao,
            "original_batch_no": yuanshipihao,
            "generation_date": shengchanriqi,
            "expiration_date": shixiaoriqi
        }
        return data
    def shezhichengben(self,id,chengben):
        return {
            "id": id,
            "cost": chengben
        }
    def sel_coa(self,prod_id,sku_id,kucun=''):
        params = {
            'page': 1,
            'page_size': 10,
            'is_inventory_num': kucun,
            'prod_id': prod_id,
            'sku_id': sku_id
        }
        return params
    def update_coa(self, id, prod_id, sku_id, kucun, cangku_id, cangkukuwei_id, pihao, jiancejieguo='', jianyanriqi='',
                yuanshipihao='', shengchanriqi='', shixiaoriqi=''):
        data = {
            "id": id,
            "prod_id": prod_id,
            "sku_id": sku_id,
            "inventory_num": kucun,
            "attachment": [
                {
                    "id": 743,
                    "filename": "0/default/20231214/sqSDsCWJI2JwDxKrJeCgu0zXND8j2Py3mkGAqWxC_104.gif",
                    "origin": "157159616923482548.gif",
                    "showFileDel": False
                }
            ],
            "warehouse_location_id": cangku_id,
            "warehouse_id": cangkukuwei_id,
            "storage_condition": "冷冻",
            "test_purity": "98",
            "physical_character": "粉末",
            "test_result": jiancejieguo,  # qualified unqualified
            "inspector": "admin",
            "inspection_date": jianyanriqi,
            "inspection_specification": "没茅台",
            "coa_info": [
                {
                    "test_item_cn": "密度",
                    "test_item_en": "density",
                    "test_item_index": "100",
                    "test_item_result": "合格"
                },
                {
                    "test_item_cn": "熔点",
                    "test_item_en": "melting point",
                    "test_item_index": "100",
                    "test_item_result": "合格"
                }
            ],
            "batch_no": pihao,
            "original_batch_no": yuanshipihao,
            "generation_date": shengchanriqi,
            "expiration_date": shixiaoriqi
        }
        return data
    def del_coa(self,id):
        return {
            "ids": [
                id
            ]
        }
class Data_keshang():
    def sel_user(self,status='',bumen='',bianhao='',denglu_name='',xingming=''):
        params = {
            'page': '1',
            'page_size': '10',
            'status': status,
            'search[0][user_no]': bianhao,
            'search[0][username]': denglu_name,
            'search[0][name]': xingming,
            'org_id': bumen,
            'user_no': bianhao,
            'username': denglu_name,
            'name': xingming
        }
        return params
    def add_kehu(self,kehu_bianhao,name,pinyin,kehu_laiyuan,kehu_leixing,kehu_xingzhi,kehu_zhuangtai,suoshu_xiaoshou,huiyuan_dengji,
                 guojia,sheng_id,shi_id,qu_id,sheng_name,shi_name,qu_name,file_id
                 ):
        data = {
            "customer": {
                "customer_no": kehu_bianhao,
                "customer_name": name,
                "customer_pinyin": pinyin,
                "enum_customer_source_channel": kehu_laiyuan,
                "enum_customer_class": kehu_leixing,
                "enum_customer_type": kehu_xingzhi,
                "enum_customer_status": kehu_zhuangtai,
                "belongs_to_sales": suoshu_xiaoshou,
                "created_at": time.strftime("%Y-%m-%d 00:00:00"),
                "enum_customer_user_level": huiyuan_dengji,
                "company_profile": "生物、化工领域内的技术开发、技术转让、技术咨询、技术服务；化学试剂与化工产品原料（不含危险品）、电脑设备、仪器设备、五金交电、建筑材料、日用百货、针织用品、服装、有色金属、Ⅲ类医疗器械（产品范围详见许可证表述）销售；商务信息咨询（除经纪），从事货物与技术的进出口业务。 【依法须经批准的项目，经相关部门批准后方可开展经营活动】",
                "country": guojia,
                "location_area_children": [
                    sheng_id,
                    shi_id,
                    qu_id
                ],
                "area_json": f"{sheng_name}/{shi_name}/{qu_name}",
                "address": "国和路36号15幢B座306室",
                "note": "生物、化工领域内的技术开发、技术转让、技术咨询、技术服务；化学试剂与化工产品原料（不含危险品）、电脑设备、仪器设备、五金交电、建筑材料、日用百货、针织用品、服装、有色金属、Ⅲ类医疗器械（产品范围详见许可证表述）销售；商务信息咨询（除经纪），从事货物与技术的进出口业务。 【依法须经批准的项目，经相关部门批准后方可开展经营活动】",
                "province": sheng_id,
                "city": shi_id,
                "county": qu_id,
                "files": [
                    file_id
                ]
            },
            "customer_has_contacts": [
                {
                    "is_default": 1,
                    "customer_contact_name": "博勋",
                    "customer_contact_gender": 1,
                    "customer_contact_cellphone": "17345677654",
                    "customer_contact_telephone": "010-8008200",
                    "customer_contact_fax": "8008200",
                    "customer_contact_qq": "23455432",
                    "customer_contact_email": "23455432@163.com",
                    "customer_contact_address": "黄浦区国和路36号15幢B座306室"
                }
            ],
            "customer_has_attachments": [
                file_id
            ]
        }
        return data
    def sel_kehu(self,name='',bianhao='',pinyin='',laiyuan='',kehuxingzhi=''):
        params = {
            'page': '1',
            'page_size': '10',
            'search[0][customer_name]': name,
            'search[0][customer_no]': bianhao,
            'search[0][customer_pinyin]': pinyin,
            'customer_name': name,
            'customer_no': bianhao,
            'customer_pinyin': pinyin,
            'enum_customer_source_chann': laiyuan,
            'enum_customer_typ': kehuxingzhi
        }
        return params
    def update_kehu(self,kehu_id,lianxiren_id,kehu_bianhao,name,pinyin,kehu_laiyuan,kehu_leixing,kehu_xingzhi,kehu_zhuangtai,suoshu_xiaoshou,huiyuan_dengji,
                 guojia,sheng_id,shi_id,qu_id,sheng_name,shi_name,qu_name,file_id
                 ):
        data = {
            "customer": {
                "id":kehu_id,
                "customer_no": kehu_bianhao,
                "customer_name": name,
                "customer_pinyin": pinyin,
                "enum_customer_source_channel": kehu_laiyuan,
                "enum_customer_class": kehu_leixing,
                "enum_customer_type": kehu_xingzhi,
                "enum_customer_status": kehu_zhuangtai,
                "belongs_to_sales": suoshu_xiaoshou,
                "created_at": time.strftime("%Y-%m-%d 00:00:00"),
                "enum_customer_user_level": huiyuan_dengji,
                "company_profile": "生物、化工领域内的技术开发、技术转让、技术咨询、技术服务；化学试剂与化工产品原料（不含危险品）、电脑设备、仪器设备、五金交电、建筑材料、日用百货、针织用品、服装、有色金属、Ⅲ类医疗器械（产品范围详见许可证表述）销售；商务信息咨询（除经纪），从事货物与技术的进出口业务。 【依法须经批准的项目，经相关部门批准后方可开展经营活动】",
                "country": guojia,
                "location_area_children": [
                    sheng_id,
                    shi_id,
                    qu_id
                ],
                "area_json": f"{sheng_name}/{shi_name}/{qu_name}",
                "address": "国和路36号15幢B座306室",
                "note": "生物、化工领域内的技术开发、技术转让、技术咨询、技术服务；化学试剂与化工产品原料（不含危险品）、电脑设备、仪器设备、五金交电、建筑材料、日用百货、针织用品、服装、有色金属、Ⅲ类医疗器械（产品范围详见许可证表述）销售；商务信息咨询（除经纪），从事货物与技术的进出口业务。 【依法须经批准的项目，经相关部门批准后方可开展经营活动】",
                "province": sheng_id,
                "city": shi_id,
                "county": qu_id,
                "files": [
                    file_id
                ]
            },
            "customer_has_contacts": [
                {
                    "id":lianxiren_id,
                    "is_default": 1,
                    "customer_contact_name": "博勋",
                    "customer_contact_gender": 1,
                    "customer_contact_cellphone": "17345677654",
                    "customer_contact_telephone": "010-8008200",
                    "customer_contact_fax": "8008200",
                    "customer_contact_qq": "23455432",
                    "customer_contact_email": "23455432@163.com",
                    "customer_contact_address": "黄浦区国和路36号15幢B座306室"
                }
            ],
            "customer_has_attachments": [
                file_id
            ]
        }
        return data
    def del_kehu(self,id):
        return {
            "ids": [
                id
            ]
        }
    def set_vip(self,vip,id):
        return {
        "enum_customer_user_level": vip,
        "ids": id #传列表
    }
    def set_xiaoshou(self,name,user,type,xiaoshou_id,kehu_id):
        data = {
            "customer_name": name,
            "current_sale": user,
            "type": type,
            "to": xiaoshou_id,
            "note": "备注",
            "ids": [
                kehu_id
            ]
        }
        return data
    def add_genjin(self,name,kehu_id,lianxiren_id,lianxiren_name,genjin_zhuangtai,genjin_fangshi,file_id):
        data = {
            "customer_name": name,
            "contacts": [
                {
                    "id": lianxiren_id,
                    "customer_id": kehu_id,
                    "customer_contact_name": lianxiren_name,
                    "customer_contact_gender": "1",
                    "customer_contact_cellphone": "17345677654",
                    "customer_contact_telephone": "010-8008200",
                    "customer_contact_fax": "8008200",
                    "customer_contact_qq": "23455432",
                    "customer_contact_email": "23455432@163.com",
                    "customer_contact_address": "黄浦区国和路36号15幢B座306室",
                    "customer_contact_dept": None,
                    "customer_contact_position": None,
                    "is_default": 1,
                    "created_at": time.strftime("%Y-%m-%d %H:%M:%S"),
                    "updated_at": time.strftime("%Y-%m-%d %H:%M:%S"),
                    "deleted_at": None,
                    "created_user_id": 1,
                    "created_user_name": "admin",
                    "_X_ROW_KEY": "row_653"
                }
            ],
            "customer_id": kehu_id,
            "customer_contact_id": lianxiren_id,
            "enum_customer_trace_status": genjin_zhuangtai,
            "enum_customer_source_channel": genjin_fangshi,
            "trace_date": time.strftime("%Y-%m-%d"),
            "next_trace_date": time.strftime("%Y-%m-%d"),
            "visit_content": "询问客户购买意向；询问客户购买意向；询问客户购买意向；询问客户购买意向；询问客户购买意向；询问客户购买意向；询问客户购买意向；询问客户购买意向；询问客户购买意向；询问客户购买意向；询问客户购买意向；",
            "files": [
                file_id
            ]
        }
        return data
    def sel_genjin(self,kehu_name='',lianxiren_name='',kaishi_riqi='',jieshu_riqi=''):
        params = {
            'page': '1',
            'page_size': '10',
            'search[0][customer_name]': kehu_name,
            'search[0][customer_contact_name]': lianxiren_name,
            'trace_date[]': [kaishi_riqi, jieshu_riqi],
            'customer_name': kehu_name,
            'customer_contact_name': lianxiren_name
        }
        return params
    def update_genjin(self,genjin_id,name,kehu_id,lianxiren_id,lianxiren_name,genjin_zhuangtai,genjin_fangshi,file_id):
        data = {
            "customer_name": name,
            "contacts": [
                {
                    "id": lianxiren_id,
                    "customer_id": kehu_id,
                    "customer_contact_name": lianxiren_name,
                    "customer_contact_gender": "1",
                    "customer_contact_cellphone": "17345677654",
                    "customer_contact_telephone": "010-8008200",
                    "customer_contact_fax": "8008200",
                    "customer_contact_qq": "23455432",
                    "customer_contact_email": "23455432@163.com",
                    "customer_contact_address": "黄浦区国和路36号15幢B座306室",
                    "customer_contact_dept": None,
                    "customer_contact_position": None,
                    "is_default": 1,
                    "created_at": time.strftime("%Y-%m-%d %H:%M:%S"),
                    "updated_at": time.strftime("%Y-%m-%d %H:%M:%S"),
                    "deleted_at": None,
                    "created_user_id": 1,
                    "created_user_name": "admin",
                    "_X_ROW_KEY": "row_1141"
                }
            ],
            "customer_id": kehu_id,
            "customer_contact_id": lianxiren_id,
            "enum_customer_trace_status": genjin_zhuangtai,
            "enum_customer_trace_type": genjin_fangshi,
            "trace_date": time.strftime("%Y-%m-%d"),
            "next_trace_date": time.strftime("%Y-%m-%d"),
            "trace_content": "询问客户购买意向",
            "customer_trace_has_attachments": [
                file_id
            ],
            "id": genjin_id
        }
        return data
    def del_genjin(self,id):
        return {
            "ids": [
                id
            ]
        }
    def add_supplier_product_catalog(self,supplier_id,cas,prod_name_zh,prod_name_en,prod_no='',sku_no=''):
        data = {
            "supplier_id": supplier_id,
            "cas": cas,
            "prod_no": prod_no,
            "prod_name_zh": prod_name_zh,
            "prod_name_en": prod_name_en,
            "spec_no": sku_no,
            "spec": "10g，100g",
            "purity": "98%",
            "price": "100",
            "lead_time": "现货"
        }
        return data
    def update_supplier_product_catalog(self,id,supplier_id,cas,prod_name_zh,prod_name_en,prod_no='',sku_no=''):
        data = {
            "id":id,
            "supplier_id": supplier_id,
            "cas": cas,
            "prod_no": prod_no,
            "prod_name_zh": prod_name_zh,
            "prod_name_en": prod_name_en,
            "spec_no": sku_no,
            "spec": "10g，100g",
            "purity": "98%",
            "price": "100",
            "lead_time": "现货"
        }
        return data
    def sel_supplier_product_catalog(self,cas='',supplier_name='',prod_name='',prod_no='',spec_no=''):
        params = {
            'page': 1,
            'page_size': 10,
            'search[0][supplier_name]': supplier_name,
            'search[0][prod_name]': prod_name,
            'search[0][cas]': cas,
            'search[0][prod_no]': prod_no,
            'search[0][spec_no]': spec_no,
            'supplier_name': supplier_name,
            'prod_name': prod_name,
            'cas': cas,
            'prod_no': prod_no,
            'spec_no': spec_no
        }
        return params
    def del_supplier_product_catalog(self,id):
        return {
            "ids": [
                id
            ]
        }

class Data_caigou():
    def add_caigou_shenqingdan(self,type,inquiry_no,user_id,zhidanren,cangku_id,shenqing_yuanyin,
                               prod_id,prod_name,prod_no,sku_no,sku_id,cas,chundu,baozhuang,pinpai_id,pinpai_name,shuliang,beizhu='',
                               fujian_id='',fujian_name='',fujian_path=''):
        date = time.strftime("%Y-%m-%d")
        data = {
            "type": type,#save,commit
            "purchase_request": {
                "purchase_request_no": inquiry_no,
                "purchase_user_id": user_id,
                "request_date": date,
                "purchase_deadline": date,
                "apply_user_id": zhidanren,
                "warehouse_location_id": cangku_id,
                "request_reason": shenqing_yuanyin,
            },
            "purchase_request_has_prod_skus": [
                {
                    "prod_id": prod_id,
                    "prod_name": prod_name,
                    "prod_no": prod_no,
                    "sku_id": sku_id,
                    "sku_no": sku_no,
                    "cas": cas,
                    "purify_spec": chundu,
                    "package": baozhuang,
                    "brand_id": pinpai_id,
                    "brand_name": pinpai_name,
                    "quantity": shuliang,
                    "comment": beizhu,
                }
            ],
            "purchase_request_has_attaches": [
                {
                    "id": fujian_id,
                    "origin_name": fujian_name,
                    "path": fujian_path
                }
            ]
        }
        return data
    def update_caigou_shenqingdan(self,id,chanpin_id,type,inquiry_no,user_id,zhidanren,cangku_id,shenqing_yuanyin,
                               prod_id,prod_name,prod_no,sku_no,sku_id,cas,chundu,baozhuang,pinpai_id,pinpai_name,shuliang,beizhu='',
                               fujian_id='',fujian_name='',fujian_path=''):
        date = time.strftime("%Y-%m-%d")
        data = {
            "type": type,#save,commit
            "purchase_request": {
                "id":id,
                "purchase_request_no": inquiry_no,
                "purchase_user_id": user_id,
                "request_date": date,
                "purchase_deadline": date,
                "apply_user_id": zhidanren,
                "warehouse_location_id": cangku_id,
                "request_reason": shenqing_yuanyin,
            },
            "purchase_request_has_prod_skus": [
                {
                    "id":chanpin_id,
                    "prod_id": prod_id,
                    "prod_name": prod_name,
                    "prod_no": prod_no,
                    "sku_id": sku_id,
                    "sku_no": sku_no,
                    "cas": cas,
                    "purify_spec": chundu,
                    "package": baozhuang,
                    "brand_id": pinpai_id,
                    "brand_name": pinpai_name,
                    "quantity": shuliang,
                    "comment": beizhu,
                }
            ],
            "purchase_request_has_attaches": [
                {
                    "id": fujian_id,
                    "origin_name": fujian_name,
                    "path": fujian_path
                }
            ]
        }
        return data





