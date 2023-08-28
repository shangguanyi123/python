#coding=gbk
import time
import pytest

from api_framework.API_case.API_data import Data_API1
from api_framework.api.req_method import UserAPI
from api_framework.sql import MySQLHelper


dqsj1 = time.strftime("%Y-%m-%d %H:%M:%S")

class Xitongguanli():
    user_id = ''
    juese_id = ''
    danwei_id = ''
    danju_id = ''
    danjuleixing_id = ''
    danwei_bianma = ''
    diqu_id = ''
    fuzhuzilaio_fenlei_id = ''
    fuzhuzilaio_fenlei_key = ''
    fuzhuzilaio_mingcheng_id = ''
    fuzhuzilaio_mingcheng_key = ''
    fuzhushuxing_id = ''
    fuzhushuxing_field_name = ''
    #�û���ѯ
    username = ''
    user_no = ''
    name = ''
    phone = ''
    user_type = ''
    role_id = ''

    # ʹ�ò�����װ���������������
    def add_user(self,status):
        id  = int(time.time())
        uname = f"test{id}"
        #��ȡ�û����
        url = '/api/v1/system/user/userno'
        res = UserAPI.get(url)
        print('��ȡ�û����',res.json()['data'])
        bianhao = res.json()['data']
        #�����û�
        url = '/api/v1/system/user/store'
        data = Data_API1().add_user(bianhao,uname,id,status)
        res = UserAPI.post(url,data)
        print('�����û�',res.json())
        Xitongguanli.user_id = res.json()['data']['id']
        Xitongguanli.username = res.json()['data']['username']
        assert res.status_code == 200
        assert res.json()['data']['name'] == uname
        assert res.json()['data']['status'] == status,'�����û�״̬����'
        #�˽ӿ�δ����email
    def select_user(self,status):
        url = f'/api/v1/system/user/index?page=1&page_size=10&status={status}&search[0][user_no]=&search[0][username]={Xitongguanli.username}&search[0][name]=&org_id=1&user_no=&username={Xitongguanli.username}&name='
        res = UserAPI.get(url)
        assert res.status_code == 200
        assert res.json()['status'] == 0
        for i in res.json()['data']['data']:
            assert i['status'] == status,'��ѯ�û�״̬����'
        if res.json()['data']['data']:
            Xitongguanli.username = res.json()['data']['data'][0]['username']
            Xitongguanli.user_no = res.json()['data']['data'][0]['user_no']
            Xitongguanli.name = res.json()['data']['data'][0]['name']
            Xitongguanli.phone = res.json()['data']['data'][0]['phone']
            Xitongguanli.user_type = res.json()['data']['data'][0]['user_type']
            Xitongguanli.user_id = res.json()['data']['data'][0]['id']
            Xitongguanli.role_id = res.json()['data']['data'][0]['role_ids'][0]
    def update_uesr(self,bumen,juese,status):
        url = '/api/v1/system/user/update'
        data = Data_API1().update_user(Xitongguanli.username,Xitongguanli.user_no,Xitongguanli.name,bumen,Xitongguanli.phone,Xitongguanli.user_type,status,juese,Xitongguanli.user_id)
        res = UserAPI.post(url,data)
        print('�޸��û�',res.json())
        assert res.status_code == 200
        assert res.json()['message'] == '�����ɹ�'
        assert res.json()['status'] == 0
        assert res.json()['data']['roles'][0]['id'] == juese,'��ɫ��һ��'
        assert res.json()['data']['status'] == status,'״̬��һ��'
        #�˽ӿ���δ���ز����ֶ�
    def del_user(self):
        url = '/api/v1/system/user/destroy'
        data  = Data_API1().del_user(Xitongguanli.user_id)
        res = UserAPI.post(url,data)
        print('ɾ���û�',res.json())
        assert res.status_code == 200
        assert res.json()['message'] == '�����ɹ�'
        assert res.json()['status'] == 0
    def update_user_status(self,sel_status,update_status):
        #��ѯ�����û�
        url = f'/api/v1/system/user/index?page=1&page_size=10&status={sel_status}&org_id=1'
        sel_res = UserAPI.get(url)
        user_id = []
        if sel_res.json()['data']['data']:
            for i in sel_res.json()['data']['data']:
                user_id.append(i['id'])
            #�޸��û�״̬
            url = '/api/v1/system/user/status'
            data = Data_API1().update_user_status(user_id,update_status)
            res = UserAPI.post(url,data)
            assert res.status_code == 200
            assert res.json()['message'] == '�����ɹ�'
            assert len(sel_res.json()['data']['data']) == res.json()['data']
    def add_juese(self,name,status):
        #������ɫ
        url1 = '/api/v1/system/role/store'
        data1,data2 = Data_API1().add_juese(name,status)
        res1 = UserAPI.post(url1,data1)
        print('������ɫ',res1.json())
        assert res1.status_code == 200
        assert res1.json()['status'] == 0
        assert res1.json()['data']['status'] == status
        Xitongguanli.juese_id = res1.json()['data']['id']
        #��ɫ��Ȩ,Ŀǰֻ���˹���Ȩ��
        url2 = '/api/v1/system/role/assign_permissions'
        data1, data2 = Data_API1().add_juese(name, status,Xitongguanli.juese_id)
        res2 = UserAPI.post(url2,data2)
        print('��ɫ��Ȩ',res2.json())
        assert res2.status_code == 200
        assert res2.json()['status'] == 0
    def insert_uesr_juese(self):
        #���������ɫ
        url = '/api/v1/system/role/assign_users'
        data = Data_API1().insert_uesrt(Xitongguanli.user_id,Xitongguanli.juese_id)
        res = UserAPI.post(url,data)
        print('���������ɫ',res.json())
        assert res.status_code == 200
        #��ѯ�û��Ƿ���ӵ��ý�ɫ
        url = f'/api/v1/system/role/users?page=1&page_size=10&search[0][user_no]=&search[0][username]={Xitongguanli.username}&search[0][name]=&role_id={Xitongguanli.juese_id}&user_no=&username={Xitongguanli.username}&name='
        res = UserAPI.get(url)
        print('��ѯ�û��Ƿ���ӵ��ý�ɫ',res.json()['data']['data'][0]['user']['username'])
        assert res.status_code == 200
        assert res.json()['status'] == 0
        assert res.json()['data']['data'][0]['user']['username'] == Xitongguanli.username
    def del_user_juese(self):
        url = '/api/v1/system/role/remove_users'
        data = Data_API1().del_user_juese(Xitongguanli.user_id,Xitongguanli.juese_id)
        res = UserAPI.post(url,data)
        print('ɾ���û�������ɫ',res.json())
        assert res.status_code == 200
        assert res.json()['message'] == '�����ɹ�'
        assert res.json()['status'] == 0
        url = f'/api/v1/system/role/users?page=1&page_size=10&search[0][user_no]=&search[0][username]={Xitongguanli.username}&search[0][name]=&role_id={Xitongguanli.juese_id}&user_no=&username={Xitongguanli.username}&name='
        res = UserAPI.get(url)
        print('ɾ�����ѯ�ý�ɫ',res.json()['data']['data'])
        assert res.status_code == 200
        assert res.json()['data']['data'] == [], 'ɾ����ɫʧ�ܣ���ɫ���Ǵ���'
    def del_juese(self):
        url = '/api/v1/system/role/destroy'
        data = Data_API1().del_juese(Xitongguanli.juese_id)
        res = UserAPI.post(url,data)
        print('ɾ����ɫ',res.json())
        assert res.status_code == 200
        assert res.json()['status'] == 0
        MySQLHelper().execute_delete('roles','deleted_at IS NOT NULL')
    def add_danwei(self,leixing,danwei,zhuangtai,jl_danwei=None,jibengang=None,zhuanhualv=None):#jl_danwei:weight length area volume number_of_packages time other
        url = '/api/v1/system/base/units/store'
        data = Data_API1().add_danwei(leixing,danwei,zhuangtai,jl_danwei,jibengang,zhuanhualv)
        res = UserAPI.post(url,data)
        print('������λ',res.json())
        assert res.status_code == 200
        assert res.json()['status'] == 0
        assert res.json()['data']['status'] == zhuangtai
        assert res.json()['data']['name'] == danwei
        Xitongguanli.danwei_bianma = res.json()['data']['code']
        Xitongguanli.danwei_id= res.json()['data']['id']
    def sel_danwei(self,danweileixing): #package package
        url = f'/api/v1/system/base/units/index?page=1&page_size=10&classes={danweileixing}'
        res = UserAPI.get(url)
        assert res.status_code == 200
        assert res.json()['status'] == 0
        if res.json()['data']['data']:
            for i in res.json()['data']['data']:
                assert i['classes'] == danweileixing
    def update_danwei(self, leixing, danwei, zhuangtai, jl_danwei=None, jibengang=None,zhuanhualv=None):  # jl_danwei:weight length area volume number_of_packages time other
        url = '/api/v1/system/base/units/update'
        data = Data_API1().update_danwei(leixing, danwei, zhuangtai,Xitongguanli.danwei_id,Xitongguanli.danwei_bianma,jl_danwei, jibengang, zhuanhualv)
        res = UserAPI.post(url, data)
        print('�޸ĵ�λ', res.json())
        assert res.status_code == 200
        assert res.json()['status'] == 0
        assert res.json()['data']['status'] == zhuangtai
        assert res.json()['data']['name'] == danwei
    def del_danwei(self):
        url = '/api/v1/system/base/units/destroy'
        data = Data_API1().del_danwei(Xitongguanli.danwei_id)
        res = UserAPI().post(url,data)
        print('ɾ����λ',res.json())
        assert res.status_code == 200
        assert res.json()['status'] == 0
    def select_danjuleixing_shengheduize_id(self,dj_leixing,dj_guize):
        # ��ѯ�������ͣ���˹���
        url_sel = '/api/v1/system/individuation/documents/cases'
        res_sel = UserAPI.get(url_sel)
        assert res_sel.status_code == 200
        assert res_sel.json()['status'] == 0
        # print('��ѯ���������ͣ���˹���',res_sel.json())
        danjuleixing = {}
        shenheguize = {}
        # �ѵ������ͺ���˹���浽�ֵ�
        for i in res_sel.json()['data']['business_document_values']:
            danjuleixing.update({i['name']: i['val']})
        for i in res_sel.json()['data']['option_value']:
            shenheguize.update({i['label']: i['value']})
        # print(danjuleixing,'\n',shenheguize)
        # ��ѯ����ĵ������ͣ�����
        keys_to_query = dj_leixing
        leixing_id = [danjuleixing[key] for key in keys_to_query]
        print('��һ����������id', leixing_id[0])
        Xitongguanli.danjuleixing_id = leixing_id[0]
        guize_id = shenheguize[dj_guize]
        return leixing_id,guize_id
    def add_danjushenhe(self,dj_leixing,dj_guize,price=None):
        lx_id,gz_id =Xitongguanli().select_danjuleixing_shengheduize_id(dj_leixing,dj_guize)
        # #�����������
        url_add = '/api/v1/system/individuation/documents/store'
        data_add = Data_API1().add_danjushenhe(lx_id,gz_id,price)
        res_add = UserAPI.post(url_add,data_add)
        print('�����������',res_add.json())
        assert res_add.status_code == 200
        assert res_add.json()['status'] == 0
        Xitongguanli.danju_id = res_add.json()['data']['id']
    def sel_danjushenhe(self):
        url = f'/api/v1/system/individuation/documents/index?page=1&page_size=10&val={Xitongguanli.danjuleixing_id}'
        res = UserAPI.get(url)
        #print('��ѯ�������',res.json())
        assert res.status_code == 200
        assert res.json()['status'] == 0
        assert res.json()['data']['data'][0]['id'] == Xitongguanli.danju_id
        Xitongguanli.danju_id = res.json()['data']['data'][0]['id']
    def update_danjushenhe(self,dj_leixing,dj_guize,price=None):
        lx_id, gz_id = Xitongguanli().select_danjuleixing_shengheduize_id(dj_leixing, dj_guize)
        url = '/api/v1/system/individuation/documents/update'
        data = Data_API1().update_danjushenhe(Xitongguanli.danju_id,lx_id,gz_id,price)
        res = UserAPI.post(url,data)
        print('�޸ĵ������',res.json())
        assert res.status_code == 200
        assert res.json()['status'] == 0
        assert res.json()['data'] == 1
    def del_danjushenhe(self):
        url = '/api/v1/system/individuation/documents/destroy'
        data = Data_API1().del_danjushenhe(Xitongguanli.danju_id)
        res = UserAPI.post(url,data)
        print('ɾ���������',res.json())
        assert res.status_code == 200
        assert res.json()['status'] == 0
        assert res.json()['data'] == 1
    def gonggongcanshu_email(self):
        url = '/api/v1/system/base/parameters/email/test'
        data = Data_API1().gonggongcanshu_email()
        res = UserAPI.post(url,data)
        print('ϵͳ����-�������������Ͳ����ʼ�',res.json())
        assert res.status_code == 200
        assert res.json()['message'] == '���ͳɹ�'
    def add_diqu(self,status,diqu):
        url = '/api/v1/system/base/areas/store'
        data = Data_API1().add_diqu(status,diqu)
        res = UserAPI.post(url,data)
        print('��������',res.json())
        assert res.status_code == 200
        assert res.json()['data']['status'] == status
    def sel_diqu(self,diqu):
        url = f'/api/v1/system/base/areas/index?page=1&page_size=10&name_zh={diqu}&country_id=1'
        res = UserAPI.get(url)
        print('��ѯ����',res.json()['data']['data'])
        assert res.status_code == 200
        assert res.json()['data']['data'][0]['county_name'] == diqu
        Xitongguanli.diqu_id = res.json()['data']['data'][0]['id']
    def update_diqu(self,status,diqu):
        url = '/api/v1/system/base/areas/update'
        data = Data_API1().update_diqu(status,diqu,Xitongguanli.diqu_id)
        res = UserAPI.post(url,data)
        print('�޸ĵ���',res.json())
        assert res.status_code == 200
        assert res.json()['data']['status'] == status
        assert res.json()['data']['name_zh'] == diqu
    def del_diqu(self,diqu):
        #ɾ������
        url = '/api/v1/system/base/areas/destroy'
        data =Data_API1().del_diqu(Xitongguanli.diqu_id)
        res = UserAPI.post(url,data)
        print('ɾ������',res.json())
        assert res.status_code == 200
        assert res.json()['data'] == 1
        #ɾ�����ѯ�����Ƿ����
        url = f'/api/v1/system/base/areas/index?page=1&page_size=10&name_zh={diqu}&country_id=1'
        res = UserAPI.get(url)
        assert res.json()['data']['data'] == []
    def update_biaohao_guize(self,bianmafenduan):
        dqsj = time.strftime("%Y%m%d")
        url = '/api/v1/system/individuation/numbering/update'
        data = Data_API1().update_biaohao_guize(bianmafenduan)
        res = UserAPI.post(url,data)
        if bianmafenduan == 1:
            print('�޸ı�Ź���',res.json())
            assert res.status_code == 200
            assert res.json()['data']['demo'] == '000001'
        elif bianmafenduan == 2:
            print('�޸ı�Ź���',res.json())
            assert res.status_code == 200
            assert res.json()['data']['demo'] == 'CP000001'
        elif bianmafenduan == 3:
            print('�޸ı�Ź���',res.json())
            assert res.status_code == 200
            assert res.json()['data']['demo'] == f"CP{dqsj}000001"
        elif bianmafenduan == 4:
            assert res.status_code != 200
            print('�޸ı�Ź���',res.json()['message'])
            assert res.json()['message'] == f"ͬһ�������������á���ˮ�š����ݹ���"
        elif bianmafenduan == 5:
            assert res.status_code != 200
            print('�޸ı�Ź���',res.json()['message'])
            assert res.json()['message'] == f"ͬһ�������������á���ˮ�š����ݹ���"
    def sel_biaohao_guize(self,name):
        url = f'/api/v1/system/individuation/numbering/index?page=1&page_size=10&rules_name={name}&category_name='
        res = UserAPI.get(url)
        print('��ѯ��Ź���',res.json()['data']['data'][0])
        assert res.status_code == 200
        assert res.json()['data']['data'][0]['rules_name'] == name
    def add_fuzhuzilaio_fenlei(self,name):
        url = '/api/v1/enums/category/store'
        data = Data_API1().add_fuzhuziliao_feilei(name)
        res = UserAPI.post(url,data)
        print('������������',res.json())
        assert res.status_code == 200
        Xitongguanli.fuzhuzilaio_fenlei_id = res.json()['data']['id']
        Xitongguanli.fuzhuzilaio_fenlei_key = res.json()['data']['key']
        assert res.json()['data']['title'] == name
    def update_fuzhuzilaio_fenlei(self,name):
        #�޸ĸ������Ϸ���
        url = '/api/v1/enums/category/update'
        data = Data_API1().update_fuzhuziliao_fenlei(Xitongguanli.fuzhuzilaio_fenlei_id,name)
        res = UserAPI.post(url,data)
        print('�޸ĸ������Ϸ���',res.json())
        assert res.status_code == 200
        assert res.json()['data'] == 1
    def add_fuzhuzilaio_mingcheng(self,name,status):
        url = '/api/v1/enums/store'
        data = Data_API1().add_fuzhuziliao_mingcheng(Xitongguanli.fuzhuzilaio_fenlei_key,name,status)
        res = UserAPI.post(url,data)
        print('����������������',res.json())
        assert res.status_code == 200
        assert res.json()['data']['status'] == status
        assert res.json()['data']['value']['name'] == name
        Xitongguanli.fuzhuzilaio_mingcheng_id = res.json()['data']['id']
        Xitongguanli.fuzhuzilaio_mingcheng_key = res.json()['data']['key']
    def update_fuzhuziliao_mingcheng(self,name,status):
        url = '/api/v1/enums/update'
        data = Data_API1().update_fuzhuziliao_mingcheng(Xitongguanli.fuzhuzilaio_mingcheng_id,Xitongguanli.fuzhuzilaio_mingcheng_key,name,status)
        res = UserAPI.post(url,data)
        print('�޸ĸ�����������',res.json())
        assert res.status_code == 200
        assert res.json()['data']['status'] == status
        assert res.json()['data']['value']['name'] == name
    def del_fuzhuziliao_mingcheng(self,name):
        #ɾ��������������
        url = '/api/v1/enums/destroy'
        data = Data_API1().del_fuzhuziliao_mingcheng(Xitongguanli.fuzhuzilaio_mingcheng_id)
        res = UserAPI.post(url,data)
        print('ɾ��������������',res.json())
        assert res.status_code == 200
        assert res.json()['data'] == 1
        #ɾ�����ѯ�Ƿ����
        url1 = f'/api/v1/enums/index?page=1&page_size=10&title={name}&key='
        res1 = UserAPI.get(url1)
        assert res1.json()['data']['data'] == []
    def del_fuzhuziliao_fenlei(self):
        url = '/api/v1/enums/category/destroy'
        data = Data_API1().del_fuzhuziliao_fenlei(Xitongguanli.fuzhuzilaio_fenlei_id)
        res = UserAPI.post(url,data)
        print('ɾ���������Ϸ���',res.json())
        assert res.status_code == 200
        assert res.json()['data'] == 1
    def add_fuzhushuxing(self,name,type,status,len=None): # type : varchar int timestamp auxiliary_category
        url = '/api/v1/system/individuation/profile/store'
        data = Data_API1().add_fuzhushuxing(name,type,status,len)
        res = UserAPI.post(url,data)
        print('������������',res.json())
        assert res.status_code == 200
        assert res.json()['data']['show_name'] == name
        assert res.json()['data']['data_type'] == type
        assert res.json()['data']['status'] == status
        Xitongguanli.fuzhushuxing_id = res.json()['data']['id']
        Xitongguanli.fuzhushuxing_field_name = res.json()['data']['field_name']
    def update_fuzhushuxing(self,name,type,status,len=None):
        url = '/api/v1/system/individuation/profile/update'
        data = Data_API1().update_fuzhushuxing(Xitongguanli.fuzhushuxing_id,name,type,status,len)
        res = UserAPI.post(url,data)
        print('�޸ĸ�������',res.json())
        assert res.status_code == 200
        assert res.json()['data']['show_name'] == name
        assert res.json()['data']['data_type'] == type
        assert res.json()['data']['status'] == status
    def del_fuzhushuxing(self):
        url = '/api/v1/system/individuation/profile/destroy'
        data = Data_API1().del_fuzhushuxing(Xitongguanli.fuzhushuxing_id)
        res = UserAPI.post(url,data)
        print('ɾ����������',res.json())
        assert res.status_code == 200
        assert res.json()['data'] == 1








# #�����û�-��ѯ-�޸��û�(���š���ɫ��״̬)-ɾ���û�
# Xitongguanli().add_user(1)
# Xitongguanli().select_user(1)
# Xitongguanli().update_uesr(20,1,1)
# Xitongguanli().del_user()
# Xitongguanli().update_user_status(0,1)
# #�����û�-������ɫ-����û�����ɫ-ɾ���û�������ɫ-ɾ����ɫ-ɾ���û�
# Xitongguanli().add_user(1)
# Xitongguanli().add_juese('ϵͳ����Ա����ʱ��',1)
# Xitongguanli().insert_uesr_juese()
# Xitongguanli().del_user_juese()
# Xitongguanli().del_juese()
# Xitongguanli().del_user()
# #������λ-��ѯ��λ-ɾ����λ
# Xitongguanli().add_danwei(1,'mm',1,'length',1,'0.001')
# Xitongguanli().update_danwei(0,'mm',1,)
# Xitongguanli().sel_danwei('package')
# Xitongguanli().del_danwei()
# #�����������-��ѯ�������-�޸ĵ������-ɾ���������
# Xitongguanli().add_danjushenhe(['���۶���'],'��Ҫ���')
# Xitongguanli().sel_danjushenhe()
# Xitongguanli().update_danjushenhe(['���۶���','�ɹ�����'],'����������',10000)
# Xitongguanli().del_danjushenhe()
# #ϵͳ����
# Xitongguanli().gonggongcanshu_email()
# #��������-��ѯ����-�޸ĵ���-ɾ������
# Xitongguanli().add_diqu(0,'������')
# Xitongguanli().sel_diqu('������')
# Xitongguanli().update_diqu(1,'���Ե���')
# Xitongguanli().del_diqu('���Ե���')
# #�޸ı�Ź���-��ѯ��Ź���
# Xitongguanli().update_biaohao_guize(1)
# Xitongguanli().update_biaohao_guize(2)
# Xitongguanli().update_biaohao_guize(3)
# Xitongguanli().update_biaohao_guize(4)
# Xitongguanli().update_biaohao_guize(5)
# Xitongguanli().sel_biaohao_guize('��Ʒ���')
# #�����������Ϸ���-�޸ĸ������Ϸ���-����������������-�޸ĸ�����������-ɾ��������������-ɾ���������Ϸ���
# Xitongguanli().add_fuzhuzilaio_fenlei('�������ͣ����ԣ�')
# Xitongguanli().update_fuzhuzilaio_fenlei('��������')
# Xitongguanli().add_fuzhuzilaio_mingcheng('��������vip',1)
# Xitongguanli().update_fuzhuziliao_mingcheng('����vip',0)
# Xitongguanli().del_fuzhuziliao_mingcheng('����vip')
# Xitongguanli().del_fuzhuziliao_fenlei()
# # ������������-�޸ĸ�������-ɾ����������
# Xitongguanli().add_fuzhushuxing('���ر��루���ԣ�','varchar',0,50)
# Xitongguanli().update_fuzhushuxing('���ر���test','int',1,50)
# Xitongguanli().del_fuzhushuxing()




















