'''
Code description：明细账模块 testcase
Create time：
Developer：
'''
import time

from selenium.webdriver.support.select import Select
from framfriend.test_case.models.myunit import MyunitTest
from framfriend.test_case.page_obj.generalledger_page import generalledger_page
class generalledger_Tc(MyunitTest):
    '''执行总账用例'''

    def test_time_query_1(self):
        '''时间查询'''
        menu = generalledger_page(self.driver)  # 实例化总账页面
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
        self.assertEqual(msgInfo,'显示第 1 到第 10 条记录，总共 93 条记录','查询成功')

    def test_contractsubject_query_2(self):
        '''合同主体查询'''
        menu = generalledger_page(self.driver)  # 实例化总账页面
        self.login.loginFunc()  # 登录
        menu.ingeneralledgerpage()  # 进入总账页面
        time.sleep(3)
        menu.cBtn(menu.button_list[0])
        subject = self.driver.find_element_by_xpath('//*[@id="searchForm"]/div[2]/select')
        Select(subject).select_by_value('3')  # 获取下拉选


if __name__=='__main__':
    pass