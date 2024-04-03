#encoding=utf8
import hashlib
import json,time,requests
from sql import MySQLHelper

db = MySQLHelper()

def getcookies():
    cookies = db.execute_query('select username,Cookie_json from cookies;')
    for item in cookies:
        item['Cookie_json'] = json.loads(item['Cookie_json'])
    return json.dumps(cookies, ensure_ascii=False)  # ensure_ascii=False 参数表示允许非 ASCII 字符存在于输出的 JSON 字符串中，保留其原始形式。
def message(to_user_name,from_user_name,msg_id,agent_id,content):
    return f'''
                <xml>
                    <ToUserName>{to_user_name}</ToUserName>
                    <FromUserName>{from_user_name}</FromUserName>
                    <CreateTime>{str(int(time.time()))}</CreateTime>
                    <MsgType>text</MsgType>
                    <Content>{content}</Content>
                    <MsgId>{msg_id}</MsgId>
                    <AgentID>{agent_id}</AgentID>
                </xml>
                '''
def fanyi(yuyan,text):
    url = "http://api.fanyi.baidu.com/api/trans/vip/translate"
    appid = 'appid'
    salt = str(int(time.time()))
    miyao = '秘钥'
    sign = appid + text + salt + miyao
    md5 = hashlib.md5()
    # 更新加密对象的内容
    md5.update(sign.encode('utf-8'))
    # 获取加密结果
    sign_md5 = md5.hexdigest()
    params = {
        'q': str(text),
        'from': 'auto',
        'to': 'zh' if yuyan == '汉语' else 'en' if yuyan == '英语' else 'jp' if yuyan == '日语' else 'cht' if yuyan == '繁体' else 'zh',
        'appid': appid,
        'salt': salt,
        'sign': sign_md5
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        if 'trans_result' in response.json():
            print(response.json()['trans_result'][0]['dst'])
            return response.json()['trans_result'][0]['dst']
        else:
            print(response.json())
            return response.json()
    else:
        return response.json()
