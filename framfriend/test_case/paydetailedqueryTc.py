'''
Code description : 代付明细查询 testcase
Create time:
Developer:
'''
import os
import time
from selenium.webdriver.support.select import Select
from framfriend.test_case.models.myunittest import MyunitTest
from framfriend.test_case.page_obj.paydetailedquery_page import PayDetailedQuery_Page

class PayDetaileQuery_TC(MyunitTest):
    '''代付明细查询'''
    def test_detailedquery_1(self):
        '''己方银行查询'''
        menu = PayDetailedQuery_Page(self.driver)#实例化代付明细查询页面
        self.login.loginFunc()#登录
        menu.inpaydetailedquery()#进入代付明细查询页面
        time.sleep(2)
        menu.cBtn(menu.button_list[0])
        menu.cBtn(menu.button_list[1])
        menu.cBtn(menu.button_list[2])  # 点击查询按钮
        msgInfo = menu.getValue(*menu.msg_list[0])
        self.assertIn(menu.valuelist[4], msgInfo, '提示信息正确')

    def test_detailedquery_2(self):
        '''正确收款账号查询'''
        menu = PayDetailedQuery_Page(self.driver)#实例化代付明细查询页面
        self.login.loginFunc()#登录
        menu.inpaydetailedquery()#进入代付明细查询页面
        time.sleep(2)
        menu.inputValue(menu.input_list[0],menu.valuelist[3])
        menu.cBtn(menu.button_list[2])  # 点击查询按钮
        msgInfo = menu.getValue(*menu.msg_list[0])
        self.assertIn(menu.valuelist[3], msgInfo, '提示信息正确')

    def test_detailedquery_3(self):
        '''错误收款账号查询'''
        menu = PayDetailedQuery_Page(self.driver)  # 实例化代付明细查询页面
        self.login.loginFunc()  # 登录
        menu.inpaydetailedquery()  # 进入代付明细查询页面
        time.sleep(2)
        menu.inputValue(menu.input_list[0], menu.valuelist[1])
        menu.cBtn(menu.button_list[2])  # 点击查询按钮
        time.sleep(1)
        msgInfo = menu.getValue(*menu.msg_list[1])
        self.assertIn(menu.assertlist[0], msgInfo, '提示信息正确')

    def test_detailedquery_4(self):
        '''正确收款人查询'''
        menu = PayDetailedQuery_Page(self.driver)  # 实例化代付明细查询页面
        self.login.loginFunc()  # 登录
        menu.inpaydetailedquery()  # 进入代付明细查询页面
        time.sleep(2)
        menu.inputValue(menu.input_list[1], menu.valuelist[2])
        menu.cBtn(menu.button_list[2])  # 点击查询按钮
        time.sleep(1)
        msgInfo = menu.getValue(*menu.msg_list[0])
        self.assertIn(menu.valuelist[2], msgInfo, '提示信息正确')

    def test_detailedquery_5(self):
        '''错误收款人查询'''
        menu = PayDetailedQuery_Page(self.driver)  # 实例化代付明细查询页面
        self.login.loginFunc()  # 登录
        menu.inpaydetailedquery()  # 进入代付明细查询页面
        time.sleep(2)
        menu.inputValue(menu.input_list[1], menu.valuelist[0])
        menu.cBtn(menu.button_list[2])  # 点击查询按钮
        time.sleep(1)
        msgInfo = menu.getValue(*menu.msg_list[1])
        self.assertIn(menu.assertlist[0], msgInfo, '提示信息正确')

    def test_detailedquery_6(self):
        '''正确摘要查询'''
        menu = PayDetailedQuery_Page(self.driver)  # 实例化代付明细查询页面
        self.login.loginFunc()  # 登录
        menu.inpaydetailedquery()  # 进入代付明细查询页面
        time.sleep(2)
        menu.inputValue(menu.input_list[2], menu.assertlist[1])
        menu.cBtn(menu.button_list[2]) # 点击查询按钮
        time.sleep(1)
        msgInfo = menu.getValue(*menu.msg_list[0])
        self.assertIn(menu.assertlist[1], msgInfo, '提示信息正确')

    def test_detailedquery_7(self):
        '''错误摘要查询'''
        menu = PayDetailedQuery_Page(self.driver)  # 实例化代付明细查询页面
        self.login.loginFunc()  # 登录
        menu.inpaydetailedquery()  # 进入代付明细查询页面
        time.sleep(2)
        menu.inputValue(menu.input_list[2], menu.valuelist[0])
        menu.cBtn(menu.button_list[2])  # 点击查询按钮
        time.sleep(1)
        msgInfo = menu.getValue(*menu.msg_list[1])
        self.assertIn(menu.assertlist[0], msgInfo, '提示信息正确')

    def test_detailedquery_8(self):
        '''支付结果查询'''
        menu = PayDetailedQuery_Page(self.driver)  # 实例化代付明细查询页面
        self.login.loginFunc()  # 登录
        menu.inpaydetailedquery()  # 进入代付明细查询页面
        time.sleep(2)
        result = self.driver.find_element_by_xpath('//*[@id="searchForm5"]/div[5]/select')
        Select(result).select_by_value('受理')
        menu.cBtn(menu.button_list[2])  # 点击查询按钮
        time.sleep(1)
        msgInfo = menu.getValue(*menu.msg_list[0])
        self.assertIn(menu.valuelist[5], msgInfo, '提示信息正确')

if __name__ == '__main__':
    pass