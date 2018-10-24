#!/user/bin/python
# -*-coding:utf-8-*-

from appium import webdriver


class gesture_mainpulation():

    def swipeRight(self,driver):
        x = driver.get_window_size()['width']
        y = driver.get_window_size()['height']
        driver.swipe(int(x * 0.95), int(y * 0.25), int(x * 0.25), int(y * 0.25), 5000)

    def swipeLeft(self,driver):
        x = driver.get_window_size()['width']
        y = driver.get_window_size()['height']
        driver.swipe(int(x * 0.25), int(y * 0.25), int(x * 0.97), int(y * 0.25), 5000)

    def swipeUp(self, driver):
        x = driver.get_window_size()['width']
        y = driver.get_window_size()['height']
        driver.swipe(int(x * 0.25), int(y * 0.95), int(x * 0.25), int(y * 0.25), 5000)

    def swipeDown(self, driver):
        x = driver.get_window_size()['width']
        y = driver.get_window_size()['height']
        driver.swipe(int(x * 0.95), int(y * 0.25), int(x * 0.25), int(y * 0.95), 5000)