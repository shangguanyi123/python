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
    #�����ɹ�����
    def add_caigou(self,dqsj,purchase_no):
        payload ={
            "order_date": dqsj,
            "purchase_no": purchase_no,
            "purchaser_name": "admin",
            "supplier_po": "azAZ-0099",
            "purchase_supplier": {
                "label": "�Ĵ���Ӧ��",
                "value": 33
            },
            "purchase_supplier_contacts": {
                "id": 39,
                "mobile": "˭������",
                "name": "����"
            },
            "purchase_delivery_address": {
                "address": [
                    "ɽ��ʡ��Ҵ��������",
                    "����ʡ���Ű뵺������",
                    "�ຣʡ��ԭ������",
                    "���캣�������"
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
                "label": "�������ҽҩ",
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
                    "lead_time": "�ֻ�",
                    "note": ""
                },
                {
                    "prod_no": "16013-85-7",
                    "spec": "",
                    "pack_size": 1000,
                    "pack_unit": "kg",
                    "price": 10500,
                    "lead_time": "�ֻ�",
                    "note": ""
                }
            ]
        }
        return payload
    #�޸Ĳɹ�����
    def update_caigou(self,dqsj,purchase_no):
        payload ={
            "order_date": dqsj,
            "purchase_no": purchase_no,
            "purchaser_name": "admin",
            "supplier_po": "azAZ-0099",
            "purchase_supplier": {
                "value": 33,
                "label": "�Ĵ���Ӧ��"
            },
            "purchase_supplier_contacts": {
                "id": 39,
                "mobile": "18617102646",
                "name": "����"
            },
            "purchase_delivery_address": {
                "address": [
                    "ɽ��ʡ��Ҵ��������",
                    "����ʡ���Ű뵺������",
                    "�ຣʡ��ԭ������",
                    "���캣�������"
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
                "label": "�������ҽҩ"
            },
            "invoice_or_not": 1,
            "invoice_type": 1,
            "invoice_material": 1,
            "invoice_rate": 13,
            "note": "�Ӽ�����������",
            "purchase_prods": [
                {
                    "prod_no": "1074-82-4",
                    "spec": ">=80%",
                    "pack_size": 1,
                    "pack_unit": "kg",
                    "price": "99.50",
                    "lead_time": "�ֻ�",
                    "note": None
                },
                {
                    "prod_no": "16013-85-7",
                    "spec": ">=85%",
                    "pack_size": 1,
                    "pack_unit": "kg",
                    "price": 150.5,
                    "lead_time": "�ֻ�",
                    "note": None
                }
            ]
        }
        return payload
    #�����ʼ챨��
    def zhijianbaogao(self,dqsj):
        payload ={
            "system_company": {
                "company_name": "������",
                "address": "�Ͼ����ֿ����ǻ�·128��",
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
                "prod_name": "�ڱ��������ǰ�����",
                "mw": "102.2178",
                "prod_name_en": "24324324",
                "mdl": "",
                "storage_conditions": "���±���",
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
                    "result": "ͨ��"
                },
                {
                    "item": "����",
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
    #�ɹ����
    def ruku(self,purchase_no,dqsj,ruku_id):
        payload ={
            "supplier_name": "�Ĵ���Ӧ��",
            "purchase_no": purchase_no,
            "inventory_date": dqsj,
            "purchase_address_id": "Lorem ex sit sed,18617102646,ɽ��ʡ��Ҵ������������ʡ���Ű뵺�������ຣʡ��ԭ���������캣�������,pariatur cupidatat laborum in nisi",
            "delivery_date": dqsj,
            "odd_note": "�Ӽ�����������",
            "prod_list": [
                {
                    "prod_no": "1074-82-4",
                    "prod_name": "�ڱ��������ǰ�����",
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
                    "prod_name": "2,6-����-3-�������",
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
    #���������
    def qita_ruku(self,dqsj):
        payload ={
            "inventory_type": {
                "label": "��ӯ���",
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
                    "prod_name": "�����",
                    "purpose": 1,
                    "spec": "70%",
                    "note": "Σ��Ʒ"
                }
            ]
        }
        return payload
    #����
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
    #��Ʊ
    def caigou_shoupiao(self,dqsj,purchase_no,odd_no):
        payload ={
            "receipt_date": dqsj,
            "receipt_account": "0513HLWZX51320220151828",
            "purchase_company_header": {
                "label": "�������ҽҩ",
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
    #�������۶���
    def add_xiaoshou(self,dqsj,sales_no):
        payload ={
            "order_date": dqsj,
            "sales_no": sales_no,
            "salesperson": "admin",
            "po": "AZaz09.~",
            "customer": {
                "label": "���ҽҩ",
                "value": 54
            },
            "customer_contacts": {
                "id": 71,
                "mobile": "132902387463",
                "name": "���"
            },
            "customer_delivery_address": {
                "address": [
                    "�����",
                    "ֱϽ��",
                    "��ƽ��"
                ],
                "consignee": "���",
                "consigneeMobile": "1672893736",
                "detail": "100��",
                "note": None,
                "id": 93
            },
            "collection_account": {
                "label": "��ͨ����",
                "value": 12
            },
            "invoice_company": {
                "label": "�Ͼ�����A",
                "value": 15
            },
            "payment_method": {
                "label": "���",
                "value": 7
            },
            "payment_deadline": dqsj,
            "invoice_or_not": 1,
            "customer_invoice_company": {
                "label": "���ҽҩ",
                "value": 62
            },
            "invoice_type": 1,
            "invoice_material": 1,
            "invoice_rate": 13,
            "invoice_address": "�ϰ���,13848888888,������ֱϽ��������,�����ű�·2�����鹫˾A��1209",
            "sales_prods": [
                {
                    "prod_no": "1074-82-4",
                    "prod_name": "�ڱ��������ǰ�����",
                    "cas": "1074-82-4",
                    "spec": "",
                    "pack_size": 1,
                    "pack_unit": "kg",
                    "price": 1000,
                    "lead_time": "�ֻ�",
                    "note": ""
                },
                {
                    "prod_no": "16013-85-7",
                    "prod_name": "2,6-����-3-�������",
                    "cas": "16013-85-7",
                    "spec": "",
                    "pack_size": 1,
                    "pack_unit": "kg",
                    "price": 1000,
                    "lead_time": "�ֻ�",
                    "note": ""
                }
            ]
        }
        return payload
    #�޸����۶���
    def update_xiaoshou_order(self,dqsj,dqsj1,sales_no,id1,id2,order_id):
        payload ={
            "order_date": dqsj,
            "sales_no": sales_no,
            "salesperson": "admin",
            "po": "AZaz09.~",
            "customer": {
                "value": 54,
                "label": "���ҽҩ"
            },
            "customer_contacts": {
                "id": 71,
                "mobile": "132902387463",
                "name": "���"
            },
            "customer_delivery_address": {
                "address": [
                    "�����",
                    "ֱϽ��",
                    "��ƽ��"
                ],
                "consignee": "���",
                "consigneeMobile": "1672893736",
                "detail": "100��",
                "id": 93,
                "note": None
            },
            "collection_account": {
                "value": 12,
                "label": "��ͨ����"
            },
            "invoice_company": {
                "value": 15,
                "label": "�Ͼ�����A"
            },
            "payment_method": {
                "value": 7,
                "label": "���"
            },
            "payment_deadline": dqsj,
            "invoice_or_not": 1,
            "note": None,
            "customer_invoice_company": {
                "value": 62,
                "label": "���ҽҩ"
            },
            "invoice_type": 1,
            "invoice_material": 1,
            "invoice_rate": 13,
            "invoice_address": "�ϰ���,13848888888,������ֱϽ��������,�����ű�·2�����鹫˾A��1209",
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
                    "lead_time": "�ֻ�",
                    "logistics_info": None,
                    "note": "1*1000g",
                    "pack_size": 1,
                    "pack_unit": "kg",
                    "price": "1000.00",
                    "prod_name": "�ڱ��������ǰ�����",
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
                    "lead_time": "�ֻ�",
                    "logistics_info": None,
                    "note": "1*1000g",
                    "pack_size": 1,
                    "pack_unit": "kg",
                    "price": "1000.00",
                    "prod_name": "2,6-����-3-�������",
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
    #�տ�
    def xiaoshou_shoukuan(self,dqsj,sales_no,odd_no,id1,id2):
        payload ={
            "collection_date": dqsj,
            "collection_payment_type": 1,
            "collection_no": {
                "label": "��ͨ����",
                "value": 12
            },
            "sales_no": sales_no,
            "customer": {
                "label": "���ҽҩ",
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
    #�����տ�
    def xiaoshou_piliangshoukuan(self,dqsj,id1,id2,prod_no1,prod_no2,sales_no1,sales_no2):
        payload ={
            "collection_date": dqsj,
            "collection_payment_type": 1,
            "collection_no": {
                "label": "",
                "value": ""
            },
            "customer": {
                "label": "���ҽҩ",
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
    #��Ʊ
    def xiaoshou_kaipiao(self,dqsj,sales_no,odd_no,id1,id2):
        payload ={
            "invoice_date": dqsj,
            "invoice_no": "1234567890za-ZA",
            "company_header": {
                "label": "�Ͼ�����A",
                "value": 15
            },
            "invoice_type": 1,
            "invoice_material": 1,
            "invoice_rate": 13,
            "sales_no": sales_no,
            "deposit_bank_info": {
                "bank_account": "4528576543122234567",
                "bank_name": "�й������ֿ�֧��",
                "tax_account": "962345345124567890AZ"
            },
            "odd_no": odd_no,
            "prod_list": [
                {
                    "id": id1,
                    "cas": "1074-82-4",
                    "prod_no": "1074-82-4",
                    "prod_name": "�ڱ��������ǰ�����",
                    "spec": ">=80%",
                    "this_time_price": "1000.00",
                    "this_time_size": 1
                },
                {
                    "id": id2,
                    "cas": "16013-85-7",
                    "prod_no": "16013-85-7",
                    "prod_name": "2,6-����-3-�������",
                    "spec": ">=85%",
                    "this_time_price": "1000.00",
                    "this_time_size": 1
                }
            ]
        }
        return payload
    #���۷���
    def fahuo(self,dqsj,sales_no,chuku_id,id1,id2):
        payload ={
            "customer_contacts": {
                "id": "",
                "mobile": "",
                "name": "��Ůʿ"
            },
            "delivery_date": dqsj,
            "customer_delivery_address": {
                "label": "22,������ֱϽ��������,4443",
                "id": 91
            },
            "invoice_address": "�ϰ���,13848888888,������ֱϽ��������,�����ű�·2�����鹫˾A��1209",
            "sales_no": sales_no,  # ���۵���
            "odd_no": chuku_id,  # ������
            "prod_list": [
                {
                    "id": id1,
                    "prod_no": "1074-82-4",
                    "prod_name": "�ڱ��������ǰ�����",
                    "price": "1000.00",
                    "this_time_size": 1,
                    "pack_unit": "kg",
                    "delivery_note": "",
                    "purpose": 1
                },
                {
                    "id": id2,
                    "prod_no": "16013-85-7",
                    "prod_name": "2,6-����-3-�������",
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
    #���������
    def qita_fahuo(self,dqsj):
        payload ={
            "signature": "����ҽҩ",
            "inventory_type": {
                "label": "���������",
                "value": ""
            },
            "inventory_date": dqsj,
            "operation_user_id": 68,
            "note": "����",
            "operation_user_name": "admin",
            "prod_list": [
                {
                    "prod_no": "AKP-0506",
                    "cas": "QTRK-000001",
                    "pack_unit": "g",
                    "prod_name": "�����",
                    "purpose": 1,
                    "spec": "70%",
                    "note": "1*100g",
                    "current_inventory": "300g+112ml",
                    "this_time_size": 100
                }
            ]
        }
        return payload
    #������Ʒ��Ϣ
    def add_chanpin(self,number):
        data ={
            "prod_no": number,
            "cas": "",
            "mf": "C8H18",
            "prod_name": "����ϩ",
            "mw": "114.2285",
            "prod_name_en": "BD",
            "mdl": "",
            "storage_conditions": "����",
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
    #�޸ĳ�Ʒ��Ϣ
    def update_chanpin(self,number,id):
        data ={
            "prod_no": number,
            "cas": "19-0189",
            "mf": "C8H18",
            "prod_name": "����ϩ",
            "mw": "114.2285",
            "prod_name_en": "BD",
            "mdl": "",
            "storage_conditions": "����",
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
    #���ò�Ʒ��ǩ
    def set_chanpin_biaoqian(self):
        payload = {'tag_id[0]': '71',
                   'tag_id[1]': '69'}
        return payload

class Data_API2():
    #��������
    def add_daohang(self,name,model_type):
        payload = {
            'name': name,   #��������
            'position[0]': 1,   #����
            'position[1]': 2,   #�ײ�
            'model_type': model_type,    #����ģ��1��ҳ2�б�
            'rank': 10,     #����ֵ
            'is_show': 1    #��վ��ʾ
        }
        return payload
    #�޸ĵ���
    def update_daohang(self):
        payload = {
            'name': '��ҳ',
            'position[0]': 1,
            'position[1]': 2,
            'model_type': 4,
            'rank': 10,
            'href': 'https://yiyan.baidu.com',
            'is_show': 0  # ����ʾ
        }
        return payload
    #�����б�
    def add_liebiao(self,nav_id):
        data ={
            "title": "2023��3�£�ȫ����ҵ������ǰ���������Ի�Ծ�����������չ�����Σ�������űȽ�����עĿ������430����Ԫ�չ�Seagen�ǽ�����������ģ��������֥����JIP����153����Ԫ���չ�������",
            "nav_id": nav_id,  # ����
            "publisher": "admin",
            "is_top": 0,
            "is_show": 1,
            "content": "<div class=\"post_body\">\n<p id=\"1MEHAIKA\"></p>\n<p id=\"1MEHAIKC\"><strong>���Ͳ���</strong></p>\n<p>&nbsp;</p>\n<blockquote id=\"1MEHAILH\">���������չ�����Σ��������</blockquote>\n<p>&nbsp;</p>\n<p class=\"f_center\"><img src=\"https://nimg.ws.126.net/?url=http%3A%2F%2Fdingyue.ws.126.net%2F2023%2F0404%2F26bf1d03j00rsk9mc0026d200p000b4g00it008c.jpg&amp;thumbnail=660x2147483647&amp;quality=80&amp;type=jpg\"></p>\n<p id=\"1MEHAIKE\">��ʿ��һ��������������(UBS)����ʱ��3��19�������չ�����Σ������ʿ�ڶ������м�����ʿ�Ŵ�����(Credit Suisse Group)���ܶԼ�30����ʿ���ɡ���ʿ���������м���ʿ�����г���ֶܾԴ˱�ʾ֧�֣���ʿ���н��ṩ1000����ʿ���ɵ�������֧�֡�ͬʱ����ʿ����Ϊ�����ӹܵ��ʲ���Ǳ����ʧ�ṩ90�����ɵĵ�������ʿ�����г���ֱܾ�ʾ����ֵԼ160�����ɵ�����ծȯ������ȫ���ǣ���ȷ��˽��Ͷ���߰����ֵ���ʧ��</p>\n<p>&nbsp;</p>\n<blockquote id=\"1MEHAILI\">����430����Ԫ�չ�Seagen</blockquote>\n<p>&nbsp;</p>\n<p class=\"f_center\"><img src=\"https://nimg.ws.126.net/?url=http%3A%2F%2Fdingyue.ws.126.net%2F2023%2F0404%2F528b3fd6j00rsk9md000id200p000b4g00it008c.jpg&amp;thumbnail=660x2147483647&amp;quality=80&amp;type=jpg\"></p>\n<p id=\"1MEHAIKH\">����(Pfizer)��������430����Ԫ������ҵ��ֵ�չ��������＼����˾Seagen��Seagen�����ڿ�������ҵ���������ư�֢�Ĵ�������ǿ�͵���¡�����Ʒ����ù�˾�ǿ���-ҩ��׺����(ADC)����ҵ�쵼�ߣ��ü���ּ�����õ���¡����İ���������ϸ��ɱ�˼�ֱ�ӵ�������ϸ����ADC�ѿ�ʼ�������ĳЩ������֢(�����ٰ�)����׼��Seagen��̽������������������ҩ��(����������һЩ����������Ʒ�)���ʹ�á�</p>\n<p>&nbsp;</p>\n<blockquote id=\"1MEHAILJ\">��֥����JIP����153����Ԫ�չ�</blockquote>\n<p>&nbsp;</p>\n<p class=\"f_center\"><img src=\"https://nimg.ws.126.net/?url=http%3A%2F%2Fdingyue.ws.126.net%2F2023%2F0404%2F8f200e91j00rsk9md001id200p000b4g00it008c.jpg&amp;thumbnail=660x2147483647&amp;quality=80&amp;type=jpg\"></p>\n<p id=\"1MEHAIKK\">ӵ��147����ʷ�������������������ձ�֪����ҵ���Ŷ�֥(Toshiba)3��23���������������Թ��ڻ���&ldquo;�ձ���ҵ�������&rdquo;(JIP)Ϊ������Ӫ������չ��������չ���ԼΪ2������Ԫ(Լ153����Ԫ)��JIP��Ӫ����������7����Ѯ��ʼҪԼ�չ�����֥�����չ���ժ�����У����к�������ҵ��ֵ���������С�JIP��Ӫ�а���ŷ��ʿ����ķ��Լ20�����󣬽��ṩ�����չ��ʽ�����ס�����е���ɵ����Ž���JIP�ṩ����ܼ�1.2������Ԫ�Ĵ�����֧���չ���</p>\n<p>&nbsp;</p>\n<blockquote id=\"1MEHAILK\">���������չ����������Qualtrics</blockquote>\n<p>&nbsp;</p>\n<p id=\"1MEHAIKM\">�������������Qualtrics International������ɽ��ף�ͬ���������˽ļ��Ȩ��ͷ����(Silver Lake)�ͼ��ô�������ϻ���CPPIBΪ�׵Ĳ����չ������׼۸�Ϊ125����Ԫ����һ���״��֮�ʣ�Qualtrics�Ĵ�ɶ��¹������ͷ˼����(SAP)����ͼ�������ڸù�˾��71%�ɷݣ���Ϊ��������ս�Ե�һ���֡�2018�꣬˼������80����Ԫ�չ���Qualtrics������3������������С�Qualtrics��һ��������������̣���ҵ����Щ��Ʒ������ͻ���Ա����</p>\n<p>&nbsp;</p>\n<blockquote id=\"1MEHAILL\">Apollo�����չ���������</blockquote>\n<p>&nbsp;</p>\n<p id=\"1MEHAIKO\">��ȫ�������ʲ�����˾Apollo������˾����Ļ���(Apollo Funds)����ȫ���ֽ��׷�ʽ�չ����ֻ�ѧƷ��ԭ�Ϸ��������������������(Univar Solutions)���˴ν��׶Ըù�˾�Ĺ���ԼΪ81����Ԫ������װ������԰�������Ͷ�ʾ�(ADIA)ȫ���ӹ�˾��������ȨͶ�ʡ��úϲ�Э���ѻ�������������»�һ����׼��������ɺ�������������Ϊһ��˽�˿عɹ�˾��</p>\n<p id=\"1MEHAIKR\"><strong>���ʲ���</strong></p>\n<p id=\"1MEHAIKT\">ɳ�ذ�����ǩ������Э�飬�չ���ʢʯ��10%�Ĺ�Ȩ���չ��۸�Ϊ246��Ԫ(Լ36����Ԫ)���ý��׽��������ɳ�ذ������й�������ҵ��</p>\n<p id=\"1MEHAIKV\">�����ɹ�˾(BorgWarner)������ɶԺ���׷�յ���(SSE)�綯������������������ܵ�����������Դҵ����չ����˴��չ��ǲ��������޵�����ҵ���е�һ����Ҫ�ٴ룬���Ըù�˾��ŷ�޺ͱ��������г��ҵ���γɲ��䡣</p>\n<p id=\"1MEHAIL1\"><strong>������С�Ͳ���</strong></p>\n<p id=\"1MEHAIL3\">���������ŵĶ���Hybe�����뻥������ͷKakao���Э�飬����ֹͣ�Ժ����ڶ������־��͹�˾SM����(SM Entertainment)�ľ���ս������Э�飬Kakao��ȡ��SM�ľ�ӪȨ��Hybe���������ƽ̨������Hybe��ʾ��������Kakao�ľ����Ӿ磬�չ�SM�ļ۸񳬳��˹�ƽ���չ��۸�Χ��Kakao��ʾ��Kakao�������ֲ��Ž���3��26��֮ǰ�����չ�SM�Ĺɷݣ�������ǿ��Hybe��SM��ҵ�������</p>\n<p id=\"1MEHAIL5\">��ͨ����(Dentsu Group)�������밲���ʱ�(Advent International)ǩ������Э�飬�չ�ȫ��ȫ��������Ӫ��������ͷ̫��tag(Tag Worldwide Holdings)���˴��չ��������ǿ��ͨ�Ĵ�������������������ȫ��29������/��������2800��Ա�����Լ�һ��ȫ���������ĺ�ʮ��רҵ���ġ�̫��tag������1972�꣬��2017�걻�����ʱ��չ���</p>\n<p id=\"1MEHAIL7\">������ҩ������ŵ��(Sanofi)�����ֽ��չ��ܲ�λ�����������������Լ���������ҩ��˾Provention Bio�����׵Ĺ�Ȩ��ֵΪ29����Ԫ���ý��׽�Ϊ��ŵ�ƵĲ�Ʒ��������TZIELD������ȥ�������������׼�����׸������ӻ�3��1������(T1D)�ļ�������ҩ�Proventionȥ�������������ŵ�ƴ��Э�飬��ͬ�������ƹ�����ҩ�</p>\n<p id=\"1MEHAIL9\">CF Industries Holdingsͬ����16.75����Ԫ�ļ۸�ӰĴ�����Incitec Pivot�����չ�λ������·��˹�����ݵ�Waggaman��������ʩ�����ҹ�˾��ʾ�����ǽ����չ������ó�Լ4.25����Ԫ���ڳ��ڰ���ӦЭ�飬���ݸ�Э�飬CF����IPL��Dyno Nobel�ӹ�˾ÿ�깩Ӧ���20��ֵİ���</p>\n<p id=\"1MEHAILB\">Ų������ʯ�͹�˾(Equinor)����8.5����Ԫ�չ����ô�ɭ����Դ(Suncor Energy)��Ӣ��ʯ�ͺ���Ȼ��ҵ���Ի�ü�������ʯ���ʲ��Ĺɷݡ�</p>\n<p id=\"1MEHAILD\">���м�����˾Travelport�����չ�������ù���ƽ̨Deem�����Ƴ�����һ��ƽ̨Travelport+������Travelportһֱ�ڴ��·������Ͷ�ʣ��չ�Deem�������µ�ʵ����Deem֮ǰ�����������ƶ����н�������ṩ��Enterprise Holdings��</p>\n</div>\n<div class=\"post_statement\">\n<p>�ر���������������(����ͼƬ����Ƶ���������)Ϊ��ý��ƽ̨&ldquo;���׺�&rdquo;�û��ϴ�����������ƽ̨���ṩ��Ϣ�洢����</p>\n<p>Notice: The content above (including the pictures and videos if any) is uploaded and posted by a user of NetEase Hao, which is a social media platform and only provides information storage services.</p>\n<div class=\"_xhi4tc4xf89\"><iframe id=\"iframeu6407155_1\" src=\"https://pos.baidu.com/gcdm?conwid=670&amp;conhei=250&amp;rdid=6407155&amp;dc=3&amp;di=u6407155&amp;s1=462942594&amp;s2=1234862762&amp;dri=1&amp;dis=0&amp;dai=15&amp;ps=4627x585&amp;enu=encoding&amp;exps=110283,110277,110275,110261,110252,110011&amp;ant=0&amp;psi=e158abc9fd806e99&amp;dcb=___adblockplus_&amp;dtm=HTML_POST&amp;dvi=0.0&amp;dci=-1&amp;dpt=none&amp;tpr=1680747617453&amp;ti=%E8%BE%89%E7%91%9E430%E4%BA%BF%E7%BE%8E%E5%85%83%E6%94%B6%E8%B4%ADSeagen%EF%BC%9B%E7%91%9E%E9%93%B6%E6%94%B6%E8%B4%AD%E9%99%B7%E5%85%A5%E5%8D%B1%E6%9C%BA%E7%9A%84%E7%91%9E%E4%BF%A1%20%7C%202023%E5%B9%B43%E6%9C%88%E5%85%A8%E7%90%83%E4%BC%81%E4%B8%9A%E5%B9%B6%E8%B4%AD%7C%E8%82%A1%E6%9D%83%7C%E8%B4%A2%E5%9B%A2%7C%E7%91%9E%E5%A3%AB%E9%93%B6%E8%A1%8C%7C%E7%91%9E%E9%93%B6%E9%9B%86%E5%9B%A2&amp;ari=2&amp;ver=0327&amp;dbv=2&amp;drs=3&amp;pcs=2031x1010&amp;pss=2031x8945&amp;cfv=0&amp;cpl=5&amp;chi=1&amp;cce=true&amp;cec=UTF-8&amp;tlm=1680747617&amp;prot=2&amp;rw=1010&amp;ltu=https%3A%2F%2Fwww.163.com%2Fdy%2Farticle%2FI1F8Q261053159A3.html&amp;ltr=https%3A%2F%2Fwww.163.com%2Fdy%2Fmedia%2FT1542006074249.html&amp;ecd=1&amp;dft=0&amp;uc=2048x1112&amp;pis=-1x-1&amp;sr=2048x1152&amp;tcn=1680747618&amp;qn=79e08baef9601ae6&amp;ft=1\" name=\"iframeu6407155_1\" width=\"670\" height=\"250\" frameborder=\"0\" scrolling=\"no\"></iframe></div>\n</div>",
            "images_url": "http://221.226.240.154:29090/storage/2/default/20230406/cirn4m4EUsWFubzvHNV81paCLJ2XEgslw52yIchz_1.jpg",
            "images_material_id": 689,
            "content_material_id": []
        }
        return data
    #�޸��б�
    def update_liebiao(self):
        data ={
            "title": "2023��3�£�ȫ����ҵ������ǰ���������Ի�Ծ�����������չ�����Σ�������űȽ�����עĿ������430����Ԫ�չ�Seagen�ǽ�����������ģ��������֥����JIP����153����Ԫ���չ�������",
            "nav_id": 4,  # ������Ѷ
            "publisher": "admin",
            "rank": 0,
            "images": "2/default/20230406/cirn4m4EUsWFubzvHNV81paCLJ2XEgslw52yIchz_1.jpg",
            "is_top": 0,
            "is_show": 0,
            "description": "2023��3�£�ȫ����ҵ������ǰ���������Ի�Ծ�����������չ�����Σ�������űȽ�����עĿ������430����Ԫ�չ�Seagen�ǽ�����������ģ��������֥����JIP����153����Ԫ���չ�������",
            "content": "<div class=\"post_body\">\n<p id=\"1MEHAIKA\"></p>\n<p id=\"1MEHAIKC\"><strong>���Ͳ���</strong></p>\n<p>&nbsp;</p>\n<blockquote id=\"1MEHAILH\">���������չ�����Σ��������</blockquote>\n<p>&nbsp;</p>\n<p class=\"f_center\"><img src=\"https://nimg.ws.126.net/?url=http%3A%2F%2Fdingyue.ws.126.net%2F2023%2F0404%2F26bf1d03j00rsk9mc0026d200p000b4g00it008c.jpg&amp;thumbnail=660x2147483647&amp;quality=80&amp;type=jpg\"></p>\n<p id=\"1MEHAIKE\">��ʿ��һ��������������(UBS)����ʱ��3��19�������չ�����Σ������ʿ�ڶ������м�����ʿ�Ŵ�����(Credit Suisse Group)���ܶԼ�30����ʿ���ɡ���ʿ���������м���ʿ�����г���ֶܾԴ˱�ʾ֧�֣���ʿ���н��ṩ1000����ʿ���ɵ�������֧�֡�ͬʱ����ʿ����Ϊ�����ӹܵ��ʲ���Ǳ����ʧ�ṩ90�����ɵĵ�������ʿ�����г���ֱܾ�ʾ����ֵԼ160�����ɵ�����ծȯ������ȫ���ǣ���ȷ��˽��Ͷ���߰����ֵ���ʧ��</p>\n<p>&nbsp;</p>\n<blockquote id=\"1MEHAILI\">����430����Ԫ�չ�Seagen</blockquote>\n<p>&nbsp;</p>\n<p class=\"f_center\"><img src=\"https://nimg.ws.126.net/?url=http%3A%2F%2Fdingyue.ws.126.net%2F2023%2F0404%2F528b3fd6j00rsk9md000id200p000b4g00it008c.jpg&amp;thumbnail=660x2147483647&amp;quality=80&amp;type=jpg\"></p>\n<p id=\"1MEHAIKH\">����(Pfizer)��������430����Ԫ������ҵ��ֵ�չ��������＼����˾Seagen��Seagen�����ڿ�������ҵ���������ư�֢�Ĵ�������ǿ�͵���¡�����Ʒ����ù�˾�ǿ���-ҩ��׺����(ADC)����ҵ�쵼�ߣ��ü���ּ�����õ���¡����İ���������ϸ��ɱ�˼�ֱ�ӵ�������ϸ����ADC�ѿ�ʼ�������ĳЩ������֢(�����ٰ�)����׼��Seagen��̽������������������ҩ��(����������һЩ����������Ʒ�)���ʹ�á�</p>\n<p>&nbsp;</p>\n<blockquote id=\"1MEHAILJ\">��֥����JIP����153����Ԫ�չ�</blockquote>\n<p>&nbsp;</p>\n<p class=\"f_center\"><img src=\"https://nimg.ws.126.net/?url=http%3A%2F%2Fdingyue.ws.126.net%2F2023%2F0404%2F8f200e91j00rsk9md001id200p000b4g00it008c.jpg&amp;thumbnail=660x2147483647&amp;quality=80&amp;type=jpg\"></p>\n<p id=\"1MEHAIKK\">ӵ��147����ʷ�������������������ձ�֪����ҵ���Ŷ�֥(Toshiba)3��23���������������Թ��ڻ���&ldquo;�ձ���ҵ�������&rdquo;(JIP)Ϊ������Ӫ������չ��������չ���ԼΪ2������Ԫ(Լ153����Ԫ)��JIP��Ӫ����������7����Ѯ��ʼҪԼ�չ�����֥�����չ���ժ�����У����к�������ҵ��ֵ���������С�JIP��Ӫ�а���ŷ��ʿ����ķ��Լ20�����󣬽��ṩ�����չ��ʽ�����ס�����е���ɵ����Ž���JIP�ṩ����ܼ�1.2������Ԫ�Ĵ�����֧���չ���</p>\n<p>&nbsp;</p>\n<blockquote id=\"1MEHAILK\">���������չ����������Qualtrics</blockquote>\n<p>&nbsp;</p>\n<p id=\"1MEHAIKM\">�������������Qualtrics International������ɽ��ף�ͬ���������˽ļ��Ȩ��ͷ����(Silver Lake)�ͼ��ô�������ϻ���CPPIBΪ�׵Ĳ����չ������׼۸�Ϊ125����Ԫ����һ���״��֮�ʣ�Qualtrics�Ĵ�ɶ��¹������ͷ˼����(SAP)����ͼ�������ڸù�˾��71%�ɷݣ���Ϊ��������ս�Ե�һ���֡�2018�꣬˼������80����Ԫ�չ���Qualtrics������3������������С�Qualtrics��һ��������������̣���ҵ����Щ��Ʒ������ͻ���Ա����</p>\n<p>&nbsp;</p>\n<blockquote id=\"1MEHAILL\">Apollo�����չ���������</blockquote>\n<p>&nbsp;</p>\n<p id=\"1MEHAIKO\">��ȫ�������ʲ�����˾Apollo������˾����Ļ���(Apollo Funds)����ȫ���ֽ��׷�ʽ�չ����ֻ�ѧƷ��ԭ�Ϸ��������������������(Univar Solutions)���˴ν��׶Ըù�˾�Ĺ���ԼΪ81����Ԫ������װ������԰�������Ͷ�ʾ�(ADIA)ȫ���ӹ�˾��������ȨͶ�ʡ��úϲ�Э���ѻ�������������»�һ����׼��������ɺ�������������Ϊһ��˽�˿عɹ�˾��</p>\n<p id=\"1MEHAIKR\"><strong>���ʲ���</strong></p>\n<p id=\"1MEHAIKT\">ɳ�ذ�����ǩ������Э�飬�չ���ʢʯ��10%�Ĺ�Ȩ���չ��۸�Ϊ246��Ԫ(Լ36����Ԫ)���ý��׽��������ɳ�ذ������й�������ҵ��</p>\n<p id=\"1MEHAIKV\">�����ɹ�˾(BorgWarner)������ɶԺ���׷�յ���(SSE)�綯������������������ܵ�����������Դҵ����չ����˴��չ��ǲ��������޵�����ҵ���е�һ����Ҫ�ٴ룬���Ըù�˾��ŷ�޺ͱ��������г��ҵ���γɲ��䡣</p>\n<p id=\"1MEHAIL1\"><strong>������С�Ͳ���</strong></p>\n<p id=\"1MEHAIL3\">���������ŵĶ���Hybe�����뻥������ͷKakao���Э�飬����ֹͣ�Ժ����ڶ������־��͹�˾SM����(SM Entertainment)�ľ���ս������Э�飬Kakao��ȡ��SM�ľ�ӪȨ��Hybe���������ƽ̨������Hybe��ʾ��������Kakao�ľ����Ӿ磬�չ�SM�ļ۸񳬳��˹�ƽ���չ��۸�Χ��Kakao��ʾ��Kakao�������ֲ��Ž���3��26��֮ǰ�����չ�SM�Ĺɷݣ�������ǿ��Hybe��SM��ҵ�������</p>\n<p id=\"1MEHAIL5\">��ͨ����(Dentsu Group)�������밲���ʱ�(Advent International)ǩ������Э�飬�չ�ȫ��ȫ��������Ӫ��������ͷ̫��tag(Tag Worldwide Holdings)���˴��չ��������ǿ��ͨ�Ĵ�������������������ȫ��29������/��������2800��Ա�����Լ�һ��ȫ���������ĺ�ʮ��רҵ���ġ�̫��tag������1972�꣬��2017�걻�����ʱ��չ���</p>\n<p id=\"1MEHAIL7\">������ҩ������ŵ��(Sanofi)�����ֽ��չ��ܲ�λ�����������������Լ���������ҩ��˾Provention Bio�����׵Ĺ�Ȩ��ֵΪ29����Ԫ���ý��׽�Ϊ��ŵ�ƵĲ�Ʒ��������TZIELD������ȥ�������������׼�����׸������ӻ�3��1������(T1D)�ļ�������ҩ�Proventionȥ�������������ŵ�ƴ��Э�飬��ͬ�������ƹ�����ҩ�</p>\n<p id=\"1MEHAIL9\">CF Industries Holdingsͬ����16.75����Ԫ�ļ۸�ӰĴ�����Incitec Pivot�����չ�λ������·��˹�����ݵ�Waggaman��������ʩ�����ҹ�˾��ʾ�����ǽ����չ������ó�Լ4.25����Ԫ���ڳ��ڰ���ӦЭ�飬���ݸ�Э�飬CF����IPL��Dyno Nobel�ӹ�˾ÿ�깩Ӧ���20��ֵİ���</p>\n<p id=\"1MEHAILB\">Ų������ʯ�͹�˾(Equinor)����8.5����Ԫ�չ����ô�ɭ����Դ(Suncor Energy)��Ӣ��ʯ�ͺ���Ȼ��ҵ���Ի�ü�������ʯ���ʲ��Ĺɷݡ�</p>\n<p id=\"1MEHAILD\">���м�����˾Travelport�����չ�������ù���ƽ̨Deem�����Ƴ�����һ��ƽ̨Travelport+������Travelportһֱ�ڴ��·������Ͷ�ʣ��չ�Deem�������µ�ʵ����Deem֮ǰ�����������ƶ����н�������ṩ��Enterprise Holdings��</p>\n</div>\n<div class=\"post_statement\">\n<p>�ر���������������(����ͼƬ����Ƶ���������)Ϊ��ý��ƽ̨&ldquo;���׺�&rdquo;�û��ϴ�����������ƽ̨���ṩ��Ϣ�洢����</p>\n<p>Notice: The content above (including the pictures and videos if any) is uploaded and posted by a user of NetEase Hao, which is a social media platform and only provides information storage services.</p>\n<div class=\"_xhi4tc4xf89\"><iframe id=\"iframeu6407155_1\" src=\"https://pos.baidu.com/gcdm?conwid=670&amp;conhei=250&amp;rdid=6407155&amp;dc=3&amp;di=u6407155&amp;s1=462942594&amp;s2=1234862762&amp;dri=1&amp;dis=0&amp;dai=15&amp;ps=4627x585&amp;enu=encoding&amp;exps=110283,110277,110275,110261,110252,110011&amp;ant=0&amp;psi=e158abc9fd806e99&amp;dcb=___adblockplus_&amp;dtm=HTML_POST&amp;dvi=0.0&amp;dci=-1&amp;dpt=none&amp;tpr=1680747617453&amp;ti=%E8%BE%89%E7%91%9E430%E4%BA%BF%E7%BE%8E%E5%85%83%E6%94%B6%E8%B4%ADSeagen%EF%BC%9B%E7%91%9E%E9%93%B6%E6%94%B6%E8%B4%AD%E9%99%B7%E5%85%A5%E5%8D%B1%E6%9C%BA%E7%9A%84%E7%91%9E%E4%BF%A1%20%7C%202023%E5%B9%B43%E6%9C%88%E5%85%A8%E7%90%83%E4%BC%81%E4%B8%9A%E5%B9%B6%E8%B4%AD%7C%E8%82%A1%E6%9D%83%7C%E8%B4%A2%E5%9B%A2%7C%E7%91%9E%E5%A3%AB%E9%93%B6%E8%A1%8C%7C%E7%91%9E%E9%93%B6%E9%9B%86%E5%9B%A2&amp;ari=2&amp;ver=0327&amp;dbv=2&amp;drs=3&amp;pcs=2031x1010&amp;pss=2031x8945&amp;cfv=0&amp;cpl=5&amp;chi=1&amp;cce=true&amp;cec=UTF-8&amp;tlm=1680747617&amp;prot=2&amp;rw=1010&amp;ltu=https%3A%2F%2Fwww.163.com%2Fdy%2Farticle%2FI1F8Q261053159A3.html&amp;ltr=https%3A%2F%2Fwww.163.com%2Fdy%2Fmedia%2FT1542006074249.html&amp;ecd=1&amp;dft=0&amp;uc=2048x1112&amp;pis=-1x-1&amp;sr=2048x1152&amp;tcn=1680747618&amp;qn=79e08baef9601ae6&amp;ft=1\" name=\"iframeu6407155_1\" width=\"670\" height=\"250\" frameborder=\"0\" scrolling=\"no\"></iframe></div>\n</div>",
            "images_url": "http://221.226.240.154:29090/storage/2/default/20230406/cirn4m4EUsWFubzvHNV81paCLJ2XEgslw52yIchz_1.jpg",
            "images_material_id": None,
            "content_material_id": []
        }
        return data
    #������ҳ
    def add_danye(self,nav_id):
        data ={
            "title": "2023��3�£�ȫ����ҵ������ǰ���������Ի�Ծ�����������չ�����Σ�������űȽ�����עĿ������430����Ԫ�չ�Seagen�ǽ�����������ģ��������֥����JIP����153����Ԫ���չ�������",
            "nav_id": nav_id,
            "publisher": "admin",
            "is_show": 1,
            "content": "<div class=\"post_body\">\n<p id=\"1MEHAIKA\"></p>\n<p id=\"1MEHAIKC\"><strong>���Ͳ���</strong></p>\n<p>&nbsp;</p>\n<blockquote id=\"1MEHAILH\">���������չ�����Σ��������</blockquote>\n<p>&nbsp;</p>\n<p class=\"f_center\"><img src=\"https://nimg.ws.126.net/?url=http%3A%2F%2Fdingyue.ws.126.net%2F2023%2F0404%2F26bf1d03j00rsk9mc0026d200p000b4g00it008c.jpg&amp;thumbnail=660x2147483647&amp;quality=80&amp;type=jpg\"></p>\n<p id=\"1MEHAIKE\">��ʿ��һ��������������(UBS)����ʱ��3��19�������չ�����Σ������ʿ�ڶ������м�����ʿ�Ŵ�����(Credit Suisse Group)���ܶԼ�30����ʿ���ɡ���ʿ���������м���ʿ�����г���ֶܾԴ˱�ʾ֧�֣���ʿ���н��ṩ1000����ʿ���ɵ�������֧�֡�ͬʱ����ʿ����Ϊ�����ӹܵ��ʲ���Ǳ����ʧ�ṩ90�����ɵĵ�������ʿ�����г���ֱܾ�ʾ����ֵԼ160�����ɵ�����ծȯ������ȫ���ǣ���ȷ��˽��Ͷ���߰����ֵ���ʧ��</p>\n<p>&nbsp;</p>\n<blockquote id=\"1MEHAILI\">����430����Ԫ�չ�Seagen</blockquote>\n<p>&nbsp;</p>\n<p class=\"f_center\"><img src=\"https://nimg.ws.126.net/?url=http%3A%2F%2Fdingyue.ws.126.net%2F2023%2F0404%2F528b3fd6j00rsk9md000id200p000b4g00it008c.jpg&amp;thumbnail=660x2147483647&amp;quality=80&amp;type=jpg\"></p>\n<p id=\"1MEHAIKH\">����(Pfizer)��������430����Ԫ������ҵ��ֵ�չ��������＼����˾Seagen��Seagen�����ڿ�������ҵ���������ư�֢�Ĵ�������ǿ�͵���¡�����Ʒ����ù�˾�ǿ���-ҩ��׺����(ADC)����ҵ�쵼�ߣ��ü���ּ�����õ���¡����İ���������ϸ��ɱ�˼�ֱ�ӵ�������ϸ����ADC�ѿ�ʼ�������ĳЩ������֢(�����ٰ�)����׼��Seagen��̽������������������ҩ��(����������һЩ����������Ʒ�)���ʹ�á�</p>\n<p>&nbsp;</p>\n<blockquote id=\"1MEHAILJ\">��֥����JIP����153����Ԫ�չ�</blockquote>\n<p>&nbsp;</p>\n<p class=\"f_center\"><img src=\"https://nimg.ws.126.net/?url=http%3A%2F%2Fdingyue.ws.126.net%2F2023%2F0404%2F8f200e91j00rsk9md001id200p000b4g00it008c.jpg&amp;thumbnail=660x2147483647&amp;quality=80&amp;type=jpg\"></p>\n<p id=\"1MEHAIKK\">ӵ��147����ʷ�������������������ձ�֪����ҵ���Ŷ�֥(Toshiba)3��23���������������Թ��ڻ���&ldquo;�ձ���ҵ�������&rdquo;(JIP)Ϊ������Ӫ������չ��������չ���ԼΪ2������Ԫ(Լ153����Ԫ)��JIP��Ӫ����������7����Ѯ��ʼҪԼ�չ�����֥�����չ���ժ�����У����к�������ҵ��ֵ���������С�JIP��Ӫ�а���ŷ��ʿ����ķ��Լ20�����󣬽��ṩ�����չ��ʽ�����ס�����е���ɵ����Ž���JIP�ṩ����ܼ�1.2������Ԫ�Ĵ�����֧���չ���</p>\n<p>&nbsp;</p>\n<blockquote id=\"1MEHAILK\">���������չ����������Qualtrics</blockquote>\n<p>&nbsp;</p>\n<p id=\"1MEHAIKM\">�������������Qualtrics International������ɽ��ף�ͬ���������˽ļ��Ȩ��ͷ����(Silver Lake)�ͼ��ô�������ϻ���CPPIBΪ�׵Ĳ����չ������׼۸�Ϊ125����Ԫ����һ���״��֮�ʣ�Qualtrics�Ĵ�ɶ��¹������ͷ˼����(SAP)����ͼ�������ڸù�˾��71%�ɷݣ���Ϊ��������ս�Ե�һ���֡�2018�꣬˼������80����Ԫ�չ���Qualtrics������3������������С�Qualtrics��һ��������������̣���ҵ����Щ��Ʒ������ͻ���Ա����</p>\n<p>&nbsp;</p>\n<blockquote id=\"1MEHAILL\">Apollo�����չ���������</blockquote>\n<p>&nbsp;</p>\n<p id=\"1MEHAIKO\">��ȫ�������ʲ�����˾Apollo������˾����Ļ���(Apollo Funds)����ȫ���ֽ��׷�ʽ�չ����ֻ�ѧƷ��ԭ�Ϸ��������������������(Univar Solutions)���˴ν��׶Ըù�˾�Ĺ���ԼΪ81����Ԫ������װ������԰�������Ͷ�ʾ�(ADIA)ȫ���ӹ�˾��������ȨͶ�ʡ��úϲ�Э���ѻ�������������»�һ����׼��������ɺ�������������Ϊһ��˽�˿عɹ�˾��</p>\n<p id=\"1MEHAIKR\"><strong>���ʲ���</strong></p>\n<p id=\"1MEHAIKT\">ɳ�ذ�����ǩ������Э�飬�չ���ʢʯ��10%�Ĺ�Ȩ���չ��۸�Ϊ246��Ԫ(Լ36����Ԫ)���ý��׽��������ɳ�ذ������й�������ҵ��</p>\n<p id=\"1MEHAIKV\">�����ɹ�˾(BorgWarner)������ɶԺ���׷�յ���(SSE)�綯������������������ܵ�����������Դҵ����չ����˴��չ��ǲ��������޵�����ҵ���е�һ����Ҫ�ٴ룬���Ըù�˾��ŷ�޺ͱ��������г��ҵ���γɲ��䡣</p>\n<p id=\"1MEHAIL1\"><strong>������С�Ͳ���</strong></p>\n<p id=\"1MEHAIL3\">���������ŵĶ���Hybe�����뻥������ͷKakao���Э�飬����ֹͣ�Ժ����ڶ������־��͹�˾SM����(SM Entertainment)�ľ���ս������Э�飬Kakao��ȡ��SM�ľ�ӪȨ��Hybe���������ƽ̨������Hybe��ʾ��������Kakao�ľ����Ӿ磬�չ�SM�ļ۸񳬳��˹�ƽ���չ��۸�Χ��Kakao��ʾ��Kakao�������ֲ��Ž���3��26��֮ǰ�����չ�SM�Ĺɷݣ�������ǿ��Hybe��SM��ҵ�������</p>\n<p id=\"1MEHAIL5\">��ͨ����(Dentsu Group)�������밲���ʱ�(Advent International)ǩ������Э�飬�չ�ȫ��ȫ��������Ӫ��������ͷ̫��tag(Tag Worldwide Holdings)���˴��չ��������ǿ��ͨ�Ĵ�������������������ȫ��29������/��������2800��Ա�����Լ�һ��ȫ���������ĺ�ʮ��רҵ���ġ�̫��tag������1972�꣬��2017�걻�����ʱ��չ���</p>\n<p id=\"1MEHAIL7\">������ҩ������ŵ��(Sanofi)�����ֽ��չ��ܲ�λ�����������������Լ���������ҩ��˾Provention Bio�����׵Ĺ�Ȩ��ֵΪ29����Ԫ���ý��׽�Ϊ��ŵ�ƵĲ�Ʒ��������TZIELD������ȥ�������������׼�����׸������ӻ�3��1������(T1D)�ļ�������ҩ�Proventionȥ�������������ŵ�ƴ��Э�飬��ͬ�������ƹ�����ҩ�</p>\n<p id=\"1MEHAIL9\">CF Industries Holdingsͬ����16.75����Ԫ�ļ۸�ӰĴ�����Incitec Pivot�����չ�λ������·��˹�����ݵ�Waggaman��������ʩ�����ҹ�˾��ʾ�����ǽ����չ������ó�Լ4.25����Ԫ���ڳ��ڰ���ӦЭ�飬���ݸ�Э�飬CF����IPL��Dyno Nobel�ӹ�˾ÿ�깩Ӧ���20��ֵİ���</p>\n<p id=\"1MEHAILB\">Ų������ʯ�͹�˾(Equinor)����8.5����Ԫ�չ����ô�ɭ����Դ(Suncor Energy)��Ӣ��ʯ�ͺ���Ȼ��ҵ���Ի�ü�������ʯ���ʲ��Ĺɷݡ�</p>\n<p id=\"1MEHAILD\">���м�����˾Travelport�����չ�������ù���ƽ̨Deem�����Ƴ�����һ��ƽ̨Travelport+������Travelportһֱ�ڴ��·������Ͷ�ʣ��չ�Deem�������µ�ʵ����Deem֮ǰ�����������ƶ����н�������ṩ��Enterprise Holdings��</p>\n</div>",
            "content_material_id": []
        }
        return data
    #�޸ĵ�ҳ
    def update_danye(self):
        data ={
            "title": "2023��3�£�ȫ����ҵ������ǰ���������Ի�Ծ�����������չ�����Σ�������űȽ�����עĿ������430����Ԫ�չ�Seagen�ǽ�����������ģ��������֥����JIP����153����Ԫ���չ�������",
            "nav_id": 58,
            "publisher": "admin",
            "is_show": 0,
            "content": "<div class=\"post_body\">\n<p id=\"1MEHAIKA\"></p>\n<p id=\"1MEHAIKC\"><strong>���Ͳ���</strong></p>\n<p>&nbsp;</p>\n<blockquote id=\"1MEHAILH\">���������չ�����Σ��������</blockquote>\n<p>&nbsp;</p>\n<p class=\"f_center\"><img src=\"https://nimg.ws.126.net/?url=http%3A%2F%2Fdingyue.ws.126.net%2F2023%2F0404%2F26bf1d03j00rsk9mc0026d200p000b4g00it008c.jpg&amp;thumbnail=660x2147483647&amp;quality=80&amp;type=jpg\"></p>\n<p id=\"1MEHAIKE\">��ʿ��һ��������������(UBS)����ʱ��3��19�������չ�����Σ������ʿ�ڶ������м�����ʿ�Ŵ�����(Credit Suisse Group)���ܶԼ�30����ʿ���ɡ���ʿ���������м���ʿ�����г���ֶܾԴ˱�ʾ֧�֣���ʿ���н��ṩ1000����ʿ���ɵ�������֧�֡�ͬʱ����ʿ����Ϊ�����ӹܵ��ʲ���Ǳ����ʧ�ṩ90�����ɵĵ�������ʿ�����г���ֱܾ�ʾ����ֵԼ160�����ɵ�����ծȯ������ȫ���ǣ���ȷ��˽��Ͷ���߰����ֵ���ʧ��</p>\n<p>&nbsp;</p>\n<blockquote id=\"1MEHAILI\">����430����Ԫ�չ�Seagen</blockquote>\n<p>&nbsp;</p>\n<p class=\"f_center\"><img src=\"https://nimg.ws.126.net/?url=http%3A%2F%2Fdingyue.ws.126.net%2F2023%2F0404%2F528b3fd6j00rsk9md000id200p000b4g00it008c.jpg&amp;thumbnail=660x2147483647&amp;quality=80&amp;type=jpg\"></p>\n<p id=\"1MEHAIKH\">����(Pfizer)��������430����Ԫ������ҵ��ֵ�չ��������＼����˾Seagen��Seagen�����ڿ�������ҵ���������ư�֢�Ĵ�������ǿ�͵���¡�����Ʒ����ù�˾�ǿ���-ҩ��׺����(ADC)����ҵ�쵼�ߣ��ü���ּ�����õ���¡����İ���������ϸ��ɱ�˼�ֱ�ӵ�������ϸ����ADC�ѿ�ʼ�������ĳЩ������֢(�����ٰ�)����׼��Seagen��̽������������������ҩ��(����������һЩ����������Ʒ�)���ʹ�á�</p>\n<p>&nbsp;</p>\n<blockquote id=\"1MEHAILJ\">��֥����JIP����153����Ԫ�չ�</blockquote>\n<p>&nbsp;</p>\n<p class=\"f_center\"><img src=\"https://nimg.ws.126.net/?url=http%3A%2F%2Fdingyue.ws.126.net%2F2023%2F0404%2F8f200e91j00rsk9md001id200p000b4g00it008c.jpg&amp;thumbnail=660x2147483647&amp;quality=80&amp;type=jpg\"></p>\n<p id=\"1MEHAIKK\">ӵ��147����ʷ�������������������ձ�֪����ҵ���Ŷ�֥(Toshiba)3��23���������������Թ��ڻ���&ldquo;�ձ���ҵ�������&rdquo;(JIP)Ϊ������Ӫ������չ��������չ���ԼΪ2������Ԫ(Լ153����Ԫ)��JIP��Ӫ����������7����Ѯ��ʼҪԼ�չ�����֥�����չ���ժ�����У����к�������ҵ��ֵ���������С�JIP��Ӫ�а���ŷ��ʿ����ķ��Լ20�����󣬽��ṩ�����չ��ʽ�����ס�����е���ɵ����Ž���JIP�ṩ����ܼ�1.2������Ԫ�Ĵ�����֧���չ���</p>\n<p>&nbsp;</p>\n<blockquote id=\"1MEHAILK\">���������չ����������Qualtrics</blockquote>\n<p>&nbsp;</p>\n<p id=\"1MEHAIKM\">�������������Qualtrics International������ɽ��ף�ͬ���������˽ļ��Ȩ��ͷ����(Silver Lake)�ͼ��ô�������ϻ���CPPIBΪ�׵Ĳ����չ������׼۸�Ϊ125����Ԫ����һ���״��֮�ʣ�Qualtrics�Ĵ�ɶ��¹������ͷ˼����(SAP)����ͼ�������ڸù�˾��71%�ɷݣ���Ϊ��������ս�Ե�һ���֡�2018�꣬˼������80����Ԫ�չ���Qualtrics������3������������С�Qualtrics��һ��������������̣���ҵ����Щ��Ʒ������ͻ���Ա����</p>\n<p>&nbsp;</p>\n<blockquote id=\"1MEHAILL\">Apollo�����չ���������</blockquote>\n<p>&nbsp;</p>\n<p id=\"1MEHAIKO\">��ȫ�������ʲ�����˾Apollo������˾����Ļ���(Apollo Funds)����ȫ���ֽ��׷�ʽ�չ����ֻ�ѧƷ��ԭ�Ϸ��������������������(Univar Solutions)���˴ν��׶Ըù�˾�Ĺ���ԼΪ81����Ԫ������װ������԰�������Ͷ�ʾ�(ADIA)ȫ���ӹ�˾��������ȨͶ�ʡ��úϲ�Э���ѻ�������������»�һ����׼��������ɺ�������������Ϊһ��˽�˿عɹ�˾��</p>\n<p id=\"1MEHAIKR\"><strong>���ʲ���</strong></p>\n<p id=\"1MEHAIKT\">ɳ�ذ�����ǩ������Э�飬�չ���ʢʯ��10%�Ĺ�Ȩ���չ��۸�Ϊ246��Ԫ(Լ36����Ԫ)���ý��׽��������ɳ�ذ������й�������ҵ��</p>\n<p id=\"1MEHAIKV\">�����ɹ�˾(BorgWarner)������ɶԺ���׷�յ���(SSE)�綯������������������ܵ�����������Դҵ����չ����˴��չ��ǲ��������޵�����ҵ���е�һ����Ҫ�ٴ룬���Ըù�˾��ŷ�޺ͱ��������г��ҵ���γɲ��䡣</p>\n<p id=\"1MEHAIL1\"><strong>������С�Ͳ���</strong></p>\n<p id=\"1MEHAIL3\">���������ŵĶ���Hybe�����뻥������ͷKakao���Э�飬����ֹͣ�Ժ����ڶ������־��͹�˾SM����(SM Entertainment)�ľ���ս������Э�飬Kakao��ȡ��SM�ľ�ӪȨ��Hybe���������ƽ̨������Hybe��ʾ��������Kakao�ľ����Ӿ磬�չ�SM�ļ۸񳬳��˹�ƽ���չ��۸�Χ��Kakao��ʾ��Kakao�������ֲ��Ž���3��26��֮ǰ�����չ�SM�Ĺɷݣ�������ǿ��Hybe��SM��ҵ�������</p>\n<p id=\"1MEHAIL5\">��ͨ����(Dentsu Group)�������밲���ʱ�(Advent International)ǩ������Э�飬�չ�ȫ��ȫ��������Ӫ��������ͷ̫��tag(Tag Worldwide Holdings)���˴��չ��������ǿ��ͨ�Ĵ�������������������ȫ��29������/��������2800��Ա�����Լ�һ��ȫ���������ĺ�ʮ��רҵ���ġ�̫��tag������1972�꣬��2017�걻�����ʱ��չ���</p>\n<p id=\"1MEHAIL7\">������ҩ������ŵ��(Sanofi)�����ֽ��չ��ܲ�λ�����������������Լ���������ҩ��˾Provention Bio�����׵Ĺ�Ȩ��ֵΪ29����Ԫ���ý��׽�Ϊ��ŵ�ƵĲ�Ʒ��������TZIELD������ȥ�������������׼�����׸������ӻ�3��1������(T1D)�ļ�������ҩ�Proventionȥ�������������ŵ�ƴ��Э�飬��ͬ�������ƹ�����ҩ�</p>\n<p id=\"1MEHAIL9\">CF Industries Holdingsͬ����16.75����Ԫ�ļ۸�ӰĴ�����Incitec Pivot�����չ�λ������·��˹�����ݵ�Waggaman��������ʩ�����ҹ�˾��ʾ�����ǽ����չ������ó�Լ4.25����Ԫ���ڳ��ڰ���ӦЭ�飬���ݸ�Э�飬CF����IPL��Dyno Nobel�ӹ�˾ÿ�깩Ӧ���20��ֵİ���</p>\n<p id=\"1MEHAILB\">Ų������ʯ�͹�˾(Equinor)����8.5����Ԫ�չ����ô�ɭ����Դ(Suncor Energy)��Ӣ��ʯ�ͺ���Ȼ��ҵ���Ի�ü�������ʯ���ʲ��Ĺɷݡ�</p>\n<p id=\"1MEHAILD\">���м�����˾Travelport�����չ�������ù���ƽ̨Deem�����Ƴ�����һ��ƽ̨Travelport+������Travelportһֱ�ڴ��·������Ͷ�ʣ��չ�Deem�������µ�ʵ����Deem֮ǰ�����������ƶ����н�������ṩ��Enterprise Holdings��</p>\n</div>",
            "content_material_id": []
        }
        return data
    #������˾��Ϣ
    def gongsixinxi(self):
        data ={
            "company_name": "������",
            "address": "�Ͼ����ֿ����ǻ�·128��",
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
    #������ɫ
    def add_juese(self):
        data ={
            "name": "�ɹ�Ա",
            "permission_ids": [
                3
            ],
            "status": 1
        }
        return data
    #�޸ý�ɫ
    def update_juese(self):
        data ={
            "name": "�ɹ�Ա",
            "permission_ids": [
                3,  # �ɹ�����
                2,  # ���۹���
                4  # ������
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
    #�����û�
    def add_yonghu(self,juese_id):
        data ={
            "username": "jws",
            "password": "123456",
            "name": "����˶",
            "role_ids": [
                juese_id
            ],
            "status": 1
        }
        return data
    #ɾ���û�
    def delete_yonghu(self):
        data ={
            "_method": "DELETE"
        }
        return data
