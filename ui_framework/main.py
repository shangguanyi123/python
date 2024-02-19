#encoding=utf-8
import pytest
from Email import send_email
from API_bot import Robot

if __name__ == '__main__':
    args = ['']
    pytest.main(args)

# 在测试运行后获取测试报告的目录
report_path = "./reports/iChemBio_report.html"  # 根据实际情况修改测试报告的目录

# 调用发送邮件和企业微信的方法
if report_path:
    Robot().text_api('iChemBio线上环境报错，请及时通过测试报告产看详情','shangguanyi')
    Robot().file_api(report_path)  # 企业微信
    #send_email([report_path])  # 邮件

