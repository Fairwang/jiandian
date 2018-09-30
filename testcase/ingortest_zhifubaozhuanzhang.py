#!/user/bin/python
#  -*-coding: utf-8-*-
import unittest
from jiandian import chaxunshujuku, swipefengzhuang
import time

from jiandiandenglu.common import driver_config,gesture_mainpulation,get_toast,query_database
from jiandiandenglu.LK import creat_page
from selenium.webdriver.common.by import By
from appium import webdriver
import time
import sys
if sys.getdefaultencoding() != 'utf-8':
    reload(sys)
    sys.setdefaultencoding('utf-8')


class zhifubao(unittest.TestCase):


    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        # desired_caps['platfromVersion'] = '7.1.1'
        # desired_caps['deviceName'] = '33d04c7c'
        desired_caps['platfromVersion']='7.1.2'#红米5A
        desired_caps['deviceName']='79bad8ec7d94'
        desired_caps['appPackage'] = 'com.eg.android.AlipayGphone'
        desired_caps['automationName'] = 'uiautomator2'  ##############
        desired_caps['appActivity'] = 'com.eg.android.AlipayGphone.AlipayLogin'
        desired_caps['noReset']=True

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def test_zhifubao(self):
        driver=self.driver
        time.sleep(3)
        driver.find_element_by_xpath("//android.widget.TextView[@text='朋友']").click()
        time.sleep(1)
        driver.find_element_by_xpath("//android.widget.TextView[@text='温州赤龙网络科技有限公司']").click()
        time.sleep(1)
        f0 = open('D:\\zxtest\\zhifubao.txt', 'r')
        z = len(open('D:\\zxtest\\zhifubao.txt', 'r').readlines())
        x=[]
        while True:
            dat0 = f0.readline()

            driver.find_element_by_xpath("//android.widget.ImageView[@content-desc='更多']").click()
            time.sleep(2)
            zhuanzhang=driver.find_elements_by_xpath("//android.widget.TextView[@text='转账']")
            zhuanzhang[-1].click()
            time.sleep(1)
            driver.find_element_by_xpath("//android.widget.EditText[@content-desc='输入转账金额']").click()
            time.sleep(1)
            x=driver.get_window_size()['width']
            y=driver.get_window_size()['height']

            # time.sleep(10)
            # driver.tap([(476*x/1080, 1795*y/1920)], 0)
            # driver.tap([(735*x/1080, 1806*y/1920)], 0)
            # driver.tap([(476*x/1080, 1795*y/1920)], 0)
            # driver.tap([(278*x/1080, 1313*y/1920)], 0)
            time.sleep(1)#红米5A
            driver.tap([(355*x/720, 1207*y/1280)], 0)
            driver.tap([(44*x/720, 877*y/1280)], 0)
            driver.tap([(355*x/720, 1207*y/1280)], 0)
            driver.tap([(184*x/720, 886*y/1280)], 0)



            driver.find_element_by_xpath("//android.widget.EditText[@text='添加备注(50字以内)']").send_keys(dat0)
            time.sleep(1)

            driver.find_element_by_xpath("//android.widget.Button[@text='确认转账']").click()
            time.sleep(3)
            driver.find_element_by_xpath("//android.widget.TextView[@text='立即付款']").click()
            time.sleep(1)
            driver.tap([(140*x/1080,1500*y/1920)],0)
            time.sleep(1)
            driver.tap([(200*x/1080,1500*y/1920)],0)
            time.sleep(1)
            driver.tap([(800*x/1080,1500*y/1920)],0)
            time.sleep(1)
            driver.tap([(800*x/1080,1500*y/1920)],0)
            time.sleep(1)
            driver.tap([(500*x/1080,1680*y/1920)],0)
            time.sleep(1)
            driver.tap([(500*x/1080,1680*y/1920)],0)
            time.sleep(3)
            driver.find_element_by_xpath("//android.widget.TextView[@text='完成']").click()
            time.sleep(1)
            if dat0 == '':
                break
        f0.close()
        # driver.find_element_by_id("com.ali.user.mobile.security.ui:id/loginButton").click()
        # time.sleep(3)
        # driver.find_element_by_id("com.ali.user.mobile.security.ui:id/userAccountInput").send_keys("15868314566")
        # time.sleep(3)
        # driver.find_element_by_id("com.ali.user.mobile.security.ui:id/userPasswordInput").send_keys("ymxx158")
        # time.sleep(3)
        # driver.find_element_by_id("com.ali.user.mobile.security.ui:id/loginButton").click()
        # time.sleep(2)
        # driver.tap([(1,1380),(100,1400)],500)
        # time.sleep(2)
        # driver.tap([(1,1380),(100,1400)],500)
        # time.sleep(2)
        # driver.tap([(1000,1400),(1079,1559)],500)
        # time.sleep(2)
        # driver.tap([(1000,1400),(1079,1559)],500)
        # time.sleep(2)
        # driver.tap([(500,1600),(500,1739)],500)
        # time.sleep(2)
        # driver.tap([(500,1600),(500,1739)],500)
        #
        # driver.find_element_by_xpath("//android.widget.ImageView[@content-desc='图片 4, 2018-08-27 16:25']").click()



#     # 微信
# class weixin(unittest.TestCase):
#     def setUp(self):
#         desired_caps = {}
#         desired_caps['platformName'] = 'Android'
#         desired_caps['platfromVersion'] = '7.1.1'
#         desired_caps['deviceName'] = '33d04c7c'
#         desired_caps['appPackage'] = 'com.tencent.mm'
#         desired_caps['automationName'] = 'uiautomator2'  ##############
#         desired_caps['appActivity'] = 'ui.LauncherUI'
#         desired_caps['noReset']=True
#         self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
#
#     def test_weixin(self):
#         driver=self.driver
#         # driver.find_element_by_id("com.tencent.mm:id/ht").send_keys("juan123456789")
#         # driver.find_element_by_id("com.tencent.mm:id/byd").click()
#         time.sleep(3)
#         driver.find_element_by_id("com.tencent.mm:id/g_").click()
#         time.sleep(3)
#
#         driver.find_element_by_xpath("//android.widget.TextView[@text='扫一扫']").click()
#         time.sleep(3)
#
#         driver.find_element_by_id("com.tencent.mm:id/he").click()
#         #
#         time.sleep(3)
#         driver.find_element_by_xpath("//android.widget.TextView[@text='从相册选取二维码']").click()
#         time.sleep(3)
#
#         driver.find_element_by_xpath("//android.widget.ImageView[@content-desc='图片 1, 2018-09-01 09:27']").click()
#         time.sleep(3)
#
#         driver.find_element_by_id("com.tencent.mm:id/akb").click()
#         time.sleep(2)
#         driver.tap([(1,1380),(100,1400)],500)
#         time.sleep(2)
#         driver.tap([(1,1380),(100,1400)],500)
#         time.sleep(2)
#         driver.tap([(1000,1400),(1079,1559)],500)
#         time.sleep(2)
#         driver.tap([(1000,1400),(1079,1559)],500)
#         time.sleep(2)
#         driver.tap([(500,1700),(500,1722)],500)
#         time.sleep(2)
#         driver.tap([(500,1700),(500,1722)],500)
#         time.sleep(10)
# #
#
#





    def tearDown(self):
        self.driver.quit()

if __name__=="__main__":
    unittest.main()

