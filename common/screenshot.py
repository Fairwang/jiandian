#!user/bin/python
# coding: utf-8
from selenium import webdriver
import os

# class screenshot():
#     def __int__(self,driver):
#         self.driver=driver
def screenshot(driver,filename):
    # driver=self.driver
    base=os.path.dirname(__file__)
    base=base.split('/common')[0]
    file_path=base+"/report/screenshot/"+filename
    driver.get_screenshot_as_file(file_path)

if __name__=='__main__':
    driver=webdriver.Firefox()
    driver.get("http://www.baidu.com")
    screenshot(driver,'baidu.png')
    driver.quit()
