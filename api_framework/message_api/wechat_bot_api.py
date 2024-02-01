#coding=gbk
import sys
import time,requests,json,base64,hashlib
from urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
key = '81971e4f-d268-4031-9059-2edd14f6a975'
url = f'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key={key}'
headers = {
        'Content-Type': 'application/json'
    }

class Robot():
    def APIwenben(self,text,name=None): #qywx().APIwenben('test',["shangguanyi"])
        #�ı���Ϣ
        wenben = json.dumps({
            "msgtype": "text",
            "text": {
                "content": text,
                "mentioned_list":name, #@ �Ǳ���
                #"mentioned_mobile_list":["13848886443","@all"] #�ֻ����б� �Ǳ���
            }
        })
        requests.packages.urllib3.disable_warnings()    #�ر�У��
        reqwenben = requests.request('POST',url=url,headers=headers,data=wenben,verify=False)
        print('���ͳɹ�',reqwenben.text)

    def APItupian(self,file): #qywx().qywx.APItupian(file)
        with open(file, 'rb') as f:  # �Զ����ƶ�ȡͼƬ
            # ת��base64�����ʽ
            data = f.read()  # ��ȡ�����ļ�
            encode_str = base64.b64encode(data)  # �õ� byte ���������
            # print(str(encode_str, 'utf-8'))  # ���±�������

            # ����md5
            md = hashlib.md5()
            md.update(data)  # ��md�����������Ҫ���ܵ��ַ���
            res1 = md.hexdigest()  # ��ȡ���ܺ���ַ���
            f.close()
        #����ͼƬ
        tupian = json.dumps({
            "msgtype": "image",
            "image": {
                "base64": str(encode_str, 'utf-8'),
                "md5": res1
            }
        })
        requests.packages.urllib3.disable_warnings()    #�ر�У��
        restupian = requests.request("POST", url,headers=headers, data=tupian,verify=False)
        print('���ͳɹ�',restupian.text)

    def APIwenjian(self,file): #qywx().APIwenjian(r'/Users/v_jingwenshuo/Desktop/dingdan.txt')
        id_url = f'https://qyapi.weixin.qq.com/cgi-bin/webhook/upload_media?key={key}&type=file'  # �ϴ��ļ��ӿڵ�ַ
        headers = {
            'Content-Type': 'multipart/form-data'
        }
        data = {
            'file': open(file, 'rb')# �Զ����Ƹ�ʽ��ȡ�ļ�
        }
        response = requests.post(url=id_url,headers=headers,files=data,verify=False)  # post �����ϴ��ļ�
        json_res = response.json()  # ����תΪjson
        #print(json_res)
        media_id = json_res['media_id']  # ��ȡ����ID
        data = {"msgtype": "file", "file": {"media_id": media_id}}  # post json
        requests.packages.urllib3.disable_warnings() #�ر�У��
        r = requests.post(url=url, json=data,verify=False)  # post������Ϣ
        req = r.json()
        print('���ͳɹ�',req)





#Robot().APIwenben('test',["shangguanyi",'@all'])
#Robot().APIwenjian(r'E:\PycharmProjects\l��ʱ\conftest.py')





