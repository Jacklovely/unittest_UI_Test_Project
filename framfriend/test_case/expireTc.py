'''
Code description：到期提醒模块 testcase
Create time：
Developer：
'''
import time
from framfriend.test_case.models.myunit import MyunitTest
from framfriend.test_case.page_obj.expire_page import expire_page

class expire_Tc(MyunitTest):
    '''到期提醒模块用例'''
    def test_check_contract_1(self):
        '''点击查看明细'''
        menu = expire_page(self.driver)  # 实例化到期提醒页面
        self.login.loginFunc()  # 登录
        menu.inexpirepage() # 进入到期提醒页面
        time.sleep(3)
        menu.cBtn(menu.button[0])#所有地区
        menu.cBtn(menu.button[1])#查看明细
        time.sleep(1)
        msgInfo = menu.getValue(*menu.msg_list[0])
        self.assertEqual(msgInfo,'×\n提示! 请选择一项查看','提示信息正确')

    def test_check_contract_2(self):
        '''全选点击查看明细'''
        menu = expire_page(self.driver)  # 实例化到期提醒页面
        self.login.loginFunc()  # 登录
        menu.inexpirepage()  # 进入到期提醒页面
        time.sleep(3)
        menu.cBtn(menu.button[0])  # 所有地区
        menu.cBtn(menu.check_box[0])#全选
        menu.cBtn(menu.button[1])#查看明细
        time.sleep(1)
        msgInfo = menu.getValue(*menu.msg_list[0])
        self.assertEqual(msgInfo, '×\n提示! 请选择一项查看','提示信息正确')

    def test_check_contract_3(self):
        '''选择一项点击查看明细'''
        menu = expire_page(self.driver)  # 实例化到期提醒页面
        self.login.loginFunc()  # 登录
        menu.inexpirepage()  # 进入到期提醒页面
        time.sleep(3)
        menu.cBtn(menu.button[0])  # 所有地区
        menu.cBtn(menu.check_box[1])  # 选择一项
        menu.cBtn(menu.button[1])#查看明细
        msg = menu.isElementExist(menu.msg_list[1])
        self.assertTrue(msg,'弹出查看明细窗口')

if __name__=='__main__':
    pass