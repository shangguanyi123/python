
class Assertion():

    def __init__(self,res):
        self.res = res
    def tongyong(self):
        assert self.res.status_code == 200
        assert self.res.json()['status'] == 0
        assert self.res.json()['message'] == '操作成功'
    def chapinfenlei_chaxun(self,status,name):
        assert self.res.status_code == 200
        assert self.res.json()['data']['data'][0]['status'] == status
        assert self.res.json()['data']['data'][0]['name'] == name
    def chaxun_isnull(self):
        assert self.res.status_code == 200
        assert self.res.json()['message'] == '操作成功'
        assert self.res.json()['status'] == 0
        assert self.res.json()['data']['data'] == [],'删除失败'
    def data1_notnoll(self):
        assert self.res.status_code == 200
        assert self.res.json()['status'] == 0
        assert self.res.json()['message'] == '操作成功'
        assert self.res.json()['data'], '列表返回为空'
    def data2_notnoll(self):
        assert self.res.status_code == 200
        assert self.res.json()['status'] == 0
        assert self.res.json()['message'] == '操作成功'
        assert self.res.json()['data']['data'], '列表返回为空'
    def pinpai_chaxun(self,name):
        assert self.res.status_code == 200
        assert self.res.json()['status'] == 0
        assert self.res.json()['message'] == '操作成功'
        assert self.res.json()['data']['data'][0],'列表返回为空'
        assert self.res.json()['data']['data'][0]['name'] == name
    def cas_chaxun(self,cas):
        assert self.res.status_code == 200
        assert self.res.json()['status'] == 0
        assert self.res.json()['message'] == '操作成功'
        assert self.res.json()['data']['data'], '列表返回为空'
        assert self.res.json()['data']['data'][0]['cas'] or self.res.json()['data']['data'][0]['name_en'] == cas
    def add_kehu(self,name):
        assert self.res.status_code == 200
        assert self.res.json()['status'] == 0
        assert self.res.json()['message'] == '操作成功'
        assert self.res.json()['customer']['customer_name'] == name







