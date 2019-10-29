'''
Code description： login page
Create time：
Developer：
'''
import time
from selenium.webdriver.common.by import By
import logging
import sys
from framfriend.test_case.page_obj.base_page import BasePage, eleData, testLoginData
from selenium.webdriver.common.action_chains import ActionChains
from framfriend.test_case.models.log import Logger
from selenium.webdriver.support.ui import Select
log = Logger(__name__, CmdLevel=logging.INFO, FileLevel=logging.INFO)


class LoginPage(BasePage):

    """用户名，密码，登录按钮，保存信息，错误提示"""
    userNameEle = (By.NAME, eleData.readExcel(1, 3))
    passWordEle = (By.NAME, eleData.readExcel(2, 3))
    loginBtnEle = (By.XPATH, eleData.readExcel(3, 3))
    selectKitEle = (By.XPATH, eleData.readExcel(4, 3))
    errorMessage = (By.ID, eleData.readExcel(5, 3))
    userEle = (By.XPATH, eleData.readExcel(6,3))
    userEle2 = (By.XPATH, eleData.readExcel(7,3))
    signoutEle = (By.XPATH, eleData.readExcel(8,3))
    quitkEle = (By.XPATH,eleData.readExcel(9,3))
    deterQuitEle =(By.ID,eleData.readExcel(10,3))

    # 用户名和密码
    unpwData = \
        [[testLoginData.readExcel(1, 0), int (testLoginData.readExcel(1, 1))],# 正确的用户名和正确的密码
         [testLoginData.readExcel(2, 0), int (testLoginData.readExcel(2, 1))],# 错误的用户名和正确的密码
         [testLoginData.readExcel(3, 0), int (testLoginData.readExcel(3, 1))],# 空的用户名和正确的密码
         [testLoginData.readExcel(4, 0), testLoginData.readExcel(4, 1)],# 错误的用户名和错误的密码
         [testLoginData.readExcel(5, 0), testLoginData.readExcel(5, 1)],# 正确的用户名和空密码
         [testLoginData.readExcel(6, 0), testLoginData.readExcel(6, 1)],# 正确的用户名和错误的密码
         [testLoginData.readExcel(7, 0), testLoginData.readExcel(7, 1)]]# 空用户名和空密码

    #选择套件
    def selectKit(self):
        '''

        :return:
        '''
        #定位下拉框
        Select(self.driver.find_element_by_xpath('//*[@id="accounts_select"]')).select_by_value('00010101')
        # 登录按钮
    def clickLoginBtn(self):
        """

        :return:
        """
        element = self.findElement(*self.loginBtnEle)
        element.click()
        log.logger.info('%s ,logining....!' % sys._getframe().f_code.co_name)
    # 登录失败时提示
    def getFailedText(self):
        """
        :return:
        """
        info = self.findElement(*self.errorMessage).text
        log.logger.info('login failed : %s' %info)
        return info

    # 统一登录函数
    def loginFunc(self, username='admin', password='123456'):
        """
        :param username:
        :param cipher:
        :return:
        """
        self.inputValue(self.userNameEle, username)
        self.inputValue(self.passWordEle, password)
        time.sleep(1)
        # self.selectKit()
        self.clickLoginBtn()

    # 清空输入框数据
    def clearValue(self, element):

        empty = self.findElement(*element)
        empty.clear()
        log.logger.info('emptying value.......')


    # 退出
    def quit(self):
        time.sleep(3)
        user= self.findElement(*self.userEle)
        user.click()
        ul = self.findElement(*self.userEle2)
        ul.self.findElement(*self.signoutEle).click()
        tc = self.findElement(*self.quitkEle)
        tc.self.findElement(*self.deterQuitEle).click()
        log.logger.info('quit')

if __name__ == '__main__':
    pass