'''
Code description：合同收款模块 testcase
Create time：
Developer：
'''
import time
from framfriend.test_case.models.myunit import MyunitTest
from framfriend.test_case.page_obj.receipt_page import receipt_page

class receipt_Tc(MyunitTest):
    '''合同收款模块用例'''

    def test_alone_query_1(self):
        """合同号，合同名称，客户名称，经办人单一条件查询"""
        menu = receipt_page(self.driver)  # 实例化合同收款页面
        self.login.loginFunc()  # 登录
        menu.inreceiptpage()  # 进入合同收款页面
        time.sleep(3)
        for contract_information in menu.query_list:
            menu.reset()  # 重置
            for value in menu.valuesList:
                menu.iQueryCondition(contract_information, value)
                menu.cBtn(menu.button_list[0])  # 点击[查询]
                time.sleep(3)
                flag = menu.getValue(*menu.msg_list[1])
                try:
                    self.assertIn('12010002',flag, '查询成功')
                except Exception:
                    self.assertNotIn('12010002', flag, '输入的查询条件无效')

    def test_alone_query_2(self):
        """签订时间查询"""
        menu = receipt_page(self.driver)  # 实例化合同收款页面
        self.login.loginFunc()  # 登录
        menu.inreceiptpage()  # 进入合同收款页面
        time.sleep(3)
        #选择时间2018-10-1-2019-9-1
        menu.cBtn(menu.time_list[0])
        menu.cBtn(menu.time_list[1])
        menu.cBtn(menu.time_list[2])
        menu.cBtn(menu.time_list[6])
        menu.cBtn(menu.time_list[3])
        menu.cBtn(menu.time_list[4])
        menu.cBtn(menu.time_list[5])
        menu.cBtn(menu.time_list[6])
        menu.cBtn(menu.button_list[0])#查询
        msgInfo = menu.getValue(*menu.msg_list[2])
        self.assertEqual(msgInfo,'显示第 1 到第 10 条记录，总共 123 条记录','查询正确')

    def test_check_contract_1(self):
        '''点击查看明细'''
        menu = receipt_page(self.driver)  # 实例化合同收款页面
        self.login.loginFunc()  # 登录
        menu.inreceiptpage()  # 进入合同收款页面
        time.sleep(3)
        menu.cBtn(menu.button_list[1])#查看明细
        time.sleep(1)
        msgInfo = menu.getValue(*menu.msg_list[0])
        self.assertEqual(msgInfo,'×\n提示! 请选择一项查看','提示信息正确')

    def test_check_contract_2(self):
        '''全选点击查看明细'''
        menu = receipt_page(self.driver)  # 实例化合同收款页面
        self.login.loginFunc()  # 登录
        menu.inreceiptpage()  # 进入合同收款页面
        time.sleep(3)
        menu.cBtn(menu.check_box[0])#全选
        menu.cBtn(menu.button_list[1])#查看明细
        time.sleep(1)
        msgInfo = menu.getValue(*menu.msg_list[0])
        self.assertEqual(msgInfo, '×\n提示! 请选择一项查看','提示信息正确')

    def test_check_contract_3(self):
        '''选择一项点击查看明细'''
        menu = receipt_page(self.driver)  # 实例化合同收款页面
        self.login.loginFunc()  # 登录
        menu.inreceiptpage()  # 进入合同收款页面
        time.sleep(3)
        menu.cBtn(menu.check_box[1])  # 选择一项
        menu.cBtn(menu.button_list[1])#查看明细
        msg = menu.isElementExist(menu.msg_list[3])
        self.assertTrue(msg,'弹出查看明细窗口')

if __name__=='__main__':
    pass