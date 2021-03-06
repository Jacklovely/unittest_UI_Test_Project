'''
Code description：unittest framwork
Create time：
Developer：
'''
from selenium import webdriver

from framfriend.test_case.models.driver import WDriver
import logging
import unittest
from framfriend.test_case.page_obj.login_page import LoginPage
from framfriend.test_case.models.log import Logger

log = Logger(__name__, CmdLevel=logging.INFO, FileLevel=logging.INFO)
class MyunitTest(unittest.TestCase):
    """

    """

    @classmethod
    def setUpClass(cls): # 一个测试类(文件)执行一次打开浏览器, 节约每个用例打开一次浏览器的时间

        cls.driver = WDriver().chromeDriver()
        cls.driver.maximize_window()
        log.logger.info('opened the browser successed!')
    # ----------------------------

    def setUp(self):
        """

        :return:
        """
        self.login = LoginPage(self.driver)
        self.login.open()
        log.logger.info('************************starting run test cases************************')

    def tearDown(self):
        """

        :return:
        """
        self.driver.refresh()
        log.logger.info('************************test case run completed************************')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        log.logger.info('quit the browser success!')
    #----------------------------
if __name__ == '__main__':
    unittest.main()
