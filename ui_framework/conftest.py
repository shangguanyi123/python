# encoding=utf-8
import pyautogui
import pytest, time, logging, os
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains, Keys
from Email import send_email
from API_bot import Robot

url = 'https://www.ichembio.com/'
session = 'eyJpdiI6InYxMlRPQkhWVWZ2NnFKWkpDcmoxcUE9PSIsInZhbHVlIjoiVjUxYUc2Tmh6VmZ4Ri9wN251MW1tYzQzV21jUWoxY1FGbkNqVXlva3NiRUFUQWFrSU1weVdsODRlUGlvbUxkVnBSUWtENWhOeGxmYnpGc3cvaFBIelpDd2N5T25EYWRRTVZZbGFHVlBnekJ5RERPRzRQK1hTU01POWNtSGM0S0MiLCJtYWMiOiIyMjYyNjJjMzk1ODI4MjQxZWY3ZDQ5NWM3Y2U0NzE2ZjM1YzIxZDE0MjA5YTNkNjU3ZDUyMGEwZDczNzc5NTk2IiwidGFnIjoiIn0%3D'
token   = 'eyJpdiI6InYxMlRPQkhWVWZ2NnFKWkpDcmoxcUE9PSIsInZhbHVlIjoiVjUxYUc2Tmh6VmZ4Ri9wN251MW1tYzQzV21jUWoxY1FGbkNqVXlva3NiRUFUQWFrSU1weVdsODRlUGlvbUxkVnBSUWtENWhOeGxmYnpGc3cvaFBIelpDd2N5T25EYWRRTVZZbGFHVlBnekJ5RERPRzRQK1hTU01POWNtSGM0S0MiLCJtYWMiOiIyMjYyNjJjMzk1ODI4MjQxZWY3ZDQ5NWM3Y2U0NzE2ZjM1YzIxZDE0MjA5YTNkNjU3ZDUyMGEwZDczNzc5NTk2IiwidGFnIjoiIn0%3D'



@pytest.fixture(scope='function')  # 表示这是一个 pytest fixture，作用域为测试函数级别（方法级别）。
def driver(request):
    options = webdriver.ChromeOptions()  # 定义一个 ChromeOptions 对象，可以用来设置启动 Chrome 浏览器的一些参数。
    #options.add_argument('--headless')  # 开启无界面模式（无窗口运行）
    #options.add_argument('blink-settings=imagesEnabled=false')  # 不加载图片, 提升速度
    # 去掉不安全提示short
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument("--start-maximized")  # 将启动参数 "--start-maximized" 添加到 ChromeOptions 中，表示启动浏览器时最大化窗口。
    driver = webdriver.Chrome(options=options)  # 启动 Chrome 浏览器，并传入上面定义好的 ChromeOptions 对象。
    driver.get(f"{url}")
    driver.implicitly_wait(8)
    cookies = [
        {'domain': 'www.ichembio.com', 'name': 'qs_session', 'path': '/', 'value': session},
        {'domain': 'www.ichembio.com', 'name': 'XSRF-TOKEN', 'path': '/', 'value': token}
    ]
    for i in cookies:
        driver.add_cookie(i)
    driver.refresh()
    request.addfinalizer(driver.quit)  # 将 WebDriver 对象的 quit() 方法注册为测试结束后的清理函数，以确保测试用例结束后关闭浏览器进程。
    return driver  # 将 WebDriver 对象返回，供测试函数使用。


# 配置日志记录 其中%(asctime)s表示日志记录的时间，%(levelname)s表示日志级别，%(message)s表示日志消息内容。
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


# 报错截图+日志
# tryfirst=True 表示该钩子函数将在其他同类型的钩子函数之前被调用。如果多个钩子函数具有相同的名称和类型，则使用 tryfirst=True 的函数将首先被执行。
# hookwrapper=True 表示该钩子函数是一个装饰生成器，允许你在测试过程中包装和修改执行流程。装饰生成器可以在执行前后执行额外的代码，还可以通过 yield 语句将控制权传递给其他钩子函数。
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # 在测试函数执行结束后获取测试结果并进行处理
    outcome = yield  # 使用yield 将控制权交给 pytest，然后等待测试函数执行完毕并获取测试结果。通过yield 返回一个生成器对象，outcome 可以用来获取测试结果。
    rep = outcome.get_result()  # 通过outcome 对象的get_result() 方法获取测试结果。
    now1 = time.strftime("%Y-%m-%d %H-%M-%S")  # 年月日时分秒
    # 如果测试失败，则进行屏幕截图
    if rep.when == "call" and rep.failed:  # 如果rep.when 的值为"call"（表示测试函数的调用阶段）并且rep.failed 为True（表示测试失败），则执行条件块中的代码。
        try:
            driver = item.funcargs["driver"]  # 通过item.funcargs 字典获取测试函数中的driver 对象。driver 是通过driver fixture 返回的 WebDriver 对象。
            screenshot_dir = r"E:\PycharmProjects\数据站\error_screenshot"  # 截图保存目录
            os.makedirs(screenshot_dir, exist_ok=True)  # 确保截图保存的目录存在。如果目录不存在，则创建目录。
            screenshot_path = os.path.join(screenshot_dir,
                                           "报错截图%s.png" % now1)  # 使用os.path.join() 方法将目录路径和截图文件名连接起来，得到完整的截图文件路径。
            # screenshot = pyautogui.screenshot()
            # screenshot.save(screenshot_path) #截图全屏 在无窗口模式下无用
            driver.save_screenshot(screenshot_path)  # 调用 WebDriver 对象的save_screenshot() 方法保存屏幕截图到指定路径。
            print("报错截图另存为:", screenshot_path)
            logging.info("报错截图另存为：%s", screenshot_path)
        except NoSuchElementException as e:
            print("截图失败 无搜索元素异常", e)
            logging.info("截图失败 无搜索元素异常：%s", e)
        except Exception as e:
            print("未能捕获屏幕截图:", e)
            logging.info("未能捕获屏幕截图：%s", e)


#发送测试报告
@pytest.hookimpl(trylast=True) #该钩子函数在其他同一阶段的钩子函数执行完毕后执行
def pytest_terminal_summary(terminalreporter, exitstatus, config):
    if exitstatus == pytest.ExitCode.OK:  # 测试用例全部运行成功
        report_path = terminalreporter._session.config.option.htmlpath # 获取测试报告路径
        if report_path:
            Robot().APIwenjian(report_path) #企业微信
            #send_email([report_path]) #发邮件
    elif exitstatus == pytest.ExitCode.TESTS_FAILED: # 测试用例有运行失败的
        report_path = terminalreporter._session.config.option.htmlpath # 获取测试报告路径
        if report_path:
            Robot().APIwenjian(report_path)
            #send_email([report_path])


class Select:
    def __init__(self, driver):
        self.driver = driver

    # 点击
    def click(self, types, element, index=None):
        if index is None:
            next_btn = self.driver.find_element(types, element)
            self.driver.execute_script("arguments[0].click();", next_btn)
        else:
            next_btn = self.driver.find_elements(types, element)[int(index)]
            self.driver.execute_script("arguments[0].click();", next_btn)

    # 输入
    def send(self, types, element, text, index=None):
        if index is None:
            next_btn = self.driver.find_element(types, element)
            self.driver.execute_script("arguments[0].value = arguments[1]", next_btn, text)
        else:
            next_btn = self.driver.find_elements(types, element)[index]
            self.driver.execute_script("arguments[0].value = arguments[1]", next_btn, text)

    # 悬停
    def hover(self, types, element, index=None):
        if index is None:
            but = self.driver.find_element(types, element)
            ActionChains(self.driver).move_to_element(but).perform()
        else:
            but = self.driver.find_elements(types, element)[index]
            ActionChains(self.driver).move_to_element(but).perform()

    # 判断元素是否存在
    def check_element_presence(self, types, element, index=None):
        if index is None:
            try:
                self.driver.find_element(types, element)
                return True
            except NoSuchElementException:
                return False
        else:
            try:
                but = self.driver.find_elements(types, element)[index]
                return True
            except (NoSuchElementException, IndexError):
                return False

