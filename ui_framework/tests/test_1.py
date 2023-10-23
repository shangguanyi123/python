# encoding=utf-8
import json
import re
import time
import pytest,requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from sql import MySQLHelper, MySQLHelper_cookies
from conftest import Select,url,update_cookies


db = MySQLHelper()
db_cookies = MySQLHelper_cookies()
# 登录
class TestUi():

    # 产品搜索
    def test_01(self,driver):
        click_instance = Select(driver)
        #英文名称搜索
        Product_Name = '5-Amino-2-[(4-aminophenyl)amino]benzenesulfonic acid'
        driver.get(f"{url}search?query={Product_Name}")
        name = driver.find_element(By.CLASS_NAME,'itemContent-red').text
        assert name == Product_Name
        #英文同义词
        Product_Name = '4,4-DIAMINO DIPHENYL-2-SULPHONIC ACID'
        driver.get(f"{url}search?query={Product_Name}")
        name = driver.find_element(By.CLASS_NAME, 'itemContent-red').text
        assert name == Product_Name
        # cas号
        cas = '11021-13-9'
        driver.get(f"{url}search?query={cas}")
        name = driver.find_element(By.CLASS_NAME, 'itemContent-red').text
        assert name == cas
        # 分子式
        mf = 'C53H90O22'
        driver.get(f"{url}search?query={mf}")
        name = driver.find_element(By.CLASS_NAME, 'itemContent-red').text
        assert name == mf
        # 分子量
        mw = '1079.27'
        driver.get(f"{url}search?query={mw}")
        name = driver.find_element(By.CLASS_NAME, 'itemContent-red').text
        assert name == mw
        # mdl
        mdl = 'MFCD00041836'
        driver.get(f"{url}search?query={mdl}")
        name = driver.find_element(By.CLASS_NAME, 'itemContent-red').text
        assert name == mdl
        # einecs号
        einecs = '203-661-5'
        driver.get(f"{url}search?query={einecs}")
        name = driver.find_element(By.XPATH, '//*[@id="search-prd-box"]/div[2]/div[1]/div/div[2]/div[1]/div[2]/div[2]/a').text
        assert name == '109-28-4'
        # cas号去-
        cas_ = '11021139'
        driver.get(f"{url}search?query={cas_}")
        name = driver.find_element(By.CLASS_NAME, 'itemContent-red').text
        assert name == cas_
        # einecs去-
        einecs_ = '2036615'
        driver.get(f"{url}search?query={einecs_}")
        name = driver.find_element(By.XPATH, '//*[@id="search-prd-box"]/div[2]/div[1]/div/div[2]/div[1]/div[2]/div[2]/a').text
        assert name == '109-28-4'
        # cas号模糊搜索
        cas_ = '1797-93'
        driver.get(f"{url}search?query={cas_}")
        assert click_instance.check_element_presence(By.XPATH,'//*[@id="search-prd-box"]/div[2]') == True
        # einecs号模糊搜素
        einecs_ = '203-661'
        driver.get(f"{url}search?query={einecs_}")
        assert click_instance.check_element_presence(By.XPATH, '//*[@id="search-prd-box"]/div[2]') == True
        # cas号中包含特殊字符
        cas = '203661-66-9'
        driver.get(f"{url}search?query=203661、-66-9")
        name = driver.find_element(By.XPATH,'//*[@id="search-prd-box"]/div[2]/div[1]/div/div[2]/div[1]/div[2]/div[2]/a').text
        assert name == cas
        driver.get(f"{url}search?query=20-3661-66-9")
        name = driver.find_element(By.XPATH,'//*[@id="search-prd-box"]/div[2]/div[1]/div/div[2]/div[1]/div[2]/div[2]/a').text
        assert name == cas
        # einecs号包含特殊字符
        cas = '19932-26-4'
        driver.get(f"{url}search?query=243、-431-1")
        name = driver.find_element(By.XPATH,'//*[@id="search-prd-box"]/div[2]/div[1]/div/div[2]/div[1]/div[2]/div[2]/a').text
        assert name == cas
        update_cookies(driver,'user1')
    # 谱图搜索
    def test_02(self,driver):
        click_instance = Select(driver)
        # 英文名称搜索
        Product_Name = '3-(2,2,3,3-TETRAFLUOROPROPOXY)-1,2-EPOXYPROPANE'
        driver.get(f"{url}spectra?query={Product_Name}")
        name = driver.find_element(By.XPATH, '/html/body/div[3]/section/div[1]/div[1]/div[4]/div[1]/div[1]/span[2]').text
        assert name == '19932-26-4'
        assert click_instance.check_element_presence(By.CLASS_NAME,'spectrogram-img-item') == True
        # 英文同义词
        Product_Name = '4,7-Dibromobenzo-2'
        driver.get(f"{url}spectra?query={Product_Name}")
        name = driver.find_element(By.XPATH, '/html/body/div[3]/section/div[1]/div[1]/div[4]/div[1]/div[1]/span[2]').text
        assert name == '15155-41-6','cas号不符'
        assert click_instance.check_element_presence(By.XPATH,'/html/body/div[3]/section/div[2]/div[2]/div/div[1]/img') == True,'谱图不存在'
        # cas号
        cas = '19932-26-4'
        driver.get(f"{url}spectra?query={cas}")
        name = driver.find_element(By.XPATH, '/html/body/div[3]/section/div[1]/div[1]/div[4]/div[1]/div[1]/span[2]').text
        assert name == cas,'cas号不符'
        assert click_instance.check_element_presence(By.XPATH,'/html/body/div[3]/section/div[2]/div[2]/div/div[1]/img') == True, '谱图不存在'
        # 分子式
        mf = 'C6H8F4O2'
        driver.get(f"{url}spectra?query={mf}")
        name = driver.find_element(By.XPATH,'/html/body/div[3]/section/div[1]/div[1]/div[4]/div[1]/div[1]/span[2]').text
        assert name == '19932-26-4','cas号不符'
        assert click_instance.check_element_presence(By.XPATH,'/html/body/div[3]/section/div[2]/div[2]/div/div[1]/img') == True, '谱图不存在'
        # 分子量
        mw = '471.42'
        driver.get(f"{url}spectra?query={mw}")
        assert click_instance.check_element_presence(By.CLASS_NAME,'wrap-content') == True
        assert click_instance.check_element_presence(By.XPATH,'/html/body/div[3]/section/div[2]/div[2]/div/div[1]/img') == True, '谱图不存在'
        # mdl
        mdl = 'MFCD00054682'
        driver.get(f"{url}spectra?query={mdl}")
        name = driver.find_element(By.XPATH,'/html/body/div[3]/section/div[1]/div[1]/div[4]/div[1]/div[1]/span[2]').text
        assert name == '19932-26-4','cas号不符'
        assert click_instance.check_element_presence(By.XPATH,'/html/body/div[3]/section/div[2]/div[2]/div/div[1]/img') == True, '谱图不存在'
        # einecs号
        einecs = '629-084-2'
        driver.get(f"{url}spectra?query={einecs}")
        name = driver.find_element(By.XPATH,'/html/body/div[3]/section/div[1]/div[1]/div[4]/div[1]/div[1]/span[2]').text
        assert name == '15155-41-6','cas号不符'
        assert click_instance.check_element_presence(By.XPATH,'/html/body/div[3]/section/div[2]/div[2]/div/div[1]/img') == True, '谱图不存在'
        # cas号去-
        cas_ = '19932264'
        driver.get(f"{url}spectra?query={cas_}")
        name = driver.find_element(By.XPATH,'/html/body/div[3]/section/div[1]/div[1]/div[4]/div[1]/div[1]/span[2]').text
        assert name == '19932-26-4','cas号不符'
        assert click_instance.check_element_presence(By.XPATH,'/html/body/div[3]/section/div[2]/div[2]/div/div[1]/img') == True, '谱图不存在'
        # einecs去-
        einecs_ = '2434311'
        driver.get(f"{url}spectra?query={einecs_}")
        name = driver.find_element(By.XPATH, '/html/body/div[3]/section/div[1]/div[1]/div[4]/div[1]/div[1]/span[2]').text
        assert name == '19932-26-4'
        assert click_instance.check_element_presence(By.XPATH,'/html/body/div[3]/section/div[2]/div[2]/div/div[1]/img') == True, '谱图不存在'
        # cas号模糊搜索
        cas_ = '19932-26'
        driver.get(f"{url}spectra?query={cas_}")
        name = driver.find_element(By.XPATH,'/html/body/div[3]/section/div[1]/div[1]/div[4]/div[1]/div[1]/span[2]').text
        assert name == '19932-26-4','cas号不符'
        assert click_instance.check_element_presence(By.XPATH,'/html/body/div[3]/section/div[2]/div[2]/div/div[1]/img') == True, '谱图不存在'
        # einecs号模糊搜素
        einecs_ = '243-431'
        driver.get(f"{url}spectra?query={einecs_}")
        name = driver.find_element(By.XPATH,'/html/body/div[3]/section/div[1]/div[1]/div[4]/div[1]/div[1]/span[2]').text
        assert name == '19932-26-4','cas号不符'
        assert click_instance.check_element_presence(By.XPATH,'/html/body/div[3]/section/div[2]/div[2]/div/div[1]/img') == True, '谱图不存在'
        # cas号包含特色字符
        cas = '19932-26-4'
        driver.get(f"{url}spectra?query=19932、-26-4")
        name = driver.find_element(By.XPATH,'/html/body/div[3]/section/div[1]/div[1]/div[4]/div[1]/div[1]/span[2]').text
        assert name == '19932-26-4','cas号不符'
        assert click_instance.check_element_presence(By.XPATH,'/html/body/div[3]/section/div[2]/div[2]/div/div[1]/img') == True, '谱图不存在'
        driver.get(f"{url}spectra?query=199-32-26-4")
        name = driver.find_element(By.XPATH,'/html/body/div[3]/section/div[1]/div[1]/div[4]/div[1]/div[1]/span[2]').text
        assert name == '19932-26-4','cas号不符'
        assert click_instance.check_element_presence(By.XPATH,'/html/body/div[3]/section/div[2]/div[2]/div/div[1]/img') == True, '谱图不存在'
        # einecs号中包含特殊字符
        driver.get(f"{url}spectra?query=243、-431-1")
        name = driver.find_element(By.XPATH,'/html/body/div[3]/section/div[1]/div[1]/div[4]/div[1]/div[1]/span[2]').text
        assert name == '19932-26-4','cas号不符'
        assert click_instance.check_element_presence(By.XPATH,'/html/body/div[3]/section/div[2]/div[2]/div/div[1]/img') == True, '谱图不存在'
        # driver.get(f"{url}spectra?query=24-3-431-1")
        # name = driver.find_element(By.XPATH,'/html/body/div[3]/section/div[1]/div[1]/div[4]/div[1]/div[1]/span[2]').text
        # assert name == '19932-26-4'
    # 价格搜索
    def test_03(self,driver):
        click_instance = Select(driver)
        # 英文名称搜索
        Product_Name = '3-(2,2,3,3-TETRAFLUOROPROPOXY)-1,2-EPOXYPROPANE'
        driver.get(f"{url}prices?query={Product_Name}")
        name = driver.find_element(By.XPATH,'/html/body/div[2]/div/div[1]/div[1]/div[3]/div[1]/div[1]/span[2]').text
        assert name == '19932-26-4','cas号不符'
        assert click_instance.check_element_presence(By.CLASS_NAME, 'price-table') == True,'价格不存在'
        # 英文同义词
        Product_Name = '4,7-Dibromo-2,1,3-Benzothidiazole'
        driver.get(f"{url}prices?query={Product_Name}")
        name = driver.find_element(By.XPATH,'/html/body/div[2]/div/div[1]/div[1]/div[3]/div[1]/div[1]/span[2]').text
        assert name == '15155-41-6', 'cas号不符'
        assert click_instance.check_element_presence(By.CLASS_NAME, 'price-table') == True, '价格不存在'
        # cas号
        cas = '19932-26-4'
        driver.get(f"{url}prices?query={cas}")
        name = driver.find_element(By.XPATH,'/html/body/div[2]/div/div[1]/div[1]/div[3]/div[1]/div[1]/span[2]').text
        assert name == cas, 'cas号不符'
        assert click_instance.check_element_presence(By.CLASS_NAME, 'price-table') == True, '价格不存在'
        # 分子式
        mf = 'C6H8F4O2'
        driver.get(f"{url}prices?query={mf}")
        name = driver.find_element(By.XPATH,'/html/body/div[2]/div/div[1]/div[1]/div[3]/div[1]/div[1]/span[2]').text
        assert name == '19932-26-4', 'cas号不符'
        assert click_instance.check_element_presence(By.CLASS_NAME, 'price-table') == True, '价格不存在'
        # 分子量
        mw = '471.42'
        driver.get(f"{url}prices?query={mw}")
        assert click_instance.check_element_presence(By.CLASS_NAME, 'wrap-content') == True
        assert click_instance.check_element_presence(By.CLASS_NAME, 'price-table') == True, '价格不存在'
        # mdl
        mdl = 'MFCD00054682'
        driver.get(f"{url}prices?query={mdl}")
        name = driver.find_element(By.XPATH,'/html/body/div[2]/div/div[1]/div[1]/div[3]/div[1]/div[1]/span[2]').text
        assert name == '19932-26-4', 'cas号不符'
        assert click_instance.check_element_presence(By.CLASS_NAME, 'price-table') == True, '价格不存在'
        # einecs号
        einecs = '629-084-2'
        driver.get(f"{url}prices?query={einecs}")
        name = driver.find_element(By.XPATH,'/html/body/div[2]/div/div[1]/div[1]/div[3]/div[1]/div[1]/span[2]').text
        assert name == '15155-41-6', 'cas号不符'
        assert click_instance.check_element_presence(By.CLASS_NAME, 'price-table') == True, '价格不存在'
        # cas号去-
        cas_ = '19932264'
        driver.get(f"{url}prices?query={cas_}")
        name = driver.find_element(By.XPATH,'/html/body/div[2]/div/div[1]/div[1]/div[3]/div[1]/div[1]/span[2]').text
        assert name == '19932-26-4', 'cas号不符'
        assert click_instance.check_element_presence(By.CLASS_NAME, 'price-table') == True, '价格不存在'
        # einecs去-
        einecs_ = '6290842'
        driver.get(f"{url}prices?query={einecs_}")
        name = driver.find_element(By.XPATH,'/html/body/div[2]/div/div[1]/div[1]/div[3]/div[1]/div[1]/span[2]').text
        assert name == '15155-41-6'
        assert click_instance.check_element_presence(By.CLASS_NAME, 'price-table') == True, '价格不存在'
        # cas号模糊搜索
        cas_ = '19932-26'
        driver.get(f"{url}prices?query={cas_}")
        name = driver.find_element(By.XPATH,'/html/body/div[2]/div/div[1]/div[1]/div[3]/div[1]/div[1]/span[2]').text
        assert name == '19932-26-4', 'cas号不符'
        assert click_instance.check_element_presence(By.CLASS_NAME, 'price-table') == True, '价格不存在'
        # einecs号模糊搜素
        einecs_ = '243-431'
        driver.get(f"{url}prices?query={einecs_}")
        name = driver.find_element(By.XPATH,'/html/body/div[2]/div/div[1]/div[1]/div[3]/div[1]/div[1]/span[2]').text
        assert name == '19932-26-4', 'cas号不符'
        assert click_instance.check_element_presence(By.CLASS_NAME, 'price-table') == True, '价格不存在'
        # cas号包含特色字符
        cas = '19932-26-4'
        driver.get(f"{url}prices?query=19932、-26-4")
        name = driver.find_element(By.XPATH,'/html/body/div[2]/div/div[1]/div[1]/div[3]/div[1]/div[1]/span[2]').text
        assert name == '19932-26-4', 'cas号不符'
        assert click_instance.check_element_presence(By.CLASS_NAME, 'price-table') == True, '价格不存在'
        driver.get(f"{url}prices?query=199-32-26-4")
        name = driver.find_element(By.XPATH,'/html/body/div[2]/div/div[1]/div[1]/div[3]/div[1]/div[1]/span[2]').text
        assert name == '19932-26-4', 'cas号不符'
        assert click_instance.check_element_presence(By.CLASS_NAME, 'price-table') == True, '价格不存在'
        # einecs号中包含特殊字符
        driver.get(f"{url}prices?query=243、-431-1")
        name = driver.find_element(By.XPATH,'/html/body/div[2]/div/div[1]/div[1]/div[3]/div[1]/div[1]/span[2]').text
        assert name == '19932-26-4', 'cas号不符'
        assert click_instance.check_element_presence(By.CLASS_NAME, 'price-table') == True, '价格不存在'
        # driver.get(f"{url}prices?query=24-3-431-1")
        # name = driver.find_element(By.XPATH,'/html/body/div[2]/div/div[1]/div[1]/div[3]/div[1]/div[1]/span[2]').text
        # assert name == '19932-26-4'
    # msds搜索
    def test_04(self,driver):
        click_instance = Select(driver)
        #cas号搜索
        driver.get(f'{url}msds?query=100-01-6')
        cas = driver.find_element(By.XPATH,'/html/body/div[1]/section/div/div[1]/div[1]/div[3]/div[1]/div[1]/span[2]').text
        assert cas == '100-01-6'
        assert click_instance.check_element_presence(By.CLASS_NAME,'wrap-msds') == True,'msds不存在'
        assert click_instance.check_element_presence(By.CLASS_NAME,'down-msds-btn') == True
        click_instance.click(By.XPATH,'/html/body/div[1]/section/div/div[2]/div[2]/div[1]/a')
        driver.switch_to.window(driver.window_handles[1])
        assert driver.current_url == f'{url}msds/pdf/100-01-6_8052'
        #英文名称搜索
        driver.get(f'{url}msds?query=p-Anisic acid')
        cas = driver.find_element(By.XPATH,'/html/body/div[1]/section/div/div[1]/div[1]/div[3]/div[1]/div[1]/span[2]').text
        assert cas == '100-09-4'
        assert click_instance.check_element_presence(By.CLASS_NAME, 'wrap-msds') == True, 'msds不存在'
        assert click_instance.check_element_presence(By.CLASS_NAME, 'down-msds-btn') == True
        #英文同义词搜索
        driver.get(f'{url}msds?query=p-NITROANILINE extrapure')
        cas = driver.find_element(By.XPATH,'/html/body/div[1]/section/div/div[1]/div[1]/div[3]/div[1]/div[1]/span[2]').text
        assert cas == '100-01-6'
        assert click_instance.check_element_presence(By.CLASS_NAME, 'wrap-msds') == True, 'msds不存在'
        assert click_instance.check_element_presence(By.CLASS_NAME, 'down-msds-btn') == True
        #einecs搜索
        driver.get(f'{url}msds?query=202-818-5')
        cas = driver.find_element(By.XPATH,'/html/body/div[1]/section/div/div[1]/div[1]/div[3]/div[1]/div[1]/span[2]').text
        assert cas == '100-09-4'
        assert click_instance.check_element_presence(By.CLASS_NAME, 'wrap-msds') == True, 'msds不存在'
        assert click_instance.check_element_presence(By.CLASS_NAME, 'down-msds-btn') == True
        #cas号去-
        driver.get(f'{url}msds?query=999815')
        cas = driver.find_element(By.XPATH,'/html/body/div[1]/section/div/div[1]/div[1]/div[3]/div[1]/div[1]/span[2]').text
        assert cas == '999-81-5'
        assert click_instance.check_element_presence(By.CLASS_NAME, 'wrap-msds') == True, 'msds不存在'
        assert click_instance.check_element_presence(By.CLASS_NAME, 'down-msds-btn') == True
        #einecs号去-
        driver.get(f'{url}msds?query=2028185')
        cas = driver.find_element(By.XPATH,'/html/body/div[1]/section/div/div[1]/div[1]/div[3]/div[1]/div[1]/span[2]').text
        assert cas == '100-09-4'
        assert click_instance.check_element_presence(By.CLASS_NAME, 'wrap-msds') == True, 'msds不存在'
        assert click_instance.check_element_presence(By.CLASS_NAME, 'down-msds-btn') == True
    # 搜索不存在的情况
    def test_05(self,driver):
        click_instance = Select(driver)
        #产品搜索
        driver.get(f'{url}search?query=ewrew')
        info = driver.find_element(By.CLASS_NAME,'null-result ').text
        assert info == 'Sorry, there is no query result.'
        #谱图搜索
        driver.get(f'{url}spectra?query=//')
        info = driver.find_element(By.CLASS_NAME, 'null-result ').text
        assert info == 'Sorry, no result was found'
            #无谱图
        driver.get(f'{url}spectra?query=PB-313')
        assert click_instance.check_element_presence(By.XPATH,'/html/body/div[3]/section/div[2]/div[2]/img') == True
        info = driver.find_element(By.CLASS_NAME, 'null-result ').text
        assert  'Sorry, nothing for "' in info
        #价格搜索
        driver.get(f'{url}prices?query=、、')
        info = driver.find_element(By.CLASS_NAME, 'null-result ').text
        assert info == 'Sorry, no result was found'
            #化学性质页面
        driver.get(f'{url}cas/10090-61-6')
        # if click_instance.check_element_presence(By.ID,'price') == True :
        #     assert False,'无价格产品，展示了价格模块'
        #msds搜索
        driver.get(f'{url}msds?query=qweqwe')
        info = driver.find_element(By.CLASS_NAME, 'null-result ').text
        assert info == 'Sorry, nothing for "qweqwe" was found.'
    # 供应商数量比对
    def test_06(self,driver):
        click_instance = Select(driver)
        #搜索结果页进入供应商页面
        driver.get(f'{url}search?query=100-01-6')
        search_gys_shuliang = driver.find_element(By.CLASS_NAME,'supplier-num').text
        click_instance.click(By.XPATH,'//*[@id="search-prd-box"]/div[2]/div[1]/div/div[2]/div[2]/a[1]')
        assert driver.current_url == f'{url}suppliers/100-01-6'
        Supplier_shuliang = driver.find_element(By.CLASS_NAME,'supplier-num').text
        assert search_gys_shuliang in Supplier_shuliang,'搜索结果页与供应商列表页面供应商数量不一致'
        #化学性质页面进入供应商页面
        driver.get(f'{url}cas/100-01-6')
            #上方入口
        cas_gys_shuliang = driver.find_element(By.CLASS_NAME, 'supplier-num').text
        cas_gys_shuliang_new = re.findall(r'\d+', cas_gys_shuliang)
        click_instance.click(By.CLASS_NAME, 'supplier-num')
        assert driver.current_url == f'{url}suppliers/100-01-6'
        Supplier_shuliang = driver.find_element(By.CLASS_NAME, 'supplier-num').text
        #assert cas_gys_shuliang in Supplier_shuliang, '化学性质页面与供应商列表页面供应商数量不一致'
        driver.back()
            #右侧入口
        click_instance.click(By.CLASS_NAME,'view-moreSupplier')
        assert driver.current_url == f'{url}suppliers/100-01-6'
        #查价格页面进入供应商页面
        driver.get(f'{url}prices?query=100-01-6')
        price_gys_shuliang = driver.find_element(By.CLASS_NAME, 'view-price').text
        price_gys_shuliang_new = re.findall(r'\d+',price_gys_shuliang)
        click_instance.click(By.CLASS_NAME, 'view-price')
        assert driver.current_url == f'{url}suppliers/100-01-6'
        Supplier_shuliang = driver.find_element(By.CLASS_NAME, 'supplier-num').text
        assert price_gys_shuliang_new[0] in Supplier_shuliang, '查价格页面与供应商列表页面供应商数量不一致'
        #查谱图页面进入供应商页面
        driver.get(f'{url}spectra?query=100-01-6')
        spectra_gys_shuliang = driver.find_element(By.CLASS_NAME, 'view-price').text
        spectra_gys_shuliang_new = re.findall(r'\d+', spectra_gys_shuliang)
        click_instance.click(By.CLASS_NAME, 'view-price')
        assert driver.current_url == f'{url}suppliers/100-01-6'
        Supplier_shuliang = driver.find_element(By.CLASS_NAME, 'supplier-num').text
        assert spectra_gys_shuliang_new[0] in Supplier_shuliang, '查谱图页面与供应商列表页面供应商数量不一致'
        # #查msds页面进入供应商页面
        driver.get(f'{url}msds?query=100-01-6')
        msds_gys_shuliang = driver.find_element(By.CLASS_NAME, 'supplier-num').text
        msds_gys_shuliang_new = re.findall(r'\d+', msds_gys_shuliang)
        click_instance.click(By.XPATH, '/html/body/div[1]/section/div/div[1]/div[1]/div[2]/div/span[1]/a')
        assert driver.current_url == f'{url}suppliers/100-01-6'
        Supplier_shuliang = driver.find_element(By.CLASS_NAME, 'supplier-num').text
        assert msds_gys_shuliang_new[0] in Supplier_shuliang, '查msds页面与供应商列表页面供应商数量不一致'
    # 查看化学性质入口
    def test_07(self,driver):
        click_instance = Select(driver)
        #搜索结果页进入化学性质页面
        driver.get(f'{url}search?query=100-01-6')
        click_instance.click(By.XPATH,'//*[@id="search-prd-box"]/div[2]/div[1]/div/div[2]/div[2]/a[3]')
        driver.switch_to.window(driver.window_handles[1])
        assert driver.current_url == f'{url}cas/100-01-6'
        assert click_instance.check_element_presence(By.ID, 'basicInfo') == True, '基本信息谱图不存在'
        assert click_instance.check_element_presence(By.ID, 'poperty') == True, '化学性质不存在'
        assert click_instance.check_element_presence(By.ID, 'purpose') == True, '用途和用法不存在'
        assert click_instance.check_element_presence(By.ID,'spectrogram') == True,'谱图不存在'
        assert click_instance.check_element_presence(By.ID, 'msds') == True, 'msds不存在'
        assert click_instance.check_element_presence(By.ID, 'price') == True, '价格不存在'
        assert click_instance.check_element_presence(By.ID, 'safe') == True, '安全信息不存在'
        #查谱图页面进入化学性质页面
        driver.get(f'{url}spectra?query=100-01-6')
        click_instance.click(By.CLASS_NAME, 'supplier-num')
        assert driver.current_url == f'{url}cas/100-01-6'
        assert click_instance.check_element_presence(By.ID, 'basicInfo') == True, '基本信息谱图不存在'
        assert click_instance.check_element_presence(By.ID, 'poperty') == True, '化学性质不存在'
        assert click_instance.check_element_presence(By.ID, 'purpose') == True, '用途和用法不存在'
        assert click_instance.check_element_presence(By.ID, 'spectrogram') == True, '谱图不存在'
        assert click_instance.check_element_presence(By.ID, 'msds') == True, 'msds不存在'
        assert click_instance.check_element_presence(By.ID, 'price') == True, '价格不存在'
        assert click_instance.check_element_presence(By.ID, 'safe') == True, '安全信息不存在'
        #供应商列表页面进入化学性质页面
        driver.get(f'{url}suppliers/100-01-6')
        click_instance.click(By.XPATH, '/html/body/div[1]/section/div/div[2]/div[1]/div[1]/div[2]/div[5]/div/a')
        assert driver.current_url == f'{url}cas/100-01-6'
        assert click_instance.check_element_presence(By.ID, 'basicInfo') == True, '基本信息谱图不存在'
        assert click_instance.check_element_presence(By.ID, 'poperty') == True, '化学性质不存在'
        assert click_instance.check_element_presence(By.ID, 'purpose') == True, '用途和用法不存在'
        assert click_instance.check_element_presence(By.ID, 'spectrogram') == True, '谱图不存在'
        assert click_instance.check_element_presence(By.ID, 'msds') == True, 'msds不存在'
        assert click_instance.check_element_presence(By.ID, 'price') == True, '价格不存在'
        assert click_instance.check_element_presence(By.ID, 'safe') == True, '安全信息不存在'
        #试剂品牌馆页面进入查看化学性质页面
        driver.get(f'{url}brands/100-01-6')
        click_instance.click(By.XPATH, '/html/body/div[1]/section/div/div[2]/div[1]/div/div[1]/div[2]/div[5]/div/a')
        assert driver.current_url == f'{url}cas/100-01-6'
        assert click_instance.check_element_presence(By.ID, 'basicInfo') == True, '基本信息谱图不存在'
        assert click_instance.check_element_presence(By.ID, 'poperty') == True, '化学性质不存在'
        assert click_instance.check_element_presence(By.ID, 'purpose') == True, '用途和用法不存在'
        assert click_instance.check_element_presence(By.ID, 'spectrogram') == True, '谱图不存在'
        assert click_instance.check_element_presence(By.ID, 'msds') == True, 'msds不存在'
        assert click_instance.check_element_presence(By.ID, 'price') == True, '价格不存在'
        assert click_instance.check_element_presence(By.ID, 'safe') == True, '安全信息不存在'
        #msds页面进入化学性质页面
        driver.get(f'{url}msds?query=100-01-6')
        click_instance.click(By.XPATH, '/html/body/div[1]/section/div/div[1]/div[1]/div[2]/div/span[2]/a')
        assert driver.current_url == f'{url}cas/100-01-6'
        assert click_instance.check_element_presence(By.ID, 'basicInfo') == True, '基本信息谱图不存在'
        assert click_instance.check_element_presence(By.ID, 'poperty') == True, '化学性质不存在'
        assert click_instance.check_element_presence(By.ID, 'purpose') == True, '用途和用法不存在'
        assert click_instance.check_element_presence(By.ID, 'spectrogram') == True, '谱图不存在'
        assert click_instance.check_element_presence(By.ID, 'msds') == True, 'msds不存在'
        assert click_instance.check_element_presence(By.ID, 'price') == True, '价格不存在'
        assert click_instance.check_element_presence(By.ID, 'safe') == True, '安全信息不存在'
    # 试剂品牌馆
    def test_08(self,driver):
        click_instance = Select(driver)
        #搜索结果页进入试剂供应商页面
        driver.get(f'{url}search?query=100-55-0')
        Suppliers_num = driver.find_element(By.XPATH,'//*[@id="search-prd-box"]/div[2]/div[1]/div/div[2]/div[2]/a[2]/span').text
        click_instance.click(By.XPATH,'//*[@id="search-prd-box"]/div[2]/div[1]/div/div[2]/div[2]/a[2]')
        assert driver.current_url == f'{url}brands/100-55-0'
        assert click_instance.check_element_presence(By.XPATH,'/html/body/div[1]/section/div/div[2]/div[2]/div[3]/table/tbody') == True,'价格不存在'
        assert click_instance.check_element_presence(By.XPATH, '/html/body/div[1]/section/div/div[2]/div[1]/div/div[1]/div[2]/div[1]/img') == True, '结构式不存在'
        if 'India' in driver.find_elements(By.CLASS_NAME,'form-check-label')[0].text :
            danwei = driver.find_elements(By.CLASS_NAME,'currency')[0].text
            assert danwei == 'INR','印度本地供应商价格单位有误'
        else:
            danwei = driver.find_elements(By.CLASS_NAME, 'currency')[0].text
            assert danwei == 'USD', '非印度本地供应商价格单位有误'
        sjpp_Suppliers_num =  driver.find_element(By.XPATH,'/html/body/div[1]/section/div/div[2]/div[2]/div[1]/span').text
        assert Suppliers_num in sjpp_Suppliers_num,'搜索结果页与试剂品牌馆供应商数量不一致'
        #化学性质页面进入查价格页面
        driver.get(f'{url}cas/100-55-0')
        if driver.find_element(By.XPATH, '//*[@id="price"]/div[2]/table/tbody/tr[1]/td[1]').text == 'India':
            danwei_hxxz = driver.find_elements(By.CLASS_NAME,'currency')[0].text
            assert danwei_hxxz == 'INR', '印度本地供应商价格单位有误'
        else:
            danwei = driver.find_elements(By.CLASS_NAME, 'currency')[0].text
            assert danwei == 'USD', '非印度本地供应商价格单位有误'
        click_instance.click(By.XPATH, '//*[@id="price"]/div[2]/div/a[2]')
        assert driver.current_url == f'{url}brands/100-55-0'
        assert click_instance.check_element_presence(By.XPATH,'/html/body/div[1]/section/div/div[2]/div[2]/div[3]/table/tbody') == True, '价格不存在'
        assert click_instance.check_element_presence(By.XPATH, '/html/body/div[1]/section/div/div[2]/div[1]/div/div[1]/div[2]/div[1]/img') == True, '结构式不存在'
    # 查谱图入口
    def test_09(self,driver):
        click_instance = Select(driver)
        #搜索结果页进入查看谱图页面
        driver.get(f'{url}search?query=100-01-6')
        click_instance.click(By.XPATH, '//*[@id="search-prd-box"]/div[2]/div[1]/div/div[2]/div[2]/span')
        assert click_instance.check_element_presence(By.CLASS_NAME, 'swiper-img') == True, '谱图不存在'
        click_instance.click(By.CLASS_NAME,'viewMoreImg')
        assert driver.current_url == f'{url}spectra/100-01-6'
        assert click_instance.check_element_presence(By.CLASS_NAME, 'wrap-prdInfo-right') == True, '结构式不存在'
        assert click_instance.check_element_presence(By.XPATH,'/html/body/div[3]/section/div[2]/div[2]/div/div[1]/img') == True,'谱图不存在'
        #化学性质页面进入查谱图页面
        driver.get(f'{url}cas/100-01-6')
        click_instance.click(By.XPATH, '//*[@id="spectrogram"]/div[1]/div[2]/a')
        driver.switch_to.window(driver.window_handles[1])
        assert driver.current_url == f'{url}spectra/100-01-6'
        assert click_instance.check_element_presence(By.CLASS_NAME, 'wrap-prdInfo-right') == True, '结构式不存在'
        assert click_instance.check_element_presence(By.XPATH,'/html/body/div[3]/section/div[2]/div[2]/div/div[1]/img') == True, '谱图不存在'
    # 查msds入口
    def test_10(self,driver):
        click_instance = Select(driver)
        #化学性质页面进入msds页面
        driver.get(f'{url}cas/100-01-6')
        click_instance.click(By.XPATH,'//*[@id="msds"]/div[2]/table/tbody/tr/td[2]/div/span/a')
        driver.switch_to.window(driver.window_handles[1])
        assert click_instance.check_element_presence(By.XPATH,'/html/body/div[1]/div[2]/div/div[3]') == True,'第一节存在'
        click_instance.click(By.XPATH,'/html/body/div[1]/div[2]/div/div[1]/a')
        time.sleep(2)
        driver.switch_to.window(driver.window_handles[2])
        assert driver.current_url == f'{url}msds/pdf/100-01-6_8052'
    # 结构式入口
    def test_11(self,driver):
        click_instance = Select(driver)
        #搜索结果页进入结构式页面
        driver.get(f'{url}search?query=16')
        click_instance.click(By.XPATH,'//*[@id="search-prd-box"]/div[2]/div[1]/div[1]/div[1]/div/a[2]')
        assert f'{url}structure_search?pid=' in driver.current_url
        assert click_instance.check_element_presence(By.ID,'ketcher-editor') == True,'结构式搜索框架不存在'
        driver.back()
        click_instance.click(By.XPATH,'//*[@id="search-prd-box"]/div[2]/div[1]/div[1]/div[1]/div/span[1]')
        click_instance.click(By.ID,'render-formula-structure')
        driver.switch_to.window(driver.window_handles[1])
        assert f'{url}structure_search?pid=' in driver.current_url
        assert click_instance.check_element_presence(By.ID,'ketcher-editor') == True, '结构式搜索框架不存在'
        #化学性质页面进入结构式搜索页
        driver.get(f'{url}cas/1075-06-5')
        click_instance.click(By.XPATH,'/html/body/div[1]/section/div/div[2]/div[1]/div')
        assert f'{url}structure_search?mol_url=' in driver.current_url
        assert click_instance.check_element_presence(By.ID, 'ketcher-editor') == True, '结构式搜索框架不存在'
    #结构式查询
    def test_12(self,driver):
        click_instance = Select(driver)
        # 结构式首页，通过cas导入
        driver.get(f'{url}structure_search')
        click_instance.send(By.ID,'load_cas_structure_input','1075-06-5')
        time.sleep(2)
        click_instance.click(By.ID,'load_cas_structure')
        time.sleep(1)
        click_instance.click(By.XPATH,'/html/body/div[2]/section/div/div[1]/form/div/div[1]')
        assert click_instance.check_element_presence(By.CLASS_NAME,'wrap-search-list') == True,'精准查询失败'
        driver.back()
        click_instance.click(By.XPATH, '/html/body/div[2]/section/div/div[1]/form/div/div[2]')
        assert click_instance.check_element_presence(By.CLASS_NAME, 'wrap-search-list')== True,'子结构查询失败'
        driver.back()
        click_instance.click(By.XPATH, '/html/body/div[2]/section/div/div[1]/form/div/div[3]')
        assert click_instance.check_element_presence(By.CLASS_NAME, 'wrap-search-list') == True,'相似度查询失败'
        driver.back()
        driver.refresh()
        assert click_instance.check_element_presence(By.CLASS_NAME, 'struct-history') == True,'搜索历史不存在'
    # 供应商
    def test_13(self,driver):
        click_instance = Select(driver)
        driver.get(f'{url}suppliers/100-01-6')
        #供应商筛选
        click_instance.click(By.ID,'India')
        assert 'country=India' in driver.current_url,'查询失败，页面未跳转'
        assert click_instance.check_element_presence(By.CLASS_NAME,'wrap-filter-res') == True,'筛选后供应商不存在'
        click_instance.click(By.ID, 'India')
        click_instance.click(By.ID, 'China')
        assert 'country=China' in driver.current_url, '查询失败，页面未跳转'
        assert click_instance.check_element_presence(By.CLASS_NAME, 'wrap-filter-res') == True, '筛选后供应商不存在'
        click_instance.click(By.ID, 'Unknow')
        assert click_instance.check_element_presence(By.CLASS_NAME, 'wrap-filter-res') == True, '筛选后供应商不存在'
        #感兴趣
        click_instance.click(By.XPATH,'/html/body/div/section/div/div[2]/div[2]/div[3]/div[1]/div[2]/div[1]/div[2]/div/div[1]')
        assert click_instance.check_element_presence(By.CLASS_NAME, 'alert-msg') == True, '未提示登录'
    # 试剂品牌馆
    def test_14(self,driver):
        click_instance = Select(driver)
        driver.get(f'{url}brands/67531-86-6')
        click_instance.click(By.ID,'United States')
        assert click_instance.check_element_presence(By.CLASS_NAME,'price-table') ==True,'筛选国家后价格不存在'
        click_instance.click(By.ID, 'United States')
        click_instance.click(By.ID, 'China')
        assert click_instance.check_element_presence(By.CLASS_NAME, 'price-table') == True, '筛选国家后价格不存在'
        click_instance.click(By.ID, 'China')
        click_instance.click(By.ID, 'AIKON')
        assert click_instance.check_element_presence(By.CLASS_NAME, 'price-table') == True, '筛选供应商后价格不存在'
        click_instance.click(By.ID, 'AIKON')
        click_instance.click(By.ID, 'Aladdin')
        assert click_instance.check_element_presence(By.CLASS_NAME, 'price-table') == True, '筛选供应商后价格不存在'
        click_instance.click(By.ID, 'Aladdin')
        click_instance.click(By.ID, '250mg')
        assert click_instance.check_element_presence(By.CLASS_NAME, 'price-table') == True, '筛选包装后价格不存在'
        click_instance.click(By.ID, '250mg')
        click_instance.click(By.ID, '1g')
        assert click_instance.check_element_presence(By.CLASS_NAME, 'price-table') == True, '筛选包装后价格不存在'
    # 化工字典
    def test_15(self,driver):
        click_instance = Select(driver)
        driver.get(f'{url}chem_dict')
        click_instance.click(By.XPATH, '/html/body/div[1]/section/div/div[3]/div[1]/div[2]/a[1]')  # 点击产品名称A
        assert driver.current_url == f'{url}chem_dict/product_name_start_with_A'
        click_instance.click(By.XPATH, '/html/body/div[1]/section/div/div[4]/nav/ul/nav/ul/li[14]/a')  # 点击页码最后一页
        assert f'{url}chem_dict/product_name_start_with_A?page=' in driver.current_url
        index = driver.find_element(By.CLASS_NAME, 'btn-active').text  # 产品名称索引
        assert index == 'A'
        click_instance.click(By.XPATH, '/html/body/div[1]/section/div/div[2]/div[1]/div[2]/a[26]')  # 点击产品名称Z
        assert driver.current_url == f'{url}chem_dict/product_name_start_with_Z'
        click_instance.click(By.XPATH, '/html/body/div[1]/section/div/div[4]/nav/ul/nav/ul/li[14]/a')  # 点击页码最后一页
        index = driver.find_element(By.CLASS_NAME, 'btn-active').text  # 产品名称索引
        assert index == 'Z'
        click_instance.click(By.XPATH, '/html/body/div[1]/section/div/div[2]/div[2]/div[2]/a[1]')  # 点击cas号1
        assert driver.current_url == f'{url}chem_dict/cas_start_with_1'
        click_instance.click(By.XPATH, '/html/body/div[1]/section/div/div[4]/nav/ul/nav/ul/li[14]/a')  # 点击页码最后一页
        index = driver.find_element(By.CLASS_NAME, 'btn-active').text  # 产品名称索引
        assert index == '1'
        click_instance.click(By.XPATH, '/html/body/div[1]/section/div/div[2]/div[2]/div[2]/a[9]')  # 点击cas号9
        assert driver.current_url == f'{url}chem_dict/cas_start_with_9'
        click_instance.click(By.XPATH, '/html/body/div[1]/section/div/div[4]/nav/ul/nav/ul/li[14]/a')  # 点击页码最后一页
        index = driver.find_element(By.CLASS_NAME, 'btn-active').text  # 产品名称索引
        assert index == '9'
    # 问答
    def test_user1_16(self,driver):
        click_instance = Select(driver)
        driver.get(f'{url}questions')
        click_instance.click(By.XPATH, '//*[@id="a_ask"]')  # 我要提问
        assert click_instance.check_element_presence(By.XPATH, '/html/body/div[1]/section/div[2]/div') == True  # 提问模块
        click_instance.click(By.ID, 'validationInput')  # 标题
        click_instance.send(By.ID, 'validationInput', 'What is the vanillin map')
        click_instance.click(By.ID, 'validationTextarea')  # 详细内容
        click_instance.send(By.ID, 'validationTextarea', 'What is the vanillin map (test)')
        click_instance.click(By.ID, 'submit-question-btn')  # 提交
        info = driver.find_element(By.CLASS_NAME, 'alert-msg').text
        assert info == 'Submit successfully'
        click_instance.send(By.XPATH, '//*[@id="input_search_question"]', 'What is the vanillin map')
        click_instance.click(By.XPATH, '//*[@id="a_search_question"]/input')  # 搜索答案
        click_instance.click(By.XPATH, '/html/body/div[3]/section/div/ul/li[1]/a')  # 问题
        assert click_instance.check_element_presence(By.ID, 'editMyAnser') == True  # 我来回答按钮
        assert click_instance.check_element_presence(By.XPATH,'/html/body/div[2]/section/div/div/div[2]') == True  # 等你来答模块
        click_instance.click(By.XPATH, '/html/body/header/div/div[2]/div/a[5]')  # 问答
        click_instance.click(By.XPATH,'/html/body/div[1]/section/div/div[3]/div[1]/div[2]/ul/li[1]/a')  # 点击最新问题
        assert click_instance.check_element_presence(By.XPATH, '//*[@id="editMyAnser"]') == True  # 我来回答按钮
        assert click_instance.check_element_presence(By.XPATH,'/html/body/div[2]/section/div/div/div[2]') == True  # 等你来答模块
        driver.back()
        click_instance.click(By.XPATH,'/html/body/div[1]/section/div/div[3]/div[2]/div[2]/ul/li[1]/a')  # 点击大家热议
        assert click_instance.check_element_presence(By.XPATH, '//*[@id="editMyAnser"]') == True  # 我来回答按钮
        assert click_instance.check_element_presence(By.XPATH,'/html/body/div[2]/section/div/div/div[2]') == True  # 等你来答模块
        db.execute_delete('questions','title="What is the vanillin map"')
    # 未认证用户发布产品
    @pytest.mark.identity("user2")
    def test_17(self,driver,request):
        click_instance = Select(driver)
        #单个保存产品
        driver.get(f'{url}product/add')
        click_instance.send(By.ID,'cas','626-55-1')
        click_instance.send(By.ID,'name_en','3-Pyridyl bromide')
        click_instance.send(By.ID,'purity_specification','98%')
        click_instance.send(By.NAME,'package','25g;100g')
        click_instance.click(By.XPATH,'//*[@id="member-product-add-form"]/div[11]/button[1]') #保存
        info = driver.find_element(By.CLASS_NAME,'alert-msg').text
        assert info == 'Success','保存失败'
        #单个发布产品
        driver.get(f'{url}product/add')
        click_instance.send(By.ID, 'cas', '1075-06-5')
        click_instance.send(By.ID, 'name_en', 'PHENYLGLYOXAL MONOHYDRATE')
        click_instance.send(By.ID, 'purity_specification', '98%')
        click_instance.send(By.NAME, 'package', '25g;100g')
        click_instance.click(By.XPATH, '//*[@id="member-product-add-form"]/div[11]/button[2]')  # 保存
        info = driver.find_element(By.CLASS_NAME, 'alert-msg').text
        assert info == 'Please go through enterprise certification before posting product information for the first time!'
        #删除所有产品
        driver.get(f'{url}product/index')
        click_instance.click(By.XPATH,'/html/body/div[2]/div/div[1]/div[2]/div[5]/table/thead/tr/th[1]/input')
        click_instance.click(By.CLASS_NAME,'del-btn')
        driver.switch_to.alert.accept()
        info = driver.find_element(By.CLASS_NAME, 'alert-msg').text
        assert info == 'Success', '删除失败'
        # 批量导入产品
        driver.get(f'{url}product/bulk')
        page_source = driver.page_source #输出当前页面HTML
        token = re.findall('<meta name="csrf-token" content="(.+?)">', page_source)
        identity_marker = request.node.get_closest_marker("identity")
        username = identity_marker.args[0]
        update_cookies(driver,username)
        #上传文件
        upload_url = f"{url}api/v1/admin/upload"
        sql_cookies = db_cookies.execute_query(f"SELECT session, token FROM cookies WHERE username = '{username}'")
        headers = {
            'Cookie': 'XSRF-TOKEN=%s; qs_session=%s' % (sql_cookies[0]['token'],sql_cookies[0]['session'])
        }
        with open(r"C:\Users\shangguanyi\Downloads\Manufacturer_Supplier_Template (3).xlsx", "rb") as file:
            file_data = file.read()
        files = {
            "file": ("Manufacturer_Supplier_Template (3).xlsx", file_data)
        }
        data = {
            "id": "WU_FILE_0",
            "name": "Manufacturer_Supplier_Template (3).xlsx",
            "type": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            "lastModifiedDate": "Tue Oct 10 2023 15:13:00 GMT+0800 (中国标准时间)",
            "size": "7264"
        }
        response = requests.post(url=upload_url, headers=headers, data=data, files=files)
        path = response.json()['data']['url']
        #提交
        urltijiao = f"{url}product/upload"
        payload = f'upload_type=Update&path={path}'
        headers = {
            'Cookie': 'XSRF-TOKEN=%s; qs_session=%s'%(sql_cookies[0]['token'],sql_cookies[0]['session']),
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'X-Csrf-Token': token[0]
        }
        response = requests.request("POST", urltijiao, headers=headers, data=payload)
        #print(response.text)
        assert response.json()['message'] == 'Please go through enterprise certification before posting product information for the first time!'





















