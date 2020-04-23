'''
Code description：总账模块 testcase
Create time：
Developer：
'''
import time

from selenium.webdriver.support.select import Select
from framfriend.test_case.models.myunit import MyunitTest
from framfriend.test_case.page_obj.generalledger_page import GeneralLedger_Page
class GeneralLedger_Tc(MyunitTest):
    '''总账用例'''

    def test_time_query_1(self):
        '''时间查询'''
        menu = GeneralLedger_Page(self.driver)  # 实例化总账页面
        self.login.loginFunc()  # 登录
        menu.ingeneralledgerpage()  # 进入总账页面
        time.sleep(3)
        menu.cBtn(menu.button_list[0])
        menu.cBtn(menu.time_list[0])
        menu.cBtn(menu.time_list[1])
        for i in range(5):
            menu.cBtn(menu.time_list[2])
        menu.cBtn(menu.time_list[3])
        menu.cBtn(menu.time_list[4])
        menu.cBtn(menu.button_list[4])
        time.sleep(1)
        msgInfo = menu.getValue(*menu.msgInfo)
        self.assertIn(menu.assertlist[1],msgInfo,'查询成功')

    def test_contract(self):
        """遍历合同主体选项"""
        menu = GeneralLedger_Page(self.driver)  # 实例化总账页面
        self.login.loginFunc()  # 登录
        menu.ingeneralledgerpage()  # 进入总账页面
        time.sleep(3)
        menu.cBtn(menu.button_list[0])
        menu.cBtn(menu.button_list[1])
        list_Num = []
        for contract_handledby in menu.contractsubject:  # 循环遍历经手人下拉列表
            text, contract_handledby = menu.contractOption(*contract_handledby)
            list_Num.append(text)
        self.assertEqual('请选择', list_Num[0])
        self.assertEqual('房屋租赁', list_Num[1])
        self.assertEqual('场地租赁', list_Num[2])
        self.assertEqual('土地承包', list_Num[3])
        self.assertEqual('资产', list_Num[4])
        self.assertEqual('建地', list_Num[5])

    def test_contractsubject_query_2_1(self):
        '''合同主体-房屋租赁查询'''
        menu = GeneralLedger_Page(self.driver)  # 实例化总账页面
        self.login.loginFunc()  # 登录
        menu.ingeneralledgerpage()  # 进入总账页面
        time.sleep(3)
        menu.cBtn(menu.button_list[0])
        subject = self.driver.find_element_by_xpath('//*[@id="searchForm"]/div[2]/select')
        Select(subject).select_by_value('3')  # 获取下拉选
        menu.cBtn(menu.button_list[4])
        time.sleep(1)
        msginfo = menu.getValue(*menu.msgInfo)
        self.assertIn(menu.assertlist[2],msginfo,'查询成功')

    def test_contractsubject_query_2_2(self):
        '''合同主体-场地租赁查询'''
        menu = GeneralLedger_Page(self.driver)  # 实例化总账页面
        self.login.loginFunc()  # 登录
        menu.ingeneralledgerpage()  # 进入总账页面
        time.sleep(3)
        menu.cBtn(menu.button_list[0])
        subject = self.driver.find_element_by_xpath('//*[@id="searchForm"]/div[2]/select')
        Select(subject).select_by_value('4')  # 获取下拉选
        menu.cBtn(menu.button_list[4])
        time.sleep(1)
        msginfo = menu.getValue(*menu.msgInfo)
        self.assertIn(menu.assertlist[3],msginfo,'查询成功')

    def test_contractsubject_query_2_3(self):
        '''合同主体-土地承包查询'''
        menu = GeneralLedger_Page(self.driver)  # 实例化总账页面
        self.login.loginFunc()  # 登录
        menu.ingeneralledgerpage()  # 进入总账页面
        time.sleep(3)
        menu.cBtn(menu.button_list[0])
        subject = self.driver.find_element_by_xpath('//*[@id="searchForm"]/div[2]/select')
        Select(subject).select_by_value('2')  # 获取下拉选
        menu.cBtn(menu.button_list[4])
        time.sleep(1)
        msginfo = menu.getValue(*menu.msgInfo)
        self.assertIn(menu.assertlist[4],msginfo,'查询成功')

    def test_contractsubject_query_2_4(self):
        '''合同主体-资产查询'''
        menu = GeneralLedger_Page(self.driver)  # 实例化总账页面
        self.login.loginFunc()  # 登录
        menu.ingeneralledgerpage()  # 进入总账页面
        time.sleep(3)
        menu.cBtn(menu.button_list[0])
        subject = self.driver.find_element_by_xpath('//*[@id="searchForm"]/div[2]/select')
        Select(subject).select_by_value('0')  # 获取下拉选
        menu.cBtn(menu.button_list[4])
        time.sleep(1)
        msginfo = menu.getValue(*menu.msgInfo)
        self.assertIn(menu.assertlist[5],msginfo,'查询成功')

    def test_contractsubject_query_2_5(self):
        '''合同主体-建地查询'''
        menu = GeneralLedger_Page(self.driver)  # 实例化总账页面
        self.login.loginFunc()  # 登录
        menu.ingeneralledgerpage()  # 进入总账页面
        time.sleep(3)
        menu.cBtn(menu.button_list[0])
        subject = self.driver.find_element_by_xpath('//*[@id="searchForm"]/div[2]/select')
        Select(subject).select_by_value('1')  # 获取下拉选
        menu.cBtn(menu.button_list[4])
        time.sleep(1)
        msginfo = menu.getValue(*menu.msgInfo)
        self.assertIn(menu.assertlist[0],msginfo,'查询成功')

    def test_tendering_3(self):
        '''招标方式-下拉选'''
        menu = GeneralLedger_Page(self.driver)  # 实例化总账页面
        self.login.loginFunc()  # 登录
        menu.ingeneralledgerpage()  # 进入总账页面
        time.sleep(3)
        menu.cBtn(menu.button_list[0])
        menu.cBtn(menu.button_list[2])
        list_Num = []
        for tendering in menu.tender:  # 循环遍历经手人下拉列表
            text, tendering = menu.contractOption(*tendering)
            list_Num.append(text)
        self.assertEqual('请选择', list_Num[0])
        self.assertEqual('公开协作', list_Num[1])
        self.assertEqual('公开竞标', list_Num[2])
        self.assertEqual('其他', list_Num[3])
        self.assertEqual('招投标', list_Num[4])
        self.assertEqual('拍卖', list_Num[5])

    def test_tendering_query_3_1(self):
        '''招标方式-公开协作查询'''
        menu = GeneralLedger_Page(self.driver)  # 实例化总账页面
        self.login.loginFunc()  # 登录
        menu.ingeneralledgerpage()  # 进入总账页面
        time.sleep(3)
        menu.cBtn(menu.button_list[0])
        subject = self.driver.find_element_by_xpath('//*[@id="searchForm"]/div[3]/select')
        Select(subject).select_by_value('0')  # 获取下拉选
        menu.cBtn(menu.button_list[4])
        time.sleep(1)
        msginfo = menu.getValue(*menu.msgInfo)
        self.assertIn(menu.assertlist[6],msginfo,'查询成功')

    def test_tendering_query_3_2(self):
        '''招标方式-公开竞标查询'''
        menu = GeneralLedger_Page(self.driver)  # 实例化总账页面
        self.login.loginFunc()  # 登录
        menu.ingeneralledgerpage()  # 进入总账页面
        time.sleep(3)
        menu.cBtn(menu.button_list[0])
        subject = self.driver.find_element_by_xpath('//*[@id="searchForm"]/div[3]/select')
        Select(subject).select_by_value('1')  # 获取下拉选
        menu.cBtn(menu.button_list[4])
        time.sleep(1)
        msginfo = menu.getValue(*menu.msgInfo)
        self.assertIn(menu.assertlist[7],msginfo,'查询成功')

    def test_tendering_query_3_3(self):
        '''招标方式-其他查询'''
        menu = GeneralLedger_Page(self.driver)  # 实例化总账页面
        self.login.loginFunc()  # 登录
        menu.ingeneralledgerpage()  # 进入总账页面
        time.sleep(3)
        menu.cBtn(menu.button_list[0])
        subject = self.driver.find_element_by_xpath('//*[@id="searchForm"]/div[3]/select')
        Select(subject).select_by_value('4')  # 获取下拉选
        menu.cBtn(menu.button_list[4])
        time.sleep(1)
        msginfo = menu.getValue(*menu.msgInfo)
        self.assertIn(menu.assertlist[8],msginfo,'查询成功')

    def test_tendering_query_3_4(self):
        '''招标方式-招投标查询'''
        menu = GeneralLedger_Page(self.driver)  # 实例化总账页面
        self.login.loginFunc()  # 登录
        menu.ingeneralledgerpage()  # 进入总账页面
        time.sleep(3)
        menu.cBtn(menu.button_list[0])
        subject = self.driver.find_element_by_xpath('//*[@id="searchForm"]/div[3]/select')
        Select(subject).select_by_value('2')  # 获取下拉选
        menu.cBtn(menu.button_list[4])
        time.sleep(1)
        msginfo = menu.getValue(*menu.msgInfo)
        self.assertIn(menu.assertlist[0],msginfo,'查询成功')

    def test_tendering_query_3_5(self):
        '''招标方式-拍卖查询'''
        menu = GeneralLedger_Page(self.driver)  # 实例化总账页面
        self.login.loginFunc()  # 登录
        menu.ingeneralledgerpage()  # 进入总账页面
        time.sleep(3)
        menu.cBtn(menu.button_list[0])
        subject = self.driver.find_element_by_xpath('//*[@id="searchForm"]/div[3]/select')
        Select(subject).select_by_value('3')  # 获取下拉选
        menu.cBtn(menu.button_list[4])
        time.sleep(1)
        msginfo = menu.getValue(*menu.msgInfo)
        self.assertIn(menu.assertlist[0],msginfo,'查询成功')

    def test_receivables_4(self):
        '''收款状态-下拉选'''
        menu = GeneralLedger_Page(self.driver)  # 实例化总账页面
        self.login.loginFunc()  # 登录
        menu.ingeneralledgerpage()  # 进入总账页面
        time.sleep(3)
        menu.cBtn(menu.button_list[0])
        menu.cBtn(menu.button_list[3])
        list_Num = []
        for receivables in menu.paymentstatus:  # 循环遍历经手人下拉列表
            text, receivables = menu.contractOption(*receivables)
            list_Num.append(text)
        self.assertEqual('请选择', list_Num[0])
        self.assertEqual('正常履约', list_Num[1])
        self.assertEqual('已终止', list_Num[2])
        self.assertEqual('超期未收', list_Num[3])
        self.assertEqual('待收款', list_Num[4])

    def test_receivables_query_4_1(self):
        '''收款状态-正常履约查询'''
        menu = GeneralLedger_Page(self.driver)  # 实例化总账页面
        self.login.loginFunc()  # 登录
        menu.ingeneralledgerpage()  # 进入总账页面
        time.sleep(3)
        menu.cBtn(menu.button_list[0])
        subject = self.driver.find_element_by_xpath('//*[@id="searchForm"]/div[4]/select')
        Select(subject).select_by_value('0')  # 获取下拉选
        menu.cBtn(menu.button_list[4])
        time.sleep(1)
        msginfo = menu.getValue(*menu.msgInfo)
        self.assertIn(menu.assertlist[0],msginfo,'查询成功')

    def test_receivables_query_4_2(self):
        '''收款状态-已终止查询'''
        menu = GeneralLedger_Page(self.driver)  # 实例化总账页面
        self.login.loginFunc()  # 登录
        menu.ingeneralledgerpage()  # 进入总账页面
        time.sleep(3)
        menu.cBtn(menu.button_list[0])
        subject = self.driver.find_element_by_xpath('//*[@id="searchForm"]/div[4]/select')
        Select(subject).select_by_value('0')  # 获取下拉选
        menu.cBtn(menu.button_list[4])
        time.sleep(1)
        msginfo = menu.getValue(*menu.msgInfo)
        self.assertIn(menu.assertlist[0],msginfo,'查询成功')

    def test_receivables_query_4_3(self):
        '''收款状态-超期未收查询'''
        menu = GeneralLedger_Page(self.driver)  # 实例化总账页面
        self.login.loginFunc()  # 登录
        menu.ingeneralledgerpage()  # 进入总账页面
        time.sleep(3)
        menu.cBtn(menu.button_list[0])
        subject = self.driver.find_element_by_xpath('//*[@id="searchForm"]/div[4]/select')
        Select(subject).select_by_value('2')  # 获取下拉选
        menu.cBtn(menu.button_list[4])
        time.sleep(1)
        msginfo = menu.getValue(*menu.msgInfo)
        self.assertIn(menu.assertlist[0],msginfo,'查询成功')

    def test_receivables_query_4_4(self):
        '''收款状态-待收款查询'''
        menu = GeneralLedger_Page(self.driver)  # 实例化总账页面
        self.login.loginFunc()  # 登录
        menu.ingeneralledgerpage()  # 进入总账页面
        time.sleep(3)
        menu.cBtn(menu.button_list[0])
        subject = self.driver.find_element_by_xpath('//*[@id="searchForm"]/div[4]/select')
        Select(subject).select_by_value('3')  # 获取下拉选
        menu.cBtn(menu.button_list[4])
        time.sleep(1)
        msginfo = menu.getValue(*menu.msgInfo)
        self.assertIn(menu.assertlist[9],msginfo,'查询成功')

if __name__=='__main__':
    pass