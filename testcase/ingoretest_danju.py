#!/user/bin/python
# -*-coding:utf-8-*-
from appium import webdriver
from jiandiandenglu.common import  driver_config,gesture_mainpulation,query_database
from jiandiandenglu.LK import creat_page
from selenium.webdriver.common.by import By
# from selenium import webdriver
import unittest

import time
from decimal import *

class danju(unittest.TestCase):
    def setUp(self):
        configure=driver_config.driver_configure()
        self.driver=configure.get_driver()
        self.gm=gesture_mainpulation.gesture_mainpulation()
        self.login_page=creat_page.login_page(self.driver)
        self.query_database=query_database.Query_database()

    def test_danju(self):
# 测试登录成功并退出APP
        driver = self.driver
        for i in range(3):
            self.driver.implicitly_wait(10)
            self.gm.swipeRight(self.driver)

        text ='15868314566'
        pasw='123456'
        self.login_page.input_user(text)
        self.login_page.input_pws(pasw)
        self.login_page.click_btnlogin()
        self.login_page.click_danju()
#判断订单详情页面部分数据是否与数据库一致
        self.login_page.click_order()
        #判断详情页面和数据库是否一致
        detail=(By.ID,'site.weide.shopmanage:id/order_number')
        text=self.login_page.find_element(*detail).text
        sql="select price,ispay,pay_way,pay_type from t_pay_order where order_id="+"'"+text+"'"
        print sql
        search_result=self.query_database.query_database(sql)
        # print dingdan
        # print dingdan[0],dingdan[1],dingdan[2],dingdan [3]
#交易价格
        apprice=driver.find_element_by_id('site.weide.shopmanage:id/order_price').text
        print "apprice type%s" %type(apprice)
        print apprice
        price=Decimal(apprice[1:])
        print price,search_result[0]
        print type(price),type(search_result[0])
        assert search_result[0]==price
#交易进程
        ispay=driver.find_element_by_id('site.weide.shopmanage:id/bill_states').text
        print  "yixiadaying "
        print  search_result[1],ispay
        if search_result==1 and ispay==u"已完成":
            print u"订单交易进程正确"
        else:
            print u"订单交易进程错误"
        # assert dingdan[1]==ispay
#交易类型、判断主扫和被扫
        payway=driver.find_element_by_id('site.weide.shopmanage:id/transaction_mode').text
        if payway==u'微信支付':
            payway='micropay'
        if payway==u'支付宝支付':
            payway='torepay'
        print search_result[2],payway
        assert search_result[2]==payway
#支付类型、交易方式
        paytype=driver.find_element_by_id('site.weide.shopmanage:id/transaction_type').text
        if paytype==u'扫码支付':
            paytype=1
        elif paytype==u'外卖订单'or paytype==u'堂食订单'or paytype==u'会员充值':
            paytype=2
        else:
            paytype=3
        assert search_result[3]==paytype

#选择订单类型后判断订单是否均显示所选择的订单类型


    def tearDown(self):
        self.driver.quit()

# if __name__ == '__main__':
#     # suite = unittest.TestSuite()
#     # suite.addTest(LoginTestjiandian('test_login'))
#     # filename = 'D:\\app.html'
#     # fb=file(filename,'wb')
#     # runner = HTMLTestRunner.HTMLTestRunner(stream=fb, title=u'简店登录注册测试', description=u'简店登录注册测试')
#     # runner.run(suite)
#     # fb.close()
#     unittest.main()


