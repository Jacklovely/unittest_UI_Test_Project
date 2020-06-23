'''
Code description：转账查询模块 testcase
Create time：
Developer：
'''
import time
from selenium.webdriver.support.select import Select
import logging
from framfriend.test_case.models.log import Logger
from framfriend.test_case.models.myunittest import MyunitTest
from framfriend.test_case.page_obj.IntegratedQuery_page import IntegratedQuery_Page
log = Logger(__name__, CmdLevel=logging.INFO, FileLevel=logging.INFO)
class IntegratedQuery_Tc(MyunitTest):
    '''转账查询模块用例'''

    def test_query1(self):
        """按己方户名查询"""
        menu = IntegratedQuery_Page(self.driver)  # 实例化转账查询页面
        self.login.loginFunc()  # 登录
        menu.inIntegratedQuery()  # 进入转账查询页面
        time.sleep(3)
        menu.cBtn(menu.button_list[10])
        menu.cBtn(menu.button_list[11])
        menu.cBtn(menu.button_list[2])  # 点击查询按钮
        msgInfo = menu.getValue(*menu.msg[1])
        self.assertIn(menu.check_list[0],msgInfo, '查询成功')

    def test_query2(self):
        """按对方户名查询"""
        menu = IntegratedQuery_Page(self.driver)  # 实例化转账查询页面
        self.login.loginFunc()  # 登录
        menu.inIntegratedQuery()  # 进入转账查询页面
        time.sleep(3)
        menu.inputValue(menu.query_list[1],menu.valuesList[1])
        menu.cBtn(menu.button_list[2])  # 点击查询按钮
        msgInfo = menu.getValue(*menu.msg[1])
        self.assertIn(menu.check_list[1],msgInfo, '查询成功')

    def test_query2_1(self):
        """按不存在对方户名查询"""
        menu = IntegratedQuery_Page(self.driver)  # 实例化转账查询页面
        self.login.loginFunc()  # 登录
        menu.inIntegratedQuery()  # 进入转账查询页面
        time.sleep(3)
        menu.inputValue(menu.query_list[1],menu.valuesList[0])
        menu.cBtn(menu.button_list[2])  # 点击查询按钮
        msgInfo = menu.getValue(*menu.msg[1])
        self.assertIn(menu.check_list[3],msgInfo, '查询成功')

    def test_query3(self):
        """按摘要查询"""
        menu = IntegratedQuery_Page(self.driver)  # 实例化转账查询页面
        self.login.loginFunc()  # 登录
        menu.inIntegratedQuery()  # 进入转账查询页面
        time.sleep(3)
        menu.inputValue(menu.query_list[2],menu.valuesList[2])
        menu.cBtn(menu.button_list[2])  # 点击查询按钮
        msgInfo = menu.getValue(*menu.msg[1])
        self.assertIn(menu.check_list[2],msgInfo, '查询成功')

    def test_query2(self):
        """按不存在摘要查询"""
        menu = IntegratedQuery_Page(self.driver)  # 实例化转账查询页面
        self.login.loginFunc()  # 登录
        menu.inIntegratedQuery()  # 进入转账查询页面
        time.sleep(3)
        menu.inputValue(menu.query_list[2],menu.valuesList[0])
        menu.cBtn(menu.button_list[2])  # 点击查询按钮
        msgInfo = menu.getValue(*menu.msg[1])
        self.assertIn(menu.check_list[3],msgInfo, '查询成功')

    # def test_time_query2(self):
    #     '''订单开始时间查询'''
    #     menu = IntegratedQuery_Page(self.driver)  # 实例化转账查询页面
    #     self.login.loginFunc()  # 登录
    #     menu.inIntegratedQuery()  # 进入转账查询页面
    #     time.sleep(3)
    #     '''设置订单开始时间'''
    #     menu.cBtn(menu.button_list[0])#开始时间
    #     menu.cBtn(menu.button_list[4])#切换年
    #     menu.cBtn(menu.button_list[5])#切换月
    #     menu.cBtn(menu.button_list[6])#选择日
    #     menu.cBtn(menu.button_list[7])#确定
    #     menu.cBtn(menu.button_list[1])#截止时间
    #     menu.cBtn(menu.button_list[8])#现在
    #     menu.cBtn(menu.button_list[2])#点击查询按钮
    #     time.sleep(3)
    #     flag = menu.isElementExist(menu.msg[1])
    #     self.assertTrue(flag,'查询验证')
    #     if flag:
    #         msgInfo = menu.getValue(*menu.msg[1])
    #         self.assertEqual(msgInfo, '显示第 1 到第 10 条记录，总共 22 条记录', '查询成功')

    def test_state_query3_1(self):
        '''交易状态支付中查询'''
        menu = IntegratedQuery_Page(self.driver)  # 实例化转账查询页面
        self.login.loginFunc()  # 登录
        menu.inIntegratedQuery()  # 进入转账查询页面
        time.sleep(3)
        state = self.driver.find_element_by_xpath('//*[@id="searchForm"]/div[5]/select')
        Select(state).select_by_value('0')  # 获取下拉选
        menu.cBtn(menu.button_list[2])  # 点击[查询]
        time.sleep(1)
        msgInfo1 = menu.getValue(*menu.msg[1])
        self.assertIn(menu.check_list[4],msgInfo1, '查询成功')

    def test_state_query3_2(self):
        '''交易状态已受理查询'''
        menu = IntegratedQuery_Page(self.driver)  # 实例化转账查询页面
        self.login.loginFunc()  # 登录
        menu.inIntegratedQuery()  # 进入转账查询页面
        time.sleep(3)
        state = self.driver.find_element_by_xpath('//*[@id="searchForm"]/div[5]/select')
        Select(state).select_by_value('1')  # 获取下拉选
        menu.cBtn(menu.button_list[2])  # 点击[查询]
        time.sleep(1)
        msgInfo2 = menu.getValue(*menu.msg[1])
        self.assertIn(menu.check_list[5], msgInfo2, '查询成功')

    def test_state_query3_3(self):
        '''交易状态支付成功查询'''
        menu = IntegratedQuery_Page(self.driver)  # 实例化转账查询页面
        self.login.loginFunc()  # 登录
        menu.inIntegratedQuery()  # 进入转账查询页面
        time.sleep(3)
        state = self.driver.find_element_by_xpath('//*[@id="searchForm"]/div[5]/select')
        Select(state).select_by_value('2')  # 获取下拉选
        menu.cBtn(menu.button_list[2])  # 点击[查询]
        time.sleep(1)
        msgInfo3 = menu.getValue(*menu.msg[1])
        self.assertIn(menu.check_list[6], msgInfo3, '查询成功')
    
    def test_state_query3_4(self):
        '''交易状态支付失败查询'''
        menu = IntegratedQuery_Page(self.driver)  # 实例化转账查询页面
        self.login.loginFunc()  # 登录
        menu.inIntegratedQuery()  # 进入转账查询页面
        time.sleep(3)
        state = self.driver.find_element_by_xpath('//*[@id="searchForm"]/div[5]/select')
        Select(state).select_by_value('3')  # 获取下拉选
        menu.cBtn(menu.button_list[2])  # 点击[查询]
        time.sleep(1)
        msgInfo4 = menu.getValue(*menu.msg[1])
        self.assertIn(menu.check_list[7], msgInfo4, '查询成功')

    def test_dataprint(self):
        '''点击订单后打印按钮'''
        menu = IntegratedQuery_Page(self.driver)  # 实例化转账查询页面
        self.login.loginFunc()  # 登录
        menu.inIntegratedQuery()  # 进入转账查询页面
        time.sleep(3)
        menu.cBtn(menu.dataprint)#点击数据后打印按钮
        time.sleep(2)
        # flag = menu.isElementExist(menu.msg[2])
        # self.assertTrue(flag,'弹出打印页面')

    def test_bulkprint_1(self):
        '''单数据点击批量打印'''
        menu = IntegratedQuery_Page(self.driver)  # 实例化转账查询页面
        self.login.loginFunc()  # 登录
        menu.inIntegratedQuery()  # 进入转账查询页面
        time.sleep(3)
        menu.cBtn(menu.checkbox_list[0])#选择一项
        menu.cBtn(menu.button_list[3])#点击批量打印
        time.sleep(2)
        # flag = menu.isElementExist(menu.msg[2])
        # self.assertTrue(flag, '弹出打印页面')

    def test_bulkprint_2(self):
        '''全选点击批量打印'''
        menu = IntegratedQuery_Page(self.driver)  # 实例化转账查询页面
        self.login.loginFunc()  # 登录
        menu.inIntegratedQuery()  # 进入转账查询页面
        time.sleep(3)
        menu.cBtn(menu.checkbox_list[1])#全选
        menu.cBtn(menu.button_list[3])#点击批量打印
        time.sleep(2)
        # flag = menu.isElementExist(menu.msg[2])
        # self.assertTrue(flag, '弹出打印页面')

if __name__=='__main__':
    pass

