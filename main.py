#!/user/bin/python
# -*-coding:utf-8-*-

import unittest
import HTMLTestRunner
from common import send_email
import os,glob
#相对路径
testcase_path = ".\\testcase"
report_path = ".\\report\\appium_report.html"


def creat_suite():
    suite = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(testcase_path,pattern="test_*.py")
    for test_suite in discover:
        # print(test_suite)
        for test_case in test_suite:
            suite.addTest(test_case)
    return suite

suite = creat_suite()
fp = open(report_path,"w+")
runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title=u"测试结果",description=u"简店test")
runner.run(suite)
fp.close()



email=send_email.Send_mail()

email.send_mail('D:\\Users\Asus\\PycharmProjects\\untitled1\\jiandiandenglu\\report\\appium_report.html')
#
# if __name__=="__main__":
#     suite = unittest.TestSuite()
#     discover = unittest.defaultTestLoader.discover(testcase_path,pattern="test_*.py")
#     for test_suite in discover:
#         # print(test_suite)
#         for test_case in test_suite:
#             suite.addTest(test_case)


