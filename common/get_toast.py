#!/user/bin/python
# -*-coding:utf-8-*-
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import logging

logging.getLogger().setLevel(logging.INFO)
class get_toast():
    def __init__(self,driver):
        self.driver=driver
    def get_toast(self,message):
        try:
            logging.info("need find is:%s" % (message))
            message='//*[@text=\'{}\']'.format(message)
            WebDriverWait(self.driver,5,0.5).until(expected_conditions.presence_of_element_located((By.XPATH,message)))
            logging.info("pass:%s"%message)

            return True
        except:
            logging.info("ERROR :%s"%message)
            # logging.info("ERROR")
            return False






