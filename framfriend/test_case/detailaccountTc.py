'''
Code description：明细账模块 testcase
Create time：
Developer：
'''
import time

from selenium.webdriver.support.select import Select

from framfriend.test_case.models.myunit import MyunitTest
from framfriend.test_case.page_obj.detailaccount_page import detailaccount_page
class executivecondition_Tc(MyunitTest):
    '''执行明细账用例'''

    def test_alone_query_1(self):
        """合同号，合同名称，客户名称，合同年限单一条件查询"""
        menu = detailaccount_page(self.driver)  # 实例化明细账页面
        self.login.loginFunc()  # 登录
        menu.indetailaccountpage()  # 进入明细账页面
        time.sleep(3)
        menu.cBtn(menu.button_list[0])
        for contract_information in menu.query_list:
            menu.reset()  # 重置
            for value in menu.valuesList:
                menu.iQueryCondition(contract_information, value)
                menu.cBtn(menu.button_list[1])  # 点击[查询]
                time.sleep(2)
                flag = menu.getValue(*menu.msg_list[0])
                try:
                    self.assertIn('12130003', flag, '查询成功')
                except Exception:
                    self.assertNotIn('12130003', flag, '输入的查询条件无效')

    def test_account_query_2(self):
        """签订时间查询"""
        menu = detailaccount_page(self.driver)  # 实例化明细账页面
        self.login.loginFunc()  # 登录
        menu.indetailaccountpage()  # 进入明细账页面
        time.sleep(3)
        menu.cBtn(menu.button_list[0])
        # 选择时间2018-10-1-2019-9-1
        menu.cBtn(menu.time_list[0])
        menu.cBtn(menu.time_list[2])
        menu.cBtn(menu.time_list[3])
        menu.cBtn(menu.time_list[6])
        menu.cBtn(menu.time_list[1])
        menu.cBtn(menu.time_list[4])
        menu.cBtn(menu.time_list[5])
        menu.cBtn(menu.time_list[6])
        menu.cBtn(menu.button_list[1])  # 查询
        time.sleep(1)
        msgInfo = menu.getValue(*menu.msg_list[1])
        self.assertEqual(msgInfo, '显示第 1 到第 10 条记录，总共 123 条记录', '查询正确')

    def test_account_query_3(self):
        """经手人查询"""
        menu = detailaccount_page(self.driver)  # 实例化明细账页面
        self.login.loginFunc()  # 登录
        menu.indetailaccountpage()  # 进入明细账页面
        time.sleep(3)
        menu.cBtn(menu.button_list[0])
        # 选择时间2018-10-1-2019-9-1
        menu.cBtn(menu.time_list[0])
        menu.cBtn(menu.time_list[2])
        menu.cBtn(menu.time_list[3])
        menu.cBtn(menu.time_list[6])
        menu.cBtn(menu.time_list[1])
        menu.cBtn(menu.time_list[4])
        menu.cBtn(menu.time_list[5])
        menu.cBtn(menu.time_list[6])
        account = self.driver.find_element_by_xpath('//*[@id="hand_man"]')
        Select(account).select_by_value('b4293243a3da4d1a9e9b7b9805721687')  # 获取下拉选
        menu.cBtn(menu.button_list[1])  # 查询
        time.sleep(1)
        msgInfo = menu.getValue(*menu.msg_list[1])
        self.assertEqual(msgInfo, '显示第 1 到第 3 条记录，总共 3 条记录', '查询正确')

    def test_years_query_4(self):
        """合同年限查询"""
        menu = detailaccount_page(self.driver)  # 实例化明细账页面
        self.login.loginFunc()  # 登录
        menu.indetailaccountpage()  # 进入明细账页面
        time.sleep(3)
        menu.cBtn(menu.button_list[0])
        # 选择时间2018-10-1-2019-9-1
        menu.cBtn(menu.time_list[0])
        menu.cBtn(menu.time_list[2])
        menu.cBtn(menu.time_list[3])
        menu.cBtn(menu.time_list[6])
        menu.cBtn(menu.time_list[1])
        menu.cBtn(menu.time_list[4])
        menu.cBtn(menu.time_list[5])
        menu.cBtn(menu.time_list[6])
        years = self.driver.find_element_by_xpath('//*[@id="searchForm"]/div[7]/select')
        Select(years).select_by_value('3')  # 获取下拉选
        menu.cBtn(menu.button_list[1])  # 查询
        time.sleep(1)
        msgInfo = menu.getValue(*menu.msg_list[1])
        self.assertEqual(msgInfo, '显示第 1 到第 10 条记录，总共 123 条记录', '查询正确')

    def test_handledby(self):
        """遍历经手人选项"""
        menu = detailaccount_page(self.driver)  # 实例化明细账页面
        self.login.loginFunc()  # 登录
        menu.indetailaccountpage()  # 进入明细账页面
        time.sleep(3)
        menu.cBtn(menu.button_list[3])
        list_Num = []
        for contract_handledby in menu.handledby:  # 循环遍历经手人下拉列表
            text, contract_handledby = menu.contractOption(*contract_handledby)
            list_Num.append(text)
        self.assertEqual('请选择', list_Num[0])
        self.assertEqual('管理员', list_Num[1])
        self.assertEqual('曲盼盼', list_Num[2])
        self.assertEqual('孙宏', list_Num[3])
        self.assertEqual('刘佳', list_Num[4])

    def test_paymentstatus(self):
        """遍历收款状态选项"""
        menu = detailaccount_page(self.driver)  # 实例化明细账页面
        self.login.loginFunc()  # 登录
        menu.indetailaccountpage()  # 进入明细账页面
        time.sleep(3)
        menu.cBtn(menu.button_list[4])
        list_Num = []
        for contract_paymentstatus in menu.paymentstatus:  # 循环遍历收款状态下拉列表
            text, contract_paymentstatus = menu.contractOption(*contract_paymentstatus)
            list_Num.append(text)
        self.assertEqual('请选择', list_Num[0])
        self.assertEqual('正常履约', list_Num[1])
        self.assertEqual('已终止', list_Num[2])
        self.assertEqual('超期未收', list_Num[3])
        self.assertEqual('待收款', list_Num[4])

    def test_detail_check(self):
        """明细查看"""
        menu = detailaccount_page(self.driver)  # 实例化明细账页面
        self.login.loginFunc()  # 登录
        menu.indetailaccountpage()  # 进入明细账页面
        time.sleep(3)
        menu.cBtn(menu.button_list[0])
        menu.cBtn(menu.button_list[2])
        time.sleep(1)
        msg = menu.isElementExist(menu.msg_list[2])
        self.assertTrue(msg,'弹出明细窗口')

if __name__ == '__main__':
    pass
