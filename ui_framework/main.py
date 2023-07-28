#encoding=utf-8
import pytest
from Email import send_email
from API_bot import Robot

if __name__ == '__main__':
    args = ['pytest','tests/']
    pytest.main(args)

    # 在测试运行后获取测试报告的目录
    report_path = "./reports/iChemBio_report.html"  # 根据实际情况修改测试报告的目录

    # 调用发送邮件和企业微信的方法
    if report_path:
        Robot().APIwenjian(report_path)  # 企业微信
        send_email([report_path])  # 邮件

