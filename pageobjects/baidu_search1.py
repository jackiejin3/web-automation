#coding=utf-8

import time
import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.baidu_homepage import HomePage
from framework.base_page import BasePage

class BaiduSearch(unittest.TestCase):

    def setUp(self):
        browser = BrowserEngine()
        self.driver = browser.open_browser()

    def tearDown(self):
        self.driver.quit()

    #通过homepage中方法进行案例执行
    '''def test_baidu_search(self):
        homepage = HomePage(self.driver)
        homepage.type_search("selenium")
        homepage.send_submit_btn()
        time.sleep(2)
        homepage.get_windows_img()
        try:
            assert 'selenium' in homepage.get_page_title()
            print('Test pass')
        except Exception as e:
            print('Test Fail.', format(e))'''

    #直接调用base_page类
    def test_baidu_search2(self):
        test = BasePage(self.driver)
        test.type("id=>kw", "selenium")
        test.click_selector("id=>su")
        time.sleep(1)
        #test.click("xpath=>/html/body/div[1]/div[5]/div[1]/div[3]/div[2]/div[1]/h3/a")



