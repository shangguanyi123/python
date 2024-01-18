# encoding=utf-8
import pyautogui
import pytest, time, logging, os, threading ,json
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from sql import MySQLHelper_cookies

url = 'http://spider.aikonchem.com:48888/'
db = MySQLHelper_cookies()

@pytest.fixture(scope='function')  # 表示这是一个 pytest fixture，作用域为测试函数级别（方法级别）。
def driver(request):
    identity_marker = request.node.get_closest_marker("identity") #获取与测试函数相标记为identity
    if identity_marker is not None:
        username = identity_marker.args[0] # 返回这个元组中的第一个参数，即user2
        cookie_data = db.execute_query(f"SELECT session, token FROM cookies WHERE username = '{username}'")
    else:
        # 如果没有标记，默认使用 'user1' 身份
        cookie_data = db.execute_query("select session,token from cookies where username = 'user1'")

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
        {'name': 'qs_session', 'path': '/', 'value': cookie_data[0]['session']},
        {'name': 'XSRF-TOKEN', 'path': '/', 'value': cookie_data[0]['token']}
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
            screenshot_dir = r".E:\venv3.8\India_data\error_screenshot"  # 截图保存目录
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

class WebAutomation:
    def __init__(self, driver):
        self.driver = driver

    # 点击，class有多层，示例：.btn_add.mouse
    def selenium_click(self, types, element, index=None):
        if index is None:
            next_btn = self.driver.find_element(types, element)
            self.driver.execute_script("arguments[0].click();", next_btn)
        else:
            next_btn = self.driver.find_elements(types, element)[int(index)]
            self.driver.execute_script("arguments[0].click();", next_btn)

    # 输入
    def selenium_send(self, types, element, text, index=None):
        if index is None:
            next_btn = self.driver.find_element(types, element)
            self.driver.execute_script("arguments[0].value = arguments[1]", next_btn, text)
        else:
            next_btn = self.driver.find_elements(types, element)[index]
            self.driver.execute_script("arguments[0].value = arguments[1]", next_btn, text)

    # 点击 class有多层，示例：.btn_add.mouse
    def jquery_click(self, element, index=None):
        if index is None:
            self.driver.execute_script(f"return $('{element}')[0].click()")
        else:
            elements = self.driver.execute_script(f"return $('{element}')")
            if 0 < index < len(elements):
                element_to_click = elements[index]
                element_to_click.click()
            else:
                print(f"Index {index} 超出索引范围.")

    # 输入文本
    def jquery_input_text(self, element, text=None, index=None):
        if index is None:
            self.driver.execute_script(f"return $('{element}').val('{text}')")
        else:
            elements = self.driver.execute_script(f"return $('{element}')")
            if 0 < index < len(elements):
                element_to_input = elements[index]
                self.driver.execute_script(f"arguments[0].value = '{text}';", element_to_input)
            else:
                print(f"Index {index} 超出索引范围.")

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

    # 获取文本内容
    def text_content(self, types, element, index=None):
        if index is None:
            info = self.driver.find_element(types, element).text
            return info
        else:
            info = self.driver.find_elements(types, element)[index].text
            return info

    # 切入ifram框，一般情况
    def cut_in_ifram(self, types, element, index=None):
        if index is None:
            self.driver.switch_to.frame(self.driver.find_element(types, element))
        else:
            self.driver.switch_to.frame(self.driver.find_elements(types, element)[int(index)])

    # 切入ifram框，特殊情况
    def cut_in_ifram_not_unique(self, types, element, index=None):
        if index is None:
            parent_element = self.driver.find_element(types, element)
        else:
            parent_element = self.driver.find_elements(types, element)[int(index)]
        self.driver.switch_to.frame(parent_element.find_element(By.TAG_NAME, 'iframe'))

    # 切出ifram
    def cut_out_ifram(self):
        self.driver.switch_to.default_content()

    # 下拉选项框
    def select(self, types, element, index, class_index=None):
        if class_index is None:
            Select(self.driver.find_element(types, element)).select_by_index(int(index))
        else:
            Select(self.driver.find_elements(types, element)[int(class_index)]).select_by_index(int(index))

    # 显示等待
    def wait(self, types, element):
        WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((types, element)))

    # 切换窗口
    def switch_windows(self, index):
        self.driver.switch_to.window(self.driver.window_handles[int(index)])

    # 打开第二个网页
    def opens_new_tab(self, url, index):
        self.driver.execute_script(f"window.open('{url}');")
        self.driver.switch_to.window(self.driver.window_handles[int(index)])

    # 界面上下滑动
    def up_down_slide(self, bili):
        # bili为0表示滑动到页面最上方，1为最下方，0.65为页面从上到下的65%处,范围在0-1
        self.driver.execute_script(f"window.scrollTo(0, document.body.scrollHeight * {bili});")  # 滑动到屏幕57%处

    # 元素滑动
    def element_slide(self, types, element, zuoyou, sahngxia, index=None):
        if index is None:
            # 获取要操作的元素
            ele = self.driver.find_element(types, element)
            # 创建一个ActionChains对象
            '''
                    上滑移动50个像素 move_by_offset( 0,-50)
                    下滑移动50个像素 move_by_offset( 0, 50)
                    左滑移动50个像素 move_by_offset(-50, 0)
                    右滑移动50个像素 move_by_offset( 50, 0)
            '''
            ActionChains(self.driver).move_to_element(ele).move_by_offset(zuoyou, sahngxia).perform()
        else:
            ele = self.driver.find_elements(types, element)[int(index)]
            ActionChains(self.driver).move_to_element(ele).move_by_offset(zuoyou, sahngxia).perform()

def update_cookies(driver,username):
    cookies = driver.get_cookies()
    cookie_json = json.dumps(cookies)  # 转为json
    cookie_data = json.loads(cookie_json)  # 转为python字典
    db.execute_update(
        'UPDATE cookies SET token = "%s", session = "%s",Cookie_json="%s",update_time = "%s" WHERE username = "%s"' % (
            cookie_data[0]['value'], cookie_data[2]['value'],cookie_json,time.strftime("%Y-%m-%d %H:%M:%S"), username)
    )
    
    
