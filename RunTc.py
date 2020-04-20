#! user/bin/python

'''                                                           
Code description：auto run test case
Create time：
Developer：
'''

import unittest
import time
from BeautifulReport import BeautifulReport
from framfriend.config.conf import *
from framfriend.test_case.models.sendmail import SendMail, getReceiverInfo
from framfriend.test_case.models.testreport import testreport

# TODO : will be use jenkins continuous intergration teachnology manage the auto project
if __name__ == '__main__':

    # currTime = time.strftime('%Y-%m-%d %H_%M_%S')
    # filename = currTime + '.html'
    # # 第一种测试报告
    # test_suite = unittest.defaultTestLoader.discover(tcPath, pattern='*Tc.py')
    # result = BeautifulReport(test_suite)
    # result.report(filename= filename, description='test report', log_psath=reportPath)

    # # 第二种测试报告
    runner, fp, fileName = testreport()
    test_suite = unittest.defaultTestLoader.discover(tcPath, pattern='register.py')
    runner.run(test_suite)
    fp.close()
    # read_msg = getReceiverInfo(r'E:\python_test\framfriend_Test_Project\framfriend\data\TestData\mail_receiver.txt')
    # sendmail = SendMail(read_msg)
    # sendmail.sendEmail(fileName)