import pytest
from website_api.ichempro_api import Xitongguanli

@pytest.mark.xfail
def test_100():
    # 用户重复
    pass
def test_101():
    # 角色重复
    Xitongguanli().add_juese('系统管理员（临时）',1)
    Xitongguanli().add_juese('系统管理员（临时）', 1)
    Xitongguanli().del_juese()
def test_102_A():
    # 单位重复
    Xitongguanli().add_danwei(1, 'm100', 1, 'length', 0, '0.001')
    Xitongguanli().add_danwei(1, 'm100', 1, 'length', 0, '0.001')
    Xitongguanli().del_danwei()
def test_102_B():
    # 基本纲重复
    Xitongguanli().add_danwei(1, 'm101', 1, 'length', 1, '0.001')
    Xitongguanli().add_danwei(1, 'm102', 1, 'length', 1, '0.001')
    Xitongguanli().del_danwei()
def test_103():
    # 单据重复
    Xitongguanli().add_danjushenhe(['销项发票'], '需要审核')
    Xitongguanli().add_danjushenhe(['销项发票'], '需要审核')
    Xitongguanli().del_danjushenhe()
def test_104():
    # 地区重复
    pass
@pytest.mark.skip(reason="Skip this test as it's expected to return 422 status code")
def test_105():
    # 辅助资料分类重复
    Xitongguanli().add_fuzhuzilaio_fenlei('辅助类型（test）')
    Xitongguanli().add_fuzhuzilaio_fenlei('辅助类型（test）')
    Xitongguanli().del_fuzhuziliao_fenlei()
    # 辅助资料名称重复
    Xitongguanli().add_fuzhuzilaio_mingcheng('超级测试vip', 1)
    Xitongguanli().add_fuzhuzilaio_mingcheng('超级测试vip', 1)
    Xitongguanli().del_fuzhuziliao_mingcheng('超级vip')
def test_106():
    # 辅助属性
    Xitongguanli().add_fuzhushuxing('海关编码（test）', 'varchar', 0, 50)
    Xitongguanli().add_fuzhushuxing('海关编码（test）', 'varchar', 0, 50)
    Xitongguanli().del_fuzhushuxing()
