#!/user/bin/python
# -*-coding:utf-8-*-
import base_page
from appium import webdriver
from selenium.webdriver.common.by import By
from appium import webdriver

#"登录页面"
class login_page(base_page.BaseAaction):
    def __init__(self,driver):
        self.driver=driver

# 登录
    user_loc=(By.ID,'site.weide.shopmanage:id/editText_login_usermobile')
    pws_loc=(By.ID,'site.weide.shopmanage:id/editText_login_userpass')
    btnlogin_loc=(By.ID,'site.weide.shopmanage:id/button_login_login')
    def input_user(self,username):
        self.send_keys(username,*self.user_loc)
    def input_pws(self,password):
        self.send_keys(password,*self.pws_loc)
    def click_btnlogin(self):
        self.click(*self.btnlogin_loc)

#单据
    danju_loc=(By.ID,'site.weide.shopmanage:id/activity_base_tab3_group')
    order_loc=(By.XPATH,"//android.widget.LinearLayout[@index='0']")
    order_price=(By.ID,'site.weide.shopmanage:id/order_price')
    ispay_price=(By.ID,'site.weide.shopmanage:id/bill_states')
    payway_price=(By.ID,'site.weide.shopmanage:id/transaction_mode')
    # paytype_loc=(By.ID,'')

    def click_danju(self):
        self.click(*self.danju_loc)
    def click_order(self):
        self.click(*self.order_loc)
    # def click



#营销活动界面
    active_loc=(By.ID ,'site.weide.shopmanage:id/active')
    def click_active(self):
        self.click(*self.active_loc)

#满减活动页面
    fullcut_loc=(By.ID,'site.weide.shopmanage:id/full_cut')
    def click_fullcut(self):
        self.click(*self.fullcut_loc)
    #原价
    original_loc=(By.ID,'site.weide.shopmanage:id/original_price_layout')
    def click_original(self):
        self.click(*self.original_loc)


#立减
    gd_full_loc = (By.ID, 'site.weide.shopmanage:id/gd_full_cut_layout')
    lijian_loc = (By.XPATH, "//android.widget.TextView[@text='元,立减']")
    #满价格
    gd_full_money=(By.ID,"site.weide.shopmanage:id/gd_full_money")
    gd_cut_money=(By.ID,'site.weide.shopmanage:id/gd_cut_money')
    gd_submitBtn=(By.ID,'site.weide.shopmanage:id/submitBtn')

    def click_gd_full(self):
        self.click(*self.gd_full_loc)

    def click_lijian(self):
        self.click(*self.lijian_loc)

    def input_gull_money(self,gull):
        self.send_keys(gull,*self.gd_full_money)

    def input_cut_money(self,cut):
        self.send_keys(cut,*self.gd_cut_money)

    def click_submitBtn(self):
        self.click(*self.gd_submitBtn)

#随机减
    random_reduce=(By.XPATH,"//android.widget.TextView[@text='元,随机减']")
    sj_full_money=(By.ID,"site.weide.shopmanage:id/sj_full_money")
    sj_min_money=(By.ID,'site.weide.shopmanage:id/sj_cut_min_money')
    sj_max_money = (By.ID, 'site.weide.shopmanage:id/sj_cut_max_money')



    def click_random(self):
        self.click(*self.random_reduce)
    def input_sjfull(self,sjfull):
        self.send_keys(sjfull,*self.sj_full_money)
    def input_sjmin(self, sjmin):
        self.send_keys(sjmin, *self.sj_min_money)
    def input_sjmax(self, sjmax):
        self.send_keys(sjmax, *self.sj_max_money)




#我的

    wode_loc=(By.ID,"site.weide.shopmanage:id/activity_base_tab4_group")
    member_loc=(By.XPATH,"//android.widget.LinearLayout[@index='7']")
    store_loc=(By.ID,"site.weide.shopmanage:id/stored_value_ll")#储值
    opensend_loc=(By.ID,"site.weide.shopmanage:id/isOpenSend")
    add_loc=(By.ID,"site.weide.shopmanage:id/add_layout")
    reduce_loc=(By.ID,"site.weide.shopmanage:id/reduce_img")
    submit_loc=(By.ID,"site.weide.shopmanage:id/submit_btn")
    chongzhi01_loc=(By.ID,"site.weide.shopmanage:id/recharge_tx1")
    send01_loc=(By.ID,"site.weide.shopmanage:id/send_tx1")
    chongzhi_loc=(By.ID,"site.weide.shopmanage:id/recharge_tx")
    send_loc=(By.ID,"site.weide.shopmanage:id/send_tx")
    button2_loc=(By.ID,"android:id/button2")
    chongzhi4_loc=(By.XPATH,"//android.widget.EditText[@index='25']")
    send4_loc=(By.XPATH,"//android.widget.EditText[@index='27']")
    #tishi_loc=(By.XPATH,"//android.widget.TextView[@text='确认要关闭吗?']")


#判断函数是否存在

    def isElementExit(self,*element_loc):
        flag=True
        try:
            self.find_element(*element_loc)
            return flag
        except:
            flag=False
            return  flag


    def wode_click(self):
        self.driver.implicitly_wait(2)
        self.click(*self.wode_loc)

    def member_click(self):
        self.driver.implicitly_wait(2)
        self.click(*self.member_loc)

#储值设置
    def store_click(self):
        self.driver.implicitly_wait(2)
        self.click(*self.store_loc)

    def opensend_click(self):
        self.driver.implicitly_wait(2)
        self.click(*self.opensend_loc)

    def add_click(self):
        self.driver.implicitly_wait(2)
        self.click(*self.add_loc)
    def reduce_click(self):
        self.driver.implicitly_wait(2)
        self.click(*self.reduce_loc)

    def submit_click(self):
        self.driver.implicitly_wait(2)
        self.click(*self.submit_loc)

    def chongzhi01_input(self,chongzhi):
        self.driver.implicitly_wait(2)
        self.send_keys(chongzhi,*self.chongzhi01_loc)



    def send01_input(self,send):
        self.driver.implicitly_wait(2)
        self.send_keys(send,*self.send01_loc)

    def chongzhi_input(self,chongzhi):
        self.driver.implicitly_wait(2)
        self.send_keys(chongzhi,*self.chongzhi_loc)


    def send_input(self,send):
        self.driver.implicitly_wait(2)
        self.send_keys(send,*self.send_loc)

    def button2_click(self):
        self.click(*self.button2_loc)

    def chongzhi4_input(self,chongzhi):
        self.send_keys(chongzhi,*self.chongzhi_loc)

    def send4_input(self,send):
        self.send_keys(send,*self.send4_loc)


    #周报
    zhoubao_loc=(By.XPATH,"//android.widget.TextView[@text='周报']")


    def zhoubao_click(self):
        self.click(*self.zhoubao_loc)








