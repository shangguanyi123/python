# encoding=utf-8
import json
import random
import time
import pytest
from API_case.API1 import Chanpinguanli, Xitongguanli
from assertion import Assertion
from sql import MySQLHelper

db = MySQLHelper()


@pytest.fixture()
def chain_data():
    return {
        '一级测试产品分类id': [],
        '二级测试产品分类id': [],
        '产品编号': '',
        '危险品标识id': '',
        '品牌id': '',
        '品牌名称': '',
        '包装id': '',
        '包装名称': '',
        '计量id': '',
        '计量名称': '',
        'mol': {
            'id': '',
            'filename': '',
            'path_url': '',
            '分子式': '',
            '分子量': '',
            '分子结构': ''
        },
        '图片': {
            'id': '',
            'filename': '',
            'path_url': ''
        },
        '辅助属性': {},
        '产品': {
            '产品id': '',
            '产品编号': '',
            'cas':'',
            '产品名称':'',
            '产品分类': '',
            '产品类型': '',
            '储存条件': '',
            '危险品标签id': '',
            '产品属性': '',
            '图片': {
                'id':'',
                '名称':'',
                'url':''
            },
            '规格id': '',
            '规格编号': '',
            '纯度': '',
            '品牌id': '',
            '品牌名称': '',
            '计量id': '',
            '计量名称': '',
            '包装id': '',
            '包装名称': '',
            '单位转换':'',
            '包装': '',
            '价格': '',
            '货期': ''
        },
        '': [],

    }

# 新增产品分类
def test_01_a(chain_data):
    print(
        '新增一级产品分类(状态开启)-查询一级产品分类-修改一级产品分类-查询-新增二级产品分类(状态开启)-查询二级产品分类-修改二级产品分类-查询-删除二级产品分类-删除一级产品分类')
    # 新增一级产品分类
    res1 = Chanpinguanli().add_chanpinfenlei(0, int(time.time()), '一级测试产品分类', 1, '1')
    print('新增一级产品分类', res1.json())
    Assertion(res1).tongyong()
    # 查询一级测试产品分类
    res2 = Chanpinguanli().sel_chanpinfenlei('一级测试产品分类')
    print('查询一级测试产品分类', res2.json())
    Assertion(res2).chapinfenlei_chaxun(1, '一级测试产品分类')
    chain_data.update({'一级测试产品分类id': res2.json()['data']['data'][0]['id']})
    # 修改一级测试产品分类
    res6 = Chanpinguanli().update_chanpinfenlei(0, chain_data['一级测试产品分类id'], int(time.time()),
                                                '一级测试产品分类test', 0, 1)
    print('修改一级测试产品分类', res6.json())
    Assertion(res6).tongyong()
    # 查询一级测试产品分类
    res9 = Chanpinguanli().sel_chanpinfenlei('一级测试产品分类test')
    print('查询一级测试产品分类test', res9.json())
    Assertion(res9).chapinfenlei_chaxun(1, '一级测试产品分类test')
    chain_data.update({'一级测试产品分类id': res9.json()['data']['data'][0]['id']})
    # 新增二级测试产品分类
    res3 = Chanpinguanli().add_chanpinfenlei(1, int(time.time()), '二级测试产品分类', 1, 1,
                                             chain_data['一级测试产品分类id'])
    print('新增二级测试产品分类', res3.json())
    Assertion(res3).tongyong()
    # 查询二级测试产品分类
    res4 = Chanpinguanli().sel_chanpinfenlei('二级测试产品分类')
    print('查询二级测试产品分类', res4.json())
    Assertion(res4).chapinfenlei_chaxun(1, '二级测试产品分类')
    chain_data.update({'二级测试产品分类id': res4.json()['data']['data'][0]['id']})
    # 修改产品分类
    res7 = Chanpinguanli().update_chanpinfenlei(chain_data['一级测试产品分类id'], chain_data['二级测试产品分类id'],
                                                int(time.time()),
                                                '二级测试产品分类test', 0, 1)
    print('修改二级级测试产品分类', res7.json())
    Assertion(res7).tongyong()
    # 查询
    res10 = Chanpinguanli().sel_chanpinfenlei('二级测试产品分类test')
    print('查询二级测试产品分类test', res10.json())
    Assertion(res10).chapinfenlei_chaxun(1, '二级测试产品分类test')
    chain_data.update({'二级测试产品分类id': res10.json()['data']['data'][0]['id']})
    # 删除二级产品分类
    res5 = Chanpinguanli().del_chanpinfenlei(chain_data['二级测试产品分类id'])
    print('删除二级测试产品分类', res5.json())
    Assertion(res5).tongyong()
    # 删除一级产品分类
    res11 = Chanpinguanli().del_chanpinfenlei(chain_data['一级测试产品分类id'])
    print('删除一级测试产品分类', res11.json())
    Assertion(res11).tongyong()
    # 查询
    res8 = Chanpinguanli().sel_chanpinfenlei('测试产品分类test')
    print('查询', res8.json())
    Assertion(res8).chaxun_isnull()
def test_01_b(chain_data):
    print(
        '新增一级产品分类(状态开启)-查询一级产品分类-新增二级产品分类(状态开启)-查询耳机产品分类-删除二级产品分类-删除一级产品分类')
    # 新增一级产品分类
    res1 = Chanpinguanli().add_chanpinfenlei(0, int(time.time()), '一级测试产品分类', 1, '1')
    print('新增一级产品分类', res1.json())
    Assertion(res1).tongyong()
    # 查询一级测试产品分类
    res2 = Chanpinguanli().sel_chanpinfenlei('一级测试产品分类')
    print('查询一级测试产品分类', res2.json())
    Assertion(res2).chapinfenlei_chaxun(1, '一级测试产品分类')
    chain_data.update({'一级测试产品分类id': res2.json()['data']['data'][0]['id']})
    # 新增二级产品分类
    res3 = Chanpinguanli().add_chanpinfenlei(1, int(time.time()), '二级测试产品分类', 1, 1,
                                             chain_data['一级测试产品分类id'])
    print('新增二级测试产品分类', res3.json())
    Assertion(res3).tongyong()
    res4 = Chanpinguanli().sel_chanpinfenlei('二级测试产品分类')
    print('查询二级测试产品分类', res4.json())
    Assertion(res4).chapinfenlei_chaxun(1, '二级测试产品分类')
    chain_data.update({'二级产测试产品分类id': res4.json()['data']['data'][0]['id']})
    # 删除一级产品分类
    res5 = Chanpinguanli().del_chanpinfenlei(chain_data['一级测试产品分类id'])
    print('删除一级测试产品分类', res5.json())
    assert res5.json()['message'] == '当前分类下有子分类，不可删除'
    # 删除二级产品分类
    res6 = Chanpinguanli().del_chanpinfenlei(chain_data['二级产测试产品分类id'])
    print('删除二级产品分类', res6.json())
    Assertion(res6).tongyong()
    # 删除一级产品分类
    res7 = Chanpinguanli().del_chanpinfenlei(chain_data['一级测试产品分类id'])
    print('删除一级测试产品分类', res7.json())
    Assertion(res7).tongyong()
    # 查询
    res8 = Chanpinguanli().sel_chanpinfenlei('测试产品分类')
    Assertion(res8).chaxun_isnull()
def test_02_a(chain_data):
    res1 = Chanpinguanli().add_pinpai('测试品牌', 5.5, 7.25, 1)
    print('新增品牌', res1.json())
    Assertion(res1).tongyong()
    res2 = Chanpinguanli().sel_pinpai('测试品牌')
    print('查询测试品牌', res2.json())
    Assertion(res2).pinpai_chaxun('测试品牌')
    chain_data.update({'品牌id': res2.json()['data']['data'][0]['id']})
    res3 = Chanpinguanli().update_pinpai(chain_data['品牌id'], '测试品牌test', 4.5, 7.5, 1)
    print('修改品牌', res3.json())
    Assertion(res3).tongyong()
    res4 = Chanpinguanli().sel_pinpai('测试品牌test')
    print('查询', res4.json())
    Assertion(res4).pinpai_chaxun('测试品牌test')
    res5 = Chanpinguanli().del_pinpai(chain_data['品牌id'])
    print('删除品牌', res5.json())
    Assertion(res5).tongyong()
    res6 = Chanpinguanli().sel_pinpai('测试品牌test')
    Assertion(res6).chaxun_isnull()
def test_03_a(chain_data):
    res1 = Chanpinguanli().cas_shangchuan_mol(r'C:\Users\shangguanyi\Downloads\1189169-37-6.mol')
    print('上传mol文件', res1.json())
    Assertion(res1).data1_notnoll()
    # chanpin_data.update({'mol': {'id': res1.json()['data']['structure_img']['id']}})
    # chanpin_data.update({'mol': {'filename': res1.json()['data']['structure_img']['filename']}})
    # chanpin_data.update({'mol': {'path_url': res1.json()['data']['structure_img']['path_url']}})
    # chanpin_data.update({'mol': {'分子式': res1.json()['data']['formula']}})
    # chanpin_data.update({'mol': {'分子量': res1.json()['data']['molecular_weight']}})
    # chanpin_data.update({'mol': {'分子结构 ': res1.json()['data']['smiles']}})
    res2 = Chanpinguanli().cas_shangchuan_tupian(r'C:\Users\shangguanyi\Desktop\上官一\后台\3.png')
    print('上传图片', res2.json())
    Assertion(res2).data1_notnoll()
    # chanpin_data.update({'mol': {'id': res2.json()['data'][0]['id']}})
    # chanpin_data.update({'mol': {'filename': res2.json()['data'][0]['filename']}})
    # chanpin_data.update({'mol': {'path_url': res2.json()['data'][0]['path_url']}})
    res5 = Chanpinguanli().weixianpin_biaoqian()
    print('获取危险品标识', res5.json())
    Assertion(res5).data2_notnoll()
    res3 = Chanpinguanli().iChembio_info('1189169-37-6')
    print('从iChembio获取信息', res3.json())
    Assertion(res3).data1_notnoll()
    res4 = Chanpinguanli().add_cas(
        res3.json()['data'][0]['cas'],
        res3.json()['data'][0]['name_en'],
        '1-(5-溴嘧啶-2-基)乙酮',
        res3.json()['data'][0]['smiles'],
        res3.json()['data'][0]['formula'],
        res3.json()['data'][0]['molecular_weight'],
        res3.json()['data'][0]['mdl'],
        res3.json()['data'][0]['einecs'],
        res5.json()['data']['data'][0]['id'],
        res1.json()['data']['structure_img']['id'],
        res1.json()['data']['structure_img']['filename'],
        res1.json()['data']['structure_img']['path_url']
    )
    print('新增CAS', res4.text)
    Assertion(res4).tongyong()
    res6 = Chanpinguanli().sel_cas('1189169-37-6')
    print('查询CAS', res6.text)
    Assertion(res6).cas_chaxun('1189169-37-6')

    res8 = Chanpinguanli().update_cas(
        res6.json()['data']['data'][0]['id'],
        res3.json()['data'][0]['cas'],
        res3.json()['data'][0]['name_en'],
        '1-(5-溴嘧啶-2-基)乙酮',
        res3.json()['data'][0]['smiles'],
        res3.json()['data'][0]['formula'],
        res3.json()['data'][0]['molecular_weight'],
        res3.json()['data'][0]['mdl'],
        res3.json()['data'][0]['einecs'],
        res5.json()['data']['data'][0]['id'],
        res2.json()['data'][0]['id'],
        res2.json()['data'][0]['filename'],
        res2.json()['data'][0]['path_url']
    )
    print('修改CAS', res8.json())
    res9 = Chanpinguanli().sel_cas(res3.json()['data'][0]['name_en'])
    print('查询CAS', res9.text)
    Assertion(res9).cas_chaxun(res3.json()['data'][0]['name_en'])
    res7 = Chanpinguanli().del_cas(res6.json()['data']['data'][0]['id'])
    print('删除CAS', res7.json())
    Assertion(res7).tongyong()
    res8 = Chanpinguanli().sel_cas('1189169-37-6')
    Assertion(res8).chaxun_isnull()
# 新增产品
def test_04_a(chain_data):
    res1 = Chanpinguanli().sel_prod_number()
    print('获取产品编号', res1.json())
    chain_data['产品编号'] = res1.json()['data']
    res2 = Chanpinguanli().chanpinfenlei()
    print('获取产品分类', res2.json())
    res3 = Chanpinguanli().weixianpin_biaoqian()
    print('获取危险品标识', res3.json())
    chain_data['危险品标识id'] = res3.json()['data']['data'][0]['id']
    res4 = Chanpinguanli().chanpin_fuzhushuxing()
    print('获取产品辅助属性', res4.json())
    res5 = Chanpinguanli().chucuntiaojian()
    print('获取产品存储条件', res5.json())
    res6 = Chanpinguanli().sel_pinpai()
    print('获取产品品牌', res6.json())
    res7 = Xitongguanli().sel_danwei('package')
    print('获取包装单位', res7.json())
    chain_data['包装id'] = res7.json()['data']['data'][0]['id']
    chain_data['包装名称'] = res7.json()['data']['data'][0]['name']
    res8 = Xitongguanli().sel_danwei('measure')
    print('获取计量单位', res8.json())
    chain_data['计量id'] = res8.json()['data']['data'][0]['id']
    chain_data['计量名称'] = res8.json()['data']['data'][0]['name']
    res9 = Chanpinguanli().cas_shangchuan_tupian(r'C:\Users\shangguanyi\Desktop\上官一\后台\3.png')
    print('上传图片', res9.json())
    Assertion(res9).data1_notnoll()
    chain_data['图片']['id'] = res9.json()['data'][0]['id']
    chain_data['图片']['filename'] = res9.json()['data'][0]['filename']
    chain_data['图片']['path_url'] = res9.json()['data'][0]['path_url']
    # 新增一级产品分类
    # res11 = Chanpinguanli().add_chanpinfenlei(0, int(time.time()), '一级测试产品分类', 1, '1')
    # print('新增一级产品分类', res11.json())
    # Assertion(res11).tongyong()
    res12 = Chanpinguanli().sel_chanpinfenlei('一级测试产品分类')
    print('查询一级测试产品分类', res12.json())
    chain_data['一级测试产品分类id'] = res12.json()['data']['data'][0]['id']
    # 新增品牌
    res13 = Chanpinguanli().add_pinpai('测试品牌', 5.5, 7.25, 1)
    print('新增品牌', res13.json())
    Assertion(res13).tongyong()
    res14 = Chanpinguanli().sel_pinpai('测试品牌')
    print('查询测试品牌', res14.json())
    Assertion(res14).pinpai_chaxun('测试品牌')
    chain_data['品牌id'] = res14.json()['data']['data'][0]['id']
    chain_data['品牌名称'] = res14.json()['data']['data'][0]['name']
    # 辅助属性取值
    for i in range(0, len(res4.json()['data']['prods'])):
        if res4.json()['data']['prods'][i]['enum_key']:
            field_name = res4.json()['data']['prods'][i]['field_name']
            enum_val = res4.json()['data']['prods'][i]['enum_val']
            chain_data['辅助属性'][f'{field_name}'] = str(random.randint(1, len(enum_val)))
        else:
            field_name = res4.json()['data']['prods'][i]['field_name']
            chain_data['辅助属性'][f'{field_name}'] = 'test'
    print(chain_data)
    res10 = Chanpinguanli().add_chanpin(
        chain_data['产品编号'],
        '904886-12-0',
        'Benzo[h]quinoline-2-carboxaldehyde',
        chain_data['一级测试产品分类id'],
        'raw_material',
        '冷藏',
        chain_data['危险品标识id'],
        chain_data['辅助属性'],
        chain_data['图片']['id'],
        chain_data['图片']['filename'],
        chain_data['图片']['path_url'],
        chain_data['产品编号'] + '-10kg',
        '98%',
        chain_data['品牌名称'],
        chain_data['品牌id'],
        chain_data['包装id'],
        chain_data['包装名称'],
        chain_data['计量id'],
        chain_data['计量名称'],
        10,
        '10kg',
        '100.98',
        '现货'
    )
    print('新增产品', res10.json())
    res15 = Chanpinguanli().sel_chanpin('904886-12-0')
    print('查询', json.dumps(res15.json()))
    info = res15.json()['data']['data'][0]
    new_values = {
        '产品': {
            '产品id': info['id'],
            '产品编号': info['prod_no'],
            'cas': info['cas'],
            '产品名称': info['name_en'],
            '产品分类': info['prod_category'][0],
            '产品类型': info['prod_type'],
            '储存条件': info['storage_condition'],
            '危险品标签id': info['dangerous_label'][0],
            '产品属性': info['data'],
            '图片': {
                'id': info['structure_img'][0]['id'],
                '名称': info['structure_img'][0]['filename'],
                'url': info['structure_img'][0]['img_show']
            },
            '规格id': info['prod_has_skus'][0]['id'],
            '规格编号': info['prod_has_skus'][0]['sku_no'],
            '纯度': info['prod_has_skus'][0]['purity_specification'],
            '品牌id': info['prod_has_skus'][0]['brand_id'],
            '品牌名称': info['prod_has_skus'][0]['brand_name'],
            '计量id': info['prod_has_skus'][0]['measuring_unit_label']['value'],
            '计量名称': info['prod_has_skus'][0]['measuring_unit_label']['label'],
            '包装id': info['prod_has_skus'][0]['packing_unit_label']['value'],
            '包装名称': info['prod_has_skus'][0]['packing_unit_label']['label'],
            '单位转换':info['prod_has_skus'][0]['unit_conversion'],
            '包装': info['prod_has_skus'][0]['packing'],
            '价格': info['prod_has_skus'][0]['price'],
            '货期': info['prod_has_skus'][0]['delivery_time']
        }
    }
    chain_data = {**chain_data, **new_values}
    print(chain_data)
    res17 = Chanpinguanli().cas_shangchuan_mol(r'C:\Users\shangguanyi\Downloads\1189169-37-6.mol')
    print('上传mol',res17.json())
    chain_data['mol']['id'] = res17.json()['data']['structure_img']['id']
    chain_data['mol']['filename'] = res17.json()['data']['structure_img']['filename']
    chain_data['mol']['path_url'] = res17.json()['data']['structure_img']['path_url']
    res18 = Chanpinguanli().sel_pinpai()
    print('查询品牌',res18.json())
    index = random.randint(0, len(res18.json()['data']['data']) - 1)
    chain_data['品牌id2'] = res18.json()['data']['data'][index]['id']
    chain_data['品牌名称2'] = res18.json()['data']['data'][index]['name']
    res19 = Xitongguanli().sel_danwei('package')
    print('查询包装单位',res19.json())
    index = random.randint(0,len(res19.json()['data']['data'])-1)
    chain_data['包装id'] = res19.json()['data']['data'][index]['id']
    chain_data['包装名称'] = res19.json()['data']['data'][index]['name']
    res20 = Xitongguanli().sel_danwei('measure')
    print('查询计量单位',res20.json())
    index = random.randint(0, len(res20.json()['data']['data']) - 1)
    chain_data['计量id'] = res20.json()['data']['data'][index]['id']
    chain_data['计量名称'] = res20.json()['data']['data'][index]['name']
    # 修改产品
    res16 = Chanpinguanli().update_chanpin(
        chain_data['产品']['产品id'],
        chain_data['产品']['产品编号'],
        chain_data['产品']['cas'],
        chain_data['产品']['产品名称'],
        chain_data['产品']['产品分类'],
        chain_data['产品']['产品类型'],
        chain_data['产品']['储存条件'],
        chain_data['产品']['危险品标签id'],
        1,
        chain_data['产品']['产品属性'],
        chain_data['产品']['图片']['id'],
        chain_data['产品']['图片']['名称'],
        chain_data['产品']['图片']['url'],
        chain_data['mol']['id'],
        chain_data['mol']['filename'],
        chain_data['mol']['path_url'],
        chain_data['产品']['规格id'],
        chain_data['产品']['规格编号'],
        chain_data['产品']['纯度'],
        chain_data['产品']['品牌id'],
        chain_data['产品']['品牌名称'],
        chain_data['产品']['包装id'],
        chain_data['产品']['包装名称'],
        chain_data['产品']['单位转换'],
        chain_data['产品']['计量id'],
        chain_data['产品']['计量名称'],
        chain_data['产品']['包装'],
        chain_data['产品']['价格'],
        chain_data['产品']['货期'],
        chain_data['产品']['产品编号'] + '-100' + chain_data['计量名称'],
        '88%',
        chain_data['品牌id2'],
        chain_data['品牌名称2'],
        chain_data['包装id'],
        chain_data['包装名称'],
        '100',
        chain_data['计量id'],
        chain_data['计量名称'],
        '100' + chain_data["计量名称"],
        '88.88',
        '现货'
    )
    print('修改产品',res16.json())
    #删除产品
    res20 = Chanpinguanli().del_chanpin(chain_data['产品']['产品id'])
    print('删除产品',res20.json())
    #查询
    res21 = Chanpinguanli().sel_chanpin('',chain_data['产品编号'])
    Assertion(res21).chaxun_isnull()
    #删除品牌、分类
    res22 = Chanpinguanli().del_pinpai(chain_data['品牌id'])
    print('删除品牌',res22.json())
    Assertion(res22).tongyong()
    res23 = Chanpinguanli().del_chanpinfenlei(chain_data['一级测试产品分类id'])
    print('删除产品分类',res23.json())
    Assertion(res23).tongyong()
def test_05_a(chain_data):

    pass

def test_100_add_prod(chain_data):
    for i in open(r'C:\Users\shangguanyi\Desktop\products.txt', 'r', encoding='utf-8'):
        new = i.split(',')
        print(new[0], new[1], new[2])
        res1 = Chanpinguanli().sel_prod_number()
        print('获取产品编号', res1.json())
        chain_data['产品编号'] = res1.json()['data']
        res2 = Chanpinguanli().chanpinfenlei()
        print('获取产品分类', res2.json())
        res3 = Chanpinguanli().weixianpin_biaoqian()
        print('获取危险品标识', res3.json())
        chain_data['危险品标识id'] = res3.json()['data']['data'][0]['id']
        res4 = Chanpinguanli().chanpin_fuzhushuxing()
        print('获取产品辅助属性', res4.json())
        res5 = Chanpinguanli().chucuntiaojian()
        print('获取产品存储条件', res5.json())
        res6 = Chanpinguanli().sel_pinpai()
        print('获取产品品牌', res6.json())
        res7 = Xitongguanli().sel_danwei('package')
        print('获取包装单位', res7.json())
        chain_data['包装id'] = res7.json()['data']['data'][0]['id']
        chain_data['包装名称'] = res7.json()['data']['data'][0]['name']
        res8 = Xitongguanli().sel_danwei('measure')
        print('获取计量单位', res8.json())
        chain_data['计量id'] = res8.json()['data']['data'][0]['id']
        chain_data['计量名称'] = res8.json()['data']['data'][0]['name']
        res9 = Chanpinguanli().cas_shangchuan_tupian(r'C:\Users\shangguanyi\Desktop\上官一\后台\3.png')
        print('上传图片', res9.json())
        Assertion(res9).data1_notnoll()
        chain_data['图片']['id'] = res9.json()['data'][0]['id']
        chain_data['图片']['filename'] = res9.json()['data'][0]['filename']
        chain_data['图片']['path_url'] = res9.json()['data'][0]['path_url']
        # 新增一级产品分类
        # res11 = Chanpinguanli().add_chanpinfenlei(0, int(time.time()), '一级测试产品分类', 1, '1')
        # print('新增一级产品分类', res11.json())
        # Assertion(res11).tongyong()
        # res12 = Chanpinguanli().sel_chanpinfenlei('一级测试产品分类')
        # print('查询一级测试产品分类', res12.json())
        # chain_data['一级测试产品分类id'] = res12.json()['data']['data'][0]['id']
        # 新增品牌
        res14 = Chanpinguanli().sel_pinpai()
        print('查询测试品牌', res14.json())
        index = random.randint(0,len(res14.json()['data']['data'])-1)
        chain_data['品牌id'] = res14.json()['data']['data'][index]['id']
        chain_data['品牌名称'] = res14.json()['data']['data'][index]['name']
        # 辅助属性取值
        for i in range(0, len(res4.json()['data']['prods'])):
            if res4.json()['data']['prods'][i]['enum_key']:
                field_name = res4.json()['data']['prods'][i]['field_name']
                enum_val = res4.json()['data']['prods'][i]['enum_val']
                chain_data['辅助属性'][f'{field_name}'] = str(random.randint(1, len(enum_val)))
            else:
                field_name = res4.json()['data']['prods'][i]['field_name']
                chain_data['辅助属性'][f'{field_name}'] = 'test'
        print(chain_data)
        res10 = Chanpinguanli().add_chanpin(
            chain_data['产品编号'],
            new[0],
            new[2],
            12,
            'raw_material',
            '冷藏',
            chain_data['危险品标识id'],
            chain_data['辅助属性'],
            chain_data['图片']['id'],
            chain_data['图片']['filename'],
            chain_data['图片']['path_url'],
            chain_data['产品编号'] + '-10kg',
            '98%',
            chain_data['品牌名称'],
            chain_data['品牌id'],
            chain_data['包装id'],
            chain_data['包装名称'],
            chain_data['计量id'],
            chain_data['计量名称'],
            10,
            '10kg',
            '100.98',
            '现货'
        )
        print('新增产品', res10.json())

