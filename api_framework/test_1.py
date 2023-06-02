#coding=gbk
from API_case.API1 import Space
from API_case.API2 import Xitong, Yuniyng


def test1():
    # 新增采购订单-查询采购订单-修改采购订单-初始库存查询-采购入库-入库后库存查询-新增销售订单-查询销售订单-修改销售订单-销售发货-发货后库存查询
    print('\n新增采购订单-查询采购订单-修改采购订单-初始库存查询-采购入库-入库后库存查询-新增销售订单-查询销售订单-修改销售订单-销售发货-发货后库存查询')
    Space().add_caigou()
    Space().select_caigou()
    kucun = Space().select_kucun('1074-82-4')  # 初始库存
    Space().update_caigou_order()
    Space().ruku()
    rkcun = Space().select_kucun('1074-82-4')  # 入库后的库存
    assert kucun + 1000 == rkcun
    Space().add_xiaoshou()
    Space().id()
    Space().select_xiaoshou()
    Space().update_xiaoshou_order()
    Space().fahuo()
    ckkucun = Space().select_kucun('1074-82-4')  # 出库后的库存
    assert rkcun - 1000 == ckkucun
    assert kucun == ckkucun

def test2():
    #新增采购订单-查询采购订单-修改采购订单-删除采购订单
    print('\n新增采购订单-查询采购订单-修改采购订单-删除采购订单')
    Space().add_caigou()
    Space().select_caigou()
    Space().update_caigou_order()
    Space().delect_caigou()

def test3():
    #新增销售订单-查询销售订单-修改销售订单-删除销售订单
    print('\n新增销售订单-查询销售订单-修改销售订单-删除销售订单')
    Space().add_xiaoshou()
    Space().id()
    Space().select_xiaoshou()
    Space().update_xiaoshou_order()
    Space().delete_xiaoshou()

def test4():
    # 其他类型入库、出库
    print('\n其他类型入库、出库')
    kucun = Space().select_kucun('QTRK-000001') #初始库存
    Space().qita_ruku()
    rkkucun = Space().select_kucun('QTRK-000001') #入库后库存
    assert kucun + 100 == rkkucun
    Space().qita_fahuo()
    ckkucun = Space().select_kucun('QTRK-000001') #出库后库存
    assert rkkucun - 100 == ckkucun
    assert kucun == ckkucun

def test5():
    # 新增产品-修改产品信息-设置产品标签-删除产品；出入库查询
    print('\n新增产品-修改产品信息-设置产品标签-删除产品；出入库查询')
    Space().add_chanpin()
    Space().update_chanpin()
    Space().set_chanpin_biaoqian()
    Space().delete_chanpin()
    Space().select_churuku()

def test6():
    #新增采购订单-查询采购订单-修改采购订单-付款-收票-生成质检报告-采购入库-打印入库订单
    print('\n新增采购订单-查询采购订单-修改采购订单-付款-收票-生成质检报告-采购入库-打印入库订单')
    Space().add_caigou()
    Space().select_caigou()
    Space().update_caigou_order()
    Space().caigou_fukuan()
    Space().caigou_shoupiao()
    Space().zhijianbaogao()
    Space().ruku()
    Space().dayin_ruku()

def test7():
    #新增销售订单-查询销售订单-修改销售订单-收款-开票-销售发货-打印发货订单
    print('\n新增销售订单-查询销售订单-修改销售订单-收款-开票-销售发货-打印发货订单')
    Space().add_xiaoshou()
    Space().id()
    Space().select_xiaoshou()
    Space().update_xiaoshou_order()
    Space().xiaoshou_shoukuan()
    Space().xiaoshou_kaipiao()
    Space().fahuo()
    Space().dayin_fahuo()

def test8():
    #批量收款
    print('\n批量收款')
    Space().xiaoshou_piliangshoukuan()

def test9():
    # 新增单页导航-查询导航-新增单页（关联相应导航）-查询单页-修改单页-删除单页-修改导航-删除导航
    print('\n新增单页导航-查询导航-新增单页（关联相应导航）-查询单页-修改单页-删除单页-修改导航-删除导航')
    Yuniyng().add_daohang('单页',1)
    Yuniyng().select_daohang()
    Yuniyng().add_danye()
    Yuniyng().select_danye()
    Yuniyng().update_danye()
    Yuniyng().delete_danye()
    Yuniyng().update_daohang()
    Yuniyng().delete_daohang()

def test10():
    #新增列表导航-查询导航-新增列表（关联相应导航）-查询列表-修改列表-删除列表-修改导航-删除导航;会员管理 查询用户信息
    print('\n新增列表导航-查询导航-新增列表（关联相应导航）-查询列表-修改列表-删除列表-修改导航-删除导航;会员管理 查询用户信息')
    Yuniyng().add_daohang('列表',2)
    Yuniyng().select_daohang()
    Yuniyng().add_liebiao()
    Yuniyng().select_liebiao()
    Yuniyng().update_liebiao()
    Yuniyng().delete_liebiao()
    Yuniyng().update_daohang()
    Yuniyng().delete_daohang()
    Yuniyng().select_vip()

def test11():
    # 系统管理 新增角色-查询角色-新增用户-查询用户-删除用户-修改角色-删除角色
    print('\n系统管理 新增角色-查询角色-新增用户-查询用户-删除用户-修改角色-删除角色')
    Xitong().add_juese()
    Xitong().select_juese()
    Xitong().add_yonghu()
    Xitong().select_yonghu()
    Xitong().delete_yonghu()
    Xitong().update_juese()
    Xitong().delete_juese()


