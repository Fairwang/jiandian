#!/user/bin/python
# -*-coding:utf-8-*-
from appium import webdriver
# from selenium import webdriver
import unittest
from jiandian import chaxunshujuku, swipefengzhuang
import time

from jiandiandenglu.common import driver_config,gesture_mainpulation,get_toast,query_database
from jiandiandenglu.LK import creat_page
from selenium.webdriver.common.by import By
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

        text ='15868314566'
        pasw='123456'
        self.login_page.input_user(text)
        self.login_page.input_pws(pasw)
        self.login_page.click_btnlogin()

        driver.implicitly_wait(5)
        self.login_page.click_active()
        #driver.find_element_by_id('site.weide.shopmanage:id/active').click()#进入营销页面
        driver.implicitly_wait(5)
        self.login_page.click_fullcut()
        # driver.find_element_by_id('site.weide.shopmanage:id/full_cut').click()#满减活动
        driver.implicitly_wait(5)
#原价
        self.login_page.click_original()
        driver.implicitly_wait(5)
        self.login_page.click_submitBtn()
        self.get_toast.get_toast("设置成功")
        # get_toast.find_Toast2(self, "设置成功")
        sql="select cid FROM t_sys_adminuser WHERE  username = '15868314566'"
        #a= chaxunshujuku.shujuku(sql)
        a=self.database.query_database(sql)
        #cid=a[0]
        print a
        sql="SELECT fullprice,minprice,maxprice,cid FROM t_promotion_reduce_rule WHERE  cid =436"
       # sql="SELECT fullprice,minprice,maxprice,cid FROM t_promotion_reduce_rule WHERE  "+"cid="+cid
        # sql='SELECT fullprice,minprice,maxprice,cid FROM t_promotion_reduce_rule WHERE  cid =436'
        print "this is sql %s"%sql
        #original_price= chaxunshujuku.shujuku(sql)
        original_price=self.database.query_database(sql)
        print original_price
        fullrice=original_price[0]
        minprice=original_price[1]
        maxprice=original_price[2]
        if fullrice==minprice==maxprice:
            print "yuanjia_success"
#立减(正常)

        driver.implicitly_wait(5)
        self.login_page.click_lijian()
        driver.implicitly_wait(5)

        full="10"
        self.login_page.input_gull_money(full)
        driver.implicitly_wait(5)
        cut="2"
        self.login_page.input_cut_money(cut)
        driver.implicitly_wait(5)
        self.login_page.click_submitBtn()
        self.get_toast.get_toast("设置成功")
        time.sleep(2)
        sql ='SELECT fullprice,minprice,maxprice,cid FROM t_promotion_reduce_rule WHERE  cid =436'
        print  "zheli"
        # original_price = chaxunshujuku.shujuku(sql)
        original_price = self.database.query_database(sql)
        print original_price
        print original_price[0],original_price[1], original_price[2]
        if original_price[0] ==10 and original_price[1] ==2 and original_price[2]==2:
            print "lijian_success"
        else:
            print "lijian_failure"
#随机减（正常）
        time.sleep(2)
        self.login_page.click_random()
        #driver.find_element_by_xpath("//android.widget.TextView[@text='元,随机减']").click()
        print u"随机减"
        time.sleep(2)
        sjfull='30'
        sjmax='20'
        sjmin='10'
        self.login_page.input_sjfull(sjfull)
        self.login_page.input_sjmax(sjmax)
        self.login_page.input_sjmin(sjmin)
        self.login_page.click_submitBtn()
        self.get_toast.get_toast("设置成功")
        # driver.find_element_by_id('site.weide.shopmanage:id/sj_full_money').send_keys('30')
        # driver.find_element_by_id('site.weide.shopmanage:id/sj_cut_min_money').send_keys('10')
        # driver.find_element_by_id("site.weide.shopmanage:id/sj_cut_max_money").send_keys('20')
        # driver.find_element_by_id("site.weide.shopmanage:id/submitBtn").click()
        # get_toast.find_Toast2(self, "设置成功")
        sql = 'SELECT fullprice,minprice,maxprice,cid FROM t_promotion_reduce_rule WHERE  cid =436'
        # original_price = chaxunshujuku.shujuku(sql)
        original_price = self.database.query_database(sql)
        #print original_price
       # print original_price[0], original_price[1], original_price[2]
        if original_price[0] ==30 and original_price[1] ==10 and original_price[2]==20:
            print u"满30减10-20设置成功"
        else:
            print u"满30减10-20设置成功"


#
# 立减(满小于减)

        driver.implicitly_wait(5)
        self.login_page.click_lijian()
        driver.implicitly_wait(5)

        full="10"
        self.login_page.input_gull_money(full)
        driver.implicitly_wait(5)
        cut="20"
        self.login_page.input_cut_money(cut)
        driver.implicitly_wait(5)
        self.login_page.click_submitBtn()
        self.get_toast.get_toast("优惠金额必须小于起始条件金额")
        time.sleep(2)
        sql ='SELECT fullprice,minprice,maxprice,cid FROM t_promotion_reduce_rule WHERE  cid =436'
        print  "zheli"
        # original_price = chaxunshujuku.shujuku(sql)
        original_price = self.database.query_database(sql)
        print original_price
        print original_price[0],original_price[1], original_price[2]
        if original_price[0] ==30 and original_price[1] ==10 and original_price[2]==20:
            print u"数据库显示立减（满小于减）未设置成功"
        else:
            print u"ERROR：立减 满小于减设置成功"

        # time.sleep(1)
        # driver.find_element_by_id('site.weide.shopmanage:id/gd_full_cut_layout').click()
        # time.sleep(2)
        # driver.find_element_by_xpath("//android.widget.TextView[@text='元,立减']").click()
        # print "dianji lijian"
        # time.sleep(5)
        # driver.find_element_by_id('site.weide.shopmanage:id/gd_full_money').send_keys("0")
        # driver.find_element_by_id('site.weide.shopmanage:id/gd_cut_money').click()
        # driver.find_element_by_id('site.weide.shopmanage:id/gd_cut_money').send_keys('3')
        # driver.find_element_by_id("site.weide.shopmanage:id/submitBtn").click()
        # get_toast.find_Toast2(self, "优惠金额必须小于起始条件金额")
#立减（输入信息不完整）
    #满金额元素为空
        driver.implicitly_wait(5)
        self.login_page.click_lijian()
        driver.implicitly_wait(5)

        full=""
        self.login_page.input_gull_money(full)
        driver.implicitly_wait(5)
        cut="220"
        self.login_page.input_cut_money(cut)
        driver.implicitly_wait(5)
        self.login_page.click_submitBtn()
        self.get_toast.get_toast("请填写完整")
        time.sleep(2)
        sql ='SELECT fullprice,minprice,maxprice,cid FROM t_promotion_reduce_rule WHERE  cid =436'
        print  "zheli"
        # original_price = chaxunshujuku.shujuku(sql)
        original_price = self.database.query_database(sql)
        print original_price
        print original_price[0],original_price[1], original_price[2]
        if original_price[0] ==30 and original_price[1] ==10 and original_price[2]==20:
            print u"数据库显示立减（满元素为空）未设置成功"
        else:
            print u"ERROR：立减 满小于减设置成功"



        # time.sleep(1)
        # driver.find_element_by_id('site.weide.shopmanage:id/gd_full_cut_layout').click()
        # time.sleep(2)
        # driver.find_element_by_xpath("//android.widget.TextView[@text='元,立减']").click()
        # print "dianji lijian"
        # time.sleep(5)
        # driver.find_element_by_id('site.weide.shopmanage:id/gd_full_money').clear()
        # driver.find_element_by_id('site.weide.shopmanage:id/gd_cut_money').click()
        # driver.find_element_by_id('site.weide.shopmanage:id/gd_cut_money').send_keys('3')
        # driver.find_element_by_id("site.weide.shopmanage:id/submitBtn").click()
        # get_toast.find_Toast2(self, "请填写完整")
    #  减金额元素为空
        driver.implicitly_wait(5)
        self.login_page.click_lijian()
        driver.implicitly_wait(5)

        full=""
        self.login_page.input_gull_money(full)
        driver.implicitly_wait(5)
        cut="20"
        self.login_page.input_cut_money(cut)
        driver.implicitly_wait(5)
        self.login_page.click_submitBtn()
        self.get_toast.get_toast("请填写完整")
        time.sleep(2)
        sql ='SELECT fullprice,minprice,maxprice,cid FROM t_promotion_reduce_rule WHERE  cid =436'
        print  "zheli"
        # original_price = chaxunshujuku.shujuku(sql)
        original_price = self.database.query_database(sql)
        print original_price
        print original_price[0],original_price[1], original_price[2]
        if original_price[0] ==30 and original_price[1] ==10 and original_price[2]==20:
            print u"数据库显示立减（减元素为空）未设置成功"
        else:
            print u"ERROR：立减 满小于减设置成功"
    #     time.sleep(1)
    #     driver.find_element_by_id('site.weide.shopmanage:id/gd_full_cut_layout').click()
    #     time.sleep(2)
    #     driver.find_element_by_xpath("//android.widget.TextView[@text='元,立减']").click()
    #     print "dianji lijian"
    #     time.sleep(5)
    #     driver.find_element_by_id('site.weide.shopmanage:id/gd_full_money').send_keys("5")
    #     driver.find_element_by_id('site.weide.shopmanage:id/gd_cut_money').click()
    #     driver.find_element_by_id('site.weide.shopmanage:id/gd_cut_money').clear()
    #     driver.find_element_by_id("site.weide.shopmanage:id/submitBtn").click()
    #     get_toast.find_Toast2(self, "请填写完整")
    #     #满价格小于减价格
    #     time.sleep(1)
    #     driver.find_element_by_id('site.weide.shopmanage:id/gd_full_cut_layout').click()
    #     time.sleep(2)
    #     driver.find_element_by_xpath("//android.widget.TextView[@text='元,立减']").click()
    #     print "dianji lijian"
    #     time.sleep(5)
    #     driver.find_element_by_id('site.weide.shopmanage:id/gd_full_money').clear()
    #     driver.find_element_by_id('site.weide.shopmanage:id/gd_full_money').send_keys("6")
    #     driver.find_element_by_id('site.weide.shopmanage:id/gd_cut_money').click()
    #     driver.find_element_by_id('site.weide.shopmanage:id/gd_cut_money').send_keys("8")
    #     driver.find_element_by_id("site.weide.shopmanage:id/submitBtn").click()
    #     get_toast.find_Toast2(self, "优惠金额必须小于起始条件金额")
#随机减  元素为空  满a减b-c
        #a<b>c
        time.sleep(2)
        self.login_page.click_random()
        #driver.find_element_by_xpath("//android.widget.TextView[@text='元,随机减']").click()
        print u"随机减"
        time.sleep(2)
        sjfull='5'
        sjmax='8'
        sjmin='10'
        self.login_page.input_sjfull(sjfull)
        self.login_page.input_sjmax(sjmax)
        self.login_page.input_sjmin(sjmin)
        self.login_page.click_submitBtn()
        self.get_toast.get_toast("优惠金额必须小于起始条件金额")
        # driver.find_element_by_id('site.weide.shopmanage:id/sj_full_money').send_keys('30')
        # driver.find_element_by_id('site.weide.shopmanage:id/sj_cut_min_money').send_keys('10')
        # driver.find_element_by_id("site.weide.shopmanage:id/sj_cut_max_money").send_keys('20')
        # driver.find_element_by_id("site.weide.shopmanage:id/submitBtn").click()
        # get_toast.find_Toast2(self, "设置成功")
        sql = 'SELECT fullprice,minprice,maxprice,cid FROM t_promotion_reduce_rule WHERE  cid =436'
        # original_price = chaxunshujuku.shujuku(sql)
        original_price = self.database.query_database(sql)
        #print original_price
       # print original_price[0], original_price[1], original_price[2]
        if original_price[0] ==30 and original_price[1] ==10 and original_price[2]==20:
            print u"a<b<c设置失败"
        else:
            print u"a<b<c设置成功"


        #
        # time.sleep(2)
        # driver.find_element_by_xpath("//android.widget.TextView[@text='元,随机减']").click()
        # print u"随机减"
        # time.sleep(2)
        # driver.find_element_by_id('site.weide.shopmanage:id/sj_full_money').clear()
        # driver.find_element_by_id('site.weide.shopmanage:id/sj_full_money').send_keys('2')
        # driver.find_element_by_id('site.weide.shopmanage:id/sj_cut_min_money').clear()
        # driver.find_element_by_id('site.weide.shopmanage:id/sj_cut_min_money').send_keys('30')
        # driver.find_element_by_id("site.weide.shopmanage:id/sj_cut_max_money").clear()
        # driver.find_element_by_id("site.weide.shopmanage:id/sj_cut_max_money").send_keys('20')
        # driver.find_element_by_id("site.weide.shopmanage:id/submitBtn").click()
        # get_toast.find_Toast2(self, "设置成功")
#a>b<c
        time.sleep(2)
        self.login_page.click_random()
        #driver.find_element_by_xpath("//android.widget.TextView[@text='元,随机减']").click()
        print u"随机减"
        time.sleep(2)
        sjfull='12'
        sjmax='8'
        sjmin='10'
        self.login_page.input_sjfull(sjfull)
        self.login_page.input_sjmax(sjmax)
        self.login_page.input_sjmin(sjmin)
        self.login_page.click_submitBtn()
        self.get_toast.get_toast("优惠金额必须小于起始条件金额")
        # driver.find_element_by_id('site.weide.shopmanage:id/sj_full_money').send_keys('30')
        # driver.find_element_by_id('site.weide.shopmanage:id/sj_cut_min_money').send_keys('10')
        # driver.find_element_by_id("site.weide.shopmanage:id/sj_cut_max_money").send_keys('20')
        # driver.find_element_by_id("site.weide.shopmanage:id/submitBtn").click()
        # get_toast.find_Toast2(self, "设置成功")
        sql = 'SELECT fullprice,minprice,maxprice,cid FROM t_promotion_reduce_rule WHERE  cid =436'
        # original_price = chaxunshujuku.shujuku(sql)
        original_price = self.database.query_database(sql)
        #print original_price
       # print original_price[0], original_price[1], original_price[2]
        if original_price[0] ==30 and original_price[1] ==10 and original_price[2]==20:
            print u"a>b<c设置失败"
        else:
            print u"a>b<c设置成功"


        # time.sleep(2)
        # driver.find_element_by_xpath("//android.widget.TextView[@text='元,随机减']").click()
        # print u"随机减"
        # time.sleep(2)
        # driver.find_element_by_id('site.weide.shopmanage:id/sj_full_money').clear()
        # driver.find_element_by_id('site.weide.shopmanage:id/sj_full_money').send_keys('20')
        # driver.find_element_by_id('site.weide.shopmanage:id/sj_cut_min_money').clear()
        # driver.find_element_by_id('site.weide.shopmanage:id/sj_cut_min_money').send_keys('3')
        # driver.find_element_by_id("site.weide.shopmanage:id/sj_cut_max_money").clear()
        # driver.find_element_by_id("site.weide.shopmanage:id/sj_cut_max_money").send_keys('20')
        # driver.find_element_by_id("site.weide.shopmanage:id/submitBtn").click()
        # get_toast.find_Toast2(self, "设置成功")
#立减数据特殊字符
        #-

        time.sleep(2)
        self.login_page.click_random()
        #driver.find_element_by_xpath("//android.widget.TextView[@text='元,随机减']").click()
        print u"随机减"
        time.sleep(2)
        sjfull='-1'
        sjmax='%'
        sjmin='10'
        self.login_page.input_sjfull(sjfull)
        self.login_page.input_sjmax(sjmax)
        self.login_page.input_sjmin(sjmin)
        self.login_page.click_submitBtn()
        self.get_toast.get_toast("优惠金额必须小于起始条件金额")
        # driver.find_element_by_id('site.weide.shopmanage:id/sj_full_money').send_keys('30')
        # driver.find_element_by_id('site.weide.shopmanage:id/sj_cut_min_money').send_keys('10')
        # driver.find_element_by_id("site.weide.shopmanage:id/sj_cut_max_money").send_keys('20')
        # driver.find_element_by_id("site.weide.shopmanage:id/submitBtn").click()
        # get_toast.find_Toast2(self, "设置成功")
        sql = 'SELECT fullprice,minprice,maxprice,cid FROM t_promotion_reduce_rule WHERE  cid =436'
        # original_price = chaxunshujuku.shujuku(sql)
        original_price = self.database.query_database(sql)
        #print original_price
       # print original_price[0], original_price[1], original_price[2]
        if original_price[0] ==30 and original_price[1] ==10 and original_price[2]==20:
            print u"特殊数字设置失败"
        else:
            print u"特殊数字设置成功"
        #
        # time.sleep(1)
        # driver.find_element_by_id('site.weide.shopmanage:id/gd_full_cut_layout').click()
        # time.sleep(2)
        # driver.find_element_by_xpath("//android.widget.TextView[@text='元,立减']").click()
        # print "dianji lijian"
        # time.sleep(5)
        # driver.find_element_by_id('site.weide.shopmanage:id/gd_full_money').send_keys("-")
        # driver.find_element_by_id('site.weide.shopmanage:id/gd_cut_money').click()
        # driver.find_element_by_id('site.weide.shopmanage:id/gd_cut_money').send_keys('2')
        # driver.find_element_by_id("site.weide.shopmanage:id/submitBtn").click()
        # get_toast.find_Toast2(self, "设置成功")
        # #&
        # time.sleep(1)
        # driver.find_element_by_id('site.weide.shopmanage:id/gd_full_cut_layout').click()
        # time.sleep(2)
        # driver.find_element_by_xpath("//android.widget.TextView[@text='元,立减']").click()
        # print "dianji lijian"
        # time.sleep(5)
        # driver.find_element_by_id('site.weide.shopmanage:id/gd_full_money').send_keys("*")
        # driver.find_element_by_id('site.weide.shopmanage:id/gd_cut_money').click()
        # driver.find_element_by_id('site.weide.shopmanage:id/gd_cut_money').send_keys('&')
        # driver.find_element_by_id("site.weide.shopmanage:id/submitBtn").click()
        # get_toast.find_Toast2(self, "设置成功")








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

