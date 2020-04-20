'''
Code description：合同收款模块 testcase
Create time：
Developer：
'''
import time
from framfriend.test_case.models.myunit import MyunitTest
from framfriend.test_case.page_obj.receipt_page import Receipt_Page

class Receipt_Tc(MyunitTest):
    '''合同收款模块用例'''

    def test_alone_query_1_1(self):
        '''正确合同号查询'''
        menu = Receipt_Page(self.driver)  # 实例化合同收款页面
        self.login.loginFunc()  # 登录
        menu.inreceiptpage()  # 进入合同收款页面
        time.sleep(3)
        menu.inputValue(menu.query_list[0],menu.valuesList[0])
        menu.cBtn(menu.button_list[0])  # 点击[查询]
        time.sleep(3)
        msgInfo = menu.getValue(*menu.msg_list[1])
        self.assertIn(menu.valuesList[0], msgInfo, '提示信息正确')

    def test_alone_query_1_2(self):
        '''错误合同号查询'''
        menu = Receipt_Page(self.driver)  # 实例化合同收款页面
        self.login.loginFunc()  # 登录
        menu.inreceiptpage()  # 进入合同收款页面
        time.sleep(3)
        menu.inputValue(menu.query_list[0], menu.valuesList[1])
        menu.cBtn(menu.button_list[0])  # 点击[查询]
        time.sleep(3)
        msgInfo = menu.getValue(*menu.msg_list[2])
        self.assertIn(menu.assertlist[0], msgInfo, '提示信息正确')

    def test_alone_query_1_3(self):
        '''正确合同名称查询'''
        menu = Receipt_Page(self.driver)  # 实例化合同收款页面
        self.login.loginFunc()  # 登录
        menu.inreceiptpage()  # 进入合同收款页面
        time.sleep(3)
        menu.inputValue(menu.query_list[1], menu.valuesList[1])
        menu.cBtn(menu.button_list[0])  # 点击[查询]
        time.sleep(3)
        msgInfo = menu.getValue(*menu.msg_list[1])
        self.assertIn(menu.valuesList[1], msgInfo, '提示信息正确')

    def test_alone_query_1_4(self):
        '''错误合同名称查询'''
        menu = Receipt_Page(self.driver)  # 实例化合同收款页面
        self.login.loginFunc()  # 登录
        menu.inreceiptpage()  # 进入合同收款页面
        time.sleep(3)
        menu.inputValue(menu.query_list[1], menu.valuesList[0])
        menu.cBtn(menu.button_list[0])  # 点击[查询]
        time.sleep(3)
        msgInfo = menu.getValue(*menu.msg_list[2])
        self.assertIn(menu.assertlist[0], msgInfo, '提示信息正确')

    def test_alone_query_1_5(self):
        '''正确客户名称查询'''
        menu = Receipt_Page(self.driver)  # 实例化合同收款页面
        self.login.loginFunc()  # 登录
        menu.inreceiptpage()  # 进入合同收款页面
        time.sleep(3)
        menu.inputValue(menu.query_list[2], menu.valuesList[2])
        menu.cBtn(menu.button_list[0])  # 点击[查询]
        time.sleep(3)
        msgInfo = menu.getValue(*menu.msg_list[1])
        self.assertIn(menu.valuesList[2], msgInfo, '提示信息正确')

    def test_alone_query_1_6(self):
        '''错误客户名称查询'''
        menu = Receipt_Page(self.driver)  # 实例化合同收款页面
        self.login.loginFunc()  # 登录
        menu.inreceiptpage()  # 进入合同收款页面
        time.sleep(3)
        menu.inputValue(menu.query_list[2], menu.valuesList[1])
        menu.cBtn(menu.button_list[0])  # 点击[查询]
        time.sleep(3)
        msgInfo = menu.getValue(*menu.msg_list[2])
        self.assertIn(menu.assertlist[0], msgInfo, '提示信息正确')

    def test_alone_query_1_7(self):
        '''正确经办人查询'''
        menu = Receipt_Page(self.driver)  # 实例化合同收款页面
        self.login.loginFunc()  # 登录
        menu.inreceiptpage()  # 进入合同收款页面
        time.sleep(3)
        menu.inputValue(menu.query_list[3], int(menu.valuesList[3]))
        menu.cBtn(menu.button_list[0])  # 点击[查询]
        time.sleep(3)
        msgInfo = menu.getValue(*menu.msg_list[1])
        self.assertIn(menu.valuesList[2], msgInfo, '提示信息正确')

    def test_alone_query_1_8(self):
        '''错误经办人查询'''
        menu = Receipt_Page(self.driver)  # 实例化合同收款页面
        self.login.loginFunc()  # 登录
        menu.inreceiptpage()  # 进入合同收款页面
        time.sleep(3)
        menu.inputValue(menu.query_list[3], menu.valuesList[1])
        menu.cBtn(menu.button_list[0])  # 点击[查询]
        time.sleep(3)
        msgInfo = menu.getValue(*menu.msg_list[2])
        self.assertIn(menu.assertlist[0], msgInfo, '提示信息正确')

    # def test_alone_query_2(self):
    #     """签订时间查询"""
    #     menu = Receipt_Page(self.driver)  # 实例化合同收款页面
    #     self.login.loginFunc()  # 登录
    #     menu.inreceiptpage()  # 进入合同收款页面
    #     time.sleep(3)
    #     #选择时间2018-10-1-2019-9-1
    #     menu.cBtn(menu.time_list[0])
    #     menu.cBtn(menu.time_list[1])
    #     menu.cBtn(menu.time_list[2])
    #     menu.cBtn(menu.time_list[6])
    #     menu.cBtn(menu.time_list[3])
    #     menu.cBtn(menu.time_list[4])
    #     menu.cBtn(menu.time_list[5])
    #     menu.cBtn(menu.time_list[6])
    #     menu.cBtn(menu.button_list[0])#查询
    #     msgInfo = menu.getValue(*menu.msg_list[2])
    #     self.assertIn(menu.assertlist[0], msgInfo, '提示信息正确')

    def test_check_contract_1(self):
        '''点击查看明细'''
        menu = Receipt_Page(self.driver)  # 实例化合同收款页面
        self.login.loginFunc()  # 登录
        menu.inreceiptpage()  # 进入合同收款页面
        time.sleep(3)
        menu.cBtn(menu.button_list[1])#查看明细
        time.sleep(1)
        msgInfo = menu.getValue(*menu.msg_list[0])
        self.assertIn(menu.assertlist[1], msgInfo, '提示信息正确')

    def test_check_contract_2(self):
        '''全选点击查看明细'''
        menu = Receipt_Page(self.driver)  # 实例化合同收款页面
        self.login.loginFunc()  # 登录
        menu.inreceiptpage()  # 进入合同收款页面
        time.sleep(3)
        menu.cBtn(menu.check_box[0])#全选
        menu.cBtn(menu.button_list[1])#查看明细
        time.sleep(1)
        msgInfo = menu.getValue(*menu.msg_list[0])
        self.assertIn(menu.assertlist[1], msgInfo, '提示信息正确')

    def test_check_contract_3(self):
        '''选择一项点击查看明细'''
        menu = Receipt_Page(self.driver)  # 实例化合同收款页面
        self.login.loginFunc()  # 登录
        menu.inreceiptpage()  # 进入合同收款页面
        time.sleep(3)
        menu.cBtn(menu.check_box[1])  # 选择一项
        menu.cBtn(menu.button_list[1])#查看明细
        msg = menu.isElementExist(menu.msg_list[3])
        self.assertTrue(msg,'弹出查看明细窗口')

if __name__=='__main__':
    pass