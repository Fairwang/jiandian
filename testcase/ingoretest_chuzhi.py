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

        # 进入我的页面
        self.login_page.wode_click()
        self.login_page.member_click()

        #test添加条数、减少条数、数据为空时提交
        self.login_page.store_click()
        self.login_page.opensend_click()#默认关闭，打开
        tishi_loc = (By.XPATH, "//android.widget.TextView[@text='确认要关闭吗?']")
        flag=self.login_page.isElementExit(*tishi_loc)
        if flag:
            self.login_page.button2_click()
        else:
            pass
        flag=self.login_page.isElementExit(*self.login_page.add_loc)
        if flag:
            for i in range(6):
                self.login_page.add_click()
            self.get_toast.get_toast("最多只能添加六项哦~")

            for i in range(5):
                self.login_page.reduce_click()
            self.login_page.submit_click()
            self.get_toast.get_toast("请至少添加一项")
        else:
            logging.info("add element is not exit")

        #充值金额为大于零的数字、零、特殊字符、负数
        chongzhi1="23"
        send1="5"
        self.login_page.chongzhi01_input(chongzhi1)
        self.login_page.send01_input(send1)
        self.login_page.submit_click()
        self.get_toast.get_toast("设置成功")

        chongzhi="0"
        send="1"
        self.login_page.chongzhi01_input(chongzhi)
        self.login_page.send01_input(send)
        self.login_page.submit_click()
        self.get_toast.get_toast("充值金额必须大于零的数字")

        chongzhi="1"
        send="0"
        self.login_page.chongzhi01_input(chongzhi)
        self.login_page.send01_input(send)
        self.login_page.submit_click()
        self.get_toast.get_toast("赠送金额必须大于零的数字")

        chongzhi="+-5"
        send="2"
        self.login_page.chongzhi01_input(chongzhi)
        self.login_page.send01_input(send)
        self.login_page.submit_click()
        self.get_toast.get_toast("充值金额必须大于零的数字")

        chongzhi="-5"
        send="2"
        self.login_page.chongzhi01_input(chongzhi)
        self.login_page.send01_input(send)
        self.login_page.submit_click()
        self.get_toast.get_toast("充值金额必须大于零的数字")
        # sql = "SELECT `price`,`give_price`,`sort` FROM `t_member_store_rule` WHERE  (  cid = 444 and status = 1 ) ORDER BY `sort`  asc"
        # chongzhisql = self.database.query_database(sql)
        # logging.info("%s"%chongzhisql)
        # price = chongzhisql[0]
        # give_price = chongzhisql[1]
        # if price == null and give_price == null:
        #     logging.info("danbi tese success")


        sql="SELECT `price`,`give_price`,`sort` FROM `t_member_store_rule` WHERE  (  cid = 436 and status = 1 ) ORDER BY `sort`  asc"
        chongzhisql=self.database.query_database(sql)
        logging.info("%s"%chongzhisql)

        if chongzhisql[0][0]==chongzhi1 and chongzhisql[0][1]==send1:
            logging.info("danbi test success")
        else:
            logging.info("danbi test failure")



#第二个充值送test
        chongzhi="23"
        send="5"
        self.login_page.chongzhi01_input(chongzhi)
        self.login_page.send01_input(send)
        self.login_page.submit_click()
        self.get_toast.get_toast("设置成功")

        # flag=self.login_page.isElementExit(*self.login_page.chongzhi_loc)
        # if flag:
        #     logging.info("not dierge chongzhisong")
        # else:
        for i in range(6):
            self.login_page.add_click()
            chongzhi="5"
            send="3"
            self.login_page.chongzhi_input(chongzhi)
            self.login_page.send_input(send)
        self.login_page.submit_click()


        time.sleep(5)
        sql="SELECT `price`,`give_price`,`sort` FROM `t_member_store_rule` WHERE  (  cid = 436 and status = 1 ) ORDER BY `sort`  asc"
        chongzhisql=self.database.query_database(sql)

        print chongzhisql
        print chongzhisql[1][0],chongzhisql[1][1]
        if chongzhisql[1][0]==chongzhi and chongzhisql[1][1]==send:
            logging.info("danbi test success")
        else:
            logging.info("danbi test failure")
#
# #输入六个充值送-测试
#         flag=self.login_page.isElementExit(*tishi_loc)
#         if flag:
#             self.login_page.button2_click()
#         else:
#             pass
#         flag=self.login_page.isElementExit(*self.login_page.add_loc)
#         if flag:
#             for i in range(5):
#                 self.login_page.add_click()
#                 chongzhi=10
#                 send=20
#                 self.login_page.chongzhi_input(chongzhi)
#                 self.login_page.send_input(send)
#             self.get_toast.get_toast("最多只能添加六项哦~")
#         chongzhi = 10
#         send = 20
#         self.login_page.chongzhi4_input(chongzhi)
#         self.login_page.send4_input(send)#使用index 进行xpath进行定位 无法定位成功
#         self.login_page.submit_click()
#         time.sleep(5)
#         sql = "SELECT `price`,`give_price`,`sort` FROM `t_member_store_rule` WHERE  (  cid = 436 and status = 1 ) ORDER BY `sort`  asc"
#         chongzhisql = self.database.query_database(sql)
#         print chongzhisql
#         if chongzhisql[2][0]==chongzhi and  chongzhisql[2][1]==send:
#             logging.info("six test success")

if __name__ == '__main__':
    unittest.main()


