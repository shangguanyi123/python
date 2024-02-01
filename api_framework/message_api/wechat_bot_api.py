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
        #文本消息
        wenben = json.dumps({
            "msgtype": "text",
            "text": {
                "content": text,
                "mentioned_list":name, #@ 非必填
                #"mentioned_mobile_list":["13848886443","@all"] #手机号列表 非必填
            }
        })
        requests.packages.urllib3.disable_warnings()    #关闭校验
        reqwenben = requests.request('POST',url=url,headers=headers,data=wenben,verify=False)
        print('发送成功',reqwenben.text)

    def APItupian(self,file): #qywx().qywx.APItupian(file)
        with open(file, 'rb') as f:  # 以二进制读取图片
            # 转化base64编码格式
            data = f.read()  # 读取整个文件
            encode_str = base64.b64encode(data)  # 得到 byte 编码的数据
            # print(str(encode_str, 'utf-8'))  # 重新编码数据

            # 生成md5
            md = hashlib.md5()
            md.update(data)  # 在md上面更新所需要加密的字符串
            res1 = md.hexdigest()  # 获取加密后的字符串
            f.close()
        #发送图片
        tupian = json.dumps({
            "msgtype": "image",
            "image": {
                "base64": str(encode_str, 'utf-8'),
                "md5": res1
            }
        })
        requests.packages.urllib3.disable_warnings()    #关闭校验
        restupian = requests.request("POST", url,headers=headers, data=tupian,verify=False)
        print('发送成功',restupian.text)

    def APIwenjian(self,file): #qywx().APIwenjian(r'/Users/v_jingwenshuo/Desktop/dingdan.txt')
        id_url = f'https://qyapi.weixin.qq.com/cgi-bin/webhook/upload_media?key={key}&type=file'  # 上传文件接口地址
        headers = {
            'Content-Type': 'multipart/form-data'
        }
        data = {
            'file': open(file, 'rb')# 以二进制格式读取文件
        }
        response = requests.post(url=id_url,headers=headers,files=data,verify=False)  # post 请求上传文件
        json_res = response.json()  # 返回转为json
        #print(json_res)
        media_id = json_res['media_id']  # 提取返回ID
        data = {"msgtype": "file", "file": {"media_id": media_id}}  # post json
        requests.packages.urllib3.disable_warnings() #关闭校验
        r = requests.post(url=url, json=data,verify=False)  # post请求消息
        req = r.json()
        print('发送成功',req)





#Robot().APIwenben('test',["shangguanyi",'@all'])
#Robot().APIwenjian(r'E:\PycharmProjects\l临时\conftest.py')





