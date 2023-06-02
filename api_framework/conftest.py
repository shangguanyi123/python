#encoding=utf-8
import pytest,sys
from _pytest.config import create_terminal_writer

from API_case.API_robot import Robot


@pytest.hookimpl(tryfirst=True) #tryfirst=True：该钩子函数优先于其他同一阶段的钩子函数执行
def pytest_terminal_summary(terminalreporter, exitstatus, config):
    #检查是否配置了 htmlpath 选项，即是否指定了生成 HTML 报告的路径。如果没有配置，则直接返回，不进行后续的处理。
    if not terminalreporter.config.getoption("htmlpath"):
        return
    #创建一个用于在终端上输出的 writer 对象，可以使用该对象来打印信息。
    writer = create_terminal_writer(terminalreporter.config)
    #获取在测试过程中捕获的输出内容。_tw 是 terminalreporter 的一个属性，表示测试过程中的输出流。
    captured_output = terminalreporter._tw.captured.getvalue()
    #打开指定的 HTML 报告文件，以追加模式写入内容。
    with open(terminalreporter.config.getoption("htmlpath"), "a") as html_report:
        #在终端输出一个分隔线，用于标识开始捕获的输出内容。
        writer.sep("-", "Captured Output")
        #在终端输出捕获的输出内容。
        writer.line(captured_output)
        #在终端输出一个分隔线，用于标识结束捕获的输出内容。
        writer.sep("-", "End of Captured Output")
        writer.line()
        #将一个标题标签写入 HTML 报告中，用于标识捕获的输出内容。
        html_report.write("<h2>Captured Output:</h2>")
        #将捕获的输出内容以 <pre> 标签的形式写入 HTML 报告中，保留原始的格式。
        html_report.write("<pre>{}</pre>".format(captured_output))


#发送测试报告
@pytest.hookimpl(trylast=True) #该钩子函数在其他同一阶段的钩子函数执行完毕后执行
def pytest_terminal_summary(terminalreporter, exitstatus, config):
    if exitstatus == pytest.ExitCode.OK:  # 测试用例全部运行成功
        report_path = terminalreporter._session.config.option.htmlpath # 获取测试报告路径
        if report_path:
            Robot().APIwenjian(report_path)
    elif exitstatus == pytest.ExitCode.TESTS_FAILED: # 测试用例有运行失败的
        report_path = terminalreporter._session.config.option.htmlpath # 获取测试报告路径
        if report_path:
            Robot().APIwenjian(report_path)
