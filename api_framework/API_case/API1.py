#coding=gbk
import time
from api_framework.API_case.API_data import Data_API1
from api_framework.api.req_method import UserAPI


dqsj = time.strftime("%Y-%m-%d")
dqsj1 = time.strftime("%Y-%m-%d %H:%M:%S")


class Space():
    purchase_no = ''  # 采购订单号
    sales_no = ''  # 销售订单号
    caigou_id = ''  # 获取采购ID，查询、修改采购订单时会用到.
    xiaoshou_id = ''  # 获取销售ID，查询、修改销售订单时会用到
    ruku_id = ''  # 入库id
    chuku_id = ''  # 出库id
    xs_price = ''  # 销售总金额
    cg_price = ''  # 采购总金额
    order_id = ''  # 收款需要用到
    chanpin_id = ''  # 产品id，修改产品信息会用到
    number = ''  # 产品编号
    id1 = ''  # 修改、收款、开票需要用到
    id2 = ''  # 修改、收款、开票需要用到

    # 新增采购订单
    def add_caigou(self):
        # 生成采购订单号
        a = int(time.time())
        Space.purchase_no = 'CG%s' % a
        payload = Data_API1().add_caigou(dqsj, Space.purchase_no)
        urloreder =  '/api/v1/erp_starter/purchase/order'
        res = UserAPI.post(urloreder, payload)
        print('新增采购订单', res.json())
        assert res.json()['data']['purchase_no'] == Space.purchase_no
        assert res.json()['status'] == 0

    # 查询采购订单
    def select_caigou(self):
        time.sleep(4)
        urlselect_caigou =  "/api/v1/erp_starter/purchase/order?all=&prod_name=&cas=&purchase_no=%s&note=&supplier_name=&start_date=&end_date=&page_no=1&page_size=20&prod_no=" % Space.purchase_no
        # print('查询采购URL',urlselect_caigou)
        UserAPI.get(urlselect_caigou)
        response = UserAPI.get(urlselect_caigou)
        print('查询采购订单', response.json())
        print('采购ID', response.json()['data']['data'][0]['id'])
        Space.caigou_id = response.json()['data']['data'][0]['id']
        assert response.json()['data']['data'][0]['purchase_no'] == Space.purchase_no  # 存在查询的采购订单号
        assert response.json()['status'] == 0

    # 修改采购订单
    def update_caigou_order(self):
        payload = Data_API1().update_caigou(dqsj, Space.purchase_no)
        urlupdate_order =  '/api/v1/erp_starter/purchase/order/%s' % Space.caigou_id
        # print('修改采购订单URL',urlupdate_order)
        response = UserAPI.put(urlupdate_order, payload)
        print('修改采购订单', response.json())
        assert response.json()['message'] == '操作成功'
        assert response.json()['status'] == 0
        assert response.json()['data']['purchase_no'] == Space.purchase_no
        Space.cg_price = response.json()['data']['total_price'].split('.')[0]  # 采购总金额

    # 删除采购订单
    def delect_caigou(self):
        urldel_caigou =  "/api/v1/erp_starter/purchase/order/%s" % Space.caigou_id
        # print('删除采购订单URL',urldel_caigou)
        response = UserAPI.delete(urldel_caigou)
        print('删除采购订单', response.json())
        assert response.json()['status'] == 0

    # 生成质检报告
    def zhijianbaogao(self):
        urlreport =  "/api/v1/erp_starter/inventory/product/qa/report/1074-82-4"
        payload = Data_API1().zhijianbaogao(dqsj)

        response = UserAPI.post(urlreport, payload)
        print('生成质检报告', response.json())
        assert response.json()['status'] == 0
        assert response.json()['data']['prod_no'] == "1074-82-4"  # 产品编号

    # 采购入库
    def ruku(self):
        urlodd_no =  '/api/v1/erp_starter/purchase/order/inventory/generate/odd'
        res = UserAPI.get(urlodd_no)
        # print(res.json())
        print('查询采购号', res.json()['data']['current_odd_no'])
        Space.ruku_id = res.json()['data']['current_odd_no']
        urlinbound =  '/api/v1/erp_starter/purchase/order/inbound'
        payload = Data_API1().ruku(Space.purchase_no, dqsj, Space.ruku_id)
        response = UserAPI.post(urlinbound, payload)
        print('采购入库', response.json())
        assert response.json()['status'] == 0
        assert response.json()['data']['purchase_no'] == Space.purchase_no

    # 其他类入库
    def qita_ruku(self):
        urlqitaruku =  "/api/v1/erp_starter/inventory/inbound"
        payload = Data_API1().qita_ruku(dqsj)
        response = UserAPI.post(urlqitaruku, payload)
        print('其他类入库', response.json())
        assert response.json()['status'] == 0
        assert response.json()['data']['prod_list'][0]['cas'] == 'QTRK-000001'
        print('入库号', response.json()['data']['odd_no'])

    # 打印入库单-需要入库才能打印
    def dayin_ruku(self):
        urlruku =  "/api/v1/erp_starter/purchase/order/inventory/list/%s" % Space.purchase_no
        response = UserAPI.get(urlruku)
        print('打印入库单', response.text)
        assert response.json()['data'][0]['odd_no'] == Space.ruku_id
        total_price = response.json()['data'][0]['total_price'].split('.')[0]
        print('采购总金额', Space.cg_price, '入库单总金额', total_price)
        assert Space.cg_price == total_price  # 采购总金额与入库单总金额对比

    # 付款
    def caigou_fukuan(self):
        urlodd =  "/api/v1/erp_starter/purchase/order/pay/generate/odd"
        response = UserAPI.get(urlodd)
        # print(response.text)
        print('付款id', response.json()['data']['current_odd_no'])
        odd_no = response.json()['data']['current_odd_no']
        urlfukuan =  '/api/v1/erp_starter/purchase/order/pay'
        payload = Data_API1().caigou_fukuan(dqsj, Space.purchase_no, odd_no)
        res = UserAPI.post(urlfukuan, payload)
        print('付款', res.json())
        assert res.json()['status'] == 0
        assert res.json()['data']['purchase_no'] == Space.purchase_no

    # 收票
    def caigou_shoupiao(self):
        urlodd =  '/api/v1/erp_starter/purchase/order/receipt/generate/odd'
        response = UserAPI.get( urlodd)
        # print(response.text)
        print('收票id', response.json()['data']['current_odd_no'])
        odd_no = response.json()['data']['current_odd_no']
        urlshoupiao =  '/api/v1/erp_starter/purchase/order/receipt'
        payload = Data_API1().caigou_shoupiao(dqsj, Space.purchase_no, odd_no)
        res = UserAPI.post( urlshoupiao, payload)
        print('收票', res.json())
        assert res.json()['status'] == 0
        assert res.json()['data']['purchase_no'] == Space.purchase_no

    # 库存查询
    def select_kucun(self, CAS_id):
        time.sleep(5)
        urlkucun =  '/api/v1/erp_starter/inventory/product?all=&prod_name=&prod_no=&cas=%s&show_0_inventory=0&page_no=1&page_size=20' % CAS_id
        res = UserAPI.get(urlkucun)
        # print(res.json())
        print('剩余库存', res.json()['data']['data'][0]['weight_total_inventory'])
        return res.json()['data']['data'][0]['weight_total_inventory']  # 剩余库存总量

    # 新增销售订单
    def add_xiaoshou(self):
        a = int(time.time())
        Space.sales_no = 'XS%s' % a
        urladd_xiaoshou =  '/api/v1/erp_starter/sales/order'
        payload = Data_API1().add_xiaoshou(dqsj, Space.sales_no)
        res = UserAPI.post(urladd_xiaoshou, payload)
        print('新增销售订单', res.json())
        assert res.json()['data']['sales_no'] == Space.sales_no
        assert res.json()['status'] == 0
        # print('order_id', res.json()['data']['id'])
        Space.order_id = res.json()['data']['id']

    # 查询销售订单
    def select_xiaoshou(self):
        time.sleep(5)
        # 商城销售订单
        urlshop =  '/api/v1/erp_starter/sales/order?all=&cas=&customer=&start_date=&end_date=&note=&prod_name=&prod_no=&sales_no=&sales_no_and_customer=&page_no=1&page_size=20&is_bind_shop_order=1'
        res = UserAPI.get(urlshop)
        print('商城订单', res.json())
        for i in range(0, 20):
            print('商城订单index', i)
            is_bind_shop_order = res.json()['data']['data'][i]['is_bind_shop_order']  # 商城订单
            assert is_bind_shop_order == 1
        # 非商城订单
        urlshop =  '/api/v1/erp_starter/sales/order?all=&cas=&customer=&start_date=&end_date=&note=&prod_name=&prod_no=&sales_no=&sales_no_and_customer=&page_no=1&page_size=20&is_bind_shop_order=0'

        res = UserAPI.get(urlshop)
        print('非商城订单', res.text)
        for i in range(0, 20):
            print('非商城订单index', i)
            is_bind_shop_order = res.json()['data']['data'][i]['is_bind_shop_order']  # 非商城订单
            assert is_bind_shop_order == 0

        urlselect_xiaoshou =  "/api/v1/erp_starter/sales/order?all=&cas=&customer=&start_date=&end_date=&note=&prod_name=&prod_no=&sales_no=%s&sales_no_and_customer=&page_no=1&page_size=20" % Space.sales_no
        # print('查询销售订单URL',urlselect_xiaoshou)
        UserAPI.get(urlselect_xiaoshou)
        time.sleep(1)
        UserAPI.get( urlselect_xiaoshou)
        response = UserAPI.get(urlselect_xiaoshou)
        print('查询销售订单', response.json())
        print('销售订单ID', response.json()['data']['data'][0]['id'])
        Space.xiaoshou_id = response.json()['data']['data'][0]['id']
        return response.json()['data']['data'][0]['id']

    # 修改销售订单
    def update_xiaoshou_order(self):
        urlupdate_order =  "/api/v1/erp_starter/sales/order/%s" % Space.xiaoshou_id
        # print(urlupdate_order)
        payload = Data_API1().update_xiaoshou_order(dqsj, dqsj1, Space.sales_no, Space.id1, Space.id2, Space.order_id)
        response = UserAPI.put(urlupdate_order, payload)
        print('修改销售订单', response.json())
        assert response.json()['status'] == 0
        Space.xs_price = response.json()['data']['total_price'].split('.')[0]  # 销售总金额

    # 删除销售订单
    def delete_xiaoshou(self):
        del_xiaoshou =  '/api/v1/erp_starter/sales/order/%s' % Space.xiaoshou_id
        response = UserAPI.delete( del_xiaoshou)
        print('删除销售订单', response.json())
        assert response.json()['status'] == 0

    # 收款
    def xiaoshou_shoukuan(self):
        urlodd =  '/api/v1/erp_starter/sales/order/collection/generate/odd'  # 收款id
        response = UserAPI.get(urlodd)
        # print(response.text)
        print('收款id', response.json()['data']['current_odd_no'])
        odd_no = response.json()['data']['current_odd_no']
        urlshoukuan =  '/api/v1/erp_starter/sales/order/collection'
        # 需要改payload
        payload = Data_API1().xiaoshou_shoukuan(dqsj, Space.sales_no, odd_no, Space.id1, Space.id2)
        res = UserAPI.post( urlshoukuan, payload)
        print('收款', res.json())
        assert res.json()['status'] == 0
        assert res.json()['data']['sales_no'] == Space.sales_no

    # 批量收款
    def xiaoshou_piliangshoukuan(self):
        urldata =  "/api/v1/erp_starter/sales/order/collection/batch/filter?collection_status[]=1&collection_status[]=2&all=&cas=&prod_name=&note=&sales_no=&customer=天津医药&order_id="
        UserAPI.get(urldata)
        time.sleep(2)
        response = UserAPI.get(urldata)
        time.sleep(3)
        print('未收款订单', response.json())
        sales_no1 = response.json()['data'][0]['sales_no']
        prod_no1 = response.json()['data'][0]['sales_order_prods'][0]['prod_no']
        id1 = response.json()['data'][0]['sales_order_prods'][0]['id']
        sales_no2 = response.json()['data'][1]['sales_no']
        prod_no2 = response.json()['data'][1]['sales_order_prods'][0]['prod_no']
        id2 = response.json()['data'][1]['sales_order_prods'][0]['id']
        # sales_no3 = response.json()['data'][2]['sales_no']
        # prod_no3 = response.json()['data'][2]['sales_order_prods'][0]['prod_no']
        # id3 = response.json()['data'][2]['sales_order_prods'][0]['id']
        # print('prod_no1', prod_no1)
        # print('prod_no2',prod_no2)
        # print('sales_no1', sales_no1)
        # print('sales_no2', sales_no2)
        # print(id1)
        # print(id2)
        urlpiliang =  '/api/v1/erp_starter/sales/order/collection/batch'
        payload = Data_API1().xiaoshou_piliangshoukuan(dqsj, id1, id2, prod_no1, prod_no2, sales_no1, sales_no2)
        response = UserAPI.post(urlpiliang, payload)
        time.sleep(2)
        print('批量收款', response.json())
        assert response.json()['status'] == 0
        assert response.json()['data'][0]['sales_no'] == sales_no1
        assert response.json()['data'][1]['sales_no'] == sales_no2
        # assert response.json()['data'][2]['sales_no'] == sales_no3

    # 开票
    def xiaoshou_kaipiao(self):
        urlodd =  '/api/v1/erp_starter/sales/order/invoice/generate/odd'
        response = UserAPI.get(urlodd)
        # print(response.text)
        print('开票id', response.json()['data']['current_odd_no'])
        odd_no = response.json()['data']['current_odd_no']
        urlkaipiao =  '/api/v1/erp_starter/sales/order/invoice'
        payload = Data_API1().xiaoshou_kaipiao(dqsj, Space.sales_no, odd_no, Space.id1, Space.id2)
        res = UserAPI.post(urlkaipiao, payload)
        print('开票', res.json())
        assert res.json()['status'] == 0
        assert res.json()['data']['sales_no'] == Space.sales_no

    # 销售发货
    def fahuo(self):
        # 查询发货号
        urlodd =  "/api/v1/erp_starter/sales/order/delivery/generate/odd"
        response = UserAPI.get(urlodd)
        # print(response.json())
        print('查询发货号', response.json()['data']['current_odd_no'])  # 查询发货号
        Space.chuku_id = response.json()['data']['current_odd_no']
        # 发货
        order_fahuo =  "/api/v1/erp_starter/sales/order/delivery"
        payload = Data_API1().fahuo(dqsj, Space.sales_no, Space.chuku_id, Space.id1, Space.id2)
        response = UserAPI.post(order_fahuo, payload)
        print("发货", response.text)
        assert response.json()['status'] == 0
        assert response.json()['data']['sales_no'] == Space.sales_no

    # 其他类出库
    def qita_fahuo(self):
        urlqita =  "/api/v1/erp_starter/inventory/outbound"
        payload = Data_API1().qita_fahuo(dqsj)
        response = UserAPI.post(urlqita, payload)
        print('其他类出库', response.json())
        assert response.json()['status'] == 0
        print('发货号', response.json()['data']['odd_no'])

    # 打印发货单
    def dayin_fahuo(self):
        urlfahuo =  '/api/v1/erp_starter/sales/order/delivery/list/%s' % Space.sales_no
        response = UserAPI.get(urlfahuo)
        print('打印发货单', response.text)
        # print('发货号',response.json()['data'][0]['odd_no'])
        # print('Space.chuku_id',Space.chuku_id)
        assert response.json()['data'][0]['odd_no'] == Space.chuku_id
        # Space.xs_price = response.json()['data']['total_price'].split('.')[0]
        total_price = response.json()['data'][0]['total_price'].split('.')[0]  # 发货订单总金额
        print('销售总金额', Space.xs_price, '发货单总金额', total_price)
        assert Space.xs_price == total_price  # 销售金额与发货单金额对比

    # id1,id2;要放在修改销售订单后面
    def id(self):
        urlid =  '/api/v1/erp_starter/sales/order/%s' % Space.order_id
        response = UserAPI.get( urlid)
        print('id1', response.json()['data']['sales_order_prods'][0]['id'])
        print('id2', response.json()['data']['sales_order_prods'][1]['id'])
        Space.id1 = response.json()['data']['sales_order_prods'][0]['id']  # id1 收款需要对应的产品id
        Space.id2 = response.json()['data']['sales_order_prods'][1]['id']  # id2

    # 出入库明细查询
    def select_churuku(self):
        urlchuru =  '/api/v1/erp_starter/inventory/details?all=&cas=&prod_name=&prod_no=&start_date=&end_date=&page_no=1&page_size=20'
        res = UserAPI.get(urlchuru)
        assert res.json()['status'] == 0
        assert res.json()['message'] == '操作成功'

    # 新增产品信息
    def add_chanpin(self):
        urlodd =  '/api/v1/erp_starter/inventory/product/generate/odd'
        res = UserAPI.get(urlodd)  # 生成产品编号
        print('产品编号', res.json()['data']['current_odd_no'])
        Space.number = res.json()['data']['current_odd_no']
        urladd =  '/api/v1/erp_starter/inventory/product'
        data = Data_API1().add_chanpin(Space.number)
        res = UserAPI.post(urladd, data)
        print('新增产品', res.json())
        Space.chanpin_id = res.json()['data']['id']
        assert res.json()['status'] == 0
        assert Space.number == res.json()['data']['prod_no']

    # 修改产品信息
    def update_chanpin(self):
        urlid =  '/api/v1/erp_starter/inventory/product/%s' % Space.chanpin_id
        res = UserAPI.get( urlid)
        # print('获取产品信息',res.json())
        id = res.json()['data']['skus'][0]['id']
        # print('id', res.json()['data']['skus'][0]['id'])
        urlupdata =  '/api/v1/erp_starter/inventory/product/prod_no/%s' % Space.number
        data = Data_API1().update_chanpin(Space.number, id)
        res = UserAPI.put( urlupdata, data)
        print('修改产品信息', res.json())
        assert res.json()['status'] == 0
        assert res.json()['data']['cas'] == '19-0189'

    # 设置产品标签
    def set_chanpin_biaoqian(self):
        urlset =  '/api/v1/erp_starter/inventory/product/tag/prod/%s' % Space.chanpin_id
        payload = Data_API1().set_chanpin_biaoqian()
        res = UserAPI.post_biaodan(urlset, payload)
        print('设置产品标签', res.json())
        assert res.json()['status'] == 0

    # 删除产品
    def delete_chanpin(self):
        urldel =  '/api/v1/erp_starter/inventory/product/%s' % Space.chanpin_id
        res = UserAPI.delete(urldel)
        print('删除产品', res.json())
        assert res.json()['status'] == 0

# 新增采购订单-查询采购订单-修改采购订单-付款-收票-生成质检报告-采购入库-打印入库订单
# print()
# Space().add_caigou()
# Space().select_caigou()
# Space().update_caigou_order()
# Space().caigou_fukuan()
# Space().caigou_shoupiao()
# Space().zhijianbaogao()
# Space().ruku()
# Space().dayin_ruku()
# 新增销售订单-查询销售订单-修改销售订单-收款-开票-销售发货-打印发货订单
# print()
# Space().add_xiaoshou()
# Space().id()
# Space().select_xiaoshou()
# Space().update_xiaoshou_order()
# Space().xiaoshou_shoukuan()
# Space().xiaoshou_kaipiao()
# Space().fahuo()
# Space().dayin_fahuo()
# 新增采购订单-查询采购订单-修改采购订单-删除采购订单
# print()
# Space().add_caigou()
# Space().select_caigou()
# Space().update_caigou_order()
# Space().delect_caigou()
# 新增销售订单-查询销售订单-修改销售订单-删除销售订单
# print()
# Space().add_xiaoshou()
# Space().select_xiaoshou()
# Space().update_xiaoshou_order()
# Space().delete_xiaoshou()
# 新增采购订单-查询采购订单-修改采购订单-初始库存查询-采购入库-入库后库存查询-新增销售订单-查询销售订单-修改销售订单-销售发货-发货后库存查询
# Space().add_caigou()
# Space().select_caigou()
# kucun = Space().select_kucun('1074-82-4')  # 初始库存
# Space().update_caigou_order()
# Space().ruku()
# rkcun = Space().select_kucun('1074-82-4')  # 入库后的库存
# assert kucun + 1000 == rkcun
# Space().add_xiaoshou()
# Space().id()
# Space().select_xiaoshou()
# Space().update_xiaoshou_order()
# Space().fahuo()
# ckkuncun = Space().select_kucun('1074-82-4')  # 出库后的库存
# assert kucun == ckkuncun
# 其他类出库、入库
# kucun = Space().select_kucun('QTRK-000001') #初始库存
# Space().qita_ruku()
# rkkucun = Space().select_kucun('QTRK-000001') #入库后库存
# assert kucun + 100 == rkkucun
# Space().qita_fahuo()
# ckkucun = Space().select_kucun('QTRK-000001') #出库后库存
# assert rkkucun - 100 == ckkucun
# assert kucun == ckkucun
# 批量收款
# Space().xiaoshou_piliangshoukuan()
# 出入库查询
# Space().select_churuku()
# 新增产品-修改产品信息-设置产品标签-删除产品
# Space().add_chanpin()
# Space().update_chanpin()
# Space().set_chanpin_biaoqian()
# Space().delete_chanpin()

