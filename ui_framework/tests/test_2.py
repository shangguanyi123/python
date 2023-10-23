#encoding=utf-8
import re
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from sql import MySQLHelper
from conftest import Select,url

db = MySQLHelper()
#未登录
class TestUi():
    #查价格
    def test_01(self,driver):
        driver.delete_all_cookies()
    #查图谱
    def test_02(self,driver):
        driver.delete_all_cookies()
        click_instance = Select(driver)
        #搜索结果页
        driver.get(f'{url}search?query=100-01-6')
        click_instance.click(By.XPATH, '//*[@id="search-prd-box"]/div[2]/div[1]/div/div[2]/div[2]/span')
        assert click_instance.check_element_presence(By.XPATH,'/html/body/div/div/div') == True,'账号登录页面不存在'
        driver.back()
        #化学性质页面
        click_instance.click(By.XPATH,'//*[@id="search-prd-box"]/div[2]/div[1]/div/div[2]/div[2]/a[3]')
        driver.switch_to.window(driver.window_handles[1])
        assert driver.current_url == f'{url}cas/100-01-6'
        click_instance.click(By.XPATH,'//*[@id="spectrogram"]/div[2]/div/div/div[2]/div[2]/a')
        assert click_instance.check_element_presence(By.XPATH, '/html/body/div/div/div') == True,'账号登录页面不存在'
        driver.back()
        click_instance.click(By.CLASS_NAME,'pointer')
        driver.switch_to.window(driver.window_handles[2])
        assert click_instance.check_element_presence(By.XPATH, '/html/body/div/div/div') == True,'账号登录页面不存在'
    #问答
    def test_03(self,driver):
        driver.delete_all_cookies()
        click_instance = Select(driver)
        driver.get(f'{url}questions')
        click_instance.click(By.ID,'a_ask')
        assert click_instance.check_element_presence(By.XPATH, '/html/body/div/div/div') == True,'账号登录页面不存在'
    #供应商列表感兴趣
    def test_04(self,driver):
        driver.delete_all_cookies()
        click_instance = Select(driver)
        driver.get(f'{url}suppliers/42895-58-9')
        click_instance.click(By.XPATH,'/html/body/div/section/div/div[2]/div[2]/div[3]/div[1]/div[2]/div[1]/div[2]/div/div[1]')
        assert click_instance.check_element_presence(By.CLASS_NAME,'alert-msg') == True,'未提示登录'









