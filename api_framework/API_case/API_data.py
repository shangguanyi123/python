#coding=gbk
import json

cookies = 'Hm_lvt_b97569d26a525941d8d163729d284198=1680501637,1680847848,1681091049,1682210849; Hm_lvt_e8002ef3d9e0d8274b5b74cc4a027d08=1680501637,1680847848,1681091049,1682210849; SECKEY_ABVK=Hc0MvfZ3SjitS9F8draPLyyOQ0vjafau+pyaUjX0PM8=; BMAP_SECKEY=Hc0MvfZ3SjitS9F8draPL-Tf4IuLmXZuDk8RCxneVN280dPDLjMwKcO2UTdtb_l9gkGh7MWlnFh56lXLxFemN4o1yixL9vL7Ns4yR9fEFJY9ZURbRYROSmqVOzJGA9_Mt01QLQ8YHd8BcfEN4uTMV0z9Bs0ro9tJJrYnTYY8ooivkbt6zZq2U-61ZFsMyjpR'

authorization = 'Bearer 2993|agl2meQ7GbTUOodTdbMIqo2YFrJ8uSHkOV9D1M66'

class Config:
    api_host = "http://221.226.240.154:28090"
    headers = {
    'Authorization': authorization,
    'Cookie': cookies
    }
    headers_json = {
    'Authorization': authorization,
    'Cookie': cookies,
    'Content-Type': 'application/json'
    }


class Data_API1():
    #新增采购订单
    def add_caigou(self,dqsj,purchase_no):
        payload ={
            "order_date": dqsj,
            "purchase_no": purchase_no,
            "purchaser_name": "admin",
            "supplier_po": "azAZ-0099",
            "purchase_supplier": {
                "label": "四川供应商",
                "value": 33
            },
            "purchase_supplier_contacts": {
                "id": 39,
                "mobile": "谁极爱你",
                "name": "张丽"
            },
            "purchase_delivery_address": {
                "address": [
                    "山西省张掖市宁江区",
                    "海南省澳门半岛凤阳县",
                    "青海省固原市西区",
                    "重庆海外金湾区"
                ],
                "consignee": "Lorem ex sit sed",
                "consigneeMobile": "18617102646",
                "detail": "pariatur cupidatat laborum in nisi",
                "note": "",
                "id": 40
            },
            "delivery_date": dqsj,
            "settlement_style": {
                "label": "elit occaecat mollit aliquip",
                "value": 12
            },
            "payment_deadline": dqsj,
            "purchase_company_header": {
                "label": "天津生物医药",
                "value": 20
            },
            "invoice_or_not": 1,
            "invoice_type": 1,
            "invoice_material": 1,
            "invoice_rate": 13,
            "purchase_prods": [
                {
                    "prod_no": "1074-82-4",
                    "spec": "",
                    "pack_size": 10,
                    "pack_unit": "kg",
                    "price": 99.5,
                    "lead_time": "现货",
                    "note": ""
                },
                {
                    "prod_no": "16013-85-7",
                    "spec": "",
                    "pack_size": 1000,
                    "pack_unit": "kg",
                    "price": 10500,
                    "lead_time": "现货",
                    "note": ""
                }
            ]
        }
        return payload
    #修改采购订单
    def update_caigou(self,dqsj,purchase_no):
        payload ={
            "order_date": dqsj,
            "purchase_no": purchase_no,
            "purchaser_name": "admin",
            "supplier_po": "azAZ-0099",
            "purchase_supplier": {
                "value": 33,
                "label": "四川供应商"
            },
            "purchase_supplier_contacts": {
                "id": 39,
                "mobile": "18617102646",
                "name": "张丽"
            },
            "purchase_delivery_address": {
                "address": [
                    "山西省张掖市宁江区",
                    "海南省澳门半岛凤阳县",
                    "青海省固原市西区",
                    "重庆海外金湾区"
                ],
                "consignee": "Lorem ex sit sed",
                "consigneeMobile": "18617102646",
                "detail": "pariatur cupidatat laborum in nisi",
                "id": 40,
                "note": None
            },
            "delivery_date": dqsj,
            "settlement_style": {
                "value": 12,
                "label": "elit occaecat mollit aliquip"
            },
            "payment_deadline": dqsj,
            "purchase_company_header": {
                "value": 20,
                "label": "天津生物医药"
            },
            "invoice_or_not": 1,
            "invoice_type": 1,
            "invoice_material": 1,
            "invoice_rate": 13,
            "note": "加急发货！！！",
            "purchase_prods": [
                {
                    "prod_no": "1074-82-4",
                    "spec": ">=80%",
                    "pack_size": 1,
                    "pack_unit": "kg",
                    "price": "99.50",
                    "lead_time": "现货",
                    "note": None
                },
                {
                    "prod_no": "16013-85-7",
                    "spec": ">=85%",
                    "pack_size": 1,
                    "pack_unit": "kg",
                    "price": 150.5,
                    "lead_time": "现货",
                    "note": None
                }
            ]
        }
        return payload
    #生成质检报告
    def zhijianbaogao(self,dqsj):
        payload ={
            "system_company": {
                "company_name": "阿拉丁",
                "address": "南京市浦口区星火路128号",
                "postal_code": "990001",
                "company_phone": "987789987789",
                "fax": "021-88299999",
                "email": "999000111@163.com",
                "domain": "http://221.226.240.154:29090",
                "logo": "2/default/20230322/ZpX86VWSZJDtIBXgRFc9VAz1ta6EQ1Ghvi1K1T68_1.png"
            },
            "prod": {
                "prod_no": "1074-82-4",
                "cas": "1074-82-4",
                "mf": "C7H18",
                "prod_name": "邻苯二甲酰亚胺钾盐",
                "mw": "102.2178",
                "prod_name_en": "24324324",
                "mdl": "",
                "storage_conditions": "低温保存",
                "smiles": "CC.CCCCC",
                "img": "structure/tmp/8670/1680828670.png"
            },
            "batch_info": {
                "batch_no": "2023",
                "manufacture_date": dqsj,
                "pack_size": 1000,
                "pack_unit": "g"
            },
            "analysis_infos": [
                {
                    "item": "Duis officia Excepteur",
                    "standard": "velit",
                    "result": "通过"
                },
                {
                    "item": "纯度",
                    "standard": "80%",
                    "result": "85%"
                }
            ],
            "analyst": "admin",
            "analysis_date": dqsj,
            "auditor": "admin",
            "audit_date": dqsj
        }
        return payload
    #采购入库
    def ruku(self,purchase_no,dqsj,ruku_id):
        payload ={
            "supplier_name": "四川供应商",
            "purchase_no": purchase_no,
            "inventory_date": dqsj,
            "purchase_address_id": "Lorem ex sit sed,18617102646,山西省张掖市宁江区海南省澳门半岛凤阳县青海省固原市西区重庆海外金湾区,pariatur cupidatat laborum in nisi",
            "delivery_date": dqsj,
            "odd_note": "加急发货！！！",
            "prod_list": [
                {
                    "prod_no": "1074-82-4",
                    "prod_name": "邻苯二甲酰亚胺钾盐",
                    "cas": "1074-82-4",
                    "spec": ">=80%",
                    "pack_unit": "kg",
                    "price": "99.50",
                    "pack_size": 1,
                    "inventory_size": 0,
                    "this_time_size": "1.000",
                    "purpose": 1,
                    "odd_prod_note": "1*1000g",
                    "_key_id": 1
                },
                {
                    "prod_no": "16013-85-7",
                    "prod_name": "2,6-二氯-3-硝基吡啶",
                    "cas": "16013-85-7",
                    "spec": ">=85%",
                    "pack_unit": "kg",
                    "price": "150.50",
                    "pack_size": 1,
                    "inventory_size": 0,
                    "this_time_size": "1.000",
                    "purpose": 1,
                    "odd_prod_note": "1*1000g",
                    "_key_id": 2
                }
            ],
            "odd_no": ruku_id
        }
        return payload
    #其他类入库
    def qita_ruku(self,dqsj):
        payload ={
            "inventory_type": {
                "label": "盘盈入库",
                "value": 29
            },
            "inventory_date": dqsj,
            "operation_user_id": 68,
            "operation_user_name": "admin",
            "prod_list": [
                {
                    "prod_no": "AKP-0506",
                    "cas": "QTRK-000001",
                    "this_time_size": 100,
                    "pack_unit": "g",
                    "prod_name": "硝酸钾",
                    "purpose": 1,
                    "spec": "70%",
                    "note": "危险品"
                }
            ]
        }
        return payload
    #付款
    def caigou_fukuan(self,dqsj,purchase_no,odd_no):
        payload ={
            "payment_date": dqsj,
            "payment_type": 1,
            "payment_account": {
                "label": "sint mollit pariatur occaecat",
                "value": 25
            },
            "purchase_no": purchase_no,
            "odd_no": odd_no,
            "prod_list": [
                {
                    "prod_no": "1074-82-4",
                    "this_time_price": 99.5
                },
                {
                    "prod_no": "16013-85-7",
                    "this_time_price": 150.5
                }
            ]
        }
        return payload
    #收票
    def caigou_shoupiao(self,dqsj,purchase_no,odd_no):
        payload ={
            "receipt_date": dqsj,
            "receipt_account": "0513HLWZX51320220151828",
            "purchase_company_header": {
                "label": "天津生物医药",
                "value": 20
            },
            "invoice_type": 1,
            "invoice_material": 1,
            "invoice_rate": 13,
            "purchase_no": purchase_no,
            "odd_no": odd_no,
            "prod_list": [
                {
                    "prod_no": "1074-82-4",
                    "this_time_price": "99.50",
                    "this_time_size": 1
                },
                {
                    "prod_no": "16013-85-7",
                    "this_time_price": "150.50",
                    "this_time_size": 1
                }
            ]
        }
        return payload
    #新增销售订单
    def add_xiaoshou(self,dqsj,sales_no):
        payload ={
            "order_date": dqsj,
            "sales_no": sales_no,
            "salesperson": "admin",
            "po": "AZaz09.~",
            "customer": {
                "label": "天津医药",
                "value": 54
            },
            "customer_contacts": {
                "id": 71,
                "mobile": "132902387463",
                "name": "天津"
            },
            "customer_delivery_address": {
                "address": [
                    "天津市",
                    "直辖区",
                    "和平区"
                ],
                "consignee": "天津",
                "consigneeMobile": "1672893736",
                "detail": "100号",
                "note": None,
                "id": 93
            },
            "collection_account": {
                "label": "交通银行",
                "value": 12
            },
            "invoice_company": {
                "label": "南京爱康A",
                "value": 15
            },
            "payment_method": {
                "label": "电汇",
                "value": 7
            },
            "payment_deadline": dqsj,
            "invoice_or_not": 1,
            "customer_invoice_company": {
                "label": "天津医药",
                "value": 62
            },
            "invoice_type": 1,
            "invoice_material": 1,
            "invoice_rate": 13,
            "invoice_address": "上安逸,13848888888,北京市直辖区朝阳区,酒仙桥北路2号明珠公司A栋1209",
            "sales_prods": [
                {
                    "prod_no": "1074-82-4",
                    "prod_name": "邻苯二甲酰亚胺钾盐",
                    "cas": "1074-82-4",
                    "spec": "",
                    "pack_size": 1,
                    "pack_unit": "kg",
                    "price": 1000,
                    "lead_time": "现货",
                    "note": ""
                },
                {
                    "prod_no": "16013-85-7",
                    "prod_name": "2,6-二氯-3-硝基吡啶",
                    "cas": "16013-85-7",
                    "spec": "",
                    "pack_size": 1,
                    "pack_unit": "kg",
                    "price": 1000,
                    "lead_time": "现货",
                    "note": ""
                }
            ]
        }
        return payload
    #修改销售订单
    def update_xiaoshou_order(self,dqsj,dqsj1,sales_no,id1,id2,order_id):
        payload ={
            "order_date": dqsj,
            "sales_no": sales_no,
            "salesperson": "admin",
            "po": "AZaz09.~",
            "customer": {
                "value": 54,
                "label": "天津医药"
            },
            "customer_contacts": {
                "id": 71,
                "mobile": "132902387463",
                "name": "天津"
            },
            "customer_delivery_address": {
                "address": [
                    "天津市",
                    "直辖区",
                    "和平区"
                ],
                "consignee": "天津",
                "consigneeMobile": "1672893736",
                "detail": "100号",
                "id": 93,
                "note": None
            },
            "collection_account": {
                "value": 12,
                "label": "交通银行"
            },
            "invoice_company": {
                "value": 15,
                "label": "南京爱康A"
            },
            "payment_method": {
                "value": 7,
                "label": "电汇"
            },
            "payment_deadline": dqsj,
            "invoice_or_not": 1,
            "note": None,
            "customer_invoice_company": {
                "value": 62,
                "label": "天津医药"
            },
            "invoice_type": 1,
            "invoice_material": 1,
            "invoice_rate": 13,
            "invoice_address": "上安逸,13848888888,北京市直辖区朝阳区,酒仙桥北路2号明珠公司A栋1209",
            "sales_prods": [
                {
                    "id": id1,
                    "cas": "1074-82-4",
                    "collection_price": "0.00",
                    "collection_status": 1,
                    "collection_status_lock": None,
                    "created_at": dqsj1,
                    "created_user_id": 68,
                    "created_user_name": "admin",
                    "deleted_at": None,
                    "invoice_price": "0.00",
                    "invoice_size": 0,
                    "invoice_status": 1,
                    "invoice_status_lock": None,
                    "lead_time": "现货",
                    "logistics_info": None,
                    "note": "1*1000g",
                    "pack_size": 1,
                    "pack_unit": "kg",
                    "price": "1000.00",
                    "prod_name": "邻苯二甲酰亚胺钾盐",
                    "prod_no": "1074-82-4",
                    "scc_id": 0,
                    "shipment_size": 0,
                    "shipment_status": 1,
                    "shipment_status_lock": None,
                    "spec": ">=80%",
                    "un_collection_price": "1000.00",
                    "un_invoice_price": "1000.00",
                    "un_invoice_size": 1,
                    "un_shipment_size": 1,
                    "unit_price": "1000.000",
                    "updated_at": dqsj1,
                    "order_id": order_id,
                    "raw_material_inventory_text": "962965g",
                    "finished_product_inventory_text": ""
                },
                {
                    "id": id2,
                    "cas": "16013-85-7",
                    "collection_price": "0.00",
                    "collection_status": 1,
                    "collection_status_lock": None,
                    "created_at": dqsj1,
                    "created_user_id": 68,
                    "created_user_name": "admin",
                    "deleted_at": None,
                    "invoice_price": "0.00",
                    "invoice_size": 0,
                    "invoice_status": 1,
                    "invoice_status_lock": None,
                    "lead_time": "现货",
                    "logistics_info": None,
                    "note": "1*1000g",
                    "pack_size": 1,
                    "pack_unit": "kg",
                    "price": "1000.00",
                    "prod_name": "2,6-二氯-3-硝基吡啶",
                    "prod_no": "16013-85-7",
                    "scc_id": 0,
                    "shipment_size": 0,
                    "shipment_status": 1,
                    "shipment_status_lock": None,
                    "spec": ">=85%",
                    "un_collection_price": "1000.00",
                    "un_invoice_price": "1000.00",
                    "un_invoice_size": 1,
                    "un_shipment_size": 1,
                    "unit_price": "1000.000",
                    "updated_at": dqsj1,
                    "order_id": order_id,
                    "raw_material_inventory_text": "10000g",
                    "finished_product_inventory_text": ""
                }
            ]
        }
        return payload
    #收款
    def xiaoshou_shoukuan(self,dqsj,sales_no,odd_no,id1,id2):
        payload ={
            "collection_date": dqsj,
            "collection_payment_type": 1,
            "collection_no": {
                "label": "交通银行",
                "value": 12
            },
            "sales_no": sales_no,
            "customer": {
                "label": "天津医药",
                "value": 54
            },
            "odd_no": odd_no,
            "prod_list": [
                {
                    "id": id1,
                    "prod_no": "1074-82-4",
                    "un_collection_price": "1000.00",
                    "this_time_price": 1000
                },
                {
                    "id": id2,
                    "prod_no": "16013-85-7",
                    "un_collection_price": "1000.00",
                    "this_time_price": 1000
                }
            ]
        }
        return payload
    #批量收款
    def xiaoshou_piliangshoukuan(self,dqsj,id1,id2,prod_no1,prod_no2,sales_no1,sales_no2):
        payload ={
            "collection_date": dqsj,
            "collection_payment_type": 1,
            "collection_no": {
                "label": "",
                "value": ""
            },
            "customer": {
                "label": "天津医药",
                "value": 54
            },
            "prod_list": [
                {
                    "id": id1,
                    "prod_no":prod_no1,
                    "sales_no": sales_no1,
                    "un_collection_price": "1000.00",
                    "this_time_price": 1000
                },
                {
                    "id": id2,
                    "prod_no": prod_no2,
                    "sales_no": sales_no2,
                    "un_collection_price": "1000.00",
                    "this_time_price": 1000
                }
            ]
        }
        return payload
    #开票
    def xiaoshou_kaipiao(self,dqsj,sales_no,odd_no,id1,id2):
        payload ={
            "invoice_date": dqsj,
            "invoice_no": "1234567890za-ZA",
            "company_header": {
                "label": "南京爱康A",
                "value": 15
            },
            "invoice_type": 1,
            "invoice_material": 1,
            "invoice_rate": 13,
            "sales_no": sales_no,
            "deposit_bank_info": {
                "bank_account": "4528576543122234567",
                "bank_name": "中国银行浦口支行",
                "tax_account": "962345345124567890AZ"
            },
            "odd_no": odd_no,
            "prod_list": [
                {
                    "id": id1,
                    "cas": "1074-82-4",
                    "prod_no": "1074-82-4",
                    "prod_name": "邻苯二甲酰亚胺钾盐",
                    "spec": ">=80%",
                    "this_time_price": "1000.00",
                    "this_time_size": 1
                },
                {
                    "id": id2,
                    "cas": "16013-85-7",
                    "prod_no": "16013-85-7",
                    "prod_name": "2,6-二氯-3-硝基吡啶",
                    "spec": ">=85%",
                    "this_time_price": "1000.00",
                    "this_time_size": 1
                }
            ]
        }
        return payload
    #销售发货
    def fahuo(self,dqsj,sales_no,chuku_id,id1,id2):
        payload ={
            "customer_contacts": {
                "id": "",
                "mobile": "",
                "name": "放女士"
            },
            "delivery_date": dqsj,
            "customer_delivery_address": {
                "label": "22,北京市直辖区西城区,4443",
                "id": 91
            },
            "invoice_address": "上安逸,13848888888,北京市直辖区朝阳区,酒仙桥北路2号明珠公司A栋1209",
            "sales_no": sales_no,  # 销售单号
            "odd_no": chuku_id,  # 发货号
            "prod_list": [
                {
                    "id": id1,
                    "prod_no": "1074-82-4",
                    "prod_name": "邻苯二甲酰亚胺钾盐",
                    "price": "1000.00",
                    "this_time_size": 1,
                    "pack_unit": "kg",
                    "delivery_note": "",
                    "purpose": 1
                },
                {
                    "id": id2,
                    "prod_no": "16013-85-7",
                    "prod_name": "2,6-二氯-3-硝基吡啶",
                    "price": "1000.00",
                    "this_time_size": 1,
                    "pack_unit": "kg",
                    "delivery_note": "",
                    "purpose": 1
                }
            ],
            "delivery_setting_type": 3
        }
        return payload
    #其他类出库
    def qita_fahuo(self,dqsj):
        payload ={
            "signature": "江林医药",
            "inventory_type": {
                "label": "其他类出库",
                "value": ""
            },
            "inventory_date": dqsj,
            "operation_user_id": 68,
            "note": "补发",
            "operation_user_name": "admin",
            "prod_list": [
                {
                    "prod_no": "AKP-0506",
                    "cas": "QTRK-000001",
                    "pack_unit": "g",
                    "prod_name": "硝酸钾",
                    "purpose": 1,
                    "spec": "70%",
                    "note": "1*100g",
                    "current_inventory": "300g+112ml",
                    "this_time_size": 100
                }
            ]
        }
        return payload
    #新增产品信息
    def add_chanpin(self,number):
        data ={
            "prod_no": number,
            "cas": "",
            "mf": "C8H18",
            "prod_name": "丁二烯",
            "mw": "114.2285",
            "prod_name_en": "BD",
            "mdl": "",
            "storage_conditions": "低温",
            "is_show": 1,
            "smiles": "C(CCCC)(C)CC",
            "img": "structure/tmp/7743/1680587743.png",
            "img_url": "http://221.226.240.154:29090/storage/structure/tmp/7743/1680587743.png",
            "img_material_id": 686,
            "product_skus": [
                {
                    "0": {
                        "invoice_rate": "",
                        "invoice_type": "",
                        "pack_size": "",
                        "pack_unit": "",
                        "price": "",
                        "spec": ""
                    },
                    "spec": ">=80%",
                    "pack_size": 100,
                    "pack_unit": "g",
                    "price": 100,
                    "invoice_type": 2,
                    "invoice_rate": 10
                }
            ]
        }
        return data
    #修改成品信息
    def update_chanpin(self,number,id):
        data ={
            "prod_no": number,
            "cas": "19-0189",
            "mf": "C8H18",
            "prod_name": "丁二烯",
            "mw": "114.2285",
            "prod_name_en": "BD",
            "mdl": "",
            "storage_conditions": "低温",
            "is_show": 1,
            "smiles": "C(CCCC)(C)CC",
            "img": "structure/tmp/7743/1680587743.png",
            "img_url": "http://221.226.240.154:29090/storage/structure/tmp/7743/1680587743.png",
            "img_material_id": None,
            "product_skus": [
                {
                    "id": id,
                    "spec": ">=80%",
                    "pack_size": "100.000",
                    "pack_unit": "g",
                    "price": "100.00",
                    "invoice_type": 2,
                    "invoice_rate": 10
                }
            ]
        }
        return data
    #设置产品标签
    def set_chanpin_biaoqian(self):
        payload = {'tag_id[0]': '71',
                   'tag_id[1]': '69'}
        return payload

class Data_API2():
    #新增导航
    def add_daohang(self,name,model_type):
        payload = {
            'name': name,   #导航名称
            'position[0]': 1,   #顶部
            'position[1]': 2,   #底部
            'model_type': model_type,    #内容模型1单页2列表
            'rank': 10,     #排序值
            'is_show': 1    #网站显示
        }
        return payload
    #修改导航
    def update_daohang(self):
        payload = {
            'name': '单页',
            'position[0]': 1,
            'position[1]': 2,
            'model_type': 4,
            'rank': 10,
            'href': 'https://yiyan.baidu.com',
            'is_show': 0  # 不显示
        }
        return payload
    #新增列表
    def add_liebiao(self,nav_id):
        data ={
            "title": "2023年3月，全球企业并购比前两个月明显活跃。瑞银宣布收购陷入危机的瑞信比较引人注目，辉瑞430亿美元收购Seagen是今年以来最大规模并购，东芝接受JIP财团153亿美元的收购方案。",
            "nav_id": nav_id,  # 导航
            "publisher": "admin",
            "is_top": 0,
            "is_show": 1,
            "content": "<div class=\"post_body\">\n<p id=\"1MEHAIKA\"></p>\n<p id=\"1MEHAIKC\"><strong>大型并购</strong></p>\n<p>&nbsp;</p>\n<blockquote id=\"1MEHAILH\">瑞银宣布收购陷入危机的瑞信</blockquote>\n<p>&nbsp;</p>\n<p class=\"f_center\"><img src=\"https://nimg.ws.126.net/?url=http%3A%2F%2Fdingyue.ws.126.net%2F2023%2F0404%2F26bf1d03j00rsk9mc0026d200p000b4g00it008c.jpg&amp;thumbnail=660x2147483647&amp;quality=80&amp;type=jpg\"></p>\n<p id=\"1MEHAIKE\">瑞士第一大银行瑞银集团(UBS)当地时间3月19日宣布收购陷入危机的瑞士第二大银行集团瑞士信贷银行(Credit Suisse Group)，总对价30亿瑞士法郎。瑞士政府、央行及瑞士金融市场监管局对此表示支持，瑞士央行将提供1000亿瑞士法郎的流动性支持。同时，瑞士政府为瑞银接管的资产的潜在损失提供90亿瑞郎的担保。瑞士金融市场监管局表示，价值约160亿瑞郎的瑞信债券将被完全减记，以确保私人投资者帮助分担损失。</p>\n<p>&nbsp;</p>\n<blockquote id=\"1MEHAILI\">辉瑞430亿美元收购Seagen</blockquote>\n<p>&nbsp;</p>\n<p class=\"f_center\"><img src=\"https://nimg.ws.126.net/?url=http%3A%2F%2Fdingyue.ws.126.net%2F2023%2F0404%2F528b3fd6j00rsk9md000id200p000b4g00it008c.jpg&amp;thumbnail=660x2147483647&amp;quality=80&amp;type=jpg\"></p>\n<p id=\"1MEHAIKH\">辉瑞(Pfizer)宣布将以430亿美元的总企业价值收购美国生物技术公司Seagen。Seagen致力于开发和商业化用于治疗癌症的创新型增强型单克隆抗体疗法。该公司是抗体-药物缀合物(ADC)的行业领导者，该技术旨在利用单克隆抗体的靶向能力将细胞杀伤剂直接递送至癌细胞。ADC已开始获得用于某些常见癌症(如乳腺癌)的批准，Seagen已探索将它们与其他抗癌药物(包括世界上一些最畅销的免疫疗法)结合使用。</p>\n<p>&nbsp;</p>\n<blockquote id=\"1MEHAILJ\">东芝接受JIP财团153亿美元收购</blockquote>\n<p>&nbsp;</p>\n<p class=\"f_center\"><img src=\"https://nimg.ws.126.net/?url=http%3A%2F%2Fdingyue.ws.126.net%2F2023%2F0404%2F8f200e91j00rsk9md001id200p000b4g00it008c.jpg&amp;thumbnail=660x2147483647&amp;quality=80&amp;type=jpg\"></p>\n<p id=\"1MEHAIKK\">拥有147年历史、但近年陷入挣扎的日本知名企业集团东芝(Toshiba)3月23日宣布，将接受以国内基金&ldquo;日本产业合作伙伴&rdquo;(JIP)为主的阵营提出的收购方案。收购额约为2万亿日元(约153亿美元)。JIP阵营力争大致在7月下旬开始要约收购。东芝考虑收购后摘牌退市，退市后提升企业价值再重新上市。JIP阵营中包括欧力士、罗姆等约20家日企，将提供部分收购资金。三井住友银行等组成的银团将向JIP提供最多总计1.2万亿日元的贷款以支持收购。</p>\n<p>&nbsp;</p>\n<blockquote id=\"1MEHAILK\">银湖财团收购软件销售商Qualtrics</blockquote>\n<p>&nbsp;</p>\n<p id=\"1MEHAIKM\">美国软件销售商Qualtrics International宣布达成交易，同意接受美国私募股权巨头银湖(Silver Lake)和加拿大最大养老基金CPPIB为首的财团收购，交易价格为125亿美元。这一交易达成之际，Qualtrics的大股东德国软件巨头思爱普(SAP)正试图剥离其在该公司的71%股份，作为集团重组战略的一部分。2018年，思爱普以80亿美元收购了Qualtrics，并于3年后在美国上市。Qualtrics是一家软件工具销售商，企业用这些产品来调查客户和员工。</p>\n<p>&nbsp;</p>\n<blockquote id=\"1MEHAILL\">Apollo基金收购尤尼威尔</blockquote>\n<p>&nbsp;</p>\n<p id=\"1MEHAIKO\">由全球另类资产管理公司Apollo附属公司管理的基金(Apollo Funds)将以全部现金交易方式收购特种化学品和原料分销商尤尼威尔解决方案(Univar Solutions)，此次交易对该公司的估价约为81亿美元。这项交易包括来自阿布扎比投资局(ADIA)全资子公司的少数股权投资。该合并协议已获得尤尼威尔董事会一致批准。交易完成后，尤尼威尔将成为一家私人控股公司。</p>\n<p id=\"1MEHAIKR\"><strong>中资并购</strong></p>\n<p id=\"1MEHAIKT\">沙特阿美已签署最终协议，收购荣盛石化10%的股权，收购价格为246亿元(约36亿美元)。该交易将大大扩大沙特阿美在中国的下游业务。</p>\n<p id=\"1MEHAIKV\">博格华纳公司(BorgWarner)宣布完成对湖北追日电气(SSE)电动汽车充电解决方案、智能电网和智能能源业务的收购。此次收购是博格华纳亚洲电气化业务中的一项重要举措，将对该公司在欧洲和北美的现有充电业务形成补充。</p>\n<p id=\"1MEHAIL1\"><strong>其他中小型并购</strong></p>\n<p id=\"1MEHAIL3\">防弹少年团的东家Hybe宣布与互联网巨头Kakao达成协议，决定停止对韩国第二大娱乐经纪公司SM娱乐(SM Entertainment)的竞购战。根据协议，Kakao将取得SM的经营权，Hybe将与其进行平台合作。Hybe表示，由于与Kakao的竞争加剧，收购SM的价格超出了公平的收购价格范围。Kakao表示，Kakao及其娱乐部门将在3月26日之前继续收购SM的股份，并将加强与Hybe和SM的业务合作。</p>\n<p id=\"1MEHAIL5\">电通集团(Dentsu Group)宣布已与安宏资本(Advent International)签订最终协议，收购全球全渠道数字营销制作巨头太意tag(Tag Worldwide Holdings)。此次收购将大大增强电通的创意数字生产能力，在全球29个国家/地区增加2800名员工，以及一个全球生产中心和十个专业中心。太意tag成立于1972年，于2017年被安宏资本收购。</p>\n<p id=\"1MEHAIL7\">法国制药集团赛诺菲(Sanofi)将以现金收购总部位于美国的自身免疫性疾病生物制药公司Provention Bio，交易的股权价值为29亿美元。该交易将为赛诺菲的产品组合中添加TZIELD，后者去年在美国获得批准，是首个用于延缓3期1型糖尿病(T1D)的疾病改善药物。Provention去年年底宣布与赛诺菲达成协议，共同在美国推广这种药物。</p>\n<p id=\"1MEHAIL9\">CF Industries Holdings同意以16.75亿美元的价格从澳大利亚Incitec Pivot手中收购位于美国路易斯安那州的Waggaman氨生产设施。两家公司表示，他们将从收购价中拿出约4.25亿美元用于长期氨供应协议，根据该协议，CF将向IPL的Dyno Nobel子公司每年供应多达20万吨的氨。</p>\n<p id=\"1MEHAILB\">挪威国家石油公司(Equinor)拟以8.5亿美元收购加拿大森科能源(Suncor Energy)的英国石油和天然气业务，以获得几处北海石油资产的股份。</p>\n<p id=\"1MEHAILD\">旅行技术公司Travelport宣布收购商务差旅管理平台Deem。自推出其下一代平台Travelport+以来，Travelport一直在创新方面进行投资，收购Deem则是最新的实例。Deem之前的所有人是移动出行解决方案提供商Enterprise Holdings。</p>\n</div>\n<div class=\"post_statement\">\n<p>特别声明：以上内容(如有图片或视频亦包括在内)为自媒体平台&ldquo;网易号&rdquo;用户上传并发布，本平台仅提供信息存储服务。</p>\n<p>Notice: The content above (including the pictures and videos if any) is uploaded and posted by a user of NetEase Hao, which is a social media platform and only provides information storage services.</p>\n<div class=\"_xhi4tc4xf89\"><iframe id=\"iframeu6407155_1\" src=\"https://pos.baidu.com/gcdm?conwid=670&amp;conhei=250&amp;rdid=6407155&amp;dc=3&amp;di=u6407155&amp;s1=462942594&amp;s2=1234862762&amp;dri=1&amp;dis=0&amp;dai=15&amp;ps=4627x585&amp;enu=encoding&amp;exps=110283,110277,110275,110261,110252,110011&amp;ant=0&amp;psi=e158abc9fd806e99&amp;dcb=___adblockplus_&amp;dtm=HTML_POST&amp;dvi=0.0&amp;dci=-1&amp;dpt=none&amp;tpr=1680747617453&amp;ti=%E8%BE%89%E7%91%9E430%E4%BA%BF%E7%BE%8E%E5%85%83%E6%94%B6%E8%B4%ADSeagen%EF%BC%9B%E7%91%9E%E9%93%B6%E6%94%B6%E8%B4%AD%E9%99%B7%E5%85%A5%E5%8D%B1%E6%9C%BA%E7%9A%84%E7%91%9E%E4%BF%A1%20%7C%202023%E5%B9%B43%E6%9C%88%E5%85%A8%E7%90%83%E4%BC%81%E4%B8%9A%E5%B9%B6%E8%B4%AD%7C%E8%82%A1%E6%9D%83%7C%E8%B4%A2%E5%9B%A2%7C%E7%91%9E%E5%A3%AB%E9%93%B6%E8%A1%8C%7C%E7%91%9E%E9%93%B6%E9%9B%86%E5%9B%A2&amp;ari=2&amp;ver=0327&amp;dbv=2&amp;drs=3&amp;pcs=2031x1010&amp;pss=2031x8945&amp;cfv=0&amp;cpl=5&amp;chi=1&amp;cce=true&amp;cec=UTF-8&amp;tlm=1680747617&amp;prot=2&amp;rw=1010&amp;ltu=https%3A%2F%2Fwww.163.com%2Fdy%2Farticle%2FI1F8Q261053159A3.html&amp;ltr=https%3A%2F%2Fwww.163.com%2Fdy%2Fmedia%2FT1542006074249.html&amp;ecd=1&amp;dft=0&amp;uc=2048x1112&amp;pis=-1x-1&amp;sr=2048x1152&amp;tcn=1680747618&amp;qn=79e08baef9601ae6&amp;ft=1\" name=\"iframeu6407155_1\" width=\"670\" height=\"250\" frameborder=\"0\" scrolling=\"no\"></iframe></div>\n</div>",
            "images_url": "http://221.226.240.154:29090/storage/2/default/20230406/cirn4m4EUsWFubzvHNV81paCLJ2XEgslw52yIchz_1.jpg",
            "images_material_id": 689,
            "content_material_id": []
        }
        return data
    #修改列表
    def update_liebiao(self):
        data ={
            "title": "2023年3月，全球企业并购比前两个月明显活跃。瑞银宣布收购陷入危机的瑞信比较引人注目，辉瑞430亿美元收购Seagen是今年以来最大规模并购，东芝接受JIP财团153亿美元的收购方案。",
            "nav_id": 4,  # 新闻资讯
            "publisher": "admin",
            "rank": 0,
            "images": "2/default/20230406/cirn4m4EUsWFubzvHNV81paCLJ2XEgslw52yIchz_1.jpg",
            "is_top": 0,
            "is_show": 0,
            "description": "2023年3月，全球企业并购比前两个月明显活跃。瑞银宣布收购陷入危机的瑞信比较引人注目，辉瑞430亿美元收购Seagen是今年以来最大规模并购，东芝接受JIP财团153亿美元的收购方案。",
            "content": "<div class=\"post_body\">\n<p id=\"1MEHAIKA\"></p>\n<p id=\"1MEHAIKC\"><strong>大型并购</strong></p>\n<p>&nbsp;</p>\n<blockquote id=\"1MEHAILH\">瑞银宣布收购陷入危机的瑞信</blockquote>\n<p>&nbsp;</p>\n<p class=\"f_center\"><img src=\"https://nimg.ws.126.net/?url=http%3A%2F%2Fdingyue.ws.126.net%2F2023%2F0404%2F26bf1d03j00rsk9mc0026d200p000b4g00it008c.jpg&amp;thumbnail=660x2147483647&amp;quality=80&amp;type=jpg\"></p>\n<p id=\"1MEHAIKE\">瑞士第一大银行瑞银集团(UBS)当地时间3月19日宣布收购陷入危机的瑞士第二大银行集团瑞士信贷银行(Credit Suisse Group)，总对价30亿瑞士法郎。瑞士政府、央行及瑞士金融市场监管局对此表示支持，瑞士央行将提供1000亿瑞士法郎的流动性支持。同时，瑞士政府为瑞银接管的资产的潜在损失提供90亿瑞郎的担保。瑞士金融市场监管局表示，价值约160亿瑞郎的瑞信债券将被完全减记，以确保私人投资者帮助分担损失。</p>\n<p>&nbsp;</p>\n<blockquote id=\"1MEHAILI\">辉瑞430亿美元收购Seagen</blockquote>\n<p>&nbsp;</p>\n<p class=\"f_center\"><img src=\"https://nimg.ws.126.net/?url=http%3A%2F%2Fdingyue.ws.126.net%2F2023%2F0404%2F528b3fd6j00rsk9md000id200p000b4g00it008c.jpg&amp;thumbnail=660x2147483647&amp;quality=80&amp;type=jpg\"></p>\n<p id=\"1MEHAIKH\">辉瑞(Pfizer)宣布将以430亿美元的总企业价值收购美国生物技术公司Seagen。Seagen致力于开发和商业化用于治疗癌症的创新型增强型单克隆抗体疗法。该公司是抗体-药物缀合物(ADC)的行业领导者，该技术旨在利用单克隆抗体的靶向能力将细胞杀伤剂直接递送至癌细胞。ADC已开始获得用于某些常见癌症(如乳腺癌)的批准，Seagen已探索将它们与其他抗癌药物(包括世界上一些最畅销的免疫疗法)结合使用。</p>\n<p>&nbsp;</p>\n<blockquote id=\"1MEHAILJ\">东芝接受JIP财团153亿美元收购</blockquote>\n<p>&nbsp;</p>\n<p class=\"f_center\"><img src=\"https://nimg.ws.126.net/?url=http%3A%2F%2Fdingyue.ws.126.net%2F2023%2F0404%2F8f200e91j00rsk9md001id200p000b4g00it008c.jpg&amp;thumbnail=660x2147483647&amp;quality=80&amp;type=jpg\"></p>\n<p id=\"1MEHAIKK\">拥有147年历史、但近年陷入挣扎的日本知名企业集团东芝(Toshiba)3月23日宣布，将接受以国内基金&ldquo;日本产业合作伙伴&rdquo;(JIP)为主的阵营提出的收购方案。收购额约为2万亿日元(约153亿美元)。JIP阵营力争大致在7月下旬开始要约收购。东芝考虑收购后摘牌退市，退市后提升企业价值再重新上市。JIP阵营中包括欧力士、罗姆等约20家日企，将提供部分收购资金。三井住友银行等组成的银团将向JIP提供最多总计1.2万亿日元的贷款以支持收购。</p>\n<p>&nbsp;</p>\n<blockquote id=\"1MEHAILK\">银湖财团收购软件销售商Qualtrics</blockquote>\n<p>&nbsp;</p>\n<p id=\"1MEHAIKM\">美国软件销售商Qualtrics International宣布达成交易，同意接受美国私募股权巨头银湖(Silver Lake)和加拿大最大养老基金CPPIB为首的财团收购，交易价格为125亿美元。这一交易达成之际，Qualtrics的大股东德国软件巨头思爱普(SAP)正试图剥离其在该公司的71%股份，作为集团重组战略的一部分。2018年，思爱普以80亿美元收购了Qualtrics，并于3年后在美国上市。Qualtrics是一家软件工具销售商，企业用这些产品来调查客户和员工。</p>\n<p>&nbsp;</p>\n<blockquote id=\"1MEHAILL\">Apollo基金收购尤尼威尔</blockquote>\n<p>&nbsp;</p>\n<p id=\"1MEHAIKO\">由全球另类资产管理公司Apollo附属公司管理的基金(Apollo Funds)将以全部现金交易方式收购特种化学品和原料分销商尤尼威尔解决方案(Univar Solutions)，此次交易对该公司的估价约为81亿美元。这项交易包括来自阿布扎比投资局(ADIA)全资子公司的少数股权投资。该合并协议已获得尤尼威尔董事会一致批准。交易完成后，尤尼威尔将成为一家私人控股公司。</p>\n<p id=\"1MEHAIKR\"><strong>中资并购</strong></p>\n<p id=\"1MEHAIKT\">沙特阿美已签署最终协议，收购荣盛石化10%的股权，收购价格为246亿元(约36亿美元)。该交易将大大扩大沙特阿美在中国的下游业务。</p>\n<p id=\"1MEHAIKV\">博格华纳公司(BorgWarner)宣布完成对湖北追日电气(SSE)电动汽车充电解决方案、智能电网和智能能源业务的收购。此次收购是博格华纳亚洲电气化业务中的一项重要举措，将对该公司在欧洲和北美的现有充电业务形成补充。</p>\n<p id=\"1MEHAIL1\"><strong>其他中小型并购</strong></p>\n<p id=\"1MEHAIL3\">防弹少年团的东家Hybe宣布与互联网巨头Kakao达成协议，决定停止对韩国第二大娱乐经纪公司SM娱乐(SM Entertainment)的竞购战。根据协议，Kakao将取得SM的经营权，Hybe将与其进行平台合作。Hybe表示，由于与Kakao的竞争加剧，收购SM的价格超出了公平的收购价格范围。Kakao表示，Kakao及其娱乐部门将在3月26日之前继续收购SM的股份，并将加强与Hybe和SM的业务合作。</p>\n<p id=\"1MEHAIL5\">电通集团(Dentsu Group)宣布已与安宏资本(Advent International)签订最终协议，收购全球全渠道数字营销制作巨头太意tag(Tag Worldwide Holdings)。此次收购将大大增强电通的创意数字生产能力，在全球29个国家/地区增加2800名员工，以及一个全球生产中心和十个专业中心。太意tag成立于1972年，于2017年被安宏资本收购。</p>\n<p id=\"1MEHAIL7\">法国制药集团赛诺菲(Sanofi)将以现金收购总部位于美国的自身免疫性疾病生物制药公司Provention Bio，交易的股权价值为29亿美元。该交易将为赛诺菲的产品组合中添加TZIELD，后者去年在美国获得批准，是首个用于延缓3期1型糖尿病(T1D)的疾病改善药物。Provention去年年底宣布与赛诺菲达成协议，共同在美国推广这种药物。</p>\n<p id=\"1MEHAIL9\">CF Industries Holdings同意以16.75亿美元的价格从澳大利亚Incitec Pivot手中收购位于美国路易斯安那州的Waggaman氨生产设施。两家公司表示，他们将从收购价中拿出约4.25亿美元用于长期氨供应协议，根据该协议，CF将向IPL的Dyno Nobel子公司每年供应多达20万吨的氨。</p>\n<p id=\"1MEHAILB\">挪威国家石油公司(Equinor)拟以8.5亿美元收购加拿大森科能源(Suncor Energy)的英国石油和天然气业务，以获得几处北海石油资产的股份。</p>\n<p id=\"1MEHAILD\">旅行技术公司Travelport宣布收购商务差旅管理平台Deem。自推出其下一代平台Travelport+以来，Travelport一直在创新方面进行投资，收购Deem则是最新的实例。Deem之前的所有人是移动出行解决方案提供商Enterprise Holdings。</p>\n</div>\n<div class=\"post_statement\">\n<p>特别声明：以上内容(如有图片或视频亦包括在内)为自媒体平台&ldquo;网易号&rdquo;用户上传并发布，本平台仅提供信息存储服务。</p>\n<p>Notice: The content above (including the pictures and videos if any) is uploaded and posted by a user of NetEase Hao, which is a social media platform and only provides information storage services.</p>\n<div class=\"_xhi4tc4xf89\"><iframe id=\"iframeu6407155_1\" src=\"https://pos.baidu.com/gcdm?conwid=670&amp;conhei=250&amp;rdid=6407155&amp;dc=3&amp;di=u6407155&amp;s1=462942594&amp;s2=1234862762&amp;dri=1&amp;dis=0&amp;dai=15&amp;ps=4627x585&amp;enu=encoding&amp;exps=110283,110277,110275,110261,110252,110011&amp;ant=0&amp;psi=e158abc9fd806e99&amp;dcb=___adblockplus_&amp;dtm=HTML_POST&amp;dvi=0.0&amp;dci=-1&amp;dpt=none&amp;tpr=1680747617453&amp;ti=%E8%BE%89%E7%91%9E430%E4%BA%BF%E7%BE%8E%E5%85%83%E6%94%B6%E8%B4%ADSeagen%EF%BC%9B%E7%91%9E%E9%93%B6%E6%94%B6%E8%B4%AD%E9%99%B7%E5%85%A5%E5%8D%B1%E6%9C%BA%E7%9A%84%E7%91%9E%E4%BF%A1%20%7C%202023%E5%B9%B43%E6%9C%88%E5%85%A8%E7%90%83%E4%BC%81%E4%B8%9A%E5%B9%B6%E8%B4%AD%7C%E8%82%A1%E6%9D%83%7C%E8%B4%A2%E5%9B%A2%7C%E7%91%9E%E5%A3%AB%E9%93%B6%E8%A1%8C%7C%E7%91%9E%E9%93%B6%E9%9B%86%E5%9B%A2&amp;ari=2&amp;ver=0327&amp;dbv=2&amp;drs=3&amp;pcs=2031x1010&amp;pss=2031x8945&amp;cfv=0&amp;cpl=5&amp;chi=1&amp;cce=true&amp;cec=UTF-8&amp;tlm=1680747617&amp;prot=2&amp;rw=1010&amp;ltu=https%3A%2F%2Fwww.163.com%2Fdy%2Farticle%2FI1F8Q261053159A3.html&amp;ltr=https%3A%2F%2Fwww.163.com%2Fdy%2Fmedia%2FT1542006074249.html&amp;ecd=1&amp;dft=0&amp;uc=2048x1112&amp;pis=-1x-1&amp;sr=2048x1152&amp;tcn=1680747618&amp;qn=79e08baef9601ae6&amp;ft=1\" name=\"iframeu6407155_1\" width=\"670\" height=\"250\" frameborder=\"0\" scrolling=\"no\"></iframe></div>\n</div>",
            "images_url": "http://221.226.240.154:29090/storage/2/default/20230406/cirn4m4EUsWFubzvHNV81paCLJ2XEgslw52yIchz_1.jpg",
            "images_material_id": None,
            "content_material_id": []
        }
        return data
    #新增单页
    def add_danye(self,nav_id):
        data ={
            "title": "2023年3月，全球企业并购比前两个月明显活跃。瑞银宣布收购陷入危机的瑞信比较引人注目，辉瑞430亿美元收购Seagen是今年以来最大规模并购，东芝接受JIP财团153亿美元的收购方案。",
            "nav_id": nav_id,
            "publisher": "admin",
            "is_show": 1,
            "content": "<div class=\"post_body\">\n<p id=\"1MEHAIKA\"></p>\n<p id=\"1MEHAIKC\"><strong>大型并购</strong></p>\n<p>&nbsp;</p>\n<blockquote id=\"1MEHAILH\">瑞银宣布收购陷入危机的瑞信</blockquote>\n<p>&nbsp;</p>\n<p class=\"f_center\"><img src=\"https://nimg.ws.126.net/?url=http%3A%2F%2Fdingyue.ws.126.net%2F2023%2F0404%2F26bf1d03j00rsk9mc0026d200p000b4g00it008c.jpg&amp;thumbnail=660x2147483647&amp;quality=80&amp;type=jpg\"></p>\n<p id=\"1MEHAIKE\">瑞士第一大银行瑞银集团(UBS)当地时间3月19日宣布收购陷入危机的瑞士第二大银行集团瑞士信贷银行(Credit Suisse Group)，总对价30亿瑞士法郎。瑞士政府、央行及瑞士金融市场监管局对此表示支持，瑞士央行将提供1000亿瑞士法郎的流动性支持。同时，瑞士政府为瑞银接管的资产的潜在损失提供90亿瑞郎的担保。瑞士金融市场监管局表示，价值约160亿瑞郎的瑞信债券将被完全减记，以确保私人投资者帮助分担损失。</p>\n<p>&nbsp;</p>\n<blockquote id=\"1MEHAILI\">辉瑞430亿美元收购Seagen</blockquote>\n<p>&nbsp;</p>\n<p class=\"f_center\"><img src=\"https://nimg.ws.126.net/?url=http%3A%2F%2Fdingyue.ws.126.net%2F2023%2F0404%2F528b3fd6j00rsk9md000id200p000b4g00it008c.jpg&amp;thumbnail=660x2147483647&amp;quality=80&amp;type=jpg\"></p>\n<p id=\"1MEHAIKH\">辉瑞(Pfizer)宣布将以430亿美元的总企业价值收购美国生物技术公司Seagen。Seagen致力于开发和商业化用于治疗癌症的创新型增强型单克隆抗体疗法。该公司是抗体-药物缀合物(ADC)的行业领导者，该技术旨在利用单克隆抗体的靶向能力将细胞杀伤剂直接递送至癌细胞。ADC已开始获得用于某些常见癌症(如乳腺癌)的批准，Seagen已探索将它们与其他抗癌药物(包括世界上一些最畅销的免疫疗法)结合使用。</p>\n<p>&nbsp;</p>\n<blockquote id=\"1MEHAILJ\">东芝接受JIP财团153亿美元收购</blockquote>\n<p>&nbsp;</p>\n<p class=\"f_center\"><img src=\"https://nimg.ws.126.net/?url=http%3A%2F%2Fdingyue.ws.126.net%2F2023%2F0404%2F8f200e91j00rsk9md001id200p000b4g00it008c.jpg&amp;thumbnail=660x2147483647&amp;quality=80&amp;type=jpg\"></p>\n<p id=\"1MEHAIKK\">拥有147年历史、但近年陷入挣扎的日本知名企业集团东芝(Toshiba)3月23日宣布，将接受以国内基金&ldquo;日本产业合作伙伴&rdquo;(JIP)为主的阵营提出的收购方案。收购额约为2万亿日元(约153亿美元)。JIP阵营力争大致在7月下旬开始要约收购。东芝考虑收购后摘牌退市，退市后提升企业价值再重新上市。JIP阵营中包括欧力士、罗姆等约20家日企，将提供部分收购资金。三井住友银行等组成的银团将向JIP提供最多总计1.2万亿日元的贷款以支持收购。</p>\n<p>&nbsp;</p>\n<blockquote id=\"1MEHAILK\">银湖财团收购软件销售商Qualtrics</blockquote>\n<p>&nbsp;</p>\n<p id=\"1MEHAIKM\">美国软件销售商Qualtrics International宣布达成交易，同意接受美国私募股权巨头银湖(Silver Lake)和加拿大最大养老基金CPPIB为首的财团收购，交易价格为125亿美元。这一交易达成之际，Qualtrics的大股东德国软件巨头思爱普(SAP)正试图剥离其在该公司的71%股份，作为集团重组战略的一部分。2018年，思爱普以80亿美元收购了Qualtrics，并于3年后在美国上市。Qualtrics是一家软件工具销售商，企业用这些产品来调查客户和员工。</p>\n<p>&nbsp;</p>\n<blockquote id=\"1MEHAILL\">Apollo基金收购尤尼威尔</blockquote>\n<p>&nbsp;</p>\n<p id=\"1MEHAIKO\">由全球另类资产管理公司Apollo附属公司管理的基金(Apollo Funds)将以全部现金交易方式收购特种化学品和原料分销商尤尼威尔解决方案(Univar Solutions)，此次交易对该公司的估价约为81亿美元。这项交易包括来自阿布扎比投资局(ADIA)全资子公司的少数股权投资。该合并协议已获得尤尼威尔董事会一致批准。交易完成后，尤尼威尔将成为一家私人控股公司。</p>\n<p id=\"1MEHAIKR\"><strong>中资并购</strong></p>\n<p id=\"1MEHAIKT\">沙特阿美已签署最终协议，收购荣盛石化10%的股权，收购价格为246亿元(约36亿美元)。该交易将大大扩大沙特阿美在中国的下游业务。</p>\n<p id=\"1MEHAIKV\">博格华纳公司(BorgWarner)宣布完成对湖北追日电气(SSE)电动汽车充电解决方案、智能电网和智能能源业务的收购。此次收购是博格华纳亚洲电气化业务中的一项重要举措，将对该公司在欧洲和北美的现有充电业务形成补充。</p>\n<p id=\"1MEHAIL1\"><strong>其他中小型并购</strong></p>\n<p id=\"1MEHAIL3\">防弹少年团的东家Hybe宣布与互联网巨头Kakao达成协议，决定停止对韩国第二大娱乐经纪公司SM娱乐(SM Entertainment)的竞购战。根据协议，Kakao将取得SM的经营权，Hybe将与其进行平台合作。Hybe表示，由于与Kakao的竞争加剧，收购SM的价格超出了公平的收购价格范围。Kakao表示，Kakao及其娱乐部门将在3月26日之前继续收购SM的股份，并将加强与Hybe和SM的业务合作。</p>\n<p id=\"1MEHAIL5\">电通集团(Dentsu Group)宣布已与安宏资本(Advent International)签订最终协议，收购全球全渠道数字营销制作巨头太意tag(Tag Worldwide Holdings)。此次收购将大大增强电通的创意数字生产能力，在全球29个国家/地区增加2800名员工，以及一个全球生产中心和十个专业中心。太意tag成立于1972年，于2017年被安宏资本收购。</p>\n<p id=\"1MEHAIL7\">法国制药集团赛诺菲(Sanofi)将以现金收购总部位于美国的自身免疫性疾病生物制药公司Provention Bio，交易的股权价值为29亿美元。该交易将为赛诺菲的产品组合中添加TZIELD，后者去年在美国获得批准，是首个用于延缓3期1型糖尿病(T1D)的疾病改善药物。Provention去年年底宣布与赛诺菲达成协议，共同在美国推广这种药物。</p>\n<p id=\"1MEHAIL9\">CF Industries Holdings同意以16.75亿美元的价格从澳大利亚Incitec Pivot手中收购位于美国路易斯安那州的Waggaman氨生产设施。两家公司表示，他们将从收购价中拿出约4.25亿美元用于长期氨供应协议，根据该协议，CF将向IPL的Dyno Nobel子公司每年供应多达20万吨的氨。</p>\n<p id=\"1MEHAILB\">挪威国家石油公司(Equinor)拟以8.5亿美元收购加拿大森科能源(Suncor Energy)的英国石油和天然气业务，以获得几处北海石油资产的股份。</p>\n<p id=\"1MEHAILD\">旅行技术公司Travelport宣布收购商务差旅管理平台Deem。自推出其下一代平台Travelport+以来，Travelport一直在创新方面进行投资，收购Deem则是最新的实例。Deem之前的所有人是移动出行解决方案提供商Enterprise Holdings。</p>\n</div>",
            "content_material_id": []
        }
        return data
    #修改单页
    def update_danye(self):
        data ={
            "title": "2023年3月，全球企业并购比前两个月明显活跃。瑞银宣布收购陷入危机的瑞信比较引人注目，辉瑞430亿美元收购Seagen是今年以来最大规模并购，东芝接受JIP财团153亿美元的收购方案。",
            "nav_id": 58,
            "publisher": "admin",
            "is_show": 0,
            "content": "<div class=\"post_body\">\n<p id=\"1MEHAIKA\"></p>\n<p id=\"1MEHAIKC\"><strong>大型并购</strong></p>\n<p>&nbsp;</p>\n<blockquote id=\"1MEHAILH\">瑞银宣布收购陷入危机的瑞信</blockquote>\n<p>&nbsp;</p>\n<p class=\"f_center\"><img src=\"https://nimg.ws.126.net/?url=http%3A%2F%2Fdingyue.ws.126.net%2F2023%2F0404%2F26bf1d03j00rsk9mc0026d200p000b4g00it008c.jpg&amp;thumbnail=660x2147483647&amp;quality=80&amp;type=jpg\"></p>\n<p id=\"1MEHAIKE\">瑞士第一大银行瑞银集团(UBS)当地时间3月19日宣布收购陷入危机的瑞士第二大银行集团瑞士信贷银行(Credit Suisse Group)，总对价30亿瑞士法郎。瑞士政府、央行及瑞士金融市场监管局对此表示支持，瑞士央行将提供1000亿瑞士法郎的流动性支持。同时，瑞士政府为瑞银接管的资产的潜在损失提供90亿瑞郎的担保。瑞士金融市场监管局表示，价值约160亿瑞郎的瑞信债券将被完全减记，以确保私人投资者帮助分担损失。</p>\n<p>&nbsp;</p>\n<blockquote id=\"1MEHAILI\">辉瑞430亿美元收购Seagen</blockquote>\n<p>&nbsp;</p>\n<p class=\"f_center\"><img src=\"https://nimg.ws.126.net/?url=http%3A%2F%2Fdingyue.ws.126.net%2F2023%2F0404%2F528b3fd6j00rsk9md000id200p000b4g00it008c.jpg&amp;thumbnail=660x2147483647&amp;quality=80&amp;type=jpg\"></p>\n<p id=\"1MEHAIKH\">辉瑞(Pfizer)宣布将以430亿美元的总企业价值收购美国生物技术公司Seagen。Seagen致力于开发和商业化用于治疗癌症的创新型增强型单克隆抗体疗法。该公司是抗体-药物缀合物(ADC)的行业领导者，该技术旨在利用单克隆抗体的靶向能力将细胞杀伤剂直接递送至癌细胞。ADC已开始获得用于某些常见癌症(如乳腺癌)的批准，Seagen已探索将它们与其他抗癌药物(包括世界上一些最畅销的免疫疗法)结合使用。</p>\n<p>&nbsp;</p>\n<blockquote id=\"1MEHAILJ\">东芝接受JIP财团153亿美元收购</blockquote>\n<p>&nbsp;</p>\n<p class=\"f_center\"><img src=\"https://nimg.ws.126.net/?url=http%3A%2F%2Fdingyue.ws.126.net%2F2023%2F0404%2F8f200e91j00rsk9md001id200p000b4g00it008c.jpg&amp;thumbnail=660x2147483647&amp;quality=80&amp;type=jpg\"></p>\n<p id=\"1MEHAIKK\">拥有147年历史、但近年陷入挣扎的日本知名企业集团东芝(Toshiba)3月23日宣布，将接受以国内基金&ldquo;日本产业合作伙伴&rdquo;(JIP)为主的阵营提出的收购方案。收购额约为2万亿日元(约153亿美元)。JIP阵营力争大致在7月下旬开始要约收购。东芝考虑收购后摘牌退市，退市后提升企业价值再重新上市。JIP阵营中包括欧力士、罗姆等约20家日企，将提供部分收购资金。三井住友银行等组成的银团将向JIP提供最多总计1.2万亿日元的贷款以支持收购。</p>\n<p>&nbsp;</p>\n<blockquote id=\"1MEHAILK\">银湖财团收购软件销售商Qualtrics</blockquote>\n<p>&nbsp;</p>\n<p id=\"1MEHAIKM\">美国软件销售商Qualtrics International宣布达成交易，同意接受美国私募股权巨头银湖(Silver Lake)和加拿大最大养老基金CPPIB为首的财团收购，交易价格为125亿美元。这一交易达成之际，Qualtrics的大股东德国软件巨头思爱普(SAP)正试图剥离其在该公司的71%股份，作为集团重组战略的一部分。2018年，思爱普以80亿美元收购了Qualtrics，并于3年后在美国上市。Qualtrics是一家软件工具销售商，企业用这些产品来调查客户和员工。</p>\n<p>&nbsp;</p>\n<blockquote id=\"1MEHAILL\">Apollo基金收购尤尼威尔</blockquote>\n<p>&nbsp;</p>\n<p id=\"1MEHAIKO\">由全球另类资产管理公司Apollo附属公司管理的基金(Apollo Funds)将以全部现金交易方式收购特种化学品和原料分销商尤尼威尔解决方案(Univar Solutions)，此次交易对该公司的估价约为81亿美元。这项交易包括来自阿布扎比投资局(ADIA)全资子公司的少数股权投资。该合并协议已获得尤尼威尔董事会一致批准。交易完成后，尤尼威尔将成为一家私人控股公司。</p>\n<p id=\"1MEHAIKR\"><strong>中资并购</strong></p>\n<p id=\"1MEHAIKT\">沙特阿美已签署最终协议，收购荣盛石化10%的股权，收购价格为246亿元(约36亿美元)。该交易将大大扩大沙特阿美在中国的下游业务。</p>\n<p id=\"1MEHAIKV\">博格华纳公司(BorgWarner)宣布完成对湖北追日电气(SSE)电动汽车充电解决方案、智能电网和智能能源业务的收购。此次收购是博格华纳亚洲电气化业务中的一项重要举措，将对该公司在欧洲和北美的现有充电业务形成补充。</p>\n<p id=\"1MEHAIL1\"><strong>其他中小型并购</strong></p>\n<p id=\"1MEHAIL3\">防弹少年团的东家Hybe宣布与互联网巨头Kakao达成协议，决定停止对韩国第二大娱乐经纪公司SM娱乐(SM Entertainment)的竞购战。根据协议，Kakao将取得SM的经营权，Hybe将与其进行平台合作。Hybe表示，由于与Kakao的竞争加剧，收购SM的价格超出了公平的收购价格范围。Kakao表示，Kakao及其娱乐部门将在3月26日之前继续收购SM的股份，并将加强与Hybe和SM的业务合作。</p>\n<p id=\"1MEHAIL5\">电通集团(Dentsu Group)宣布已与安宏资本(Advent International)签订最终协议，收购全球全渠道数字营销制作巨头太意tag(Tag Worldwide Holdings)。此次收购将大大增强电通的创意数字生产能力，在全球29个国家/地区增加2800名员工，以及一个全球生产中心和十个专业中心。太意tag成立于1972年，于2017年被安宏资本收购。</p>\n<p id=\"1MEHAIL7\">法国制药集团赛诺菲(Sanofi)将以现金收购总部位于美国的自身免疫性疾病生物制药公司Provention Bio，交易的股权价值为29亿美元。该交易将为赛诺菲的产品组合中添加TZIELD，后者去年在美国获得批准，是首个用于延缓3期1型糖尿病(T1D)的疾病改善药物。Provention去年年底宣布与赛诺菲达成协议，共同在美国推广这种药物。</p>\n<p id=\"1MEHAIL9\">CF Industries Holdings同意以16.75亿美元的价格从澳大利亚Incitec Pivot手中收购位于美国路易斯安那州的Waggaman氨生产设施。两家公司表示，他们将从收购价中拿出约4.25亿美元用于长期氨供应协议，根据该协议，CF将向IPL的Dyno Nobel子公司每年供应多达20万吨的氨。</p>\n<p id=\"1MEHAILB\">挪威国家石油公司(Equinor)拟以8.5亿美元收购加拿大森科能源(Suncor Energy)的英国石油和天然气业务，以获得几处北海石油资产的股份。</p>\n<p id=\"1MEHAILD\">旅行技术公司Travelport宣布收购商务差旅管理平台Deem。自推出其下一代平台Travelport+以来，Travelport一直在创新方面进行投资，收购Deem则是最新的实例。Deem之前的所有人是移动出行解决方案提供商Enterprise Holdings。</p>\n</div>",
            "content_material_id": []
        }
        return data
    #新增公司信息
    def gongsixinxi(self):
        data ={
            "company_name": "阿拉丁",
            "address": "南京市浦口区星火路128号",
            "postal_code": "990001",
            "company_phone": "987789987789",
            "fax": "021-88299999",
            "email": "999000111@163.com",
            "domain": "http://221.226.240.154:29090",
            "logo_url": None,
            "logo": None,
            "logo_material_id": None
        }
        return data
    #新增角色
    def add_juese(self):
        data ={
            "name": "采购员",
            "permission_ids": [
                3
            ],
            "status": 1
        }
        return data
    #修该角色
    def update_juese(self):
        data ={
            "name": "采购员",
            "permission_ids": [
                3,  # 采购管理
                2,  # 销售管理
                4  # 库存管理
            ],
            "status": 1,
            "_method": "PUT"
        }
        return data
    def delete_juese(self):
        data ={
            "_method": "DELETE"
        }
        return data
    #新增用户
    def add_yonghu(self,juese_id):
        data ={
            "username": "jws",
            "password": "123456",
            "name": "荆文硕",
            "role_ids": [
                juese_id
            ],
            "status": 1
        }
        return data
    #删除用户
    def delete_yonghu(self):
        data ={
            "_method": "DELETE"
        }
        return data
