#coding=gbk
from API_case.API1 import Xitongguanli

def test_01():
    #�����û�-��ѯ-�޸��û�(���š���ɫ��״̬)-ɾ���û�;�޸������û�״̬
    print('�����û���״̬������-��ѯ-�޸��û�(���š���ɫ��״̬)-ɾ���û�;�޸������û�״̬')
    Xitongguanli().add_user(1)
    Xitongguanli().select_user(1)
    Xitongguanli().update_uesr(20,1,0)
    Xitongguanli().del_user()
    Xitongguanli().update_user_status(0,1)
    print('�����û���״̬�رգ�-��ѯ-�޸��û�(���š���ɫ��״̬)-ɾ���û�;�޸������û�״̬')
    Xitongguanli().add_user(0)
    Xitongguanli().select_user(0)
    Xitongguanli().update_uesr(20, 1, 1)
    Xitongguanli().del_user()
    Xitongguanli().update_user_status(0, 1)
def test_02():
    #�����û�-������ɫ-����û�����ɫ-ɾ���û�������ɫ-ɾ����ɫ-ɾ���û�
    print('�����û�-������ɫ-����û�����ɫ-ɾ���û�������ɫ-ɾ����ɫ-ɾ���û�')
    Xitongguanli().add_user(1)
    Xitongguanli().add_juese('ϵͳ����Ա����ʱ��',1)
    Xitongguanli().insert_uesr_juese()
    Xitongguanli().del_user_juese()
    Xitongguanli().del_juese()
    Xitongguanli().del_user()
def test_03():
    #������λ-��ѯ��λ-ɾ����λ
    print('����������λ-�޸�Ϊ������λ-��ѯ������λ-ɾ��')
    Xitongguanli().add_danwei(1,'m',1,'length',1,'0.001')
    Xitongguanli().update_danwei(1,'mm',1,'length',1,'0.001')
    Xitongguanli().sel_danwei('measure')
    Xitongguanli().del_danwei()
    print('����������λ-�޸�Ϊ��װ��λ-��ѯ��װ��λ-ɾ��')
    Xitongguanli().add_danwei(1, 'm', 1, 'length', 1, '0.01')
    Xitongguanli().update_danwei(0, 'mm', 1)
    Xitongguanli().sel_danwei('package')
    Xitongguanli().del_danwei()
    print('������װ��λ-�޸�Ϊ��װ��λ-��ѯ��װ��λ-ɾ��')
    Xitongguanli().add_danwei(0, 'km', 1)
    Xitongguanli().update_danwei(0, 'mm', 1)
    Xitongguanli().sel_danwei('package')
    Xitongguanli().del_danwei()
    print('������װ��λ-�޸�Ϊ������λ-��ѯ������λ-ɾ��')
    Xitongguanli().add_danwei(0, 'km', 1)
    Xitongguanli().update_danwei(1, 'mm', 1, 'length', 1, '0.01')
    Xitongguanli().sel_danwei('measure')
    Xitongguanli().del_danwei()


def test_04():
    #�����������-��ѯ�������-�޸ĵ������-ɾ���������
    print('�����������-��ѯ�������-�޸ĵ������-ɾ���������')
    Xitongguanli().add_danjushenhe(['���۶���'],'��Ҫ���')
    Xitongguanli().sel_danjushenhe()
    Xitongguanli().update_danjushenhe(['���۶���','�ɹ�����'],'����������',10000)
    Xitongguanli().del_danjushenhe()
def test_05():
    #ϵͳ����
    print('ϵͳ���������ʼ�����')
    Xitongguanli().gonggongcanshu_email()
def test_06():
    #��������-��ѯ����-�޸ĵ���-ɾ������
    print('��������-��ѯ����-�޸ĵ���-ɾ������')
    Xitongguanli().add_diqu(0,'������')
    Xitongguanli().sel_diqu('������')
    Xitongguanli().update_diqu(1,'���Ե���')
    Xitongguanli().del_diqu('���Ե���')
def test_07():
    # �޸ı�Ź���-��ѯ��Ź���
    print('�޸ı�Ź���-��ѯ��Ź���')
    Xitongguanli().update_biaohao_guize(1)
    Xitongguanli().update_biaohao_guize(2)
    Xitongguanli().update_biaohao_guize(3)
    Xitongguanli().update_biaohao_guize(4)
    Xitongguanli().update_biaohao_guize(5)
    Xitongguanli().sel_biaohao_guize('��Ʒ���')
def test_08():
    # �����������Ϸ���-�޸ĸ������Ϸ���-����������������-�޸ĸ�����������-ɾ��������������-ɾ���������Ϸ���
    print('�����������Ϸ���-�޸ĸ������Ϸ���-����������������-�޸ĸ�����������-ɾ��������������-ɾ���������Ϸ���')
    Xitongguanli().add_fuzhuzilaio_fenlei('�������ͣ����ԣ�')
    Xitongguanli().update_fuzhuzilaio_fenlei('��������')
    Xitongguanli().add_fuzhuzilaio_mingcheng('��������vip', 1)
    Xitongguanli().update_fuzhuziliao_mingcheng('����vip', 0)
    Xitongguanli().del_fuzhuziliao_mingcheng('����vip')
    Xitongguanli().del_fuzhuziliao_fenlei()
def test_09():
    # ������������-�޸ĸ�������-ɾ����������
    print('�����������ԣ��ı���-�޸ĸ������ԣ����֣�-ɾ����������')
    Xitongguanli().add_fuzhushuxing('���ر��루���ԣ�', 'varchar', 0, 50)
    Xitongguanli().update_fuzhushuxing('���ر���test', 'int', 1, 50)
    Xitongguanli().del_fuzhushuxing()
    print('�����������ԣ����ڣ�-�޸ĸ������ԣ����ڣ�-ɾ����������')
    Xitongguanli().add_fuzhushuxing('���ر��루���ԣ�', 'timestamp',1)
    Xitongguanli().update_fuzhushuxing('���ر���test', 'timestamp', 0)
    Xitongguanli().del_fuzhushuxing()
    print('�����������ԣ����ø������ϣ�-�޸ĸ������ԣ����ø������ϣ�-ɾ����������')
    Xitongguanli().add_fuzhushuxing('���ر��루���ԣ�', 'auxiliary_category', 0)
    Xitongguanli().update_fuzhushuxing('���ر���test', 'auxiliary_category', 1)
    Xitongguanli().del_fuzhushuxing()
    print('�����������ԣ��ı���-�޸ĸ������ԣ����ø������ϣ�-ɾ����������')
    Xitongguanli().add_fuzhushuxing('���ر��루���ԣ�', 'varchar', 1,50)
    Xitongguanli().update_fuzhushuxing('���ر���test', 'auxiliary_category', 1)
    Xitongguanli().del_fuzhushuxing()

def test_10():

    pass
