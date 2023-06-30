#coding=gbk
import time
from api_framework.API_case.API_data import Data_API1
from api_framework.api.req_method import UserAPI


dqsj = time.strftime("%Y-%m-%d")
dqsj1 = time.strftime("%Y-%m-%d %H:%M:%S")


class Space():
    purchase_no = ''  # �ɹ�������
    sales_no = ''  # ���۶�����
    caigou_id = ''  # ��ȡ�ɹ�ID����ѯ���޸Ĳɹ�����ʱ���õ�.
    xiaoshou_id = ''  # ��ȡ����ID����ѯ���޸����۶���ʱ���õ�
    ruku_id = ''  # ���id
    chuku_id = ''  # ����id
    xs_price = ''  # �����ܽ��
    cg_price = ''  # �ɹ��ܽ��
    order_id = ''  # �տ���Ҫ�õ�
    chanpin_id = ''  # ��Ʒid���޸Ĳ�Ʒ��Ϣ���õ�
    number = ''  # ��Ʒ���
    id1 = ''  # �޸ġ��տ��Ʊ��Ҫ�õ�
    id2 = ''  # �޸ġ��տ��Ʊ��Ҫ�õ�

    # �����ɹ�����
    def add_caigou(self):
        # ���ɲɹ�������
        a = int(time.time())
        Space.purchase_no = 'CG%s' % a
        payload = Data_API1().add_caigou(dqsj, Space.purchase_no)
        urloreder =  '/api/v1/erp_starter/purchase/order'
        res = UserAPI.post(urloreder, payload)
        print('�����ɹ�����', res.json())
        assert res.json()['data']['purchase_no'] == Space.purchase_no
        assert res.json()['status'] == 0

    # ��ѯ�ɹ�����
    def select_caigou(self):
        time.sleep(4)
        urlselect_caigou =  "/api/v1/erp_starter/purchase/order?all=&prod_name=&cas=&purchase_no=%s&note=&supplier_name=&start_date=&end_date=&page_no=1&page_size=20&prod_no=" % Space.purchase_no
        # print('��ѯ�ɹ�URL',urlselect_caigou)
        UserAPI.get(urlselect_caigou)
        response = UserAPI.get(urlselect_caigou)
        print('��ѯ�ɹ�����', response.json())
        print('�ɹ�ID', response.json()['data']['data'][0]['id'])
        Space.caigou_id = response.json()['data']['data'][0]['id']
        assert response.json()['data']['data'][0]['purchase_no'] == Space.purchase_no  # ���ڲ�ѯ�Ĳɹ�������
        assert response.json()['status'] == 0

    # �޸Ĳɹ�����
    def update_caigou_order(self):
        payload = Data_API1().update_caigou(dqsj, Space.purchase_no)
        urlupdate_order =  '/api/v1/erp_starter/purchase/order/%s' % Space.caigou_id
        # print('�޸Ĳɹ�����URL',urlupdate_order)
        response = UserAPI.put(urlupdate_order, payload)
        print('�޸Ĳɹ�����', response.json())
        assert response.json()['message'] == '�����ɹ�'
        assert response.json()['status'] == 0
        assert response.json()['data']['purchase_no'] == Space.purchase_no
        Space.cg_price = response.json()['data']['total_price'].split('.')[0]  # �ɹ��ܽ��

    # ɾ���ɹ�����
    def delect_caigou(self):
        urldel_caigou =  "/api/v1/erp_starter/purchase/order/%s" % Space.caigou_id
        # print('ɾ���ɹ�����URL',urldel_caigou)
        response = UserAPI.delete(urldel_caigou)
        print('ɾ���ɹ�����', response.json())
        assert response.json()['status'] == 0

    # �����ʼ챨��
    def zhijianbaogao(self):
        urlreport =  "/api/v1/erp_starter/inventory/product/qa/report/1074-82-4"
        payload = Data_API1().zhijianbaogao(dqsj)

        response = UserAPI.post(urlreport, payload)
        print('�����ʼ챨��', response.json())
        assert response.json()['status'] == 0
        assert response.json()['data']['prod_no'] == "1074-82-4"  # ��Ʒ���

    # �ɹ����
    def ruku(self):
        urlodd_no =  '/api/v1/erp_starter/purchase/order/inventory/generate/odd'
        res = UserAPI.get(urlodd_no)
        # print(res.json())
        print('��ѯ�ɹ���', res.json()['data']['current_odd_no'])
        Space.ruku_id = res.json()['data']['current_odd_no']
        urlinbound =  '/api/v1/erp_starter/purchase/order/inbound'
        payload = Data_API1().ruku(Space.purchase_no, dqsj, Space.ruku_id)
        response = UserAPI.post(urlinbound, payload)
        print('�ɹ����', response.json())
        assert response.json()['status'] == 0
        assert response.json()['data']['purchase_no'] == Space.purchase_no

    # ���������
    def qita_ruku(self):
        urlqitaruku =  "/api/v1/erp_starter/inventory/inbound"
        payload = Data_API1().qita_ruku(dqsj)
        response = UserAPI.post(urlqitaruku, payload)
        print('���������', response.json())
        assert response.json()['status'] == 0
        assert response.json()['data']['prod_list'][0]['cas'] == 'QTRK-000001'
        print('����', response.json()['data']['odd_no'])

    # ��ӡ��ⵥ-��Ҫ�����ܴ�ӡ
    def dayin_ruku(self):
        urlruku =  "/api/v1/erp_starter/purchase/order/inventory/list/%s" % Space.purchase_no
        response = UserAPI.get(urlruku)
        print('��ӡ��ⵥ', response.text)
        assert response.json()['data'][0]['odd_no'] == Space.ruku_id
        total_price = response.json()['data'][0]['total_price'].split('.')[0]
        print('�ɹ��ܽ��', Space.cg_price, '��ⵥ�ܽ��', total_price)
        assert Space.cg_price == total_price  # �ɹ��ܽ������ⵥ�ܽ��Ա�

    # ����
    def caigou_fukuan(self):
        urlodd =  "/api/v1/erp_starter/purchase/order/pay/generate/odd"
        response = UserAPI.get(urlodd)
        # print(response.text)
        print('����id', response.json()['data']['current_odd_no'])
        odd_no = response.json()['data']['current_odd_no']
        urlfukuan =  '/api/v1/erp_starter/purchase/order/pay'
        payload = Data_API1().caigou_fukuan(dqsj, Space.purchase_no, odd_no)
        res = UserAPI.post(urlfukuan, payload)
        print('����', res.json())
        assert res.json()['status'] == 0
        assert res.json()['data']['purchase_no'] == Space.purchase_no

    # ��Ʊ
    def caigou_shoupiao(self):
        urlodd =  '/api/v1/erp_starter/purchase/order/receipt/generate/odd'
        response = UserAPI.get( urlodd)
        # print(response.text)
        print('��Ʊid', response.json()['data']['current_odd_no'])
        odd_no = response.json()['data']['current_odd_no']
        urlshoupiao =  '/api/v1/erp_starter/purchase/order/receipt'
        payload = Data_API1().caigou_shoupiao(dqsj, Space.purchase_no, odd_no)
        res = UserAPI.post( urlshoupiao, payload)
        print('��Ʊ', res.json())
        assert res.json()['status'] == 0
        assert res.json()['data']['purchase_no'] == Space.purchase_no

    # ����ѯ
    def select_kucun(self, CAS_id):
        time.sleep(5)
        urlkucun =  '/api/v1/erp_starter/inventory/product?all=&prod_name=&prod_no=&cas=%s&show_0_inventory=0&page_no=1&page_size=20' % CAS_id
        res = UserAPI.get(urlkucun)
        # print(res.json())
        print('ʣ����', res.json()['data']['data'][0]['weight_total_inventory'])
        return res.json()['data']['data'][0]['weight_total_inventory']  # ʣ��������

    # �������۶���
    def add_xiaoshou(self):
        a = int(time.time())
        Space.sales_no = 'XS%s' % a
        urladd_xiaoshou =  '/api/v1/erp_starter/sales/order'
        payload = Data_API1().add_xiaoshou(dqsj, Space.sales_no)
        res = UserAPI.post(urladd_xiaoshou, payload)
        print('�������۶���', res.json())
        assert res.json()['data']['sales_no'] == Space.sales_no
        assert res.json()['status'] == 0
        # print('order_id', res.json()['data']['id'])
        Space.order_id = res.json()['data']['id']

    # ��ѯ���۶���
    def select_xiaoshou(self):
        time.sleep(5)
        # �̳����۶���
        urlshop =  '/api/v1/erp_starter/sales/order?all=&cas=&customer=&start_date=&end_date=&note=&prod_name=&prod_no=&sales_no=&sales_no_and_customer=&page_no=1&page_size=20&is_bind_shop_order=1'
        res = UserAPI.get(urlshop)
        print('�̳Ƕ���', res.json())
        for i in range(0, 20):
            print('�̳Ƕ���index', i)
            is_bind_shop_order = res.json()['data']['data'][i]['is_bind_shop_order']  # �̳Ƕ���
            assert is_bind_shop_order == 1
        # ���̳Ƕ���
        urlshop =  '/api/v1/erp_starter/sales/order?all=&cas=&customer=&start_date=&end_date=&note=&prod_name=&prod_no=&sales_no=&sales_no_and_customer=&page_no=1&page_size=20&is_bind_shop_order=0'

        res = UserAPI.get(urlshop)
        print('���̳Ƕ���', res.text)
        for i in range(0, 20):
            print('���̳Ƕ���index', i)
            is_bind_shop_order = res.json()['data']['data'][i]['is_bind_shop_order']  # ���̳Ƕ���
            assert is_bind_shop_order == 0

        urlselect_xiaoshou =  "/api/v1/erp_starter/sales/order?all=&cas=&customer=&start_date=&end_date=&note=&prod_name=&prod_no=&sales_no=%s&sales_no_and_customer=&page_no=1&page_size=20" % Space.sales_no
        # print('��ѯ���۶���URL',urlselect_xiaoshou)
        UserAPI.get(urlselect_xiaoshou)
        time.sleep(1)
        UserAPI.get( urlselect_xiaoshou)
        response = UserAPI.get(urlselect_xiaoshou)
        print('��ѯ���۶���', response.json())
        print('���۶���ID', response.json()['data']['data'][0]['id'])
        Space.xiaoshou_id = response.json()['data']['data'][0]['id']
        return response.json()['data']['data'][0]['id']

    # �޸����۶���
    def update_xiaoshou_order(self):
        urlupdate_order =  "/api/v1/erp_starter/sales/order/%s" % Space.xiaoshou_id
        # print(urlupdate_order)
        payload = Data_API1().update_xiaoshou_order(dqsj, dqsj1, Space.sales_no, Space.id1, Space.id2, Space.order_id)
        response = UserAPI.put(urlupdate_order, payload)
        print('�޸����۶���', response.json())
        assert response.json()['status'] == 0
        Space.xs_price = response.json()['data']['total_price'].split('.')[0]  # �����ܽ��

    # ɾ�����۶���
    def delete_xiaoshou(self):
        del_xiaoshou =  '/api/v1/erp_starter/sales/order/%s' % Space.xiaoshou_id
        response = UserAPI.delete( del_xiaoshou)
        print('ɾ�����۶���', response.json())
        assert response.json()['status'] == 0

    # �տ�
    def xiaoshou_shoukuan(self):
        urlodd =  '/api/v1/erp_starter/sales/order/collection/generate/odd'  # �տ�id
        response = UserAPI.get(urlodd)
        # print(response.text)
        print('�տ�id', response.json()['data']['current_odd_no'])
        odd_no = response.json()['data']['current_odd_no']
        urlshoukuan =  '/api/v1/erp_starter/sales/order/collection'
        # ��Ҫ��payload
        payload = Data_API1().xiaoshou_shoukuan(dqsj, Space.sales_no, odd_no, Space.id1, Space.id2)
        res = UserAPI.post( urlshoukuan, payload)
        print('�տ�', res.json())
        assert res.json()['status'] == 0
        assert res.json()['data']['sales_no'] == Space.sales_no

    # �����տ�
    def xiaoshou_piliangshoukuan(self):
        urldata =  "/api/v1/erp_starter/sales/order/collection/batch/filter?collection_status[]=1&collection_status[]=2&all=&cas=&prod_name=&note=&sales_no=&customer=���ҽҩ&order_id="
        UserAPI.get(urldata)
        time.sleep(2)
        response = UserAPI.get(urldata)
        time.sleep(3)
        print('δ�տ��', response.json())
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
        print('�����տ�', response.json())
        assert response.json()['status'] == 0
        assert response.json()['data'][0]['sales_no'] == sales_no1
        assert response.json()['data'][1]['sales_no'] == sales_no2
        # assert response.json()['data'][2]['sales_no'] == sales_no3

    # ��Ʊ
    def xiaoshou_kaipiao(self):
        urlodd =  '/api/v1/erp_starter/sales/order/invoice/generate/odd'
        response = UserAPI.get(urlodd)
        # print(response.text)
        print('��Ʊid', response.json()['data']['current_odd_no'])
        odd_no = response.json()['data']['current_odd_no']
        urlkaipiao =  '/api/v1/erp_starter/sales/order/invoice'
        payload = Data_API1().xiaoshou_kaipiao(dqsj, Space.sales_no, odd_no, Space.id1, Space.id2)
        res = UserAPI.post(urlkaipiao, payload)
        print('��Ʊ', res.json())
        assert res.json()['status'] == 0
        assert res.json()['data']['sales_no'] == Space.sales_no

    # ���۷���
    def fahuo(self):
        # ��ѯ������
        urlodd =  "/api/v1/erp_starter/sales/order/delivery/generate/odd"
        response = UserAPI.get(urlodd)
        # print(response.json())
        print('��ѯ������', response.json()['data']['current_odd_no'])  # ��ѯ������
        Space.chuku_id = response.json()['data']['current_odd_no']
        # ����
        order_fahuo =  "/api/v1/erp_starter/sales/order/delivery"
        payload = Data_API1().fahuo(dqsj, Space.sales_no, Space.chuku_id, Space.id1, Space.id2)
        response = UserAPI.post(order_fahuo, payload)
        print("����", response.text)
        assert response.json()['status'] == 0
        assert response.json()['data']['sales_no'] == Space.sales_no

    # ���������
    def qita_fahuo(self):
        urlqita =  "/api/v1/erp_starter/inventory/outbound"
        payload = Data_API1().qita_fahuo(dqsj)
        response = UserAPI.post(urlqita, payload)
        print('���������', response.json())
        assert response.json()['status'] == 0
        print('������', response.json()['data']['odd_no'])

    # ��ӡ������
    def dayin_fahuo(self):
        urlfahuo =  '/api/v1/erp_starter/sales/order/delivery/list/%s' % Space.sales_no
        response = UserAPI.get(urlfahuo)
        print('��ӡ������', response.text)
        # print('������',response.json()['data'][0]['odd_no'])
        # print('Space.chuku_id',Space.chuku_id)
        assert response.json()['data'][0]['odd_no'] == Space.chuku_id
        # Space.xs_price = response.json()['data']['total_price'].split('.')[0]
        total_price = response.json()['data'][0]['total_price'].split('.')[0]  # ���������ܽ��
        print('�����ܽ��', Space.xs_price, '�������ܽ��', total_price)
        assert Space.xs_price == total_price  # ���۽���뷢�������Ա�

    # id1,id2;Ҫ�����޸����۶�������
    def id(self):
        urlid =  '/api/v1/erp_starter/sales/order/%s' % Space.order_id
        response = UserAPI.get( urlid)
        print('id1', response.json()['data']['sales_order_prods'][0]['id'])
        print('id2', response.json()['data']['sales_order_prods'][1]['id'])
        Space.id1 = response.json()['data']['sales_order_prods'][0]['id']  # id1 �տ���Ҫ��Ӧ�Ĳ�Ʒid
        Space.id2 = response.json()['data']['sales_order_prods'][1]['id']  # id2

    # �������ϸ��ѯ
    def select_churuku(self):
        urlchuru =  '/api/v1/erp_starter/inventory/details?all=&cas=&prod_name=&prod_no=&start_date=&end_date=&page_no=1&page_size=20'
        res = UserAPI.get(urlchuru)
        assert res.json()['status'] == 0
        assert res.json()['message'] == '�����ɹ�'

    # ������Ʒ��Ϣ
    def add_chanpin(self):
        urlodd =  '/api/v1/erp_starter/inventory/product/generate/odd'
        res = UserAPI.get(urlodd)  # ���ɲ�Ʒ���
        print('��Ʒ���', res.json()['data']['current_odd_no'])
        Space.number = res.json()['data']['current_odd_no']
        urladd =  '/api/v1/erp_starter/inventory/product'
        data = Data_API1().add_chanpin(Space.number)
        res = UserAPI.post(urladd, data)
        print('������Ʒ', res.json())
        Space.chanpin_id = res.json()['data']['id']
        assert res.json()['status'] == 0
        assert Space.number == res.json()['data']['prod_no']

    # �޸Ĳ�Ʒ��Ϣ
    def update_chanpin(self):
        urlid =  '/api/v1/erp_starter/inventory/product/%s' % Space.chanpin_id
        res = UserAPI.get( urlid)
        # print('��ȡ��Ʒ��Ϣ',res.json())
        id = res.json()['data']['skus'][0]['id']
        # print('id', res.json()['data']['skus'][0]['id'])
        urlupdata =  '/api/v1/erp_starter/inventory/product/prod_no/%s' % Space.number
        data = Data_API1().update_chanpin(Space.number, id)
        res = UserAPI.put( urlupdata, data)
        print('�޸Ĳ�Ʒ��Ϣ', res.json())
        assert res.json()['status'] == 0
        assert res.json()['data']['cas'] == '19-0189'

    # ���ò�Ʒ��ǩ
    def set_chanpin_biaoqian(self):
        urlset =  '/api/v1/erp_starter/inventory/product/tag/prod/%s' % Space.chanpin_id
        payload = Data_API1().set_chanpin_biaoqian()
        res = UserAPI.post_biaodan(urlset, payload)
        print('���ò�Ʒ��ǩ', res.json())
        assert res.json()['status'] == 0

    # ɾ����Ʒ
    def delete_chanpin(self):
        urldel =  '/api/v1/erp_starter/inventory/product/%s' % Space.chanpin_id
        res = UserAPI.delete(urldel)
        print('ɾ����Ʒ', res.json())
        assert res.json()['status'] == 0

# �����ɹ�����-��ѯ�ɹ�����-�޸Ĳɹ�����-����-��Ʊ-�����ʼ챨��-�ɹ����-��ӡ��ⶩ��
# print()
# Space().add_caigou()
# Space().select_caigou()
# Space().update_caigou_order()
# Space().caigou_fukuan()
# Space().caigou_shoupiao()
# Space().zhijianbaogao()
# Space().ruku()
# Space().dayin_ruku()
# �������۶���-��ѯ���۶���-�޸����۶���-�տ�-��Ʊ-���۷���-��ӡ��������
# print()
# Space().add_xiaoshou()
# Space().id()
# Space().select_xiaoshou()
# Space().update_xiaoshou_order()
# Space().xiaoshou_shoukuan()
# Space().xiaoshou_kaipiao()
# Space().fahuo()
# Space().dayin_fahuo()
# �����ɹ�����-��ѯ�ɹ�����-�޸Ĳɹ�����-ɾ���ɹ�����
# print()
# Space().add_caigou()
# Space().select_caigou()
# Space().update_caigou_order()
# Space().delect_caigou()
# �������۶���-��ѯ���۶���-�޸����۶���-ɾ�����۶���
# print()
# Space().add_xiaoshou()
# Space().select_xiaoshou()
# Space().update_xiaoshou_order()
# Space().delete_xiaoshou()
# �����ɹ�����-��ѯ�ɹ�����-�޸Ĳɹ�����-��ʼ����ѯ-�ɹ����-�������ѯ-�������۶���-��ѯ���۶���-�޸����۶���-���۷���-���������ѯ
# Space().add_caigou()
# Space().select_caigou()
# kucun = Space().select_kucun('1074-82-4')  # ��ʼ���
# Space().update_caigou_order()
# Space().ruku()
# rkcun = Space().select_kucun('1074-82-4')  # ����Ŀ��
# assert kucun + 1000 == rkcun
# Space().add_xiaoshou()
# Space().id()
# Space().select_xiaoshou()
# Space().update_xiaoshou_order()
# Space().fahuo()
# ckkuncun = Space().select_kucun('1074-82-4')  # �����Ŀ��
# assert kucun == ckkuncun
# ��������⡢���
# kucun = Space().select_kucun('QTRK-000001') #��ʼ���
# Space().qita_ruku()
# rkkucun = Space().select_kucun('QTRK-000001') #������
# assert kucun + 100 == rkkucun
# Space().qita_fahuo()
# ckkucun = Space().select_kucun('QTRK-000001') #�������
# assert rkkucun - 100 == ckkucun
# assert kucun == ckkucun
# �����տ�
# Space().xiaoshou_piliangshoukuan()
# ������ѯ
# Space().select_churuku()
# ������Ʒ-�޸Ĳ�Ʒ��Ϣ-���ò�Ʒ��ǩ-ɾ����Ʒ
# Space().add_chanpin()
# Space().update_chanpin()
# Space().set_chanpin_biaoqian()
# Space().delete_chanpin()

