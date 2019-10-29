'''
Code description：批量代付模块 testcase
Create time：
Developer：
'''
import os
import time
from framfriend.test_case.models.myunit import MyunitTest
from framfriend.test_case.page_obj.issuing_page import issuing_Page

class issuing_Tc(MyunitTest):
    '''批量代付模块用例'''
    def test_singlePay_1(self):
        '''正确条件查询'''
        menu = issuing_Page(self.driver)  # 实例化批量代付页面
        self.login.loginFunc()  # 登录
        menu.inissuing() # 进入批量代付页面
        time.sleep(3)
        menu.inputValue(menu.input_list[0],menu.valueList[0])#输入查询条件
        menu.cBtn(menu.button_list[0])#点击查询按钮
        Text = menu.getValue(*menu.msg_list[0])
        self.assertEqual('显示第 1 到第 1 条记录，总共 1 条记录', Text, '提示信息正确')

    def test_singlePay_2(self):
        '''错误条件查询'''
        menu = issuing_Page(self.driver)  # 实例化批量代付页面
        self.login.loginFunc()  # 登录
        menu.inissuing() # 进入批量代付页面
        time.sleep(3)
        menu.inputValue(menu.input_list[0],menu.valueList[1])#输入查询条件
        menu.cBtn(menu.button_list[0])#点击查询按钮
        Text = menu.getValue(*menu.msg_list[0])
        self.assertEqual('显示第 1 到第 0 条记录，总共 0 条记录', Text, '提示信息正确')

    def test_singlePay_3(self):
        '''模板导出'''
        menu = issuing_Page(self.driver)  # 实例化批量代付页面
        self.login.loginFunc()  # 登录
        menu.inissuing() # 进入批量代付页面
        time.sleep(3)
        menu.cBtn(menu.button_list[1])#点击模板导出
        time.sleep(5)
        print(os.path.exists('E:\\MyDownloads\\*.xls'))#检查是否已下载

    def test_singlePay_4(self):
        '''点击批量代付'''
        menu = issuing_Page(self.driver)  # 实例化批量代付页面
        self.login.loginFunc()  # 登录
        menu.inissuing()  # 进入批量代付页面
        time.sleep(3)
        menu.cBtn(menu.button_list[2])#点击批量代发
        msg4 = menu.isElementExist(menu.msg_list[4])
        self.assertTrue(msg4,'弹出批量代发窗口')

    def test_singlePay_5(self):
        '''批量代付为空提交'''
        menu = issuing_Page(self.driver)  # 实例化批量代付页面
        self.login.loginFunc()  # 登录
        menu.inissuing()  # 进入批量代付页面
        time.sleep(3)
        menu.cBtn(menu.button_list[2])#点击批量代付
        menu.cBtn(menu.button_list[4])#点击提交
        msg5_1 = menu.isElementExist(menu.msg_list[1])
        self.assertTrue(msg5_1,'出现提示信息')
        if msg5_1:
            msgInfo = menu.getValue(*menu.msg_list[1])
            self.assertEqual(msgInfo, '不能为空', '提示信息正确')
        msg5_2 = menu.isElementExist(menu.msg_list[2])
        self.assertTrue(msg5_2, '出现提示信息')
        if msg5_2:
            msgInfo2 = menu.getValue(*menu.msg_list[1])
            self.assertEqual(msgInfo2, '不能为空', '提示信息正确')

    def test_singlePay_6(self):
        '''批量代付不输入备注提交'''
        menu = issuing_Page(self.driver)  # 实例化批量代付页面
        self.login.loginFunc()  # 登录
        menu.inissuing()  # 进入批量代付页面
        time.sleep(3)
        menu.cBtn(menu.button_list[2])#点击批量代付
        menu.inputValue(menu.input_list[2],menu.valueList[2])#输入交易密码
        menu.cBtn(menu.button_list[4])#点击提交
        msg6_1 = menu.isElementExist(menu.msg_list[1])
        self.assertTrue(msg6_1,'备注不能为空')
        if msg6_1:
            msgInfo = menu.getValue(*menu.msg_list[1])
            self.assertEqual(msgInfo, '不能为空', '提示信息正确')

    def test_singlePay_7(self):
        '''批量代付不输入交易密码提交'''
        menu = issuing_Page(self.driver)  # 实例化批量代付页面
        self.login.loginFunc()  # 登录
        menu.inissuing()  # 进入批量代付页面
        time.sleep(3)
        menu.cBtn(menu.button_list[2])#点击批量代付
        menu.inputValue(menu.input_list[1],menu.reason)#输入备注
        menu.cBtn(menu.button_list[4])#点击提交
        msg7_1 = menu.isElementExist(menu.msg_list[2])
        self.assertTrue(msg7_1, '交易密码不能为空')
        if msg7_1:
            msgInfo = menu.getValue(*menu.msg_list[2])
            self.assertEqual(msgInfo, '不能为空', '提示信息正确')

    def test_singlePay_8(self):
        '''批量代付提交验证'''
        menu = issuing_Page(self.driver)  # 实例化批量代付页面
        self.login.loginFunc()  # 登录
        menu.inissuing()  # 进入批量代付页面
        time.sleep(3)
        menu.cBtn(menu.button_list[2])#点击批量代付
        menu.inputValue(menu.input_list[1],menu.reason)#输入备注
        menu.inputValue(menu.input_list[2], menu.valueList[2])  # 输入交易密码
        menu.cBtn(menu.button_list[4])#点击提交
        msg8_1 = menu.isElementExist(menu.msg_list[3])
        self.assertTrue(msg8_1, '右上角提示')

    def test_singlePay_9(self):
        '''上传文档'''
        menu = issuing_Page(self.driver)  # 实例化批量代付页面
        self.login.loginFunc()  # 登录
        menu.inissuing()  # 进入批量代付页面
        time.sleep(3)
        menu.cBtn(menu.button_list[2])#点击批量代付
        menu.upload()
        msg9_1 = menu.isElementExist(menu.msg_list[5])
        self.assertTrue(msg9_1, '上传验证')

    def test_singlePay_10(self):
        '''点击取消按钮'''
        menu = issuing_Page(self.driver)  # 实例化批量代付页面
        self.login.loginFunc()  # 登录
        menu.inissuing()  # 进入批量代付页面
        time.sleep(3)
        menu.cBtn(menu.button_list[2])  # 点击批量代付
        menu.cBtn(menu.button_list[5])#点击取消按钮
        msg10_1 = menu.isElementExist(menu.msg_list[4])
        self.assertFalse(msg10_1, '关闭批量代发窗口')

    def test_singlePay_11(self):
        '''点击查看结果'''
        menu = issuing_Page(self.driver)  # 实例化批量代付页面
        self.login.loginFunc()  # 登录
        menu.inissuing()  # 进入批量代付页面
        time.sleep(3)
        menu.cBtn(menu.button_list[6])#点击查看结果
        msg11_1 = menu.isElementExist(menu.msg_list[6])
        self.assertTrue(msg11_1, '弹出批量代发详情窗口')

if __name__ == '__main__':
        pass