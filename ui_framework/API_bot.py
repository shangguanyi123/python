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
    def text_api(self,text,name=None):
        #文本消息
        data = json.dumps({
            "msgtype": "text",
            "text": {
                "content": text,
                "mentioned_list":[name],
                #"mentioned_mobile_list":["13848886443","@all"] #手机号列表 非必填
            }
        })
        requests.packages.urllib3.disable_warnings()    #关闭校验
        res = requests.request('POST',url=url,headers=headers,data=data,verify=False)
        print('文本消息',res.text)

    def img_api(self,file):
        with open(file, 'rb') as f:
            # 转化base64编码格式
            file_data = f.read()
            encode_str = base64.b64encode(file_data)
            # print(str(encode_str, 'utf-8'))  # 重新编码数据

            # 生成md5
            md = hashlib.md5()
            md.update(file_data)  # 在md上面更新所需要加密的字符串
            md5 = md.hexdigest()  # 获取加密后的字符串
            f.close()
        #发送图片
        data = json.dumps({
            "msgtype": "image",
            "image": {
                "base64": str(encode_str, 'utf-8'),
                "md5": md5
            }
        })
        requests.packages.urllib3.disable_warnings()    #关闭校验
        res = requests.request("POST", url=url,headers=headers, data=data,verify=False)
        print('图片消息',res.text)

    def file_api(self,file):
        file_url = f'https://qyapi.weixin.qq.com/cgi-bin/webhook/upload_media?key={key}&type=file'
        headers_form = {
            'Content-Type': 'multipart/form-data'
        }
        file_data = {
            'file': open(file, 'rb')
        }
        file_response = requests.post(url=file_url,headers=headers_form,files=file_data,verify=False)
        #print(file_response.json())

        media_id = file_response.json()['media_id']
        data = json.dumps({
            "msgtype": "file",
            "file": {
                "media_id": media_id
            }
        })
        requests.packages.urllib3.disable_warnings() #关闭校验
        res = requests.post(url=url, headers=headers,data=data,verify=False)
        print('文件消息',res.text)

    def img_text_api(self, title, link_url, img_url=None, description=None):
        data = json.dumps({
            "msgtype": "news",
            "news": {
                "articles": [
                    {
                        "title": title,
                        "description": description,
                        "url": link_url, #点击图片后跳转的链接。
                        "picurl": img_url #图文消息的图片链接
                    }
                ]
            }
        }
        )
        res = requests.post(url=url, headers=headers, data=data, verify=False)
        print('图文消息', res.text)


# 调用示例
# Robot().text_api('test','shangguanyi')
# Robot().img_api(r'C:\Users\shangguanyi\Desktop\上官一\后台\3.png')
# Robot().file_api(r'E:\PycharmProjects\ichempro\message_api\wechat_bot_api.py')
# Robot().img_text_api('标题','http://spider.aikonchem.com:9014/_nuxt/logo.8d52cbb2.png','http://spider.aikonchem.com:9014/_nuxt/logo.8d52cbb2.png','描述')
