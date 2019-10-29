'''
Code description：风格切换模块 testcase
Create time：
Developer：
'''

import time
from framfriend.test_case.models.myunit import MyunitTest
from framfriend.test_case.page_obj.switch_page import switchPage
class switch_Tc(MyunitTest):
    '''风格切换测试用例'''
    def testclick_1(self):
        menu = switchPage(self.driver)  # 实例化风格切换页面
        self.login.loginFunc()  # 登录
        menu.inswitchPage()  # 进入风格切换页面
        time.sleep(2)
        menu.cBtn(menu.element[0])
        msg1 = menu.isElementExist(menu.element[2])
        self.assertFalse(msg1,'切换横版')

    def testclick_2(self):
        menu = switchPage(self.driver)  # 实例化风格切换页面
        self.login.loginFunc()  # 登录
        time.sleep(2)
        menu.cBtn(menu.element[3])#点击基础功能
        menu.cBtn(menu.element[4])#点击切换风格
        menu.cBtn(menu.element[1])#点击切换竖版
        msg1 = menu.isElementExist(menu.element[2])
        self.assertTrue(msg1, '切换竖版')

if __name__=='__main__':
    pass