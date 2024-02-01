#encoding=utf-8
import pytest
from message_api.wechat_bot_api import Robot


# 定义一个 fixture 用于捕获标准输出
@pytest.fixture
def capture_output(capsys):
    yield capsys

# 定义一个 pytest 钩子函数，在测试结束后将标准输出写入测试报告
@pytest.hookimpl(tryfirst=True)
def pytest_terminal_summary(terminalreporter, exitstatus, config):
    # 检查是否配置了 htmlpath 选项，即是否指定了生成 HTML 报告的路径。如果没有配置，则直接返回，不进行后续的处理。
    if not terminalreporter.config.getoption("htmlpath"):
        return
    writer = terminalreporter._tw
    # 获取捕获的标准输出
    captured_output = terminalreporter.stats.get("Captured stdout")
    with open(terminalreporter.config.getoption("htmlpath"), "a") as html_report:
        writer.line()
        # 将一个标题标签写入 HTML 报告中，用于标识捕获的输出内容。
        html_report.write("<h2>捕获的输出内容:</h2>")
        # 将捕获的输出内容以 <pre> 标签的形式写入 HTML 报告中，保留原始的格式。
        html_report.write("<pre>{}</pre>".format(captured_output))

#发送测试报告
@pytest.hookimpl(trylast=True) #该钩子函数在其他同一阶段的钩子函数执行完毕后执行
def pytest_terminal_summary(terminalreporter, exitstatus, config):
    if exitstatus == pytest.ExitCode.OK:  # 测试用例全部运行成功
        report_path = terminalreporter._session.config.option.htmlpath # 获取测试报告路径
        if report_path:
            pass
            #Robot().APIwenjian(report_path)
    elif exitstatus == pytest.ExitCode.TESTS_FAILED: # 测试用例有运行失败的
        report_path = terminalreporter._session.config.option.htmlpath # 获取测试报告路径
        if report_path:
            Robot().APIwenben('ichempro运行报错，请通过测试报告查看详情！！！')
            Robot().APIwenjian(report_path)
