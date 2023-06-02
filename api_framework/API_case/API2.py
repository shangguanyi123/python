#coding=gbk
import time
import requests
import json
from API_case.API_data import Data_API2
from api.req_method import UserAPI

url = "http://221.226.240.154:28090"


class Yuniyng():
    daohang_id = '' #����id���޸ĵ������õ�
    liebiao_id = '' #�б�id
    danye_id = ''   #��ҳid
    daohang_name = '' #��������


    # ��������
    def add_daohang(self,name,model_type):#�������ƣ�����ģ��1��ҳ2�б�
        urladd = '/api/v1/erp_starter/site/nav'
        payload = Data_API2().add_daohang(name, model_type)
        # print(payload)
        res = UserAPI.post_biaodan(urladd,payload)
        print('��������', res.json())
        assert res.json()['status'] == 0
        assert res.json()['data']['is_show'] == '1'  # ��ʾ����
        Yuniyng.daohang_id = res.json()['data']['id']  # ����id
        Yuniyng.daohang_name = res.json()['data']['name']
    # ��ѯ������ʾ�½��ĵ���
    def select_daohang(self):
        urlsel = '/api/v1/erp_starter/site/nav?name=%s&is_show=1&position=1&page=1&per_page=20'%Yuniyng.daohang_name
        res = UserAPI.get(urlsel)
        print('��ѯ������ʾ�½��ĵ���', res.json())
        assert res.json()['status'] == 0
        assert res.json()['data']['data'][0]['is_show'] == 1  # ��ʾ����վ
        assert res.json()['data']['data'][0]['position'] == ["1", "2"]  # �����͵ײ���չʾ
    # �޸ĵ���
    def update_daohang(self):
        urlupdate = '/api/v1/erp_starter/site/nav/%s'%Yuniyng.daohang_id
        payload = Data_API2().update_daohang()
        res = UserAPI.post_biaodan(urlupdate,payload)
        print('�޸ĵ���', res.json())
        assert res.json()['status'] == 0
        assert res.json()['data']['is_show'] == '0'  # ����ʾ����
    # ɾ������
    def delete_daohang(self):
        urldel = '/api/v1/erp_starter/site/nav/%s'%Yuniyng.daohang_id
        res = UserAPI.delete(urldel)
        print('ɾ������', res.json())
        assert res.json()['status'] == 0
    # �����б�
    def add_liebiao(self):
        urladd = '/api/v1/erp_starter/site/node'
        data = Data_API2().add_liebiao(Yuniyng.daohang_id)
        res = UserAPI.post(urladd,data)
        print('�����б�',res.json())
        assert res.json()['status'] == 0
        assert res.json()['data']['is_show'] == 1 #��ʾ����վ
        Yuniyng.liebiao_id = res.json()['data']['id']
    # ��ѯ�������б�
    def select_liebiao(self):
        urlsel = '/api/v1/erp_starter/site/node?category_id=%s&is_show=1&page=1&per_page=20&model_type=2'%Yuniyng.daohang_id
        res = UserAPI.get(urlsel)
        print('��ѯ��ʾ������Ѷ���б�', res.json())
        assert res.json()['status'] == 0
        assert res.json()['data']['data'][0]['is_show_text'] == '��ʾ'  # ��ʾ����վ
        assert res.json()['data']['data'][0]['node_has_nav']['name'] == Yuniyng.daohang_name
    # �޸��б�
    def update_liebiao(self):
        urlupdate ='/api/v1/erp_starter/site/node/%s'%Yuniyng.liebiao_id
        data = Data_API2().update_liebiao()
        res = UserAPI.post(urlupdate, data)
        print('�޸��б�', res.json())
        assert res.json()['status'] == 0
        assert res.json()['data']['is_show'] == 0  # ����ʾ����վ
    # ɾ���б�
    def delete_liebiao(self):
        urldel = '/api/v1/erp_starter/site/node/%s'%Yuniyng.liebiao_id
        res = UserAPI.delete(urldel)
        print('ɾ���б�', res.json())
        assert res.json()['status'] == 0
    # ������ҳ
    def add_danye(self):
        urladd = '/api/v1/erp_starter/site/node'
        data = Data_API2().add_danye(Yuniyng.daohang_id)
        res = UserAPI.post(urladd, data)
        print('������ҳ', res.json())
        assert res.json()['status'] == 0
        assert res.json()['data']['is_show'] == 1  # ��ʾ����վ
        Yuniyng.danye_id = res.json()['data']['id']
    # ��ѯ��ҳ
    def select_danye(self):
        urlsel =  '/api/v1/erp_starter/site/node?category_id=%s&is_show=1&page=1&per_page=20&model_type=1'%Yuniyng.daohang_id
        res = UserAPI.get(urlsel)
        print('��ѯ�½��ĵ�ҳ', res.json())
        assert res.json()['status'] == 0
        assert res.json()['data']['data'][0]['is_show'] == 1  # ��ʾ����վ
        assert res.json()['data']['data'][0]['node_has_nav']['name'] == Yuniyng.daohang_name  # �����͵ײ���չʾ
    # �޸ĵ�ҳ
    def update_danye(self):
        urlupdate =  '/api/v1/erp_starter/site/node/%s' % Yuniyng.danye_id
        data = Data_API2().update_danye()
        res = UserAPI.post(urlupdate, data)
        print('�޸ĵ�ҳ', res.json())
        assert res.json()['status'] == 0
        assert res.json()['data']['is_show'] == 0  # ����ʾ����վ
    # ɾ����ҳ
    def delete_danye(self):
        urldel = '/api/v1/erp_starter/site/node/%s' % Yuniyng.danye_id
        res = UserAPI.delete(urldel)
        print('ɾ����ҳ', res.json())
        assert res.json()['status'] == 0
    # ��Ա���� ��ѯ����Ϊ�Ϲ�һ�Ļ�Ա�б�
    def select_vip(self):
        urlsel = '/api/v1/erp_starter/site/user?page=1&page_size=20&keywords=�Ϲ�һ'
        res = UserAPI.get(urlsel)
        print('��ѯ����Ϊ�Ϲ�һ�Ļ�Ա�б�', res.json())
        assert res.json()['status'] == 0
        assert res.json()['data']['data'][0]['status'] == 1  # ״̬����
        assert res.json()['data']['data'][0]['user_name'] == '�Ϲ�һ'  # ����


class Xitong():
    yonghu_id = '' #�û�ID
    juese_id = ''   #��ɫid
    # ������˾��Ϣ
    def gongsixinxi(self):
        urlgs ='/api/v1/erp_starter/system/company'
        data = Data_API2().gongsixinxi()
        res = UserAPI.post(urlgs,data)
        print('������ҳ', res.json())
        assert res.json()['status'] == 0
        assert res.json()['data']['company_name'] == '������'  # ��ʾ����վ
    # ��ɫ����
    # ������ɫ
    def add_juese(self):
        # ������ɫ
        urladd ='/api/v1/user/role'
        data = Data_API2().add_juese()
        res = UserAPI.post(urladd, data=data)
        print('ϵͳ����-��ɫ����������ɫ', res.json())
        assert res.json()['status'] == 0
        assert res.json()['data']['status'] == 1  # ״̬����
        assert res.json()['data']['name'] == '�ɹ�Ա'
        Xitong.juese_id = res.json()['data']['id']
    # ��ѯ��ɫ�ɹ�Ա
    def select_juese(self):
        urlsel ='/api/v1/user/role?name=%E9%87%87%E8%B4%AD%E5%91%98&page=1&per_page=20'
        res = UserAPI.get(urlsel)
        print('ϵͳ����-��ɫ������ѯ��ɫ�ɹ�Ա', res.json())
        assert res.json()['status'] == 0
        assert res.json()['data'][0]['status'] == 1  # ״̬����
        assert res.json()['data'][0]['name'] == '�ɹ�Ա'  # ����
    # �޸Ľ�ɫ
    def update_juese(self):
        urlupdate = '/api/v1/user/role/%s'%Xitong.juese_id
        data = Data_API2().update_juese()
        res = UserAPI.post(urlupdate,data)
        print('ϵͳ����-��ɫ�����޸Ľ�ɫ',res.json())
        assert res.json()['data']['status'] == 1 # ״̬����
        assert res.json()['data']['name'] == '�ɹ�Ա'
    # ɾ����ɫ
    def delete_juese(self):
        urldel ='/api/v1/user/role/%s' % Xitong.juese_id
        res = UserAPI.post(urldel, Data_API2().delete_juese())
        print('ϵͳ����-��ɫ����ɾ����ɫ', res.json())
        assert res.json()['status'] == 0
    # �û�����
    # �����û�
    def add_yonghu(self):
        urladd = '/api/v1/user'
        data = Data_API2().add_yonghu(Xitong.juese_id)
        res = UserAPI.post(urladd,data)
        print('ϵͳ����-�û����������û�', res.json())
        assert res.json()['status'] == 0
        assert res.json()['data']['roles'][0]['status'] == 1  # ״̬����
        Xitong.yonghu_id = res.json()['data']['roles'][0]['pivot']['model_id']
    # ��ѯ�û�jws
    def select_yonghu(self):
        urlsel = '/api/v1/user?username=jws&page=1&per_page=20'
        res = UserAPI.get(urlsel)
        print('ϵͳ����-�û�������ѯ�û�jsw', res.json())
        assert res.json()['status'] == 0
        assert res.json()['data']['data'][0]['status'] == 1  # ״̬����
        assert res.json()['data']['data'][0]['username'] == 'jws'  # ����
    # ɾ���û�
    def delete_yonghu(self):
        urldel = '/api/v1/user/%s' % Xitong.yonghu_id
        res = UserAPI.post(urldel,Data_API2().delete_yonghu())
        print('ϵͳ����-�û�����ɾ���û�', res.json())
        assert res.json()['status'] == 0


# ������ҳ����-��ѯ����-������ҳ��������Ӧ������-��ѯ��ҳ-�޸ĵ�ҳ-ɾ����ҳ-�޸ĵ���-ɾ������
# Yuniyng().add_daohang('��ҳ',1)
# Yuniyng().select_daohang()
# Yuniyng().add_danye()
# Yuniyng().select_danye()
# Yuniyng().update_danye()
# Yuniyng().delete_danye()
# Yuniyng().update_daohang()
# Yuniyng().delete_daohang()
# �����б���-��ѯ����-�����б�������Ӧ������-��ѯ�б�-�޸��б�-ɾ���б�-�޸ĵ���-ɾ������
# Yuniyng().add_daohang('�б�',2)
# Yuniyng().select_daohang()
# Yuniyng().add_liebiao()
# Yuniyng().select_liebiao()
# Yuniyng().update_liebiao()
# Yuniyng().delete_liebiao()
# Yuniyng().update_daohang()
# Yuniyng().delete_daohang()

# ��Ա���� ��ѯ�û���Ϣ
# Yuniyng().select_vip()
# ϵͳ���� ������ɫ-��ѯ��ɫ-�����û�-��ѯ�û�-ɾ���û�-�޸Ľ�ɫ-ɾ����ɫ
# Xitong().add_juese()
# Xitong().select_juese()
# Xitong().add_yonghu()
# Xitong().select_yonghu()
# Xitong().delete_yonghu()
# Xitong().update_juese()
# Xitong().delete_juese()
















