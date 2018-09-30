#!/usr/bin/python
# -*- coding: UTF-8 -*-

from appium import webdriver
# from selenium import webdriver
import unittest
from jiandian import chaxunshujuku, swipefengzhuang
import time
import logging
from jiandiandenglu.common import driver_config,gesture_mainpulation,get_toast,query_database
from jiandiandenglu.LK import creat_page
from selenium.webdriver.common.by import By
logging.getLogger().setLevel(logging.INFO)
from appium.webdriver.mobilecommand import MobileCommand

import sys
if sys.getdefaultencoding() != 'utf-8':
    reload(sys)
    sys.setdefaultencoding('utf-8')



class reduce(unittest.TestCase):
    def setUp(self):
        gesture=driver_config.driver_configure()
        self.driver=gesture.get_driver()
        self.gm=gesture_mainpulation.gesture_mainpulation()
        self.login_page=creat_page.login_page(self.driver)
        self.get_toast=get_toast.get_toast(self.driver)
        self.database=query_database.Query_database()

    def test_reduce(self):
        # 测试登录成功并退出APP
        driver = self.driver
        for i in range(3):
            self.driver.implicitly_wait(10)
            self.gm.swipeRight(self.driver)

        text = '15868314566'
        pasw = '123456'
        self.login_page.input_user(text)
        self.login_page.input_pws(pasw)
        self.login_page.click_btnlogin()

        # try:

        self.login_page.zhoubao_click()
        time.sleep(20)
        print driver.contexts
        print driver.current_context

        print driver.page_source
        self.login_page.driver.execute(MobileCommand.SWITCH_TO_CONTEXT,{"name":"WEBVIEW_chrome"})
        # driver.execute(MobileCommand.SWITCH_TO_CONTEXT, {"name": "NATIVE_APP"})
        print driver.current_context

        print driver.page_source



        # except Exception,e:
        #     print"zhaobudao mendiainzhoubao zenmeban "

# def switch_h5(self):
#     self.driver.execute(MobileCommand.SWITCH_TO_CONTEXT, {"name": "WEBVIEW_chrome"})
#
# def switch_app(self):
#     self.driver.execute(MobileCommand.SWITCH_TO_CONTEXT, {"name": "NATIVE_APP"})

if __name__ == '__main__':
    unittest.main()
