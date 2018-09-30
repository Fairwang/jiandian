#!user/bin/python
# coding: utf-8

from selenium import webdriver
import time
#若是浏览器打开后，没有firebug，以下为启用
# profile_directory=r"C:\Users\Asus\AppData\Roaming\Mozilla\Firefox\Profiles\m34kktik.default"
# profile=webdriver.FirefoxProfile(profile_directory)
# driver=webdriver.Firefox(profile)


driver=webdriver.Firefox()
driver.get("https://www.baidu.com")
time.sleep(3)
driver.refresh()
driver.get("http://www.hordehome.com")
time.sleep(2)
driver.back()
driver.forward()
driver.set_window_size(540,960)
time.sleep(2)
driver.maximize_window()
driver.get_screenshot_as_file("D:\\b1.jpg")



