#!/user/bin/python
#  -*-coding:utf-8-*-

from appium import webdriver

class driver_configure():
    def get_driver(self):
        try:
            desired_caps = {}
            desired_caps['platformName'] = 'Android'
            desired_caps['platfromVersion'] = '7.1.1'
            desired_caps['deviceName'] = '33d04c7c'
            desired_caps['appPackage'] = 'site.weide.shopmanage'
            desired_caps['automationName'] = 'uiautomator2'  ##############
            desired_caps['appActivity'] = 'site.weide.shopmanage.Activity.GuideActivity'
            # desired_caps['appActivity']='site.weide.shopmanage.Mactivity'
            self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
            return self.driver
        except Exception,e:
            raise e