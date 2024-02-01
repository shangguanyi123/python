import json
import random
import time
import pytest
from website_api.ichempro_api import *
from assertion import Assertion
from sql import MySQLHelper
@pytest.fixture()
def keshang_data():
    return {
        '客户编码':'',
        '拼音简称':'',
        '用户id':'',

        '省':{
            'id':'',
            'name':''
        },
        '市': {
            'id': '',
            'name': ''
        },
        '区': {
            'id': '',
            'name': ''
        },
        '文件':{
            'id':'',
            'filename':'',
            'file_url':''
        },
        '客户':{
            '用户id': '',
            '联系人id': '',

        },

    }
#新增客户-查询-修改-删除
def test_01(keshang_data):
    res1 = Keshangguanli().sel_kuhu_bianma()
    print('获取客户编码',res1.json())
    keshang_data['客户编码'] = res1.json()['data']
    res2 = Keshangguanli().sel_pinyin_jiancheng('上海美德精细化工有限公司')
    print('拼音简称',res2.json())
    keshang_data['拼音简称'] = res2.json()['data']
    res3 = Xitongguanli().sel_fuzhuziliao('','customer_source_channel','1')
    print('查询客户来源',res3.json())
    index = random.randint(0,len(res3.json()['data']['data'])-1)
    keshang_data['客户来源id'] = res3.json()['data']['data'][index]['value']['val']
    res4 = Xitongguanli().sel_fuzhuziliao('', 'customer_class', '1')
    print('查询客户类型', res4.json())
    index = random.randint(0, len(res4.json()['data']['data']) - 1)
    keshang_data['客户类型id'] = res4.json()['data']['data'][index]['value']['val']
    res5 = Xitongguanli().sel_fuzhuziliao('', 'customer_type', '1')
    print('查询客户性质', res5.json())
    index = random.randint(0, len(res5.json()['data']['data']) - 1)
    keshang_data['客户性质id'] = res5.json()['data']['data'][index]['value']['val']
    res6 = Xitongguanli().sel_fuzhuziliao('', 'customer_cooperation_status', '1')
    print('查询客户状态', res6.json())
    index = random.randint(0, len(res6.json()['data']['data']) - 1)
    keshang_data['客户状态id'] = res6.json()['data']['data'][index]['value']['val']
    res7 = Xitongguanli().sel_fuzhuziliao('', 'customer_user_level', '1')
    print('查询客户等级', res7.json())
    index = random.randint(0, len(res7.json()['data']['data']) - 1)
    keshang_data['客户等级id'] = res7.json()['data']['data'][index]['value']['val']
    res8 = Keshangguanli().sel_dizhi()
    #print(res8.json())
    sheng_id = random.randint(0,len(res8.json()['data'])-1)
    keshang_data['省']['id'] = res8.json()['data'][sheng_id]['id']
    keshang_data['省']['name'] = res8.json()['data'][sheng_id]['name_zh']
    shi_id = random.randint(0,len(res8.json()['data'][sheng_id]['children'])-1)
    keshang_data['市']['id'] = res8.json()['data'][sheng_id]['children'][shi_id]['id']
    keshang_data['市']['name'] = res8.json()['data'][sheng_id]['children'][shi_id]['name_zh']
    qu_id = random.randint(0,len(res8.json()['data'][sheng_id]['children'][shi_id]['children'])-1)
    keshang_data['区']['id'] = res8.json()['data'][sheng_id]['children'][shi_id]['children'][qu_id]['id']
    keshang_data['区']['name'] = res8.json()['data'][sheng_id]['children'][shi_id]['children'][qu_id]['name_zh']
    res9 = Chanpinguanli().cas_shangchuan_tupian(r'C:\Users\shangguanyi\Desktop\上官一\后台\157159616923482548.gif')
    print('上传文件',res9.json())
    keshang_data['文件']['id'] = res9.json()['data'][0]['id']
    res10 = Keshangguanli().sel_user(1,1)
    #print('用户查询',res10.json())
    index = random.randint(0,len(res10.json()['data']['data'])-1)
    keshang_data['用户id'] = res10.json()['data']['data'][index]['id']
    print(keshang_data)
    res = Keshangguanli().add_kehu(
        keshang_data['客户编码'],
        '上海美德精细化工有限公司',
        keshang_data['拼音简称'],
        keshang_data['客户来源id'],
        keshang_data['客户类型id'],
        keshang_data['客户性质id'],
        keshang_data['客户状态id'],
        keshang_data['用户id'],
        keshang_data['客户等级id'],
        '1',
        keshang_data['省']['id'],
        keshang_data['市']['id'],
        keshang_data['区']['id'],
        keshang_data['省']['name'],
        keshang_data['市']['name'],
        keshang_data['区']['name'],
        keshang_data['文件']['id']
    )
    print('新增客户',res.json())
    Assertion(res).add_kehu('上海美德精细化工有限公司')
    res11 = Keshangguanli().sel_kehu('上海美德精细化工有限公司')
    keshang_data['客户']['客户id'] = res11.json()['data']['data'][0]['id']
    res12 = Keshangguanli().sel_kehu_info(keshang_data['联系人id'])
    keshang_data['客户']['联系人id'] = res12.json()['data']['contacts'][0]['id']
    keshang_data['客户']['客户编码'] = res12.json()['data']['customer_no']
    keshang_data['客户']['客户名称'] = res12.json()['data']['customer_name']
    keshang_data['客户']['拼音'] = res12.json()['data']['customer_pinyin']
    res13 = Keshangguanli().update_kehu(
        keshang_data['客户']['客户id'],
        keshang_data['客户']['联系人id'],
        keshang_data['客户']['客户编码'],
        keshang_data['客户']['客户名称'],
        keshang_data['客户']['拼音'],
        keshang_data['客户']['客户编码'],
        keshang_data['客户']['客户编码'],
        keshang_data['客户']['客户编码'],
        keshang_data['客户']['客户编码'],
        keshang_data['客户']['客户编码'],
        keshang_data['客户']['客户编码'],


        '上海美德精细化工有限公司'

    )
def test_02(keshang_data):
    for i in  open(r'C:\Users\shangguanyi\Desktop\products.txt','r',encoding='utf-8'):
        new = i.split(',')
        print(new[0],new[1],new[2])
        res = Keshangguanli().add_supplier_product_catalog(43,new[0],new[2],new[1])
        print(res.json())


























