'''
Code description：合同期限预警取消模块 testcase
Create time：
Developer：
'''
import time

from selenium.webdriver.support.select import Select

from framfriend.test_case.models.myunit import MyunitTest
from framfriend.test_case.page_obj.termwarning_page import Termwarning_page
class Termwarning_Tc(MyunitTest):
    '''合同期限预警取消用例'''

    def test_alone_query_1_1(self):
        """正确合同号查询"""
        menu = Termwarning_page(self.driver)  # 实例化合同期限预警取消页面
        self.login.loginFunc()  # 登录
        menu.intermwarning()  # 进入合同期限预警取消页面
        time.sleep(3)
        menu.cBtn(menu.button_list[0])
        menu.inputValue(menu.query_list[0],menu.valuesList[0])
        menu.cBtn(menu.button_list[1])  # 点击[查询]
        time.sleep(1)
        msgInfo = menu.getValue(*menu.msg_list[0])
        self.assertIn(menu.valuesList[0], msgInfo, '查询成功')

    def test_alone_query_1_2(self):
        """错误合同号查询"""
        menu = Termwarning_page(self.driver)  # 实例化合同期限预警取消页面
        self.login.loginFunc()  # 登录
        menu.intermwarning()  # 进入合同期限预警取消页面
        time.sleep(3)
        menu.cBtn(menu.button_list[0])
        menu.inputValue(menu.query_list[0], menu.valuesList[1])
        menu.cBtn(menu.button_list[1])  # 点击[查询]
        time.sleep(2)
        msginfo = menu.getValue(*menu.msg_list[1])
        self.assertIn(menu.assertlist[0], msginfo, '查询成功')

    def test_alone_query_1_3(self):
        """正确合同名称查询"""
        menu = Termwarning_page(self.driver)  # 实例化合同期限预警取消页面
        self.login.loginFunc()  # 登录
        menu.intermwarning()  # 进入合同期限预警取消页面
        time.sleep(3)
        menu.cBtn(menu.button_list[0])
        menu.inputValue(menu.query_list[1],menu.valuesList[1])
        menu.cBtn(menu.button_list[1])  # 点击[查询]
        time.sleep(1)
        msgInfo = menu.getValue(*menu.msg_list[0])
        self.assertIn(menu.valuesList[1], msgInfo, '查询成功')

    def test_alone_query_1_4(self):
        """错误合同名称查询"""
        menu = Termwarning_page(self.driver)  # 实例化合同期限预警取消页面
        self.login.loginFunc()  # 登录
        menu.intermwarning()  # 进入合同期限预警取消页面
        time.sleep(3)
        menu.cBtn(menu.button_list[0])
        menu.inputValue(menu.query_list[1], menu.valuesList[0])
        menu.cBtn(menu.button_list[1])  # 点击[查询]
        time.sleep(2)
        msginfo = menu.getValue(*menu.msg_list[1])
        self.assertIn(menu.assertlist[0], msginfo, '查询成功')

    def test_alone_query_1_5(self):
        """正确客户名称查询"""
        menu = Termwarning_page(self.driver)  # 实例化合同期限预警取消页面
        self.login.loginFunc()  # 登录
        menu.intermwarning()  # 进入合同期限预警取消页面
        time.sleep(3)
        menu.cBtn(menu.button_list[0])
        menu.inputValue(menu.query_list[2],menu.valuesList[2])
        menu.cBtn(menu.button_list[1])  # 点击[查询]
        time.sleep(1)
        msgInfo = menu.getValue(*menu.msg_list[0])
        self.assertIn(menu.valuesList[2], msgInfo, '查询成功')

    def test_alone_query_1_6(self):
        """错误客户名称查询"""
        menu = Termwarning_page(self.driver)  # 实例化合同期限预警取消页面
        self.login.loginFunc()  # 登录
        menu.intermwarning()  # 进入合同期限预警取消页面
        time.sleep(3)
        menu.cBtn(menu.button_list[0])
        menu.inputValue(menu.query_list[2], menu.valuesList[0])
        menu.cBtn(menu.button_list[1])  # 点击[查询]
        time.sleep(2)
        msginfo = menu.getValue(*menu.msg_list[1])
        self.assertIn(menu.assertlist[0], msginfo, '查询成功')

    # def test_account_query_2(self):
    #     """签订时间查询"""
    #     menu = Termwarning_page(self.driver)  # 实例化明细账页面
    #     self.login.loginFunc()  # 登录
    #     menu.intermwarning()  # 进入明细账页面
    #     time.sleep(3)
    #     menu.cBtn(menu.button_list[0])
    #     # 选择时间2018-10-1-2019-9-1
    #     menu.cBtn(menu.time_list[0])
    #     menu.cBtn(menu.time_list[2])
    #     menu.cBtn(menu.time_list[3])
    #     menu.cBtn(menu.time_list[6])
    #     menu.cBtn(menu.time_list[1])
    #     menu.cBtn(menu.time_list[4])
    #     menu.cBtn(menu.time_list[5])
    #     menu.cBtn(menu.time_list[6])
    #     menu.cBtn(menu.button_list[1])  # 查询
    #     time.sleep(1)
    #     msgInfo = menu.getValue(*menu.msg_list[1])
    #     self.assertEqual(msgInfo, '显示第 1 到第 10 条记录，总共 123 条记录', '查询正确')

    def test_account_query_3(self):
        """经手人查询"""
        menu = Termwarning_page(self.driver)  # 实例化合同期限预警取消页面
        self.login.loginFunc()  # 登录
        menu.intermwarning()  # 进入合同期限预警取消页面
        time.sleep(3)
        menu.cBtn(menu.button_list[0])
        account = self.driver.find_element_by_xpath('//*[@id="hand_man"]')
        Select(account).select_by_value('f245671f723e47e492058ce2f2cacee4')  # 获取下拉选
        menu.cBtn(menu.button_list[1])  # 查询
        time.sleep(1)
        msgInfo = menu.getValue(*menu.msg_list[1])
        self.assertIn(menu.assertlist[1],msgInfo, '查询正确')

    def test_years_query_4(self):
        """收款状态查询"""
        menu = Termwarning_page(self.driver)  # 实例化合同期限预警取消页面
        self.login.loginFunc()  # 登录
        menu.intermwarning()  # 进入合同期限预警取消页面
        time.sleep(3)
        menu.cBtn(menu.button_list[0])
        years = self.driver.find_element_by_xpath('//*[@id="searchForm"]/div[6]/select')
        Select(years).select_by_value('0')  # 获取下拉选
        menu.cBtn(menu.button_list[1])  # 查询
        time.sleep(1)
        msgInfo = menu.getValue(*menu.msg_list[1])
        self.assertEqual(menu.assertlist[2],msgInfo, '查询正确')

    def test_handledby(self):
        """遍历经手人选项"""
        menu = Termwarning_page(self.driver)  # 实例化合同期限预警取消页面
        self.login.loginFunc()  # 登录
        menu.intermwarning()  # 进入合同期限预警取消页面
        time.sleep(3)
        menu.cBtn(menu.button_list[0])
        menu.cBtn(menu.button_list[4])
        time.sleep(1)
        list_Num = []
        for people in menu.handledby:  # 循环遍历经手人下拉列表
            text, people = menu.contractOption(*people)
            list_Num.append(text)
        self.assertEqual('请选择', list_Num[0])
        self.assertEqual('张站长', list_Num[1])
        self.assertEqual('管理员', list_Num[2])
        self.assertEqual('张昱', list_Num[3])
        self.assertEqual('徐玥', list_Num[4])
        self.assertEqual('朱红霞', list_Num[5])

    def test_paymentstatus(self):
        """遍历状态选项"""
        menu = Termwarning_page(self.driver)  # 实例化合同期限预警取消页面
        self.login.loginFunc()  # 登录
        menu.intermwarning()  # 进入合同期限预警取消页面
        time.sleep(3)
        menu.cBtn(menu.button_list[0])
        menu.cBtn(menu.button_list[5])
        list_Num = []
        for state in menu.states:  # 循环遍历状态下拉列表
            text, state = menu.contractOption(*state)
            list_Num.append(text)
        self.assertEqual('请选择', list_Num[0])
        self.assertEqual('未取消', list_Num[1])
        self.assertEqual('已取消', list_Num[2])

    def test_detail_check(self):
        """明细查看"""
        menu = Termwarning_page(self.driver)  # 实例化合同期限预警取消页面
        self.login.loginFunc()  # 登录
        menu.intermwarning()  # 进入合同期限预警取消页面
        time.sleep(3)
        menu.cBtn(menu.button_list[0])
        menu.cBtn(menu.button_list[7])
        time.sleep(1)
        msg = menu.isElementExist(menu.msg_list[2])
        self.assertTrue(msg,'弹出明细窗口')

    def test_history_check(self):
        """历史查看"""
        menu = Termwarning_page(self.driver)  # 实例化合同期限预警取消页面
        self.login.loginFunc()  # 登录
        menu.intermwarning()  # 进入合同期限预警取消页面
        time.sleep(3)
        menu.cBtn(menu.button_list[0])
        menu.cBtn(menu.button_list[6])
        time.sleep(1)
        msg = menu.isElementExist(menu.msg_list[3])
        self.assertTrue(msg,'弹出历史窗口')

    def test_cancelalert(self):
        """合同期限预警取消窗口"""
        menu = Termwarning_page(self.driver)  # 实例化合同期限预警取消页面
        self.login.loginFunc()  # 登录
        menu.intermwarning()  # 进入合同期限预警取消页面
        time.sleep(3)
        menu.cBtn(menu.button_list[0])#全部
        menu.cBtn(menu.button_list[3])#选一
        menu.cBtn(menu.button_list[2])#取消
        time.sleep(1)
        msg = menu.isElementExist(menu.msg_list[4])
        self.assertTrue(msg, '弹出取消预警窗口')

    # def test_cancelalert(self):
    #     """确定合同期限预警取消"""
    #     menu = Termwarning_page(self.driver)  # 实例化合同期限预警取消页面
    #     self.login.loginFunc()  # 登录
    #     menu.intermwarning()  # 进入合同期限预警取消页面
    #     time.sleep(3)
    #     menu.cBtn(menu.button_list[0])#全部
    #     menu.cBtn(menu.button_list[3])#选一
    #     menu.cBtn(menu.button_list[2])#取消
    #     time.sleep(1)
    #     menu.cBtn(menu.button_list[8])#确定取消

    def test_cancelalert(self):
        """取消合同期限预警取消"""
        menu = Termwarning_page(self.driver)  # 实例化合同期限预警取消页面
        self.login.loginFunc()  # 登录
        menu.intermwarning()  # 进入合同期限预警取消页面
        time.sleep(3)
        menu.cBtn(menu.button_list[0])#全部
        menu.cBtn(menu.button_list[3])#选一
        menu.cBtn(menu.button_list[2])#取消
        time.sleep(1)
        menu.cBtn(menu.button_list[9])#取消
        time.sleep(2)
        msgInfo = menu.getValue(*menu.msg_list[1])
        self.assertEqual(menu.assertlist[2], msgInfo, '查询正确')


if __name__ == '__main__':
    pass
