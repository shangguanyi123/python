#coding=gbk
import time
import requests
import json
from API_case.API_data import Data_API2
from api.req_method import UserAPI

url = "http://221.226.240.154:28090"


class Yuniyng():
    daohang_id = '' #导航id，修改导航会用到
    liebiao_id = '' #列表id
    danye_id = ''   #单页id
    daohang_name = '' #导航名字


    # 新增导航
    def add_daohang(self,name,model_type):#导航名称，内容模型1单页2列表
        urladd = '/api/v1/erp_starter/site/nav'
        payload = Data_API2().add_daohang(name, model_type)
        # print(payload)
        res = UserAPI.post_biaodan(urladd,payload)
        print('新增导航', res.json())
        assert res.json()['status'] == 0
        assert res.json()['data']['is_show'] == '1'  # 显示导航
        Yuniyng.daohang_id = res.json()['data']['id']  # 导航id
        Yuniyng.daohang_name = res.json()['data']['name']
    # 查询顶部显示新建的导航
    def select_daohang(self):
        urlsel = '/api/v1/erp_starter/site/nav?name=%s&is_show=1&position=1&page=1&per_page=20'%Yuniyng.daohang_name
        res = UserAPI.get(urlsel)
        print('查询顶部显示新建的导航', res.json())
        assert res.json()['status'] == 0
        assert res.json()['data']['data'][0]['is_show'] == 1  # 显示在网站
        assert res.json()['data']['data'][0]['position'] == ["1", "2"]  # 顶部和底部都展示
    # 修改导航
    def update_daohang(self):
        urlupdate = '/api/v1/erp_starter/site/nav/%s'%Yuniyng.daohang_id
        payload = Data_API2().update_daohang()
        res = UserAPI.post_biaodan(urlupdate,payload)
        print('修改导航', res.json())
        assert res.json()['status'] == 0
        assert res.json()['data']['is_show'] == '0'  # 不显示导航
    # 删除导航
    def delete_daohang(self):
        urldel = '/api/v1/erp_starter/site/nav/%s'%Yuniyng.daohang_id
        res = UserAPI.delete(urldel)
        print('删除导航', res.json())
        assert res.json()['status'] == 0
    # 新增列表
    def add_liebiao(self):
        urladd = '/api/v1/erp_starter/site/node'
        data = Data_API2().add_liebiao(Yuniyng.daohang_id)
        res = UserAPI.post(urladd,data)
        print('新增列表',res.json())
        assert res.json()['status'] == 0
        assert res.json()['data']['is_show'] == 1 #显示在网站
        Yuniyng.liebiao_id = res.json()['data']['id']
    # 查询新增的列表
    def select_liebiao(self):
        urlsel = '/api/v1/erp_starter/site/node?category_id=%s&is_show=1&page=1&per_page=20&model_type=2'%Yuniyng.daohang_id
        res = UserAPI.get(urlsel)
        print('查询显示新闻资讯的列表', res.json())
        assert res.json()['status'] == 0
        assert res.json()['data']['data'][0]['is_show_text'] == '显示'  # 显示在网站
        assert res.json()['data']['data'][0]['node_has_nav']['name'] == Yuniyng.daohang_name
    # 修改列表
    def update_liebiao(self):
        urlupdate ='/api/v1/erp_starter/site/node/%s'%Yuniyng.liebiao_id
        data = Data_API2().update_liebiao()
        res = UserAPI.post(urlupdate, data)
        print('修改列表', res.json())
        assert res.json()['status'] == 0
        assert res.json()['data']['is_show'] == 0  # 不显示在网站
    # 删除列表
    def delete_liebiao(self):
        urldel = '/api/v1/erp_starter/site/node/%s'%Yuniyng.liebiao_id
        res = UserAPI.delete(urldel)
        print('删除列表', res.json())
        assert res.json()['status'] == 0
    # 新增单页
    def add_danye(self):
        urladd = '/api/v1/erp_starter/site/node'
        data = Data_API2().add_danye(Yuniyng.daohang_id)
        res = UserAPI.post(urladd, data)
        print('新增单页', res.json())
        assert res.json()['status'] == 0
        assert res.json()['data']['is_show'] == 1  # 显示在网站
        Yuniyng.danye_id = res.json()['data']['id']
    # 查询单页
    def select_danye(self):
        urlsel =  '/api/v1/erp_starter/site/node?category_id=%s&is_show=1&page=1&per_page=20&model_type=1'%Yuniyng.daohang_id
        res = UserAPI.get(urlsel)
        print('查询新建的单页', res.json())
        assert res.json()['status'] == 0
        assert res.json()['data']['data'][0]['is_show'] == 1  # 显示在网站
        assert res.json()['data']['data'][0]['node_has_nav']['name'] == Yuniyng.daohang_name  # 顶部和底部都展示
    # 修改单页
    def update_danye(self):
        urlupdate =  '/api/v1/erp_starter/site/node/%s' % Yuniyng.danye_id
        data = Data_API2().update_danye()
        res = UserAPI.post(urlupdate, data)
        print('修改单页', res.json())
        assert res.json()['status'] == 0
        assert res.json()['data']['is_show'] == 0  # 不显示在网站
    # 删除单页
    def delete_danye(self):
        urldel = '/api/v1/erp_starter/site/node/%s' % Yuniyng.danye_id
        res = UserAPI.delete(urldel)
        print('删除单页', res.json())
        assert res.json()['status'] == 0
    # 会员管理 查询姓名为上官一的会员列表
    def select_vip(self):
        urlsel = '/api/v1/erp_starter/site/user?page=1&page_size=20&keywords=上官一'
        res = UserAPI.get(urlsel)
        print('查询姓名为上官一的会员列表', res.json())
        assert res.json()['status'] == 0
        assert res.json()['data']['data'][0]['status'] == 1  # 状态开启
        assert res.json()['data']['data'][0]['user_name'] == '上官一'  # 名字


class Xitong():
    yonghu_id = '' #用户ID
    juese_id = ''   #角色id
    # 新增公司信息
    def gongsixinxi(self):
        urlgs ='/api/v1/erp_starter/system/company'
        data = Data_API2().gongsixinxi()
        res = UserAPI.post(urlgs,data)
        print('新增单页', res.json())
        assert res.json()['status'] == 0
        assert res.json()['data']['company_name'] == '阿拉丁'  # 显示在网站
    # 角色管理
    # 新增角色
    def add_juese(self):
        # 新增角色
        urladd ='/api/v1/user/role'
        data = Data_API2().add_juese()
        res = UserAPI.post(urladd, data=data)
        print('系统管理-角色管理，新增角色', res.json())
        assert res.json()['status'] == 0
        assert res.json()['data']['status'] == 1  # 状态开启
        assert res.json()['data']['name'] == '采购员'
        Xitong.juese_id = res.json()['data']['id']
    # 查询角色采购员
    def select_juese(self):
        urlsel ='/api/v1/user/role?name=%E9%87%87%E8%B4%AD%E5%91%98&page=1&per_page=20'
        res = UserAPI.get(urlsel)
        print('系统管理-角色管理，查询角色采购员', res.json())
        assert res.json()['status'] == 0
        assert res.json()['data'][0]['status'] == 1  # 状态开启
        assert res.json()['data'][0]['name'] == '采购员'  # 名字
    # 修改角色
    def update_juese(self):
        urlupdate = '/api/v1/user/role/%s'%Xitong.juese_id
        data = Data_API2().update_juese()
        res = UserAPI.post(urlupdate,data)
        print('系统管理-角色管理，修改角色',res.json())
        assert res.json()['data']['status'] == 1 # 状态开启
        assert res.json()['data']['name'] == '采购员'
    # 删除角色
    def delete_juese(self):
        urldel ='/api/v1/user/role/%s' % Xitong.juese_id
        res = UserAPI.post(urldel, Data_API2().delete_juese())
        print('系统管理-角色管理，删除角色', res.json())
        assert res.json()['status'] == 0
    # 用户管理
    # 新增用户
    def add_yonghu(self):
        urladd = '/api/v1/user'
        data = Data_API2().add_yonghu(Xitong.juese_id)
        res = UserAPI.post(urladd,data)
        print('系统管理-用户管理，新增用户', res.json())
        assert res.json()['status'] == 0
        assert res.json()['data']['roles'][0]['status'] == 1  # 状态开启
        Xitong.yonghu_id = res.json()['data']['roles'][0]['pivot']['model_id']
    # 查询用户jws
    def select_yonghu(self):
        urlsel = '/api/v1/user?username=jws&page=1&per_page=20'
        res = UserAPI.get(urlsel)
        print('系统管理-用户管理，查询用户jsw', res.json())
        assert res.json()['status'] == 0
        assert res.json()['data']['data'][0]['status'] == 1  # 状态开启
        assert res.json()['data']['data'][0]['username'] == 'jws'  # 名字
    # 删除用户
    def delete_yonghu(self):
        urldel = '/api/v1/user/%s' % Xitong.yonghu_id
        res = UserAPI.post(urldel,Data_API2().delete_yonghu())
        print('系统管理-用户管理，删除用户', res.json())
        assert res.json()['status'] == 0


# 新增单页导航-查询导航-新增单页（关联相应导航）-查询单页-修改单页-删除单页-修改导航-删除导航
# Yuniyng().add_daohang('单页',1)
# Yuniyng().select_daohang()
# Yuniyng().add_danye()
# Yuniyng().select_danye()
# Yuniyng().update_danye()
# Yuniyng().delete_danye()
# Yuniyng().update_daohang()
# Yuniyng().delete_daohang()
# 新增列表导航-查询导航-新增列表（关联相应导航）-查询列表-修改列表-删除列表-修改导航-删除导航
# Yuniyng().add_daohang('列表',2)
# Yuniyng().select_daohang()
# Yuniyng().add_liebiao()
# Yuniyng().select_liebiao()
# Yuniyng().update_liebiao()
# Yuniyng().delete_liebiao()
# Yuniyng().update_daohang()
# Yuniyng().delete_daohang()

# 会员管理 查询用户信息
# Yuniyng().select_vip()
# 系统管理 新增角色-查询角色-新增用户-查询用户-删除用户-修改角色-删除角色
# Xitong().add_juese()
# Xitong().select_juese()
# Xitong().add_yonghu()
# Xitong().select_yonghu()
# Xitong().delete_yonghu()
# Xitong().update_juese()
# Xitong().delete_juese()
















