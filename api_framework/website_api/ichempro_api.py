#encoding=utf-8
import random

from website_api.ichenpro_data import *
from message_api.req_method import UserAPI

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
    #用户查询
    username = ''
    user_no = ''
    name = ''
    phone = ''
    user_type = ''
    role_id = ''


    def add_user(self,status):
        id  = int(time.time())
        uname = f"test{id}"
        #获取用户编号
        url1 = '/api/v1/system/user/userno'
        res1 = UserAPI.get(url1)
        print('获取用户编号',res1.json()['data'])
        bianhao = res1.json()['data']
        #获取部门id
        url2 = '/api/v1/system/org/index'
        res2 = UserAPI.get(url2)
        #print('获取部门',res2.json())
        bumen = random.randint(0,len(res2.json()['data'][0]['children'])-1)
        print('随机部门id',res2.json()['data'][0]['children'][bumen]['id'])
        bumen_id = res2.json()['data'][0]['children'][bumen]['id']
        #获取所有角色
        url3 = '/api/v1/system/role/index?status=1'
        res3 = UserAPI.get(url3)
        juese = random.randint(0,len(res3.json()['data'])-1)
        print('随机角色id',res3.json()['data'][juese]['id'])
        juese_id = res3.json()['data'][juese]['id']
        #新增用户
        url = '/api/v1/system/user/store'
        data = Data_xitong().add_user(bianhao,uname,bumen_id,juese_id,id,status)
        res = UserAPI.post(url,data)
        print('新增用户',res.json())
        assert res.status_code == 200
        assert res.json()['data']['name'] == uname
        assert res.json()['data']['status'] == status,'新增用户状态不符'
        Xitongguanli.user_id = res.json()['data']['id']
        Xitongguanli.username = res.json()['data']['username']
    def select_user(self,status):
        url = f'/api/v1/system/user/index?page=1&page_size=10&status={status}&search[0][user_no]=&search[0][username]={Xitongguanli.username}&search[0][name]=&org_id=1&user_no=&username={Xitongguanli.username}&name='
        res = UserAPI.get(url)
        assert res.status_code == 200
        assert res.json()['status'] == 0
        print('查询用户',res.json())
        for i in res.json()['data']['data']:
            assert i['status'] == status,'查询用户状态不符'
        if res.json()['data']['data']:
            Xitongguanli.username = res.json()['data']['data'][0]['username']
            Xitongguanli.user_no = res.json()['data']['data'][0]['user_no']
            Xitongguanli.name = res.json()['data']['data'][0]['name']
            Xitongguanli.phone = res.json()['data']['data'][0]['phone']
            Xitongguanli.user_type = res.json()['data']['data'][0]['user_type']
            Xitongguanli.user_id = res.json()['data']['data'][0]['id']
            Xitongguanli.role_id = res.json()['data']['data'][0]['role_ids'][0]
        return res
    def update_uesr(self,status):
        # 获取部门id
        url2 = '/api/v1/system/org/index'
        res2 = UserAPI.get(url2)
        # print('获取部门',res2.json())
        bumen = random.randint(0, len(res2.json()['data'][0]['children']) - 1)
        print('随机部门id', res2.json()['data'][0]['children'][bumen]['id'])
        bumen_id = res2.json()['data'][0]['children'][bumen]['id']
        # 获取所有角色
        url3 = '/api/v1/system/role/index?status=1'
        res3 = UserAPI.get(url3)
        juese = random.randint(0, len(res3.json()['data']) - 1)
        print('随机角色id', res3.json()['data'][juese]['id'])
        juese_id = res3.json()['data'][juese]['id']
        #修改用户
        url = '/api/v1/system/user/update'
        data = Data_xitong().update_user(Xitongguanli.username,Xitongguanli.user_no,Xitongguanli.name,bumen_id,Xitongguanli.phone,Xitongguanli.user_type,status,juese_id,Xitongguanli.user_id)
        res = UserAPI.post(url,data)
        print('修改用户',res.json())
        assert res.status_code == 200
        assert res.json()['message'] == '操作成功'
        assert res.json()['status'] == 0
        assert res.json()['data']['roles'][0]['id'] == juese_id,'角色不一致'
        assert res.json()['data']['status'] == status,'状态不一致'
        #此接口暂未返回部门字段
    def del_user(self):
        url = '/api/v1/system/user/destroy'
        data  = Data_xitong().del_user(Xitongguanli.user_id)
        res = UserAPI.post(url,data)
        print('删除用户',res.json())
        assert res.status_code == 200
        assert res.json()['message'] == '操作成功'
        assert res.json()['status'] == 0
    def update_user_status(self,status,update_status):
        #查询所有用户
        url = f'/api/v1/system/user/index?page=1&page_size=10&status={status}&org_id=1'
        sel_res = UserAPI.get(url)
        user_id = []
        if sel_res.json()['data']['data']:
            for i in sel_res.json()['data']['data']:
                user_id.append(i['id'])
            #修改用户状态
            url = '/api/v1/system/user/status'
            data = Data_xitong().update_user_status(user_id,update_status)
            res = UserAPI.post(url,data)
            assert res.status_code == 200
            assert res.json()['message'] == '操作成功'
            assert len(sel_res.json()['data']['data']) == res.json()['data']
    def add_juese(self,name,status):
        #新增角色
        url1 = '/api/v1/system/role/store'
        data1,data2 = Data_xitong().add_juese(name,status)
        res1 = UserAPI.post(url1,data1)
        print('新增角色',res1.json())
        if res1.status_code == 200:
            assert res1.json()['status'] == 0
            assert res1.json()['data']['status'] == status
            Xitongguanli.juese_id = res1.json()['data']['id']

            # 角色授权,目前只加了功能权限
            url2 = '/api/v1/system/role/assign_permissions'
            data1, data2 = Data_xitong().add_juese(name, status, Xitongguanli.juese_id)
            res2 = UserAPI.post(url2, data2)
            print('角色授权', res2.json())
            assert res2.status_code == 200
            assert res2.json()['status'] == 0
        elif res1.status_code == 422:
            assert res1.json()['message'] == "'角色名称'已经存在."
        else:
            assert False,'状态码错误，请检查接口返回字段'

    def insert_uesr_juese(self):
        #添加所属角色
        url = '/api/v1/system/role/assign_users'
        data = Data_xitong().insert_uesrt(Xitongguanli.user_id,Xitongguanli.juese_id)
        res = UserAPI.post(url,data)
        print('添加所属角色',res.json())
        assert res.status_code == 200
        #查询用户是否添加到该角色
        url = f'/api/v1/system/role/users?page=1&page_size=10&search[0][user_no]=&search[0][username]={Xitongguanli.username}&search[0][name]=&role_id={Xitongguanli.juese_id}&user_no=&username={Xitongguanli.username}&name='
        res = UserAPI.get(url)
        print('查询用户是否添加到该角色',res.json()['data']['data'][0]['user']['username'])
        assert res.status_code == 200
        assert res.json()['status'] == 0
        assert res.json()['data']['data'][0]['user']['username'] == Xitongguanli.username
    def del_user_juese(self):
        url = '/api/v1/system/role/remove_users'
        data = Data_xitong().del_user_juese(Xitongguanli.user_id,Xitongguanli.juese_id)
        res = UserAPI.post(url,data)
        print('删除用户所属角色',res.json())
        assert res.status_code == 200
        assert res.json()['message'] == '操作成功'
        assert res.json()['status'] == 0
        url = f'/api/v1/system/role/users?page=1&page_size=10&search[0][user_no]=&search[0][username]={Xitongguanli.username}&search[0][name]=&role_id={Xitongguanli.juese_id}&user_no=&username={Xitongguanli.username}&name='
        res = UserAPI.get(url)
        print('删除后查询该角色',res.json()['data']['data'])
        assert res.status_code == 200
        assert res.json()['data']['data'] == [], '删除角色失败，角色还是存在'
    def del_juese(self):
        url = '/api/v1/system/role/destroy'
        data = Data_xitong().del_juese(Xitongguanli.juese_id)
        res = UserAPI.post(url,data)
        print('删除角色',res.json())
        assert res.status_code == 200
        assert res.json()['status'] == 0
        #MySQLHelper().execute_update('roles','deleted_at IS NOT NULL')
    def add_danwei(self,leixing,danwei,zhuangtai,jl_danwei=None,jibengang=None,zhuanhualv=None):#jl_danwei:weight length area volume number_of_packages time other
        url = '/api/v1/system/base/units/store'
        data = Data_xitong().add_danwei(leixing,danwei,zhuangtai,jl_danwei,jibengang,zhuanhualv)
        res = UserAPI.post(url,data)
        print('新增单位',res.json())
        if res.status_code == 200:
            assert res.status_code == 200
            assert res.json()['status'] == 0
            assert res.json()['data']['status'] == zhuangtai
            assert res.json()['data']['name'] == danwei
            Xitongguanli.danwei_bianma = res.json()['data']['code']
            Xitongguanli.danwei_id = res.json()['data']['id']
        elif res.status_code == 422:
            assert res.json()['message'] == '同一所属量纲，只能有一个单位为基本纲' or "'编码'已经存在."
        else:
            assert False,'状态码错误，请检查接口返回信息'
    def sel_danwei(self,danweileixing): #package measure
        url = f'/api/v1/system/base/units/index?page=1&page_size=10&classes={danweileixing}'
        res = UserAPI.get(url)
        assert res.status_code == 200
        assert res.json()['status'] == 0
        if res.json()['data']['data']:
            for i in res.json()['data']['data']:
                assert i['classes'] == danweileixing
        return res
    def update_danwei(self, leixing, danwei, zhuangtai, jl_danwei=None, jibengang=None,zhuanhualv=None):  # jl_danwei:weight length area volume number_of_packages time other
        url = '/api/v1/system/base/units/update'
        data = Data_xitong().update_danwei(leixing, danwei, zhuangtai,Xitongguanli.danwei_id,Xitongguanli.danwei_bianma,jl_danwei, jibengang, zhuanhualv)
        res = UserAPI.post(url, data)
        print('修改单位', res.json())
        assert res.status_code == 200
        assert res.json()['status'] == 0
        assert res.json()['data']['status'] == zhuangtai
        assert res.json()['data']['name'] == danwei
    def del_danwei(self):
        url = '/api/v1/system/base/units/destroy'
        data = Data_xitong().del_danwei(Xitongguanli.danwei_id)
        res = UserAPI().post(url,data)
        print('删除单位',res.json())
        assert res.status_code == 200
        assert res.json()['status'] == 0
    def select_danjuleixing_shengheduize_id(self,dj_leixing,dj_guize):
        # 查询单据类型，审核规则
        url_sel = '/api/v1/system/individuation/documents/cases'
        res_sel = UserAPI.get(url_sel)
        assert res_sel.status_code == 200
        assert res_sel.json()['status'] == 0
        # print('查询到单据类型，审核规则',res_sel.json())
        danjuleixing = {}
        shenheguize = {}
        # 把单据类型和审核规则存到字典
        for i in res_sel.json()['data']['business_document_values']:
            danjuleixing.update({i['name']: i['val']})
        for i in res_sel.json()['data']['option_value']:
            shenheguize.update({i['label']: i['value']})
        # print(danjuleixing,'\n',shenheguize)
        # 查询输入的单据类型，规则
        leixing_id = [danjuleixing[key] for key in dj_leixing]
        print('单据类型id', leixing_id)
        Xitongguanli.danjuleixing_id = leixing_id[0]
        guize_id = shenheguize[dj_guize]
        return leixing_id,guize_id
    def add_danjushenhe(self,dj_leixing,dj_guize,price=None):
        lx_id,gz_id =Xitongguanli().select_danjuleixing_shengheduize_id(dj_leixing,dj_guize)
        # #新增单据审核
        url_add = '/api/v1/system/individuation/documents/store'
        data_add = Data_xitong().add_danjushenhe(lx_id,gz_id,price)
        res_add = UserAPI.post(url_add,data_add)
        print('新增单据审核',res_add.json())
        if res_add.status_code == 200:
            assert res_add.json()['status'] == 0
            Xitongguanli.danju_id = res_add.json()['data']['id']
        elif res_add.status_code == 422:
            assert res_add.json()['message'] == '单据类型已经存在了'
    def sel_danjushenhe(self):
        url = f'/api/v1/system/individuation/documents/index?page=1&page_size=10&val={Xitongguanli.danjuleixing_id}'
        res = UserAPI.get(url)
        #print('查询单据审核',res.json())
        assert res.status_code == 200
        assert res.json()['status'] == 0
        assert res.json()['data']['data'][0]['id'] == Xitongguanli.danju_id
        Xitongguanli.danju_id = res.json()['data']['data'][0]['id']
        return res
    def update_danjushenhe(self,dj_leixing,dj_guize,price=None):
        lx_id, gz_id = Xitongguanli().select_danjuleixing_shengheduize_id(dj_leixing, dj_guize)
        url = '/api/v1/system/individuation/documents/update'
        data = Data_xitong().update_danjushenhe(Xitongguanli.danju_id,lx_id,gz_id,price)
        res = UserAPI.post(url,data)
        print('修改单据审核',res.json())
        assert res.status_code == 200
        assert res.json()['status'] == 0
        assert res.json()['data'] == 1
    def del_danjushenhe(self):
        url = '/api/v1/system/individuation/documents/destroy'
        data = Data_xitong().del_danjushenhe(Xitongguanli.danju_id)
        res = UserAPI.post(url,data)
        print('删除单据审核',res.json())
        assert res.status_code == 200
        assert res.json()['status'] == 0
        assert res.json()['data'] == 1
    def gonggongcanshu_email(self):
        url = '/api/v1/system/base/parameters/email/test'
        data = Data_xitong().gonggongcanshu_email()
        res = UserAPI.post(url,data)
        print('系统参数-公共参数，发送测试邮件',res.json())
        assert res.status_code == 200
        assert res.json()['message'] == '发送成功'
    def add_diqu(self,status,diqu):
        url = '/api/v1/system/base/areas/store'
        data = Data_xitong().add_diqu(status,diqu)
        res = UserAPI.post(url,data)
        print('新增地区',res.json())
        assert res.status_code == 200
        assert res.json()['data']['status'] == status
    def sel_diqu(self,diqu):
        url = f'/api/v1/system/base/areas/index?page=1&page_size=10&name_zh={diqu}&country_id=1'
        res = UserAPI.get(url)
        print('查询地区',res.json()['data']['data'])
        assert res.status_code == 200
        assert res.json()['data']['data'][0]['county_name'] == diqu
        Xitongguanli.diqu_id = res.json()['data']['data'][0]['id']
        return res
    def update_diqu(self,status,diqu):
        url = '/api/v1/system/base/areas/update'
        data = Data_xitong().update_diqu(status,diqu,Xitongguanli.diqu_id)
        res = UserAPI.post(url,data)
        print('修改地区',res.json())
        assert res.status_code == 200
        assert res.json()['data']['status'] == status
        assert res.json()['data']['name_zh'] == diqu
    def del_diqu(self,diqu):
        #删除地区
        url = '/api/v1/system/base/areas/destroy'
        data =Data_xitong().del_diqu(Xitongguanli.diqu_id)
        res = UserAPI.post(url,data)
        print('删除地区',res.json())
        assert res.status_code == 200
        assert res.json()['data'] == 1
        #删除后查询地区是否存在
        url = f'/api/v1/system/base/areas/index?page=1&page_size=10&name_zh={diqu}&country_id=1'
        res = UserAPI.get(url)
        assert res.json()['data']['data'] == []
    def update_biaohao_guize(self,bianmafenduan):
        dqsj = time.strftime("%Y%m%d")
        url = '/api/v1/system/individuation/numbering/update'
        data = Data_xitong().update_biaohao_guize(bianmafenduan)
        res = UserAPI.post(url,data)
        if bianmafenduan == 1:
            print('修改编号规则',res.json())
            assert res.status_code == 200
            assert res.json()['data']['demo'] == '000001'
        elif bianmafenduan == 2:
            print('修改编号规则',res.json())
            assert res.status_code == 200
            assert res.json()['data']['demo'] == 'CP000001'
        elif bianmafenduan == 3:
            print('修改编号规则',res.json())
            assert res.status_code == 200
            assert res.json()['data']['demo'] == f"CP{dqsj}000001"
        elif bianmafenduan == 4:
            assert res.status_code != 200
            print('修改编号规则',res.json()['message'])
            assert  "同一单据类别必须设置'流水号'单据规则" in res.json()['message']
        elif bianmafenduan == 5:
            assert res.status_code != 200
            print('修改编号规则',res.json()['message'])
            assert "同一单据类别必须设置'流水号'单据规则" in res.json()['message']
    def sel_biaohao_guize(self,name):
        url = f'/api/v1/system/individuation/numbering/index?page=1&page_size=10&rules_name={name}&category_name='
        res = UserAPI.get(url)
        print('查询编号规则',res.json()['data']['data'][0])
        assert res.status_code == 200
        assert res.json()['data']['data'][0]['rules_name'] == name
        return res
    def add_fuzhuzilaio_fenlei(self,name):
        url = '/api/v1/enums/category/store'
        data = Data_xitong().add_fuzhuziliao_feilei(name)
        res = UserAPI.post(url,data)
        print('新增辅助资料',res.json())
        if res.status_code == 200:
            Xitongguanli.fuzhuzilaio_fenlei_id = res.json()['data']['id']
            Xitongguanli.fuzhuzilaio_fenlei_key = res.json()['data']['key']
            assert res.json()['data']['title'] == name
        elif res.status_code == 422:
            assert res.json()['message'] == "同一辅助资料分类下，辅助资料名称不可重复"
        else:
            assert False,'状态码错误，请检查接口返回信息'
    def update_fuzhuzilaio_fenlei(self,name):
        #修改辅助资料分类
        url = '/api/v1/enums/category/update'
        data = Data_xitong().update_fuzhuziliao_fenlei(Xitongguanli.fuzhuzilaio_fenlei_id,name)
        res = UserAPI.post(url,data)
        print('修改辅助资料分类',res.json())
        assert res.status_code == 200
        assert res.json()['data'] == 1
    def add_fuzhuzilaio_mingcheng(self,name,status):
        url = '/api/v1/enums/store'
        data = Data_xitong().add_fuzhuziliao_mingcheng(Xitongguanli.fuzhuzilaio_fenlei_key,name,status)
        res = UserAPI.post(url,data)
        print('新增辅助资料名称',res.json())
        if res.status_code == 200:
            assert res.json()['data']['status'] == status
            assert res.json()['data']['value']['name'] == name
            Xitongguanli.fuzhuzilaio_mingcheng_id = res.json()['data']['id']
            Xitongguanli.fuzhuzilaio_mingcheng_key = res.json()['data']['key']
        elif res.status_code == 422:
            assert res.json()['message'] == '同一辅助属性名称下，属性内容不可重'
        else:
            assert  False,'状态码错误，请假差接口返回信息'
    def update_fuzhuziliao_mingcheng(self,name,status):
        url = '/api/v1/enums/update'
        data = Data_xitong().update_fuzhuziliao_mingcheng(Xitongguanli.fuzhuzilaio_mingcheng_id,Xitongguanli.fuzhuzilaio_mingcheng_key,name,status)
        res = UserAPI.post(url,data)
        print('修改辅助资料名称',res.json())
        assert res.status_code == 200
        assert res.json()['data']['status'] == status
        assert res.json()['data']['value']['name'] == name
    def sel_fuzhuziliao(self,name='',type='',status=''):
        url = '/api/v1/enums/index'
        data = Data_xitong().sel_fuzhushuxing(name,type,status)
        res = UserAPI.get(url,data)
        return res
    def del_fuzhuziliao_mingcheng(self,name):
        #删除辅助资料名称
        url = '/api/v1/enums/destroy'
        data = Data_xitong().del_fuzhuziliao_mingcheng(Xitongguanli.fuzhuzilaio_mingcheng_id)
        res = UserAPI.post(url,data)
        print('删除辅助资料名称',res.json())
        assert res.status_code == 200
        assert res.json()['data'] == 1
        #删除后查询是否存在
        url1 = f'/api/v1/enums/index?page=1&page_size=10&title={name}&key='
        res1 = UserAPI.get(url1)
        assert res1.json()['data']['data'] == []
    def del_fuzhuziliao_fenlei(self):
        url = '/api/v1/enums/category/destroy'
        data = Data_xitong().del_fuzhuziliao_fenlei(Xitongguanli.fuzhuzilaio_fenlei_id)
        res = UserAPI.post(url,data)
        print('删除辅助资料分类',res.json())
        assert res.status_code == 200
        assert res.json()['data'] == 1
    def add_fuzhushuxing(self,name,type,status,len=None): # type : varchar int timestamp auxiliary_category
        url = '/api/v1/system/individuation/profile/store'
        data = Data_xitong().add_fuzhushuxing(name,type,status,len)
        res = UserAPI.post(url,data)
        print('新增辅助属性',res.json())
        if res.status_code == 200:
            assert res.json()['data']['show_name'] == name
            assert res.json()['data']['data_type'] == type
            assert res.json()['data']['status'] == status
            Xitongguanli.fuzhushuxing_id = res.json()['data']['id']
            Xitongguanli.fuzhushuxing_field_name = res.json()['data']['field_name']
        elif res.status_code == 422:
            assert res.json()['message'] == "'字段名称'已经存在."
        else:
            assert False,'状态码错误，请检查接口返回信息'
    def update_fuzhushuxing(self,name,type,status,len=None):
        url = '/api/v1/system/individuation/profile/update'
        data = Data_xitong().update_fuzhushuxing(Xitongguanli.fuzhushuxing_id,name,type,status,len)
        res = UserAPI.post(url,data)
        print('修改辅助属性',res.json())
        assert res.status_code == 200
        assert res.json()['data']['show_name'] == name
        assert res.json()['data']['data_type'] == type
        assert res.json()['data']['status'] == status
    def del_fuzhushuxing(self):
        url = '/api/v1/system/individuation/profile/destroy'
        data = Data_xitong().del_fuzhushuxing(Xitongguanli.fuzhushuxing_id)
        res = UserAPI.post(url,data)
        print('删除辅助属性',res.json())
        assert res.status_code == 200
        assert res.json()['data'] == 1
class Chanpinguanli():
    def sel_chanpinfenlei(self,name=None):
        if name == None:
            url = f'/api/v1/prod/cate/index'
            res = UserAPI.get(url)
            return res
        else:
            url = f'/api/v1/prod/cate/index?name={name}'
            res = UserAPI.get(url)
            return res
    def add_chanpinfenlei(self,fenlei,bianhao,mingcehng,paixv,zhuangtai,shangjifenlei=None):
        url = '/api/v1/prod/cate/store'
        data = Data_chanpin().add_chanpinfenlei(fenlei,bianhao,mingcehng,paixv,zhuangtai,shangjifenlei)
        res = UserAPI.post(url,data)
        return res
    def update_chanpinfenlei(self,yijifenlei_id,erjifenlei_id,bianhao,mingcheng,paixv,zhaungtai):
        url = '/api/v1/prod/cate/update'
        data = Data_chanpin().update_chanpinfenlei(yijifenlei_id,erjifenlei_id,bianhao,mingcheng,paixv,zhaungtai)
        res = UserAPI.post(url,data)
        return res
    def del_chanpinfenlei(self,id):
        url = '/api/v1/prod/cate/batch_destroy'
        data = Data_chanpin().del_chanpinfenlei(id)
        res = UserAPI().post(url,data)
        return res
    def add_pinpai(self,mingcheng,caigou_zhekou,xiaoshou_zhekou,paixu):
        url = '/api/v1/prod/brand/store'
        data = Data_chanpin().add_pinpai(mingcheng,caigou_zhekou,xiaoshou_zhekou,paixu)
        res = UserAPI.post(url,data)
        return res
    def update_pinpai(self,id,mingcheng,caigou_zhekou,xiaoshou_zhekou,paixu):
        url = '/api/v1/prod/brand/update'
        data = Data_chanpin().update_pinpai(id,mingcheng,caigou_zhekou,xiaoshou_zhekou,paixu)
        res = UserAPI.post(url,data)
        return res
    def sel_pinpai(self,name=None):
        if name == None:
            url = f'/api/v1/prod/brand/index?page=1&page_size=10'
            res = UserAPI.get(url)
            return res
        else:
            url = f'/api/v1/prod/brand/index?page=1&page_size=10&name={name}'
            res = UserAPI.get(url)
            return res
    def del_pinpai(self,id):
        url = '/api/v1/prod/brand/batch_destroy'
        data = Data_chanpin().del_pinpai(id)
        res = UserAPI.post(url,data)
        return res
    def weixianpin_biaoqian(self):
        url = '/api/v1/system/base/dangerous_label/index'
        res = UserAPI.get(url)
        return res
    def cas_shangchuan_mol(self,path):
        url = '/api/v1/base/upload/mol'
        file = Data_chanpin().cas_shangchuan_mol(path)
        res = UserAPI.post_wenjian(url,file)
        return res
    def cas_shangchuan_tupian(self,path):
        url = '/api/v1/base/upload'
        file = Data_chanpin().cas_shangchuan_tupian(path)
        res = UserAPI.post_wenjian(url, file)
        return res
    def iChembio_info(self,cas):
        url = f'/api/v1/prod/cas/get/from/iChembio?cas={cas}'
        res = UserAPI.get(url)
        return res
    def add_cas(self,cas,name,bieming,fenzijiegou,fenzishi,fenziliang,mdl,einecs,weixianbiaoshi,imgid,filename,img_show):
        url = '/api/v1/prod/cas/store'
        data = Data_chanpin().add_cas(cas,name,bieming,fenzijiegou,fenzishi,fenziliang,mdl,einecs,weixianbiaoshi,imgid,filename,img_show)
        res = UserAPI.post(url,data)
        return res
    def sel_cas(self,cas):
        url = f'/api/v1/prod/cas/index?keywords={cas}&page=1&page_size=10'
        res = UserAPI.get(url)
        return res
    def update_cas(self,id,cas,name,bieming,fenzijiegou,fenzishi,fenziliang,mdl,einecs,weixianbiaoshi,imgid,filename,img_show):
        url = '/api/v1/prod/cas/update'
        data = Data_chanpin().update_cas(id,cas,name,bieming,fenzijiegou,fenzishi,fenziliang,mdl,einecs,weixianbiaoshi,imgid,filename,img_show)
        res = UserAPI.post(url,data)
        return res
    def del_cas(self,id):
        url = '/api/v1/prod/cas/destroy'
        data = Data_chanpin().del_cas(id)
        res = UserAPI.post(url,data)
        return res
    # 新增产品相关接口
    #获取产品编号
    def sel_prod_number(self):
        url = '/api/v1/generate_no/Prod'
        res = UserAPI.get(url)
        return res
    #存储条件
    def chucuntiaojian(self):
        url = '/api/v1/prod/storage_conditions/index'
        res = UserAPI.get(url)
        return res
    #产品分类
    def chanpinfenlei(self):
        url = '/api/v1/prod/cate/index?status=1'
        res = UserAPI.get(url)
        return res
    #产品属性
    def chanpin_fuzhushuxing(self):
        url = '/api/v1/prod/profile'
        res = UserAPI.get(url)
        return res
    #新增产品
    def add_chanpin(self,bianhao,cas,name,fenlei,leixing,chucuntiaojian,weixianpin_biaoqian,fuzhushuxing,img_id,img_filename,img_img_show,guige_bianhao,chundu,pinpai_name,pinpai_id,baozhuang_id,baozhaung_name,jiliang_id,jiliang_name,danweizhaunhuan,baozhuang,jiage,huoqi):
        url = '/api/v1/prod/store'
        data = Data_chanpin().add_chanin(bianhao,cas,name,fenlei,leixing,chucuntiaojian,weixianpin_biaoqian,fuzhushuxing,img_id,img_filename,img_img_show,guige_bianhao,chundu,pinpai_name,pinpai_id,baozhuang_id,baozhaung_name,jiliang_id,jiliang_name,danweizhaunhuan,baozhuang,jiage,huoqi)
        res = UserAPI.post(url,data)
        return res
    def sel_chanpin(self,cas='', prod_no='', name_cn='', name_en='', sku_no='', fenzishi='', zhuangtai='',weixianpinbiaoqian_id='', pinpai_id='', cangku_id='', kuwei_id=''):
        url = '/api/v1/prod/index'
        params = Data_chanpin().sel_chanpin(cas, prod_no, name_cn, name_en, sku_no, fenzishi, zhuangtai,weixianpinbiaoqian_id, pinpai_id, cangku_id, kuwei_id)
        res = UserAPI.get(url,params)
        return res
    def update_chanpin(self,cp_id,chanpin_bianhao,cas,name_en,chanpinfenlei_id,chanpinleixing,chucuntiaojian,weixianpin_id,zhuangtai,fuzhushuxing,img1_id,img1_filename,img1_img_show,img2_id,img2_filename,img2_img_show,
                      guige_id1,guige_bianhao1,chundu1,pinpai_id1,pinpaimingcheng1,banzhuang_id1,baozhuang_name1,danweizhuanhuan1,jiliang_id1,jiliang_name1,baozhaung1,jiage1,huoqi1,
                      guige_bianhao2,chundu2,pinpai_id2,pinpaimingcheng2,banzhuang_id2,baozhuang_name2,danweizhuanhuan2,jiliang_id2,jiliang_name2,baozhaung2,jiage2,huoqi2):
        url = '/api/v1/prod/update'
        data = Data_chanpin().update_chanin(cp_id,chanpin_bianhao,cas,name_en,chanpinfenlei_id,chanpinleixing,chucuntiaojian,weixianpin_id,zhuangtai,fuzhushuxing,img1_id,img1_filename,img1_img_show,img2_id,img2_filename,img2_img_show,
                      guige_id1,guige_bianhao1,chundu1,pinpai_id1,pinpaimingcheng1,banzhuang_id1,baozhuang_name1,danweizhuanhuan1,jiliang_id1,jiliang_name1,baozhaung1,jiage1,huoqi1,
                      guige_bianhao2,chundu2,pinpai_id2,pinpaimingcheng2,banzhuang_id2,baozhuang_name2,danweizhuanhuan2,jiliang_id2,jiliang_name2,baozhaung2,jiage2,huoqi2)
        res = UserAPI.post(url,data)
        return res
    def del_chanpin(self,id):
        url = '/api/v1/prod/destroy'
        data = Data_chanpin().del_chanpin(id)
        res = UserAPI.post(url,data)
        return res
    def sel_chanpinxinxi(self,cas):
        url = f'/api/v1/prod/cas/get/from/erp?cas={cas}'
        res = UserAPI.get(url)
        return res
    def sel_pihao(self):
        url = '/api/v1/prod/coa/generate/odd'
        res = UserAPI.get(url)
        return res
    def sel_cangku(self):
        url = '/api/v1/warehouse/warehouse/list'
        res = UserAPI.get(url)
        return res
    def sel_cangku_kuwei(self,id):
        url = f'/api/v1/warehouse/position/list?warehouse_id={id}'
        res = UserAPI.get(url)
        return res
    def add_coa(self,prod_id,sku_id,kucun,cangku_id,cangkukuwei_id,pihao,jiancejieguo='',jianyanriqi='',yuanshipihao='',shengchanriqi='',shixiaoriqi=''):
        url = '/api/v1/prod/coa/generate/odd'
        data = Chanpinguanli().add_coa(prod_id,sku_id,kucun,cangku_id,cangkukuwei_id,pihao,jiancejieguo,jianyanriqi,yuanshipihao,shengchanriqi,shixiaoriqi)
        res = UserAPI.post(url,data)
        return res
    def set_chengben(self,id,chengben):
        url = '/api/v1/prod/coa/cost'
        data = Chanpinguanli().shezhi_chengben(id,chengben)
        res = UserAPI.post(url,data)
        return res
    def sel_coa(self,prod_id,sku_id,kucun=''):
        url = '/api/v1/prod/coa/index'
        params = Data_chanpin().sel_coa(prod_id,sku_id,kucun)
        res = UserAPI.get(url,params)
        return res
    def updata_coa(self,id, prod_id, sku_id, kucun, cangku_id, cangkukuwei_id, pihao, jiancejieguo='', jianyanriqi='',
                yuanshipihao='', shengchanriqi='', shixiaoriqi=''):
        url = '/api/v1/prod/coa/update'
        data = Data_chanpin().update_pinpai(id, prod_id, sku_id, kucun, cangku_id, cangkukuwei_id, pihao, jiancejieguo, jianyanriqi,
                yuanshipihao, shengchanriqi, shixiaoriqi)
        res = UserAPI.post(url,data)
        return res
    def del_coa(self,id):
        url = '/api/v1/prod/coa/destroy'
        data = Data_chanpin().del_coa(id)
        res = UserAPI.post(url,data)
        return res
    def set_guige_shuomingshu(self,):
        pass
class Keshangguanli():
    def sel_user(self,status='',bumen='',bianhao='',denglu_name='',xingming=''):
        url = '/api/v1/system/user/index'
        data = Data_keshang().sel_user(status,bumen,bianhao,denglu_name,xingming)
        res = UserAPI.get(url,data)
        return res
    def sel_kuhu_bianma(self):
        url = '/api/v1/generate_no/Customer'
        res = UserAPI.get(url)
        return res
    def sel_dizhi(self):
        url = '/api/v1/system/base/countries/children?id=1'
        res = UserAPI.get(url)
        return res
    def sel_pinyin_jiancheng(self,name):
        url = f'/api/v1/base/pinyin/abbr?text={name}'
        res = UserAPI.get(url)
        return res
    def add_kehu(self,kehu_bianhao,name,pinyin,kehu_laiyuan,kehu_leixing,kehu_xingzhi,kehu_zhuangtai,suoshu_xiaoshou,huiyuan_dengji,
                 guojia,sheng_id,shi_id,qu_id,sheng_name,shi_name,qu_name,file_id):
        url = '/api/v1/merchant/customer/store'
        data = Data_keshang().add_kehu(kehu_bianhao,name,pinyin,kehu_laiyuan,kehu_leixing,kehu_xingzhi,kehu_zhuangtai,suoshu_xiaoshou,huiyuan_dengji,
                 guojia,sheng_id,shi_id,qu_id,sheng_name,shi_name,qu_name,file_id)
        res = UserAPI.post(url,data)
        return res
    def sel_kehu(self,name='',bianhao='',pinyin='',laiyuan='',kehuxingzhi=''):
        url = '/api/v1/merchant/customer/index'
        params = Data_keshang().sel_kehu(name,bianhao,pinyin,laiyuan,kehuxingzhi)
        res = UserAPI.get(url,params)
        return res
    def sel_kehu_info(self,id):
        url = f'/api/v1/merchant/customer/show?id={id}'
        res = UserAPI.get(url)
        return res
    def update_kehu(self,kehu_id,lianxiren_id,kehu_bianhao,name,pinyin,kehu_laiyuan,kehu_leixing,kehu_xingzhi,kehu_zhuangtai,suoshu_xiaoshou,huiyuan_dengji,
                 guojia,sheng_id,shi_id,qu_id,sheng_name,shi_name,qu_name,file_id):
        url = '/api/v1/merchant/customer/update'
        data = Data_keshang().update_kehu(kehu_id,lianxiren_id,kehu_bianhao,name,pinyin,kehu_laiyuan,kehu_leixing,kehu_xingzhi,kehu_zhuangtai,suoshu_xiaoshou,huiyuan_dengji,
                 guojia,sheng_id,shi_id,qu_id,sheng_name,shi_name,qu_name,file_id)
        res = UserAPI.post(url,data)
        return res
    def del_kehu(self,id):
        url = '/api/v1/merchant/customer/batch_destroy'
        data = Data_keshang().del_kehu(id)
        res = UserAPI.post(url,data)
        return res
    def set_vip(self,vip,id):
        url = '/api/v1/merchant/customer/set_customer_user_level'
        data = Data_keshang().set_vip(vip,id)
        res = UserAPI.post(url,data)
        return res
    def set_xiaoshou(self,name,user,type,xiaoshou_id,kehu_id):
        url = '/api/v1/merchant/customer/belongs_to'
        data = Data_keshang().set_xiaoshou(name,user,type,xiaoshou_id,kehu_id)
        res = UserAPI.post(url,data)
        return res
    def add_genjin(self,name,kehu_id,lianxiren_id,lianxiren_name,genjin_zhuangtai,genjin_fangshi,file_id):
        url = '/api/v1/merchant/customer/trace/store'
        data = Data_keshang().add_genjin(name,kehu_id,lianxiren_id,lianxiren_name,genjin_zhuangtai,genjin_fangshi,file_id)
        res = UserAPI.post(url,data)
        return res
    def sel_genjin(self,kehu_name='',lianxiren_name='',kaishi_riqi='',jieshu_riqi=''):
        url = '/api/v1/merchant/customer/trace/index'
        data = Data_keshang().sel_genjin(kehu_name,lianxiren_name,kaishi_riqi,jieshu_riqi)
        res = UserAPI.get(url,data)
        return res
    def update_genjin(self,genjin_id,name,kehu_id,lianxiren_id,lianxiren_name,genjin_zhuangtai,genjin_fangshi,file_id):
        url = '/api/v1/merchant/customer/trace/update'
        data = Data_keshang().update_genjin(genjin_id,name,kehu_id,lianxiren_id,lianxiren_name,genjin_zhuangtai,genjin_fangshi,file_id)
        res = UserAPI.post(url, data)
        return res
    def del_genjin(self,id):
        url = '/api/v1/merchant/customer/trace/batch_destroy'
        data = Data_keshang().del_genjin(id)
        res = UserAPI.post(url,data)
        return res
    def add_supplier_product_catalog(self,supplier_id,cas,prod_name_zh,prod_name_en,prod_no='',sku_no=''):
        url = '/api/v1/merchant/supplier/prod/store'
        data = Data_keshang().add_supplier_product_catalog(supplier_id,cas,prod_name_zh,prod_name_en,prod_no,sku_no)
        res= UserAPI.post(url,data)
        return res
    def update_supplier_product_catalog(self,id,supplier_id,cas,prod_name_zh,prod_name_en,prod_no='',sku_no=''):
        url = '/api/v1/merchant/supplier/prod/update'
        data = Data_keshang().update_supplier_product_catalog(id,supplier_id,cas,prod_name_zh,prod_name_en,prod_no,sku_no)
        res = UserAPI.post(url,data)
        return res
    def sel_supplier_product_catalog(self,cas='',supplier_name='',prod_name='',prod_no='',spec_no=''):
        url = '/api/v1/merchant/supplier/prod/index'
        data = Keshangguanli().sel_supplier_product_catalog(cas,supplier_name,prod_name,prod_no,spec_no)
        res = UserAPI.get(url,data)
        return res
    def del_supplier_product_catalog(self,id):
        url = '/api/v1/merchant/supplier/prod/batch_destroy'
        data = Data_keshang().del_supplier_product_catalog(id)
        res = UserAPI.post(url,data)
        return res
    def add_supplier(self,):
        url = ''
    def sel_supplier(self,):
        url = ''

class Caigouguanli():
    def sel_caigou_xunjia_id(self,):
        url = '/api/v1/generate_no/PurchaseInquiry'
        res = UserAPI.get(url)
        return res
    def add_caigou_shenqing_baocun(self,type,inquiry_no,user_id,zhidanren,cangku_id,shenqing_yuanyin,
                               prod_id,prod_name,prod_no,sku_no,sku_id,cas,chundu,baozhuang,pinpai_id,pinpai_name,shuliang,beizhu='',
                               fujian_id='',fujian_name='',fujian_path=''):
        url = '/api/v1/purchase/inquiry/store'
        data = Data_caigou().add_caigou_shenqingdan(type,inquiry_no,user_id,zhidanren,cangku_id,shenqing_yuanyin,
                               prod_id,prod_name,prod_no,sku_no,sku_id,cas,chundu,baozhuang,pinpai_id,pinpai_name,shuliang,beizhu,
                               fujian_id,fujian_name,fujian_path)
        res = UserAPI.post(url,data)
        return res








