#coding=gbk
from API_case.API1 import Space
from API_case.API2 import Xitong, Yuniyng


def test1():
    # �����ɹ�����-��ѯ�ɹ�����-�޸Ĳɹ�����-��ʼ����ѯ-�ɹ����-�������ѯ-�������۶���-��ѯ���۶���-�޸����۶���-���۷���-���������ѯ
    print('\n�����ɹ�����-��ѯ�ɹ�����-�޸Ĳɹ�����-��ʼ����ѯ-�ɹ����-�������ѯ-�������۶���-��ѯ���۶���-�޸����۶���-���۷���-���������ѯ')
    Space().add_caigou()
    Space().select_caigou()
    kucun = Space().select_kucun('1074-82-4')  # ��ʼ���
    Space().update_caigou_order()
    Space().ruku()
    rkcun = Space().select_kucun('1074-82-4')  # ����Ŀ��
    assert kucun + 1000 == rkcun
    Space().add_xiaoshou()
    Space().id()
    Space().select_xiaoshou()
    Space().update_xiaoshou_order()
    Space().fahuo()
    ckkucun = Space().select_kucun('1074-82-4')  # �����Ŀ��
    assert rkcun - 1000 == ckkucun
    assert kucun == ckkucun

def test2():
    #�����ɹ�����-��ѯ�ɹ�����-�޸Ĳɹ�����-ɾ���ɹ�����
    print('\n�����ɹ�����-��ѯ�ɹ�����-�޸Ĳɹ�����-ɾ���ɹ�����')
    Space().add_caigou()
    Space().select_caigou()
    Space().update_caigou_order()
    Space().delect_caigou()

def test3():
    #�������۶���-��ѯ���۶���-�޸����۶���-ɾ�����۶���
    print('\n�������۶���-��ѯ���۶���-�޸����۶���-ɾ�����۶���')
    Space().add_xiaoshou()
    Space().id()
    Space().select_xiaoshou()
    Space().update_xiaoshou_order()
    Space().delete_xiaoshou()

def test4():
    # ����������⡢����
    print('\n����������⡢����')
    kucun = Space().select_kucun('QTRK-000001') #��ʼ���
    Space().qita_ruku()
    rkkucun = Space().select_kucun('QTRK-000001') #������
    assert kucun + 100 == rkkucun
    Space().qita_fahuo()
    ckkucun = Space().select_kucun('QTRK-000001') #�������
    assert rkkucun - 100 == ckkucun
    assert kucun == ckkucun

def test5():
    # ������Ʒ-�޸Ĳ�Ʒ��Ϣ-���ò�Ʒ��ǩ-ɾ����Ʒ��������ѯ
    print('\n������Ʒ-�޸Ĳ�Ʒ��Ϣ-���ò�Ʒ��ǩ-ɾ����Ʒ��������ѯ')
    Space().add_chanpin()
    Space().update_chanpin()
    Space().set_chanpin_biaoqian()
    Space().delete_chanpin()
    Space().select_churuku()

def test6():
    #�����ɹ�����-��ѯ�ɹ�����-�޸Ĳɹ�����-����-��Ʊ-�����ʼ챨��-�ɹ����-��ӡ��ⶩ��
    print('\n�����ɹ�����-��ѯ�ɹ�����-�޸Ĳɹ�����-����-��Ʊ-�����ʼ챨��-�ɹ����-��ӡ��ⶩ��')
    Space().add_caigou()
    Space().select_caigou()
    Space().update_caigou_order()
    Space().caigou_fukuan()
    Space().caigou_shoupiao()
    Space().zhijianbaogao()
    Space().ruku()
    Space().dayin_ruku()

def test7():
    #�������۶���-��ѯ���۶���-�޸����۶���-�տ�-��Ʊ-���۷���-��ӡ��������
    print('\n�������۶���-��ѯ���۶���-�޸����۶���-�տ�-��Ʊ-���۷���-��ӡ��������')
    Space().add_xiaoshou()
    Space().id()
    Space().select_xiaoshou()
    Space().update_xiaoshou_order()
    Space().xiaoshou_shoukuan()
    Space().xiaoshou_kaipiao()
    Space().fahuo()
    Space().dayin_fahuo()

def test8():
    #�����տ�
    print('\n�����տ�')
    Space().xiaoshou_piliangshoukuan()

def test9():
    # ������ҳ����-��ѯ����-������ҳ��������Ӧ������-��ѯ��ҳ-�޸ĵ�ҳ-ɾ����ҳ-�޸ĵ���-ɾ������
    print('\n������ҳ����-��ѯ����-������ҳ��������Ӧ������-��ѯ��ҳ-�޸ĵ�ҳ-ɾ����ҳ-�޸ĵ���-ɾ������')
    Yuniyng().add_daohang('��ҳ',1)
    Yuniyng().select_daohang()
    Yuniyng().add_danye()
    Yuniyng().select_danye()
    Yuniyng().update_danye()
    Yuniyng().delete_danye()
    Yuniyng().update_daohang()
    Yuniyng().delete_daohang()

def test10():
    #�����б���-��ѯ����-�����б�������Ӧ������-��ѯ�б�-�޸��б�-ɾ���б�-�޸ĵ���-ɾ������;��Ա���� ��ѯ�û���Ϣ
    print('\n�����б���-��ѯ����-�����б�������Ӧ������-��ѯ�б�-�޸��б�-ɾ���б�-�޸ĵ���-ɾ������;��Ա���� ��ѯ�û���Ϣ')
    Yuniyng().add_daohang('�б�',2)
    Yuniyng().select_daohang()
    Yuniyng().add_liebiao()
    Yuniyng().select_liebiao()
    Yuniyng().update_liebiao()
    Yuniyng().delete_liebiao()
    Yuniyng().update_daohang()
    Yuniyng().delete_daohang()
    Yuniyng().select_vip()

def test11():
    # ϵͳ���� ������ɫ-��ѯ��ɫ-�����û�-��ѯ�û�-ɾ���û�-�޸Ľ�ɫ-ɾ����ɫ
    print('\nϵͳ���� ������ɫ-��ѯ��ɫ-�����û�-��ѯ�û�-ɾ���û�-�޸Ľ�ɫ-ɾ����ɫ')
    Xitong().add_juese()
    Xitong().select_juese()
    Xitong().add_yonghu()
    Xitong().select_yonghu()
    Xitong().delete_yonghu()
    Xitong().update_juese()
    Xitong().delete_juese()


