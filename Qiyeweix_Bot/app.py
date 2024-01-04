import json
import time
from flask import Flask, request
from WXBizMsgCrypt import WXBizMsgCrypt
import xml.etree.cElementTree as ET
from method import *
from sql import MySQLHelper

app = Flask(__name__)
db = MySQLHelper()
sToken = "yPHZzZXVskML7nxWeLrLNdVgM8n1qp"
sEncodingAESKey = "gtZPw83P03zNNLo1wzygbgvK7n1w3QvRObp7M3WlCM5"
sCorpID = "ww19bc368e963e6b44"
wxcpt = WXBizMsgCrypt(sToken, sEncodingAESKey, sCorpID)

@app.route('/webhook/renzheng', methods=['GET', 'POST'])
def robot():
    msg_signature = request.args.get('msg_signature')  # 企业微信加密签名
    print('msg_signature', msg_signature)
    timestamp = request.args.get('timestamp')  # 时间戳
    nonce = request.args.get('nonce')  # 随机数
    echostr = request.args.get('echostr')  # 加密字符串
    print('echostr', echostr)

    # 验证URL有效性
    if request.method == 'GET':
        ret, sReplyEchoStr = wxcpt.VerifyURL(msg_signature, timestamp, nonce, echostr)
        if ret == 0:
            return sReplyEchoStr
        else:
            return 'ERR: VerifyURL ret:' + str(ret)

    # 接收消息
    elif request.method == 'POST':
        sEncryptMsg = ''
        ret, xml_content = wxcpt.DecryptMsg(request.data, msg_signature, timestamp, nonce)
        if ret == 0:
            root = ET.fromstring(xml_content)
            print('xml_content', xml_content)
            to_user_name = root.find('ToUserName').text
            from_user_name = root.find('FromUserName').text
            create_time = root.find('CreateTime').text
            msg_type = root.find('MsgType').text
            content = root.find('Content').text
            msg_id = root.find('MsgId').text
            agent_id = root.find('AgentID').text
            print('用户发送信息：', content)
            # return content
            timestamp = str(int(time.time()))
            if '叫' in content:
                # 被动回复
                content_info = content.split('叫')[1]
                sReplyMsg = message(
                    to_user_name,
                    from_user_name,
                    msg_id,
                    agent_id,
                    content_info
                )
                ret, sEncryptMsg = wxcpt.EncryptMsg(sReplyMsg, nonce, timestamp)
            elif '翻译成' in content:
                # 被动回复
                yuyan = content.split('翻译成')[1].split(' ')[0]
                content_info = content.split('翻译成')[1].split(' ')[1]
                print('语言',yuyan)
                print('被翻译信息',content_info)
                content_zh = fanyi(yuyan,content_info)
                sReplyMsg = message(
                    to_user_name,
                    from_user_name,
                    msg_id,
                    agent_id,
                    content_zh
                )
                ret, sEncryptMsg = wxcpt.EncryptMsg(sReplyMsg, nonce, timestamp)
            else:
                pass
            if ret == 0:
                return sEncryptMsg
            else:
                return 'ERR: EncryptMsg ret: ' + str(ret)

        else:
            return 'ERR: DecryptMsg ret:' + str(ret)



@app.route('/', methods=['GET'])
def index():
    return json.dumps({'mes':'成功'})

@app.route('/getcookies',methods=['get'])
def getcookie():
    return getcookies()


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080, debug=True)  # 启动服务

