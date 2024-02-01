import time,requests,json,base64,hashlib
from urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
key = '81971e4f-d268-4031-9059-2edd14f6a975'
url = f'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key={key}'
headers = {
        'Content-Type': 'application/json'
    }

class Robot():
    def APIwenben(self,text,name): #qywx().APIwenben('test',["shangguanyi"])
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
        print('文本消息发送',reqwenben.text)

    def APItupian(self,file): #qywx().qywx.APItupian(file)
        with open(file, 'rb') as f:  # 以二进制读取图片
            file_content = f.read()
            # 计算文件的MD5哈希值
            md5_hash = hashlib.md5(file_content).hexdigest()
            # 将文件内容进行Base64编码
            base64_encoded = base64.b64encode(file_content).decode('utf-8')
        #发送图片
        tupian = json.dumps({
            "msgtype": "image",
            "image": {
                "base64": base64_encoded,
                "md5": md5_hash
            }
        })
        requests.packages.urllib3.disable_warnings()    #关闭校验
        restupian = requests.request("POST", url,headers=headers, data=tupian,verify=False)
        print('图片消息发送',restupian.text)
    def APIwenjian(self,file): #qywx().APIwenjian(r'/Users/v_jingwenshuo/Desktop/dingdan.txt')
        id_url = f'https://qyapi.weixin.qq.com/cgi-bin/webhook/upload_media?key={key}&type=file'  # 上传文件接口地址
        headers = {
            'Content-Type': 'multipart/form-data'
        }
        data = {
            'file': open(file, 'rb')# 以二进制格式读取文件
        }
        requests.packages.urllib3.disable_warnings()    #关闭校验
        response = requests.post(url=id_url,headers=headers,files=data,verify=False)  # post 请求上传文件
        json_res = response.json()  # 返回转为json
        #print(json_res)
        media_id = json_res['media_id']  # 提取返回ID
        data = json.dumps({
            "msgtype": "file",
            "file":
                {"media_id": media_id}
        })  # post json
        requests.packages.urllib3.disable_warnings() #关闭校验
        req = requests.post(url=url, data=data,verify=False)  # post请求消息
        print('文件消息发送',req.json())
    def APItuwen(self,title,link_url,tupian=None,miaoshu=None):
        tuwen = json.dumps({
            "msgtype": "news",
            "news": {
               "articles" : [
                   {
                       "title" : title,
                       "description" : miaoshu,
                       "url" : link_url,
                       "picurl" : tupian
                   }
                ]
            }
        }
        )
        res = requests.post(url=url,headers=headers,data=tuwen,verify=False)
        print('图文消息发送',res.json())

