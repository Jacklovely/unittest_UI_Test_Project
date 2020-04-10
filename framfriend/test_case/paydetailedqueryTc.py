'''
Code description : 代付明细查询 testcase
Create time:
Developer:
'''
import os
import time
from selenium.webdriver.support.select import Select
from framfriend.test_case.models.myunit import MyunitTest
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
        self.assertIn(menu.valuelist[5], msgInfo, '提示信息正确')


if __name__ == '__main__':
    pass