#encoding=utf-8
import re
import time
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from conftest import Select
from conftest import url


#未登录
class TestUi():
    #产品搜索结果页-管制类产品搜索
    def test_1(self,driver):
        driver.delete_all_cookies()
        click_instance = Select(driver)
        driver.get(f"{url}")
        click_instance.click(By.NAME, "query")#首页搜索框
        # 管制类产品搜索
        click_instance.send(By.NAME, "query","4,4\'-二氨基-3,3\'-二氯二苯甲烷")#首页中文名称搜索
        click_instance.click(By.CLASS_NAME, "wrap-search-arrow")#搜索
        assert click_instance.check_element_presence(By.CSS_SELECTOR, ".wrap-danger") == True#管制类产品标识
        click_instance.click(By.XPATH,'/html/body/header/div/div[3]/form/div/input')#搜索框
        click_instance.send(By.XPATH,'/html/body/header/div/div[3]/form/div/input','101-14-4')#输入CAS号
        click_instance.click(By.CLASS_NAME,'wrap-cmSearch-arrow')#搜索
        assert click_instance.check_element_presence(By.CSS_SELECTOR, ".wrap-danger") == True#管制类产品标识
        click_instance.click(By.XPATH, '/html/body/header/div/div[3]/form/div/input')  # 搜索框
        click_instance.send(By.XPATH, '/html/body/header/div/div[3]/form/div/input',"4,4'-Methylene bis(2-chloroaniline)")  # 输入英文名称
        click_instance.click(By.CLASS_NAME, 'wrap-cmSearch-arrow')  # 搜索
        assert click_instance.check_element_presence(By.CSS_SELECTOR, ".wrap-danger") == True#管制类产品标识
        click_instance.click(By.XPATH, '/html/body/header/div/div[3]/form/div/input')  # 搜索框
        click_instance.send(By.XPATH, '/html/body/header/div/div[3]/form/div/input', 'C13H12Cl2N2')  # 输入分子式
        click_instance.click(By.CLASS_NAME, 'wrap-cmSearch-arrow')  # 搜索
        assert click_instance.check_element_presence(By.CSS_SELECTOR, ".wrap-danger") == True#管制类产品标识
        click_instance.click(By.XPATH, '/html/body/header/div/div[3]/form/div/input')  # 搜索框
        click_instance.send(By.XPATH, '/html/body/header/div/div[3]/form/div/input', '267.15')  # 输入分子量
        click_instance.click(By.CLASS_NAME, 'wrap-cmSearch-arrow')  # 搜索
        assert click_instance.check_element_presence(By.CSS_SELECTOR, ".wrap-danger") == True#管制类产品标识
        assert click_instance.check_element_presence(By.XPATH,'//*[@id="search-prd-box"]/div[2]/div[1]/div[1]/div[1]/img') == True#结构图
        click_instance.click(By.XPATH,'//*[@id="search-prd-box"]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/a')#点击CAS号
        xinxi = driver.find_element(By.CLASS_NAME,'prohibit-tip').text
        assert xinxi == '根据相关法律法规和政策，此化合物相关产品禁止销售！'
        click_instance.click(By.XPATH,'/html/body/div[2]/div[3]/div/a')#点击首页
        assert driver.current_url == f'{url}'
    # 普通产品搜索-简单的逻辑交互
    def test_2(self,driver):
        driver.delete_all_cookies()
        #普通产品搜索
        click_instance = Select(driver)
        driver.get(f'{url}')
        click_instance.click(By.NAME, "query")  # 首页搜索框
        click_instance.send(By.NAME, "query", "6-氨基-3,3-二甲基吲哚啉-2-酮")  # 首页中文名称搜索
        click_instance.click(By.CLASS_NAME, "wrap-search-arrow")  # 回车
        name = driver.find_element(By.XPATH,'//*[@id="search-prd-box"]/div[2]/div[1]/div[1]/div[2]/div[1]/div[3]/div[2]/a').text
        assert name == '6-氨基-3,3-二甲基吲哚啉-2-酮'
        click_instance.click(By.XPATH, '/html/body/header/div/div[3]/form/div/input')  # 搜索框
        click_instance.send(By.XPATH, '/html/body/header/div/div[3]/form/div/input', '100510-65-4')  # 输入CAS号
        click_instance.click(By.CLASS_NAME, 'wrap-cmSearch-arrow')  # 搜索
        cas = driver.find_element(By.XPATH,'//*[@id="search-prd-box"]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/a').text
        assert cas == '100510-65-4' #搜索结果页CAS号比对
        assert click_instance.check_element_presence(By.XPATH,
                                                     '//*[@id="search-prd-box"]/div[2]/div[1]/div[1]/div[2]/div[2]/a[1]') == True  # 供应商
        assert click_instance.check_element_presence(By.XPATH,
                                                     '//*[@id="search-prd-box"]/div[2]/div[1]/div[1]/div[2]/div[2]/a[2]') == True  # 化学性质
        assert click_instance.check_element_presence(By.XPATH,
                                                     '//*[@id="search-prd-box"]/div[2]/div[1]/div[1]/div[2]/div[2]/span') == True  # 图谱
        assert click_instance.check_element_presence(By.XPATH,
                                                     '//*[@id="search-prd-box"]/div[2]/div[1]/div[1]/div[2]/div[2]/a[3]') == True  # 价格
        assert click_instance.check_element_presence(By.XPATH,
                                                     '//*[@id="search-prd-box"]/div[2]/div[1]/div[1]/div[1]/img') == True  # 结构图
        click_instance.click(By.XPATH,'//*[@id="search-prd-box"]/div[2]/div[1]/div[1]/div[1]/div/a[2]')#相似结构
        driver.switch_to.window(driver.window_handles[1])#切换到结构式检索首页面
        assert f'{url}structure_search?pid=' in driver.current_url
        assert click_instance.check_element_presence(By.XPATH,'/html/body/div[3]/section/div') == True  # 存在结构式检索模块
        click_instance.click(By.XPATH, '//*[@id="form-structure-search"]/div/div[1]')  # 精准检索
        assert click_instance.check_element_presence(By.XPATH,'//*[@id="form-structure-search"]/div/div[1]/span') == True  # 存在结果
        driver.close()
        driver.switch_to.window(driver.window_handles[0])#切换到搜索结果页
        gongyingshang = driver.find_element(By.XPATH,'//*[@id="search-prd-box"]/div[2]/div[1]/div[1]/div[2]/div[2]/a[1]/span').text#供应商信息
        click_instance.click(By.XPATH,'//*[@id="search-prd-box"]/div[2]/div[1]/div[1]/div[2]/div[2]/a[1]')#进入供应商页面
        gys = driver.find_element(By.CLASS_NAME,'supplier-num').text
        assert gongyingshang in gys #搜索结果页供应商数量与供应商页面数量比对
        driver.back()
        click_instance.click(By.XPATH,'//*[@id="search-prd-box"]/div[2]/div[1]/div[1]/div[2]/div[2]/a[2]')#进入化学性质页面
        driver.switch_to.window(driver.window_handles[1])#切换到化学性质页面
        huaxue_gys = driver.find_element(By.XPATH,'/html/body/div[2]/section/div/div[1]/div[1]/div[3]/div/a[1]').text#获取供应商数量
        huaxue_gys_new = re.findall(r'\d+', huaxue_gys)#提取数字
        assert huaxue_gys_new[0] in gongyingshang #化学性质页面供应商数量与搜索结果页供应商数量比对
        assert click_instance.check_element_presence(By.XPATH,
                                                     '/html/body/div[2]/div[1]/div/div[1]/div[3]/div/a[2]') ==True #存在查看价格按钮
        assert click_instance.check_element_presence(By.CLASS_NAME,
                                                     'wrap-prdCasInfo') == True#cas号、中文同义词模块
        assert click_instance.check_element_presence(By.XPATH,
                                                     '//*[@id="basicInfo"]/div[2]') == True#基本信息
        assert click_instance.check_element_presence(By.XPATH,
                                                     '//*[@id="poperty"]/div[2]') == True#性质
        assert click_instance.check_element_presence(By.XPATH,
                                                     '//*[@id="safe"]/div[2]') == True#安全信息
        driver.switch_to.frame(driver.find_element(By.XPATH, '//*[@id="login_container"]/iframe'))#进入到iframe框
        assert click_instance.check_element_presence(By.XPATH, '//*[@id="tpl_for_iframe"]/div/div/div[2]') == True #价格模块未登录 二维码存在
        driver.switch_to.default_content()#从iframe切换到默认
        assert click_instance.check_element_presence(By.CLASS_NAME,
                                                     'content-tr-top') == True#编辑结构式
        assert click_instance.check_element_presence(By.XPATH,
                                                     '/html/body/div[2]/section/div/div[2]/div[2]/div[1]/div[2]') == True#侧边栏供应商
        assert click_instance.check_element_presence(By.CLASS_NAME,
                                                     'wrap-errorDialog') == True#信息错误报告
        click_instance.click(By.XPATH,'/html/body/div[2]/section/div/div[1]/div[1]/div[3]/div/a[1]')#点击供应商
        assert driver.current_url == f'{url}suppliers/100510-65-4'
        click_instance.click(By.CLASS_NAME,'viewMore')#查看更多
        click_instance.click(By.XPATH,'/html/body/div[2]/section/div/div[2]/div[2]/div[1]/div[2]/div[1]/a/span')#右侧查看全部供应商
        assert driver.current_url == f'{url}suppliers/100510-65-4'
        click_instance.click(By.CLASS_NAME, 'viewMore')  # 查看更多,进入化学性质页面
        gys_name = driver.find_element(By.XPATH,'/html/body/div[2]/section/div/div[2]/div[2]/div[1]/div[2]/div[2]/a').text#右侧供应商列表第一个供应商名称
        click_instance.click(By.XPATH,'/html/body/div[2]/section/div/div[2]/div[2]/div[1]/div[2]/div[2]/a')#右侧供应商列表第一个供应商
        driver.switch_to.window(driver.window_handles[2])#切换到供应商页面
        gongyingsahng_name = driver.find_element(By.XPATH,'/html/body/div/section/div[1]/div[1]/div/div[1]').text#获取供应商名称
        assert gys_name == gongyingsahng_name
        driver.close()
        driver.switch_to.window(driver.window_handles[1])#切换到化学性质页面
        click_instance.click(By.XPATH,'/html/body/div[2]/section/div/div[2]/div[1]/div')#编辑结构式
        assert '100510-65-4.mol' in driver.current_url
        assert click_instance.check_element_presence(By.XPATH,'//*[@id="form-structure-search"]/div/div[1]/span') == True  # 存在结构式检索模块
        driver.back()
        click_instance.click(By.XPATH,'/html/body/div[2]/section/div/div[1]/div[1]/div[3]/div/a[2]')#查看价格
        assert driver.current_url == f'{url}prices/100510-65-4'
        driver.close()
        driver.switch_to.window(driver.window_handles[0])#切换到搜索结果页
        click_instance.click(By.XPATH,'//*[@id="search-prd-box"]/div[2]/div[1]/div[1]/div[2]/div[2]/span')#图谱
        driver.switch_to.frame(driver.find_element(By.XPATH, '//*[@id="login_container"]/iframe'))#切换到iframe框
        assert click_instance.check_element_presence(By.XPATH,'//*[@id="tpl_for_iframe"]/div/div/div[2]/div[1]/img') == True#未登录 微信扫码
        driver.switch_to.default_content()#切换到默认
        click_instance.click(By.CLASS_NAME,'login-close')#关闭登录弹窗
        click_instance.click(By.XPATH,'//*[@id="search-prd-box"]/div[2]/div[1]/div[1]/div[2]/div[2]/a[3]')#价格
        assert driver.current_url == f'{url}prices/100510-65-4'
        driver.get(f'{url}cas/103-76-4')  # 进入化学性质页面
        click_instance.click(By.CSS_SELECTOR,
                             'div:nth-child(5) > div.content-item-right > div.content-item-value > a')  # 安全说明
        driver.switch_to.window(driver.window_handles[1])
        assert driver.current_url == f'{url}RiskAndSafety#Safety'
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        click_instance.click(By.CSS_SELECTOR,
                             'div:nth-child(8) > div.content-item-right > div.content-item-value > a')  # 危险品标识
        driver.switch_to.window(driver.window_handles[1])
        assert driver.current_url == f'{url}RiskAndSafety#hazards'
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        click_instance.click(By.CSS_SELECTOR,
                             'div.barContent.prdPropInfo-content > div:nth-child(9) > div.content-item-right > div.content-item-value > a')  # 危险类别码
        driver.switch_to.window(driver.window_handles[1])
        assert driver.current_url == f'{url}RiskAndSafety#Risk'
    # 产看产品供应商&没有海关编码的产品
    def test_2_A(self, driver):
        driver.delete_all_cookies()
        click_instance = Select(driver)
        # 产看产品供应商
        driver.get(f"{url}suppliers/100-51-6")
        cas = driver.find_element(By.XPATH, '/html/body/div[2]/section/div/div[2]/div[1]/div[2]/div/div[4]/div[2]').text
        assert cas == '100-51-6'
        wangzhi = driver.find_element(By.XPATH,
                                      '/html/body/div[2]/section/div/div[2]/div[2]/div[3]/div[9]/div[2]/div[2]/div[1]/div[2]').text
        click_instance.click(By.XPATH,
                             '/html/body/div[2]/section/div/div[2]/div[2]/div[3]/div[9]/div[2]/div[2]/div[1]/div[2]/a')  # 公司网址
        driver.switch_to.window(driver.window_handles[1])
        assert wangzhi == driver.current_url
        assert click_instance.check_element_presence(By.XPATH, '/html/body/div/section/div[3]/div[2]') == True
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        # 没有海关编码的产品
        driver.get(f'{url}search?query=5310-10-1')
        click_instance.click(By.XPATH,
                             '//*[@id="search-prd-box"]/div[2]/div[1]/div/div[2]/div[1]/div[1]/div[2]/a')  # 点击cas号,进入化学性质页面
        cas1 = driver.find_element(By.XPATH,
                                   '/html/body/div[2]/section/div/div[1]/div[1]/div[4]/div[1]/div[1]/span[2]').text
        assert cas1 == '5310-10-1'
        driver.back()
        click_instance.click(By.XPATH, '//*[@id="search-prd-box"]/div[2]/div[1]/div/div[2]/div[2]/a[1]')  # 点击化学性质
        driver.switch_to.window(driver.window_handles[1])
        cas2 = driver.find_element(By.XPATH,
                                   '/html/body/div[2]/section/div/div[1]/div[1]/div[4]/div[1]/div[1]/span[2]').text
        assert cas1 == cas2
    #查谱图-查价格
    def test_3(self,driver):
        driver.delete_all_cookies()
        click_instance = Select(driver)
        driver.get(f'{url}')
        #查谱图
        click_instance.click(By.XPATH,'/html/body/div/header/div/div[2]/div[1]/div/a[1]')#查谱图
        driver.switch_to.frame(driver.find_element(By.XPATH,'//*[@id="login_container"]/iframe'))
        assert click_instance.check_element_presence(By.XPATH,'//*[@id="tpl_for_iframe"]/div/div/div[2]') == True#未登录 二维码存在
        driver.switch_to.default_content()
        click_instance.click(By.XPATH,'/html/body/div[2]/div/div/div/div[4]/a[1]')#用户协议
        driver.switch_to.window(driver.window_handles[1])
        assert driver.current_url == f'{url}protocol/register'
        assert click_instance.check_element_presence(By.ID, 'registrationAgreement') == True  #注册协议模块
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        click_instance.click(By.XPATH, '/html/body/div[2]/div/div/div/div[4]/a[2]')  #隐私协议
        driver.switch_to.window(driver.window_handles[1])
        assert driver.current_url == f'{url}protocol/privacy'
        assert click_instance.check_element_presence(By.ID,'privacyPolicy') == True #隐私协议模块
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        #查价格
        click_instance.click(By.XPATH,'/html/body/header/div/div[2]/div/a[2]')#查价格
        click_instance.click(By.XPATH,'/html/body/div[2]/section/form/input')#查价格输入框
        click_instance.send(By.XPATH,'/html/body/div[2]/section/form/input','626-55-1')#输入CAS号
        click_instance.click(By.XPATH,'/html/body/div[2]/section/form/button')#搜索产品价格
        assert click_instance.check_element_presence(By.XPATH,'/html/body/div[4]/section/div[1]/div[1]/div[4]') == True #存在CAS号、中英文名称登
        assert click_instance.check_element_presence(By.XPATH,'/html/body/div[4]/section/div[3]/div[2]/div[2]/table/tbody/tr[1]/td[4]') == True#存在试剂参考价
        driver.switch_to.frame(driver.find_element(By.XPATH,'//*[@id="login_container"]/iframe'))
        assert click_instance.check_element_presence(By.XPATH,'//*[@id="tpl_for_iframe"]/div/div/div[2]/div[1]/img') == True #未登录，不可查看厂家价格，展示二维码
        driver.switch_to.default_content()
        cas = driver.find_element(By.XPATH,'/html/body/div[4]/section/div[1]/div[1]/div[4]/div[1]/div[1]/span[2]').text#查价格结果页获取CAS号
        assert cas == '626-55-1'
        click_instance.click(By.XPATH,'/html/body/div[4]/section/div[1]/div[1]/div[3]/div/a[1]')#产看化学性质
        hxxz_cas = driver.find_element(By.XPATH,'/html/body/div[2]/section/div/div[1]/div[1]/div[4]/div[1]/div[1]/span[2]').text #化学性质页面CAS号
        assert hxxz_cas == '626-55-1'
        driver.back()
        gongyingsahng = driver.find_element(By.XPATH,'/html/body/div[4]/section/div[1]/div[1]/div[3]/div/a[2]').text#查价格结果页获取供应商
        click_instance.click(By.XPATH,'/html/body/div[4]/section/div[1]/div[1]/div[3]/div/a[2]')#点击进入查看供应商页面
        gys = driver.find_element(By.XPATH,'/html/body/div[2]/section/div/div[2]/div[2]/div[1]/span').text#供应商数量
        newgys = re.findall('\d+',gys)
        assert newgys[0] in gongyingsahng #供应商数量比对
        driver.back()
    #海关编码
    def test_4(self, driver):
        driver.delete_all_cookies()
        click_instance = Select(driver)
        driver.get(f'{url}')
        # 海关编码
        click_instance.click(By.XPATH, '/html/body/div/header/div/div[2]/div[1]/div/a[3]')  # 海关编码
        click_instance.click(By.XPATH, '/html/body/div[2]/section/div/div[3]/a[1]/img')  # 海关商品目录
        assert click_instance.check_element_presence(By.XPATH,
                                                     '/html/body/div[2]/section/div/div[2]') == True  # 存在海关种类模块
        driver.back()
        click_instance.click(By.XPATH, '/html/body/div[2]/section/div/div[3]/a[2]/img')  # 海关监管条件码
        assert click_instance.check_element_presence(By.CLASS_NAME,
                                                     'supervision-condition-code-table') == True  # 海关监管条件代码模块
        driver.back()
        click_instance.click(By.XPATH, '/html/body/div[2]/section/div/form/input')  # 输入框
        click_instance.send(By.XPATH, '/html/body/div[2]/section/div/form/input', '100-51-6')  # 输入CAS号
        click_instance.click(By.XPATH, '/html/body/div[2]/section/div/form/button')  # 搜索
        bianma1 = driver.find_element(By.XPATH,
                                      '/html/body/div[3]/section/div/div[2]/div[1]/div[2]/div[1]/span[2]').text
        bianma2 = driver.find_element(By.XPATH, '/html/body/div[3]/section/div/table/tbody/tr/td[1]').text
        assert bianma1 == bianma2  # 海关编码比对
        cas = driver.find_element(By.XPATH,
                                  '/html/body/div[3]/section/div/div[2]/div[1]/div[2]/div[2]/div[1]/span[2]').text
        assert cas == '100-51-6'
        click_instance.click(By.XPATH, '/html/body/div[3]/section/div/table/tbody/tr/td[7]/a')  # 进入海关编码详情页面
        assert driver.current_url == f'{url}hscode/2906210000/1'
        click_instance.click(By.XPATH, '/html/body/div[2]/section/div/div[2]/div[1]/a')  # 产看更多，进入化学性质页面
        driver.switch_to.window(driver.window_handles[1])
        cas = driver.find_element(By.XPATH,
                                  '/html/body/div[2]/section/div/div[1]/div[1]/div[4]/div[1]/div[1]/span[2]').text
        assert cas == '100-51-6'
    #供应商
    def test_5(self,driver):
        driver.delete_all_cookies()
        click_instance = Select(driver)
        driver.get(f'{url}')
        click_instance.click(By.XPATH, '/html/body/div/header/div/div[2]/div[1]/div/a[4]')  # 供应商
        chanpin = driver.find_element(By.XPATH, '/html/body/div[2]/section/div/div[2]/div[1]/a[1]').text  # 第一个供应商产品名称
        click_instance.click(By.XPATH, '/html/body/div[2]/section/div/div[2]/div[1]/a[1]')  # 第一个热搜产品供应商
        gys_shuliang = driver.find_element(By.XPATH, '/html/body/div[2]/section/div/div[2]/div[2]/div[1]/span').text
        gys_shuliang_new = re.findall(r'\d+', gys_shuliang)  # 提取数字
        if gys_shuliang_new[0] != 0:
            pass
        else:
            assert False
        gys_chanpin = driver.find_element(By.XPATH,
                                          '/html/body/div[2]/section/div/div[2]/div[1]/div[1]').text  # 供应商页面，产品名称
        assert gys_chanpin in chanpin
        click_instance.click(By.CSS_SELECTOR, ' div:nth-child(5) > div > div:nth-child(2) > a')  # 安全信息，危险品标识
        assert driver.current_url == f'{url}RiskAndSafety#hazards'
        driver.back()
        # 供应商地址筛选
        driver.get(f'{url}suppliers/101-53-1?city=上海市&type=4&page=1')
        gys_shuliang_shanghai = driver.find_element(By.XPATH,
                                                    '/html/body/div[2]/section/div/div[2]/div[2]/div[1]/span').text
        assert gys_shuliang_shanghai == '（8）'
        click_instance.click(By.XPATH, '/html/body/div[2]/section/div/div[2]/div[2]/div[2]/div[2]')  # 清楚所选条件
        time.sleep(1)
        gys_shuliang_new = driver.find_element(By.XPATH, '/html/body/div[2]/section/div/div[2]/div[2]/div[1]/span').text
        assert gys_shuliang_new == '（37）'
        # 进入供应商首页
        click_instance.hover(By.XPATH,
                             '/html/body/div[2]/section/div/div[2]/div[2]/div[3]/div[1]/div[1]/div[1]')  # 悬停在第一个供应商名称上面
        assert click_instance.check_element_presence(By.XPATH,
                                                     '/html/body/div[2]/section/div/div[2]/div[2]/div[3]/div[1]/div[1]/div[1]/div/div[1]') == True  # 公司名称存在
        gys_name = driver.find_element(By.XPATH,
                                       '/html/body/div[2]/section/div/div[2]/div[2]/div[3]/div[1]/div[1]/div[1]/a').text
        click_instance.click(By.XPATH,
                             '/html/body/div[2]/section/div/div[2]/div[2]/div[3]/div[1]/div[1]/div[1]/a')  # 点击供应商名称
        driver.switch_to.window(driver.window_handles[1])  # 进入公司首页
        gys_name1 = driver.find_element(By.XPATH, '/html/body/div/section/div[1]/div[1]/div/div[1]').text  # 公司名称
        assert gys_name == gys_name1
        driver.close()
        driver.switch_to.window(driver.window_handles[0])  # 返回供应商页面
        click_instance.click(By.XPATH,
                             '/html/body/div[2]/section/div/div[2]/div[2]/div[3]/div[1]/div[2]/div[1]/div[4]/div/div[2]/a')  # 产品目录
        assert click_instance.check_element_presence(By.XPATH,
                                                     '/html/body/div/section/div[3]/div[2]') == True  # 存在商品目录
        driver.get(f'{url}suppliers')  # 进入到供应商首页面
        click_instance.click(By.XPATH, '/html/body/div[2]/section/div/div[3]/div/a[1]/button')  # 供应商索引A
        assert driver.current_url == f'{url}supplier_index/A'
        click_instance.click(By.XPATH, '/html/body/div[2]/section/div/div[4]/div/nav/ul/nav/ul/li[14]/a')  # 点击页码最后一页
        assert f'{url}supplier_index/A?page=' in driver.current_url
        index = driver.find_element(By.CLASS_NAME, 'btn-active').text
        assert index == 'A'
        click_instance.click(By.XPATH, '/html/body/div[2]/section/div/div[3]/div/a[4]/button')  # 供应商索引D
        assert driver.current_url == f'{url}supplier_index/D'
        click_instance.click(By.CLASS_NAME, 'itemContent-blue', 0)  # 第一个公司
        assert click_instance.check_element_presence(By.CLASS_NAME, 'prd-content-right') == True  # 存在产品模块
        # 供应商首页-产品目录
        driver.get(f'{url}supplier/6546')
        click_instance.click(By.XPATH, '/html/body/div/section/div[3]/div[1]/div[1]/div[2]/div/a')  # 产品目录
        assert f'{url}supplier/6546/product?cat_id=' in driver.current_url
        assert click_instance.check_element_presence(By.XPATH, '/html/body/div/section/div[3]/div[2]') == True  # 产品模块存在
        click_instance.click(By.XPATH, '/html/body/div/section/div[1]/div[2]/div/a[3]')  # 产品目录简版
        click_instance.click(By.XPATH, '/html/body/div/section/div[3]/div[1]/div[1]/div[2]/div/a')  # 产品目录
        assert f'{url}supplier/6546/productSimpify?cat_id=' in driver.current_url
        assert click_instance.check_element_presence(By.XPATH, '/html/body/div/section/div[3]/div[2]') == True  # 产品模块存在
    #结构式检索
    def test_6(self,driver):
        driver.delete_all_cookies()
        click_instance = Select(driver)
        driver.get(f'{url}search?query=118-55-8')
        click_instance.click(By.XPATH,'//*[@id="search-prd-box"]/div[2]/div[1]/div[1]/div[2]/div[2]/a[2]')#点击化学性质
        driver.switch_to.window(driver.window_handles[1])
        cas = driver.find_element(By.XPATH,'/html/body/div[2]/section/div/div[1]/div[1]/div[4]/div[1]/div[1]/span[2]').text
        click_instance.click(By.XPATH,'/html/body/div[2]/section/div/div[2]/div[1]/div')#编辑结构式
        assert cas in driver.current_url
        time.sleep(1)
        click_instance.click(By.XPATH,'//*[@id="form-structure-search"]/div/div[1]/span')#精准匹配
        jgs_cas = driver.find_element(By.XPATH,'//*[@id="search-prd-box"]/div[2]/div[1]/div/div[2]/div[1]/div[1]/div[2]/a').text
        assert jgs_cas == cas
        driver.back()
        time.sleep(1)
        click_instance.click(By.XPATH,'//*[@id="form-structure-search"]/div/div[2]/span')#子结构
        assert click_instance.check_element_presence(By.XPATH,'//*[@id="search-prd-box"]/div[2]/div[1]') == True  # 存在搜索结果模块
        driver.back()
        time.sleep(1)
        click_instance.click(By.XPATH, '//*[@id="form-structure-search"]/div/div[3]/span')  # 相似度检索
        assert click_instance.check_element_presence(By.XPATH,'//*[@id="search-prd-box"]/div[2]/div[1]') == True  # 存在搜索结果模块
    #化工字典、问答
    def test_7(self, driver):
        driver.delete_all_cookies()
        click_instance = Select(driver)
        driver.get(f'{url}')
        # 化工字典
        click_instance.click(By.CSS_SELECTOR, 'div > a:nth-child(5)')  # 化工字典
        click_instance.click(By.XPATH, '/html/body/div[2]/section/div/div[3]/div[1]/div[2]/a[1]/button')  # 点击产品名称A
        assert driver.current_url == f'{url}chem_dict/product_name_start_with_A'
        click_instance.click(By.XPATH, '/html/body/div[2]/section/div/div[4]/nav/ul/nav/ul/li[14]/a')  # 点击页码最后一页
        assert f'{url}chem_dict/product_name_start_with_A?page=' in driver.current_url
        index = driver.find_element(By.CLASS_NAME, 'btn-active').text  # 产品名称索引
        assert index == 'A'
        click_instance.click(By.XPATH, '/html/body/div[2]/section/div/div[2]/div[1]/div[2]/a[26]/button')  # 点击产品名称Z
        assert driver.current_url == f'{url}chem_dict/product_name_start_with_Z'
        click_instance.click(By.XPATH, '/html/body/div[2]/section/div/div[4]/nav/ul/nav/ul/li[14]/a')  # 点击页码最后一页
        index = driver.find_element(By.CLASS_NAME, 'btn-active').text  # 产品名称索引
        assert index == 'Z'
        click_instance.click(By.XPATH, '/html/body/div[2]/section/div/div[2]/div[2]/div[2]/a[1]/button')  # 点击cas号1
        assert driver.current_url == f'{url}chem_dict/cas_start_with_1'
        click_instance.click(By.XPATH, '/html/body/div[2]/section/div/div[4]/nav/ul/nav/ul/li[14]/a')  # 点击页码最后一页
        index = driver.find_element(By.CLASS_NAME, 'btn-active').text  # 产品名称索引
        assert index == '1'
        click_instance.click(By.XPATH, '/html/body/div[2]/section/div/div[2]/div[2]/div[2]/a[9]/button')  # 点击cas号9
        assert driver.current_url == f'{url}chem_dict/cas_start_with_9'
        click_instance.click(By.XPATH, '/html/body/div[2]/section/div/div[4]/nav/ul/nav/ul/li[14]/a')  # 点击页码最后一页
        index = driver.find_element(By.CLASS_NAME, 'btn-active').text  # 产品名称索引
        assert index == '9'
        # 问答
        click_instance.click(By.XPATH, '/html/body/header/div/div[2]/div/a[6]')  # 问答
        click_instance.click(By.XPATH, '//*[@id="a_ask"]')  # 我要提问
        driver.switch_to.frame(driver.find_element(By.XPATH,'//*[@id="login_container"]/iframe'))
        assert click_instance.check_element_presence(By.XPATH, '//*[@id="tpl_for_iframe"]/div/div/div[2]/div[1]/img') == True  # 未登录 二维码
        driver.back()
        click_instance.send(By.XPATH, '//*[@id="input_search_question"]', '什么是合成试剂')
        click_instance.click(By.XPATH, '//*[@id="a_search_question"]/input')  # 搜索答案
        click_instance.click(By.XPATH, '/html/body/div[4]/section/div/ul/li/a')  # 问题
        assert click_instance.check_element_presence(By.XPATH, '//*[@id="editMyAnser"]') == True  # 我来回答按钮
        assert click_instance.check_element_presence(By.XPATH,
                                                     '/html/body/div[3]/section/div/div/div[2]/div[2]') == True  # 等你来答模块
        click_instance.click(By.CSS_SELECTOR, 'div.header-left > div > a:nth-child(6)')  # 问答
        click_instance.click(By.XPATH,
                             '/html/body/div[2]/section/div/div[3]/div[1]/div[2]/ul/li[1]/a/div')  # 点击最新问题
        assert click_instance.check_element_presence(By.XPATH, '//*[@id="editMyAnser"]') == True  # 我来回答按钮
        assert click_instance.check_element_presence(By.XPATH,
                                                     '/html/body/div[3]/section/div/div/div[2]/div[2]') == True  # 等你来答模块
        driver.back()
        click_instance.click(By.XPATH,
                             '/html/body/div[2]/section/div/div[3]/div[2]/div[2]/ul/li[1]/a/div[1]/div')  # 点击大家热议
        assert click_instance.check_element_presence(By.XPATH, '//*[@id="editMyAnser"]') == True  # 我来回答按钮
        assert click_instance.check_element_presence(By.XPATH,
                                                     '/html/body/div[3]/section/div/div/div[2]/div[2]') == True  # 等你来答模块
    #搜索不存在的情况
    def test_8(self, driver):
        driver.delete_all_cookies()
        click_instance = Select(driver)
        driver.get(f'{url}')
        # 搜索
        click_instance.click(By.NAME, "query")  # 首页搜索框
        click_instance.send(By.NAME, "query", "1970129-05-5")  # 首页CAS号搜索
        click_instance.click(By.CLASS_NAME, "wrap-search-arrow")  # 搜索
        wenben = driver.find_element(By.CLASS_NAME, 'null-result').text
        assert wenben == '抱歉，没有找到"1970129-05-5"相关的内容~'
        click_instance.click(By.XPATH, '/html/body/header/div/div[3]/form/div/input')  # 搜索结果页顶部搜索框
        click_instance.send(By.XPATH, '/html/body/header/div/div[3]/form/div/input', '大萨达是的撒')  # 乱输入
        click_instance.click(By.XPATH, '/html/body/header/div/div[3]/form/div/button')  # 搜索
        wenben = driver.find_element(By.CLASS_NAME, 'null-result').text
        assert wenben == '抱歉，没有查询到结果哦~'
        # 化学性质
        driver.get(f'{url}cas/801303-22-111')
        wenben = driver.find_element(By.CLASS_NAME, 'null-result').text
        assert wenben == '抱歉，您访问的页面无法显示或已不存在。'
        # 查价格
        driver.get(f'{url}prices?query=火锅店方便')
        wenben = driver.find_element(By.CLASS_NAME, 'null-result').text
        assert wenben == '抱歉，没有查询到结果哦~'
        # 海关编码
        driver.get(f'{url}hscode?query=废物费')
        wenben = driver.find_element(By.CLASS_NAME, 'null-result').text
        assert wenben == '抱歉，没有查询到结果哦~'
        # 供应商
        driver.get(f'{url}supplier/11111111')
        wenben = driver.find_element(By.CLASS_NAME, 'null-result').text
        assert wenben == '抱歉，您访问的页面无法显示或已不存在。'
        # 问答
        driver.get(f'{url}questions/1111111111111')
        wenben = driver.find_element(By.CLASS_NAME, 'null-result').text
        assert wenben == '抱歉，您访问的页面无法显示或已不存在。'








