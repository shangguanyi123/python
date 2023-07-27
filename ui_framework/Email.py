#encoding=utf8
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
from email import encoders
from email.header import Header

def send_email(file_paths=None):#file_paths传的是列表
    sender_email = "jws6443@163.com"  # 你的发件人邮箱（163邮箱）
    sender_password = "CEGZGOTVOFLMLVMV"  # 你的发件人邮箱密码
    receiver_email = "249185549@qq.com"  # 收件人邮箱
    # 邮件主题和HTML格式内容
    subject = "ichembio测试报告"
    body = "<html><body><h1>请通过附件产看测试报告详情！</h1></body></html>"

    if file_paths is None:
        file_paths = []

    # 设置SMTP服务器和端口号（163邮箱）
    smtp_server = "smtp.163.com"
    smtp_port = 25  # 或使用465端口（SSL加密），但需要将server.starttls()去掉

    server = None  # 初始化server变量

    try:
        # 登录SMTP服务器
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.login(sender_email, sender_password)

        # 创建一个包含邮件内容的MIMEMultipart对象
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = receiver_email
        message["Subject"] = subject

        # 添加HTML内容
        msg = MIMEText(body, "html", "utf-8")
        message.attach(msg)

        # 添加文件附件
        if file_paths:  # 检查file_paths是否非空
            for file_path in file_paths:
                with open(file_path, "rb") as f:
                    attachment = MIMEBase("application", "octet-stream")
                    attachment.set_payload(f.read())
                    encoders.encode_base64(attachment)
                    file_name = os.path.basename(file_path)
                    attachment.add_header("Content-Disposition", "attachment", filename=Header(file_name, "utf-8").encode())
                    message.attach(attachment)

        # 发送邮件
        server.sendmail(sender_email, receiver_email, message.as_string())
        print("邮件发送成功！")
    except Exception as e:
        print(f"邮件发送失败：{e}")
    finally:
        # 关闭连接
        if server is not None:
            server.quit()


