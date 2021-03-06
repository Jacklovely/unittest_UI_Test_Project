'''
Code description：执行情况模块 testcase
Create time：
Developer：
'''
import time
from framfriend.test_case.models.myunittest import MyunitTest
from framfriend.test_case.page_obj.executivecondition_page import ExecutiveCondition_Page

class ExecutiveCondition_Tc(MyunitTest):
    '''执行情况模块用例'''
    def test_contract_query_1_1(self):
        '''履约查询'''
        menu = ExecutiveCondition_Page(self.driver)  # 实例化执行情况页面
        self.login.loginFunc()  # 登录
        menu.inexecutiveconditionpage()  # 进入执行情况页面
        time.sleep(2)
        menu.cBtn(menu.button_list[0])
        menu.cBtn(menu.checkbox[2])
        menu.cBtn(menu.button_list[1])
        time.sleep(1)
        msginfo = menu.getValue(*menu.msg_list[0])
        self.assertIn(menu.assertlist[1],msginfo,'提示信息正确')

    def test_contract_query_1_2(self):
        '''超期查询'''
        menu = ExecutiveCondition_Page(self.driver)  # 实例化执行情况页面
        self.login.loginFunc()  # 登录
        menu.inexecutiveconditionpage()  # 进入执行情况页面
        time.sleep(2)
        menu.cBtn(menu.button_list[0])
        menu.cBtn(menu.checkbox[3])
        menu.cBtn(menu.button_list[1])
        time.sleep(1)
        msginfo = menu.getValue(*menu.msg_list[0])
        self.assertIn(menu.assertlist[1],msginfo,'提示信息正确')

    def test_contract_query_1_3(self):
        '''终止查询'''
        menu = ExecutiveCondition_Page(self.driver)  # 实例化执行情况页面
        self.login.loginFunc()  # 登录
        menu.inexecutiveconditionpage()  # 进入执行情况页面
        time.sleep(2)
        menu.cBtn(menu.button_list[0])
        menu.cBtn(menu.checkbox[4])
        menu.cBtn(menu.button_list[1])
        time.sleep(1)
        msginfo = menu.getValue(*menu.msg_list[0])
        self.assertIn(menu.assertlist[1],msginfo,'提示信息正确')

    def test_contract_query_1_4(self):
        '''待收款查询'''
        menu = ExecutiveCondition_Page(self.driver)  # 实例化执行情况页面
        self.login.loginFunc()  # 登录
        menu.inexecutiveconditionpage()  # 进入执行情况页面
        time.sleep(2)
        menu.cBtn(menu.button_list[0])
        menu.cBtn(menu.checkbox[5])
        menu.cBtn(menu.button_list[1])
        time.sleep(1)
        msginfo = menu.getValue(*menu.msg_list[0])
        self.assertIn(menu.assertlist[2],msginfo,'提示信息正确')


    def test_click_detail_1(self):
        '''点击明细'''
        menu = ExecutiveCondition_Page(self.driver)  # 实例化执行情况页面
        self.login.loginFunc()  # 登录
        menu.inexecutiveconditionpage()  # 进入执行情况页面
        time.sleep(2)
        menu.cBtn(menu.button_list[0])
        menu.cBtn(menu.button_list[2])
        time.sleep(1)
        msgInfo = menu.getValue(*menu.msg_list[1])
        self.assertIn(menu.assertlist[0],msgInfo, '提示信息正确')

    def test_click_detail_2(self):
        '''全选点击明细'''
        menu = ExecutiveCondition_Page(self.driver)  # 实例化执行情况页面
        self.login.loginFunc()  # 登录
        menu.inexecutiveconditionpage()  # 进入执行情况页面
        time.sleep(2)
        menu.cBtn(menu.button_list[0])
        menu.cBtn(menu.checkbox[0])
        menu.cBtn(menu.button_list[2])
        time.sleep(1)
        msgInfo = menu.getValue(*menu.msg_list[1])
        self.assertIn(menu.assertlist[0],msgInfo, '提示信息正确')

    def test_click_detail_3(self):
        '''选择一项点击明细'''
        menu = ExecutiveCondition_Page(self.driver)  # 实例化执行情况页面
        self.login.loginFunc()  # 登录
        menu.inexecutiveconditionpage()  # 进入执行情况页面
        time.sleep(2)
        menu.cBtn(menu.button_list[0])
        menu.cBtn(menu.checkbox[1])
        menu.cBtn(menu.button_list[2])
        time.sleep(1)
        msg = menu.isElementExist(menu.msg_list[2])
        self.assertTrue(msg, '弹出明细窗口')

if __name__ == '__main__':
    pass
