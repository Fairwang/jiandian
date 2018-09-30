#!/user/bin/python
# -*-coding:UTF-8-*-
import unittest
from appium import webdriver
from jiandiandenglu.LK import creat_page,base_page,send_email
from jiandiandenglu.common import driver_config,gesture_mainpulation
#from jiandiandenglu.common.get_toast import find_toast
from jiandiandenglu.common import get_toast
import time
from selenium.webdriver.common.by import By

class Jiandiandemo(unittest.TestCase):
    # @classmethod
    def setUp(self):
        # print "11"
        # loginfengzhuang.jianguoapp(self)#引用类
        #初始化，引用类，将类实例化
        configure=driver_config.driver_configure()
        self.driver=configure.get_driver()
        self.gm=gesture_mainpulation.gesture_mainpulation()
        self.login_page = creat_page.login_page(self.driver)
        self.toast = get_toast.get_toast(self.driver)

    def test_denglu(self):
        #欢迎页面
        for i in range(3):
            self.driver.implicitly_wait(10)
            self.gm.swipeRight(self.driver)
        time.sleep(5)
#密码为错误
        text ='15868314566'
        pasw='123455'
        # login_page=creat_page.login_page(self.driver)
        self.login_page.input_user(text)
        self.login_page.input_pws(pasw)
        self.login_page.click_btnlogin()
        # toast = get_toast.get_toast(self.driver)
        self.toast.get_toast('账号不存在或密码错误')
        time.sleep(5)

#手机号不存在
        text ='10068314522'
        pasw='123456'
        # login_page=creat_page.login_page(self.driver)
        self.login_page.input_user(text)
        self.login_page.input_pws(pasw)
        self.login_page.click_btnlogin()
        self.toast.get_toast('输入的手机号码有误')
        time.sleep(5)
# 手机号为空
        text = ''
        pasw = '123456'
        self.login_page.input_user(text)
        self.login_page.input_pws(pasw)
        self.login_page.click_btnlogin()##无法点击
        self.toast.get_toast("输入的手机号号码有误")
# 密码为空
        text ='15868314522'
        pasw =''
        self.login_page.input_user(text)
        self.login_page.input_pws(pasw)
        self.login_page.click_btnlogin()#无法点击
        self.toast.get_toast("账号不存在或密码错误")

#数据正确
        text ='15868314566'
        pasw='123456'
        # login_page.click_btnlogin()
        self.login_page.input_user(text)
        self.login_page.input_pws(pasw)
        self.login_page.click_btnlogin()
        shouye_name =(By.ID, 'site.weide.shopmanage:id/shop_name')
        # try:
        #
        text=self.login_page.find_element(*shouye_name).text
        assert u'1586831456测试' in text
        print "loginuser is right"
        # except AssertionError as e:
        #     print "loinuser is error"






    def tearDown(self):
        self.driver.quit()

# if __name__ == '__main__':
#     unittest.main()











