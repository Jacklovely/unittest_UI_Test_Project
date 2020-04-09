#! user/bin/python
'''
Code description： auto run test case
Create time：
Developer：
'''

import unittest
from framfriend.test_case.models.testreport import *
from framfriend.test_case.models.sendmail import SendMail
from framfriend.test_case.models.sendmail import getReceiverInfo
from framfriend.test_case.LoginTc import Login_TC
from framfriend.test_case.JgTc import Jg_TC

 # 登录模块测试用例场景
class RunTcScript(object):
    """

    """
    def __init__(self):
        self.suite = unittest.TestSuite()
        # 2.---------------------------------
        # self.suite = addTc('login_TC.py')
        # 2.---------------------------------
    # # 登录模块测试用例
    # def load_login_tc(self,testcase):
    #     """
    #
    #     :param testcase:
    #     :return:
    #     """
    #     self.suite.addTest(Login_TC(testcase))

    #机构管理模块测试用例
    def load_Jg_tc(self,testcase):
        '''

        :param testcase:
        :return:
        '''
        self.suite.addTest(Jg_TC(testcase))

if __name__ =='__main__':
    # 1.2.3
    suite_tc = RunTcScript()
    # login test cases
    #suite_tc.load_login_tc('test_login_success_correct_username_password') # testcase 1 ： 登录成功
    suite_tc.load_Jg_tc('test_addnullJg_5')

    #3.输出到测试报告--------------------------------
    runner, fp, filename = testreport()
    runner.run(suite_tc.suite)
    # 3.--------------------------------------------
    fp.close()
    read_msg=getReceiverInfo(r'E:\python_test\framfriend_Test_Project\framfriend\data\TestData\mail_receiver.txt')
    sendmail = SendMail (read_msg)
    sendmail.sendEmail(filename)
    # 1.不输出到测试报告
    # runner = unittest.TextTestRunner(verbosity=2)# 输出详细信息
    # runner.run(suite_tc.suite)
    # fp.close()

    # 2. 输出测试报告 BeautifulReport---------------
    # 导入模块时需要使用绝对路径 否则报错
    # suite = addTc(rule='LoginTc.py')
    # runTc(suite)
    # 2 -------------------------------------------

