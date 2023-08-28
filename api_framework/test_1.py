#coding=gbk
from API_case.API1 import Xitongguanli

def test_01():
    #新增用户-查询-修改用户(部门、角色、状态)-删除用户;修改所有用户状态
    print('新增用户（状态开启）-查询-修改用户(部门、角色、状态)-删除用户;修改所有用户状态')
    Xitongguanli().add_user(1)
    Xitongguanli().select_user(1)
    Xitongguanli().update_uesr(20,1,0)
    Xitongguanli().del_user()
    Xitongguanli().update_user_status(0,1)
    print('新增用户（状态关闭）-查询-修改用户(部门、角色、状态)-删除用户;修改所有用户状态')
    Xitongguanli().add_user(0)
    Xitongguanli().select_user(0)
    Xitongguanli().update_uesr(20, 1, 1)
    Xitongguanli().del_user()
    Xitongguanli().update_user_status(0, 1)
def test_02():
    #新增用户-新增角色-添加用户到角色-删除用户所属角色-删除角色-删除用户
    print('新增用户-新增角色-添加用户到角色-删除用户所属角色-删除角色-删除用户')
    Xitongguanli().add_user(1)
    Xitongguanli().add_juese('系统管理员（临时）',1)
    Xitongguanli().insert_uesr_juese()
    Xitongguanli().del_user_juese()
    Xitongguanli().del_juese()
    Xitongguanli().del_user()
def test_03():
    #新增单位-查询单位-删除单位
    print('新增计量单位-修改为计量单位-查询计量单位-删除')
    Xitongguanli().add_danwei(1,'m',1,'length',1,'0.001')
    Xitongguanli().update_danwei(1,'mm',1,'length',1,'0.001')
    Xitongguanli().sel_danwei('measure')
    Xitongguanli().del_danwei()
    print('新增计量单位-修改为包装单位-查询包装单位-删除')
    Xitongguanli().add_danwei(1, 'm', 1, 'length', 1, '0.01')
    Xitongguanli().update_danwei(0, 'mm', 1)
    Xitongguanli().sel_danwei('package')
    Xitongguanli().del_danwei()
    print('新增包装单位-修改为包装单位-查询包装单位-删除')
    Xitongguanli().add_danwei(0, 'km', 1)
    Xitongguanli().update_danwei(0, 'mm', 1)
    Xitongguanli().sel_danwei('package')
    Xitongguanli().del_danwei()
    print('新增包装单位-修改为计量单位-查询计量单位-删除')
    Xitongguanli().add_danwei(0, 'km', 1)
    Xitongguanli().update_danwei(1, 'mm', 1, 'length', 1, '0.01')
    Xitongguanli().sel_danwei('measure')
    Xitongguanli().del_danwei()


def test_04():
    #新增单据审核-查询单据审核-修改单据审核-删除单据审核
    print('新增单据审核-查询单据审核-修改单据审核-删除单据审核')
    Xitongguanli().add_danjushenhe(['销售订单'],'需要审核')
    Xitongguanli().sel_danjushenhe()
    Xitongguanli().update_danjushenhe(['销售订单','采购订单'],'超过金额审核',10000)
    Xitongguanli().del_danjushenhe()
def test_05():
    #系统管理
    print('系统管理，测试邮件发送')
    Xitongguanli().gonggongcanshu_email()
def test_06():
    #新增地区-查询地区-修改地区-删除地区
    print('新增地区-查询地区-修改地区-删除地区')
    Xitongguanli().add_diqu(0,'测试区')
    Xitongguanli().sel_diqu('测试区')
    Xitongguanli().update_diqu(1,'测试地区')
    Xitongguanli().del_diqu('测试地区')
def test_07():
    # 修改编号规则-查询编号规则
    print('修改编号规则-查询编号规则')
    Xitongguanli().update_biaohao_guize(1)
    Xitongguanli().update_biaohao_guize(2)
    Xitongguanli().update_biaohao_guize(3)
    Xitongguanli().update_biaohao_guize(4)
    Xitongguanli().update_biaohao_guize(5)
    Xitongguanli().sel_biaohao_guize('产品编号')
def test_08():
    # 新增辅助资料分类-修改辅助资料分类-新增辅助资料名称-修改辅助资料名称-删除辅助资料名称-删除辅助资料分类
    print('新增辅助资料分类-修改辅助资料分类-新增辅助资料名称-修改辅助资料名称-删除辅助资料名称-删除辅助资料分类')
    Xitongguanli().add_fuzhuzilaio_fenlei('辅助类型（测试）')
    Xitongguanli().update_fuzhuzilaio_fenlei('辅助类型')
    Xitongguanli().add_fuzhuzilaio_mingcheng('超级测试vip', 1)
    Xitongguanli().update_fuzhuziliao_mingcheng('超级vip', 0)
    Xitongguanli().del_fuzhuziliao_mingcheng('超级vip')
    Xitongguanli().del_fuzhuziliao_fenlei()
def test_09():
    # 新增辅助属性-修改辅助属性-删除辅助属性
    print('新增辅助属性（文本）-修改辅助属性（数字）-删除辅助属性')
    Xitongguanli().add_fuzhushuxing('海关编码（测试）', 'varchar', 0, 50)
    Xitongguanli().update_fuzhushuxing('海关编码test', 'int', 1, 50)
    Xitongguanli().del_fuzhushuxing()
    print('新增辅助属性（日期）-修改辅助属性（日期）-删除辅助属性')
    Xitongguanli().add_fuzhushuxing('海关编码（测试）', 'timestamp',1)
    Xitongguanli().update_fuzhushuxing('海关编码test', 'timestamp', 0)
    Xitongguanli().del_fuzhushuxing()
    print('新增辅助属性（引用辅助资料）-修改辅助属性（引用辅助资料）-删除辅助属性')
    Xitongguanli().add_fuzhushuxing('海关编码（测试）', 'auxiliary_category', 0)
    Xitongguanli().update_fuzhushuxing('海关编码test', 'auxiliary_category', 1)
    Xitongguanli().del_fuzhushuxing()
    print('新增辅助属性（文本）-修改辅助属性（引用辅助资料）-删除辅助属性')
    Xitongguanli().add_fuzhushuxing('海关编码（测试）', 'varchar', 1,50)
    Xitongguanli().update_fuzhushuxing('海关编码test', 'auxiliary_category', 1)
    Xitongguanli().del_fuzhushuxing()

def test_10():

    pass
