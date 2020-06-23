'''
Code description：批量转账模块 testcase
Create time：
Developer：
'''
import os
import time
import logging
from framfriend.test_case.models.log import Logger
from framfriend.test_case.models.myunittest import MyunitTest
from framfriend.test_case.page_obj.transfer_page import Transfer_Page

log = Logger(__name__, CmdLevel=logging.INFO, FileLevel=logging.INFO)
class Transfer_Tc(MyunitTest):
    '''批量转账模块用例'''

    def test_alone_query(self):
        """按对方户名,账号，开户机构单一条件查询"""
        menu = Transfer_Page(self.driver)  # 实例化批量转账页面
        self.login.loginFunc()  # 登录
        menu.intransfer()  # 进入批量转账页面
        time.sleep(3)
        for name_id_organ in menu.query_list:
            menu.reset()  # 重置
            for value in menu.valuesList:
                menu.iQueryCondition(name_id_organ, value)
                menu.cBtn(menu.button_list[0])  # 点击[查询]
                time.sleep(3)
                flag = menu.getValue(*menu.msg_list[8])
                try:
                    self.assertIn('黄岛一', flag, '查询成功')
                except Exception:
                    log.logger.info('查询条件无效')

    def test_query_2(self):
        """按己方户名条件查询"""
        menu = Transfer_Page(self.driver)  # 实例化批量转账页面
        self.login.loginFunc()  # 登录
        menu.intransfer()  # 进入批量转账页面
        time.sleep(3)
        menu.cBtn(menu.button_list[21])
        menu.cBtn(menu.button_list[22])
        menu.cBtn(menu.button_list[0])  # 点击[查询]
        msgInfo = menu.getValue(*menu.msg_list[18])
        self.assertIn(menu.valueList[14],msgInfo,'提示信息正确')

    def test_add_1(self):
        """点击新增按钮"""
        menu = Transfer_Page(self.driver)  # 实例化批量转账页面
        self.login.loginFunc()  # 登录
        menu.intransfer()  # 进入批量转账页面
        time.sleep(2)
        menu.cBtn(menu.button_list[1])#点击新增按钮
        msg = menu.isElementExist(menu.msg_list[9])
        self.assertTrue(msg,'弹出新增窗口')

    def test_add_2(self):
        '''不输入必填项为空验证'''
        menu = Transfer_Page(self.driver)  # 实例化批量转账页面
        self.login.loginFunc()  # 登录
        menu.intransfer()  # 进入批量转账页面
        time.sleep(3)
        menu.cBtn(menu.button_list[1])  # 点击新增按钮
        menu.cBtn(menu.button_list[9])  #点击提交按钮
        flag = menu.isElementExist(menu.msg_list[0])
        self.assertTrue(flag,'出现提示信息')
        if flag:
            msgInfo = menu.getValue(*menu.msg_list[0])
            self.assertEqual(msgInfo,menu.valueList[5], '提示信息正确')
        flag2 = menu.isElementExist(menu.msg_list[1])
        self.assertTrue(flag2,'出现提示信息')
        if flag2:
            msgInfo2 = menu.getValue(*menu.msg_list[1])
            self.assertEqual(msgInfo2,menu.valueList[5],'提示信息正确')
        flag3 = menu.isElementExist(menu.msg_list[6])
        self.assertTrue(flag3, '出现提示信息')
        if flag3:
            msgInfo3 = menu.getValue(*menu.msg_list[6])
            self.assertEqual(msgInfo3,menu.valueList[6], '提示信息正确')
        flag4 = menu.isElementExist(menu.msg_list[3])
        self.assertTrue(flag4,'出现提示信息')
        if flag4:
            msgInfo4 = menu.getValue(*menu.msg_list[3])
            self.assertEqual(msgInfo4,menu.valueList[5],'提示信息正确')
        flag6 = menu.isElementExist(menu.msg_list[5])
        self.assertTrue(flag6, '出现提示信息')
        if flag4:
            msgInfo6 = menu.getValue(*menu.msg_list[5])
            self.assertEqual(msgInfo6,menu.valueList[5], '提示信息正确')

    def test_add_3(self):
        '''不选择户名提交'''
        menu = Transfer_Page(self.driver)  # 实例化批量转账页面
        self.login.loginFunc()  # 登录
        menu.intransfer()  # 进入批量转账页面
        time.sleep(3)
        menu.cBtn(menu.button_list[1])  # 点击新增按钮
        menu.inputValue(menu.input_list[0],menu.reason)#输入对方户名
        menu.inputValue(menu.input_list[1],menu.valueList[1])#输入账号
        menu.inputValue(menu.input_list[2],menu.valueList[2])#输入金额
        menu.inputValue(menu.input_list[3],menu.reason)#输入备注
        menu.inputValue(menu.input_list[4],menu.valueList[3])#输入联行号
        menu.inputValue(menu.input_list[5],menu.reason)#输入开户机构
        menu.cBtn(menu.button_list[9])  # 点击提交按钮
        time.sleep(2)
        flag = menu.isElementExist(menu.msg_list[0])
        self.assertTrue(flag, '出现提示信息')
        if flag:
            msgInfo = menu.getValue(*menu.msg_list[0])
            self.assertEqual(msgInfo,menu.valueList[5], '提示信息正确')

    def test_add_4(self):
        '''不输入对方户名'''
        menu = Transfer_Page(self.driver)  # 实例化批量转账页面
        self.login.loginFunc()  # 登录
        menu.intransfer()  # 进入批量转账页面
        time.sleep(3)
        menu.cBtn(menu.button_list[1])  # 点击新增按钮
        menu.cBtn(menu.button_list[7])
        menu.cBtn(menu.button_list[8])#选择银行
        menu.inputValue(menu.input_list[1],menu.valueList[1])#输入账号
        menu.inputValue(menu.input_list[2],menu.valueList[2])#输入金额
        menu.inputValue(menu.input_list[3],menu.reason)#输入备注
        menu.inputValue(menu.input_list[4],menu.valueList[3])#输入联行号
        menu.inputValue(menu.input_list[5],menu.reason)#输入开户机构
        menu.cBtn(menu.button_list[9])  # 点击提交按钮
        time.sleep(2)
        flag = menu.isElementExist(menu.msg_list[1])
        self.assertTrue(flag, '出现提示信息')
        if flag:
            msgInfo = menu.getValue(*menu.msg_list[1])
            self.assertEqual(msgInfo,menu.valueList[5], '提示信息正确')

    def test_add_6(self):
        '''不输入备注'''
        menu = Transfer_Page(self.driver)  # 实例化批量转账页面
        self.login.loginFunc()  # 登录
        menu.intransfer()  # 进入批量转账页面
        time.sleep(3)
        menu.cBtn(menu.button_list[1])  # 点击新增按钮
        menu.cBtn(menu.button_list[7])
        menu.cBtn(menu.button_list[8])#选择银行
        menu.inputValue(menu.input_list[0],menu.reason)#输入对方户名
        menu.inputValue(menu.input_list[1], menu.valueList[1])  # 输入账号
        menu.inputValue(menu.input_list[2],menu.valueList[2])#输入金额
        menu.inputValue(menu.input_list[4],menu.valueList[3])#输入联行号
        menu.inputValue(menu.input_list[5],menu.reason)#输入开户机构
        menu.cBtn(menu.button_list[9])  # 点击提交按钮
        time.sleep(2)
        flag = menu.isElementExist(menu.msg_list[3])
        self.assertTrue(flag, '出现提示信息')
        if flag:
            msgInfo = menu.getValue(*menu.msg_list[3])
            self.assertEqual(msgInfo,menu.valueList[5],'提示信息正确')

    def test_add_7(self):
        '''不输入金额'''
        menu = Transfer_Page(self.driver)  # 实例化批量转账页面
        self.login.loginFunc()  # 登录
        menu.intransfer()  # 进入批量转账页面
        time.sleep(3)
        menu.cBtn(menu.button_list[1])  # 点击新增按钮
        menu.cBtn(menu.button_list[7])
        menu.cBtn(menu.button_list[8])#选择银行
        menu.inputValue(menu.input_list[0],menu.reason)#输入对方户名
        menu.inputValue(menu.input_list[1], menu.valueList[1])  # 输入账号
        menu.inputValue(menu.input_list[3], menu.reason)  # 输入备注
        menu.inputValue(menu.input_list[4], menu.valueList[3])  # 输入联行号
        menu.inputValue(menu.input_list[5],menu.reason)#输入开户机构
        menu.cBtn(menu.button_list[9])  # 点击提交按钮
        time.sleep(2)
        flag = menu.isElementExist(menu.msg_list[6])
        self.assertTrue(flag, '出现提示信息')
        if flag:
            msgInfo = menu.getValue(*menu.msg_list[6])
            self.assertEqual(msgInfo,menu.valueList[6], '提示信息正确')

    def test_add_8(self):
        '''不输入开户机构'''
        menu = Transfer_Page(self.driver)  # 实例化批量转账页面
        self.login.loginFunc()  # 登录
        menu.intransfer()  # 进入批量转账页面
        time.sleep(3)
        menu.cBtn(menu.button_list[1])  # 点击新增按钮
        menu.cBtn(menu.button_list[7])
        menu.cBtn(menu.button_list[8])  # 选择银行
        menu.inputValue(menu.input_list[0], menu.reason)  # 输入对方户名
        menu.inputValue(menu.input_list[1], menu.valueList[1])  # 输入账号
        menu.inputValue(menu.input_list[2], menu.valueList[2])  # 输入金额
        menu.inputValue(menu.input_list[4], menu.valueList[3])  # 输入联行号
        menu.inputValue(menu.input_list[3], menu.reason)  # 输入备注
        menu.cBtn(menu.button_list[9])  # 点击提交按钮
        time.sleep(2)
        flag = menu.isElementExist(menu.msg_list[5])
        self.assertTrue(flag, '出现提示信息')
        if flag:
            msgInfo = menu.getValue(*menu.msg_list[5])
            self.assertEqual(msgInfo,menu.valueList[5], '提示信息正确')

    def test_add_9(self):
        '''输入错误账号'''
        menu = Transfer_Page(self.driver)  # 实例化批量转账页面
        self.login.loginFunc()  # 登录
        menu.intransfer()  # 进入批量转账页面
        time.sleep(3)
        menu.cBtn(menu.button_list[1])  # 点击新增按钮
        menu.cBtn(menu.button_list[7])
        menu.cBtn(menu.button_list[8])  # 选择户名
        menu.inputValue(menu.input_list[0], menu.reason)  # 输入对方户名
        menu.inputValue(menu.input_list[1], menu.reason)  # 输入错误账号
        menu.inputValue(menu.input_list[2], menu.valueList[2])  # 输入金额
        menu.inputValue(menu.input_list[4], menu.valueList[3])  # 输入联行号
        menu.inputValue(menu.input_list[3], menu.reason)  # 输入备注
        menu.inputValue(menu.input_list[5], menu.reason)  # 输入开户机构
        menu.cBtn(menu.button_list[9])  # 点击提交按钮
        time.sleep(2)
        flag = menu.isElementExist(menu.msg_list[5])
        flag = menu.isElementExist(menu.msg_list[2])
        self.assertTrue(flag, '出现提示信息')
        if flag:
            msgInfo = menu.getValue(*menu.msg_list[2])
            self.assertEqual(msgInfo,menu.valueList[6], '提示信息正确')

    def test_add_10(self):
        '''输入错误联行号'''
        menu = Transfer_Page(self.driver)  # 实例化批量转账页面
        self.login.loginFunc()  # 登录
        menu.intransfer()  # 进入批量转账页面
        time.sleep(3)
        menu.cBtn(menu.button_list[1])  # 点击新增按钮
        menu.cBtn(menu.button_list[7])
        menu.cBtn(menu.button_list[8])  # 选择户名
        menu.inputValue(menu.input_list[0], menu.reason)  # 输入对方户名
        menu.inputValue(menu.input_list[1], menu.valueList[1])  # 输入账号
        menu.inputValue(menu.input_list[2], menu.valueList[2])  # 输入金额
        menu.inputValue(menu.input_list[4], menu.reason)  # 输入错误联行号
        menu.inputValue(menu.input_list[3], menu.reason)  # 输入备注
        menu.inputValue(menu.input_list[5], menu.reason)  # 输入开户机构
        menu.cBtn(menu.button_list[9])  # 点击提交按钮
        time.sleep(2)
        flag = menu.isElementExist(menu.msg_list[4])
        self.assertTrue(flag, '出现提示信息')
        if flag:
            msgInfo = menu.getValue(*menu.msg_list[4])
            self.assertEqual(msgInfo, menu.valueList[6], '提示信息正确')

    def test_add_11(self):
        '''点击新增取消按钮'''
        menu = Transfer_Page(self.driver)  # 实例化批量转账页面
        self.login.loginFunc()  # 登录
        menu.intransfer()  # 进入批量转账页面
        time.sleep(3)
        menu.cBtn(menu.button_list[1])  # 点击新增按钮
        menu.cBtn(menu.button_list[10])  # 点击取消按钮
        time.sleep(1)
        flag = menu.isElementExist(menu.msg_list[9])
        self.assertFalse(flag, '关闭新增窗口')

    def test_add_12(self):
        '''正确新增'''
        menu = Transfer_Page(self.driver)  # 实例化批量转账页面
        self.login.loginFunc()  # 登录
        menu.intransfer()  # 进入批量转账页面
        time.sleep(3)
        menu.cBtn(menu.button_list[1])  # 点击新增按钮
        menu.cBtn(menu.button_list[7])
        menu.cBtn(menu.button_list[8])  # 选择户名
        menu.inputValue(menu.input_list[0], menu.reason)  # 输入对方户名
        menu.inputValue(menu.input_list[1], menu.valueList[1])  # 输入账号
        menu.inputValue(menu.input_list[2], menu.valueList[2])  # 输入金额
        menu.inputValue(menu.input_list[4], menu.valueList[3])  # 输入联行号
        menu.inputValue(menu.input_list[3], menu.reason)  # 输入备注
        menu.inputValue(menu.input_list[5], menu.reason)  # 输入开户机构
        menu.cBtn(menu.button_list[9])  # 点击提交按钮
        time.sleep(1)
        flag = menu.isElementExist(menu.msg_list[7])
        self.assertTrue(flag, '出现提示信息')
        if flag:
            msgInfo = menu.getValue(*menu.msg_list[7])
            self.assertIn(menu.valueList[7],msgInfo, '提示信息正确')

    def test_update_1(self):
        '''点击修改验证'''
        menu = Transfer_Page(self.driver)  # 实例化批量转账页面
        self.login.loginFunc()  # 登录
        menu.intransfer()  # 进入批量转账页面
        time.sleep(3)
        menu.cBtn(menu.button_list[2])  # 点击修改按钮
        flag = menu.isElementExist(menu.msg_list[7])
        self.assertTrue(flag, '弹出提示信息')
        if flag:
            msgInfo = menu.getValue(*menu.msg_list[7])
            self.assertIn(menu.valueList[8],msgInfo,'提示信息正确')

    def test_update_2(self):
        '''选择多项点击修改验证'''
        menu = Transfer_Page(self.driver)  # 实例化批量转账页面
        self.login.loginFunc()  # 登录
        menu.intransfer()  # 进入批量转账页面
        time.sleep(3)
        menu.cBtn(menu.checkbox_list[0])#全选
        menu.cBtn(menu.button_list[2])  # 点击修改按钮
        flag = menu.isElementExist(menu.msg_list[7])
        self.assertTrue(flag, '弹出提示信息')
        if flag:
            msgInfo = menu.getValue(*menu.msg_list[7])
            self.assertIn(menu.valueList[9],msgInfo,'提示信息正确')

    def test_update_3(self):
        '''选择一项点击修改验证'''
        menu = Transfer_Page(self.driver)  # 实例化批量转账页面
        self.login.loginFunc()  # 登录
        menu.intransfer()  # 进入批量转账页面
        time.sleep(3)
        menu.cBtn(menu.checkbox_list[1])  # 选择修改项
        menu.cBtn(menu.button_list[2])  # 点击修改按钮
        flag = menu.isElementExist(menu.msg_list[10])
        self.assertTrue(flag, '弹出修改窗口')

    def test_update_4(self):
        '''清空必填项提交'''
        menu = Transfer_Page(self.driver)  # 实例化批量转账页面
        self.login.loginFunc()  # 登录
        menu.intransfer()  # 进入批量转账页面
        time.sleep(3)
        menu.cBtn(menu.checkbox_list[1])  # 选择修改项
        menu.cBtn(menu.button_list[2])  # 点击修改按钮
        '''清空必填项'''
        menu.clearValue(menu.input_list[0])#对方户名
        menu.clearValue(menu.input_list[1])# 对方账号
        menu.clearValue(menu.input_list[2])#金额
        menu.clearValue(menu.input_list[5])#开户机构
        menu.cBtn(menu.button_list[12])#点击提交按钮
        flag1 = menu.isElementExist(menu.msg_list[6])
        self.assertTrue(flag1, '出现提示信息')
        if flag1:
            msgInfo1 = menu.getValue(*menu.msg_list[6])
            self.assertEqual(msgInfo1,menu.valueList[6], '提示信息正确')
        flag2 = menu.isElementExist(menu.msg_list[1])
        self.assertTrue(flag2, '出现提示信息')
        if flag2:
            msgInfo2 = menu.getValue(*menu.msg_list[1])
            self.assertEqual(msgInfo2,menu.valueList[5], '提示信息正确')
        flag3 = menu.isElementExist(menu.msg_list[2])
        self.assertTrue(flag3, '出现提示信息')
        if flag3:
            msgInfo3 = menu.getValue(*menu.msg_list[2])
            self.assertEqual(msgInfo3,menu.valueList[5], '提示信息正确')
        flag4 = menu.isElementExist(menu.msg_list[5])
        self.assertTrue(flag4, '出现提示信息')
        if flag4:
            msgInfo4 = menu.getValue(*menu.msg_list[5])
            self.assertEqual(msgInfo4,menu.valueList[5], '提示信息正确')

    def test_update_5(self):
        '''清空金额提交'''
        menu = Transfer_Page(self.driver)  # 实例化批量转账页面
        self.login.loginFunc()  # 登录
        menu.intransfer()  # 进入批量转账页面
        time.sleep(3)
        menu.cBtn(menu.checkbox_list[1])  # 选择修改项
        menu.cBtn(menu.button_list[2])  # 点击修改按钮
        '''清空必填项'''
        menu.clearValue(menu.input_list[2])#金额
        menu.cBtn(menu.button_list[12])#点击提交按钮
        flag1 = menu.isElementExist(menu.msg_list[6])
        self.assertTrue(flag1, '出现提示信息')
        if flag1:
            msgInfo1 = menu.getValue(*menu.msg_list[6])
            self.assertEqual(msgInfo1,menu.valueList[6], '提示信息正确')

    def test_update_6(self):
        '''清空对方户名提交'''
        menu = Transfer_Page(self.driver)  # 实例化批量转账页面
        self.login.loginFunc()  # 登录
        menu.intransfer()  # 进入批量转账页面
        time.sleep(3)
        menu.cBtn(menu.checkbox_list[1])  # 选择修改项
        menu.cBtn(menu.button_list[2])  # 点击修改按钮
        '''清空必填项'''
        menu.clearValue(menu.input_list[0])#清空对方户名
        menu.cBtn(menu.button_list[12])#点击提交按钮
        flag1 = menu.isElementExist(menu.msg_list[1])
        self.assertTrue(flag1, '出现提示信息')
        if flag1:
            msgInfo1 = menu.getValue(*menu.msg_list[1])
            self.assertEqual(msgInfo1,menu.valueList[5], '提示信息正确')

    def test_update_6_1(self):
        '''清空对方账号提交'''
        menu = Transfer_Page(self.driver)  # 实例化批量转账页面
        self.login.loginFunc()  # 登录
        menu.intransfer()  # 进入批量转账页面
        time.sleep(3)
        menu.cBtn(menu.checkbox_list[1])  # 选择修改项
        menu.cBtn(menu.button_list[2])  # 点击修改按钮
        '''清空必填项'''
        menu.clearValue(menu.input_list[1])#清空对方账号
        menu.cBtn(menu.button_list[12])#点击提交按钮
        flag1 = menu.isElementExist(menu.msg_list[14])
        self.assertTrue(flag1, '出现提示信息')
        if flag1:
            msgInfo1 = menu.getValue(*menu.msg_list[14])
            self.assertEqual(msgInfo1,menu.valueList[5], '提示信息正确')

    def test_update_6_2(self):
        '''输入错误对方账号提交'''
        menu = Transfer_Page(self.driver)  # 实例化批量转账页面
        self.login.loginFunc()  # 登录
        menu.intransfer()  # 进入批量转账页面
        time.sleep(3)
        menu.cBtn(menu.checkbox_list[1])  # 选择修改项
        menu.cBtn(menu.button_list[2])  # 点击修改按钮
        menu.inputValue(menu.input_list[1],menu.valueList[0])#输入错误账号
        menu.cBtn(menu.button_list[12])#点击提交按钮
        time.sleep(0.5)
        flag1 = menu.isElementExist(menu.msg_list[15])
        self.assertTrue(flag1, '出现提示信息')
        if flag1:
            msgInfo1 = menu.getValue(*menu.msg_list[15])
            self.assertEqual(msgInfo1,menu.valueList[6], '提示信息正确')

    def test_update_7(self):
        '''清空开户机构提交'''
        menu = Transfer_Page(self.driver)  # 实例化批量转账页面
        self.login.loginFunc()  # 登录
        menu.intransfer()  # 进入批量转账页面
        time.sleep(3)
        menu.cBtn(menu.checkbox_list[1])  # 选择修改项
        menu.cBtn(menu.button_list[2])  # 点击修改按钮
        '''清空必填项'''
        menu.clearValue(menu.input_list[5])#开户机构
        menu.cBtn(menu.button_list[12])#点击提交按钮
        flag1 = menu.isElementExist(menu.msg_list[5])
        self.assertTrue(flag1, '出现提示信息')
        if flag1:
            msgInfo1 = menu.getValue(*menu.msg_list[5])
            self.assertEqual(msgInfo1,menu.valueList[5], '提示信息正确')

    def test_update_8(self):
        '''金额输入非数字提交'''
        menu = Transfer_Page(self.driver)  # 实例化批量转账页面
        self.login.loginFunc()  # 登录
        menu.intransfer()  # 进入批量转账页面
        time.sleep(3)
        menu.cBtn(menu.checkbox_list[1])  # 选择修改项
        menu.cBtn(menu.button_list[2])  # 点击修改按钮
        menu.inputValue(menu.input_list[2],menu.reason)#输入非数字
        menu.cBtn(menu.button_list[12])#点击提交按钮
        flag1 = menu.isElementExist(menu.msg_list[6])
        self.assertTrue(flag1, '出现提示信息')
        if flag1:
            msgInfo1 = menu.getValue(*menu.msg_list[6])
            self.assertEqual(msgInfo1,menu.valueList[6], '提示信息正确')

    def test_update_9(self):
        '''联行号输入非数字提交'''
        menu = Transfer_Page(self.driver)  # 实例化批量转账页面
        self.login.loginFunc()  # 登录
        menu.intransfer()  # 进入批量转账页面
        time.sleep(3)
        menu.cBtn(menu.checkbox_list[1])  # 选择修改项
        menu.cBtn(menu.button_list[2])  # 点击修改按钮
        menu.inputValue(menu.input_list[4],menu.valueList[0])#输入非数字
        menu.cBtn(menu.button_list[12])#点击提交按钮
        flag1 = menu.isElementExist(menu.msg_list[4])
        self.assertTrue(flag1, '出现提示信息')
        if flag1:
            msgInfo1 = menu.getValue(*menu.msg_list[4])
            self.assertEqual(msgInfo1, menu.valueList[6], '提示信息正确')

    def test_update_10(self):
        '''正确修改提交'''
        menu = Transfer_Page(self.driver)  # 实例化批量转账页面
        self.login.loginFunc()  # 登录
        menu.intransfer()  # 进入批量转账页面
        time.sleep(3)
        menu.cBtn(menu.checkbox_list[1])  # 选择修改项
        menu.cBtn(menu.button_list[2])  # 点击修改按钮
        menu.inputValue(menu.input_list[0], menu.reason)  # 输入对方户名
        menu.inputValue(menu.input_list[1], menu.valueList[1])  # 输入账号
        menu.inputValue(menu.input_list[2], menu.valueList[2])  # 输入金额
        menu.inputValue(menu.input_list[4], menu.valueList[3])  # 输入联行号
        menu.inputValue(menu.input_list[3], menu.reason)  # 输入备注
        menu.inputValue(menu.input_list[5], menu.reason)  # 输入开户机构
        menu.cBtn(menu.button_list[12])  # 点击提交按钮
        time.sleep(1)
        flag = menu.isElementExist(menu.msg_list[7])
        self.assertTrue(flag, '弹出提示信息')
        if flag:
            msgInfo = menu.getValue(*menu.msg_list[7])
            self.assertIn(menu.valueList[10],msgInfo, '提示信息正确')

    def test_update_11(self):
        '''点击取消按钮'''
        menu = Transfer_Page(self.driver)  # 实例化批量转账页面
        self.login.loginFunc()  # 登录
        menu.intransfer()  # 进入批量转账页面
        time.sleep(3)
        menu.cBtn(menu.checkbox_list[1])  # 选择修改项
        menu.cBtn(menu.button_list[2])  # 点击修改按钮
        menu.cBtn(menu.button_list[13])#点击取消按钮
        flag = menu.isElementExist(menu.msg_list[10])
        self.assertFalse(flag, '关闭修改窗口')

    def test_delete_1(self):
        '''点击删除'''
        menu = Transfer_Page(self.driver)  # 实例化批量转账页面
        self.login.loginFunc()  # 登录
        menu.intransfer()  # 进入批量转账页面
        time.sleep(3)
        menu.cBtn(menu.button_list[3])#点击删除
        time.sleep(1)
        flag = menu.isElementExist(menu.msg_list[7])
        self.assertTrue(flag,'弹出提示信息')
        if flag:
            msgInfo = menu.getValue(*menu.msg_list[7])
            self.assertIn(menu.valueList[7],msgInfo, '提示信息正确')

    def test_delete_2(self):
        '''选择一项点击删除'''
        menu = Transfer_Page(self.driver)  # 实例化批量转账页面
        self.login.loginFunc()  # 登录
        menu.intransfer()  # 进入批量转账页面
        time.sleep(3)
        menu.cBtn(menu.checkbox_list[2])#选择删除项
        menu.cBtn(menu.button_list[3])#点击删除
        flag = menu.isElementExist(menu.msg_list[11])
        self.assertTrue(flag,'弹出删除窗口')

    def test_delete_3(self):
        '''选择一项点击删除确定'''
        menu = Transfer_Page(self.driver)  # 实例化批量转账页面
        self.login.loginFunc()  # 登录
        menu.intransfer()  # 进入批量转账页面
        time.sleep(3)
        menu.cBtn(menu.checkbox_list[2])  # 选择删除项
        menu.cBtn(menu.button_list[3])  # 点击删除
        menu.cBtn(menu.button_list[14])#点击确定
        time.sleep(1)
        flag = menu.isElementExist(menu.msg_list[16])
        self.assertTrue(flag, '弹出提示信息')
        if flag:
            msgInfo = menu.getValue(*menu.msg_list[16])
            self.assertIn(menu.valueList[12],msgInfo, '提示信息正确')

    def test_delete_4(self):
        '''选择一项点击删除取消'''
        menu = Transfer_Page(self.driver)  # 实例化批量转账页面
        self.login.loginFunc()  # 登录
        menu.intransfer()  # 进入批量转账页面
        time.sleep(3)
        menu.cBtn(menu.checkbox_list[2])  # 选择删除项
        menu.cBtn(menu.button_list[3])  # 点击删除
        menu.cBtn(menu.button_list[15])#点击确定
        # flag = menu.isElementExist(menu.msg_list[11])
        # self.assertFalse(flag, '关闭删除窗口')

    def test_import_1(self):
        '''点击导入验证'''
        menu = Transfer_Page(self.driver)  # 实例化批量转账页面
        self.login.loginFunc()  # 登录
        menu.intransfer()  # 进入批量转账页面
        time.sleep(3)
        menu.cBtn(menu.button_list[4])#点击数据导入
        flag = menu.isElementExist(menu.msg_list[12])
        self.assertTrue(flag,'弹出数据导入提示框')

    def test_import_2(self):
        '''上传错误文件验证'''
        menu = Transfer_Page(self.driver)  # 实例化批量转账页面
        self.login.loginFunc()  # 登录
        menu.intransfer()  # 进入批量转账页面
        time.sleep(3)
        menu.cBtn(menu.button_list[4])  # 点击数据导入
        menu.uploadfalse()
        menu.cBtn(menu.button_list[17])#点击提交按钮
        time.sleep(1)
        flag = menu.isElementExist(menu.msg_list[7])
        self.assertTrue(flag, '弹出提示信息')
        if flag:
            msgInfo = menu.getValue(*menu.msg_list[7])
            self.assertIn(menu.valueList[11],msgInfo, '提示导入失败，停留在导入窗口')

    def test_import_3(self):
        '''上传正确文件验证'''
        menu = Transfer_Page(self.driver)  # 实例化批量转账页面
        self.login.loginFunc()  # 登录
        menu.intransfer()  # 进入批量转账页面
        time.sleep(3)
        menu.cBtn(menu.button_list[4])  # 点击数据导入
        menu.uploadture()
        menu.cBtn(menu.button_list[17])#点击提交按钮
        time.sleep(2)
        flag = menu.isElementExist(menu.msg_list[7])
        self.assertTrue(flag, '弹出提示信息')
        if flag:
            msgInfo = menu.getValue(*menu.msg_list[7])
            self.assertIn(menu.valueList[13],msgInfo, '提示信息正确')

    def test_import_4(self):
        '''不上传文件提交验证'''
        menu = Transfer_Page(self.driver)  # 实例化批量转账页面
        self.login.loginFunc()  # 登录
        menu.intransfer()  # 进入批量转账页面
        time.sleep(3)
        menu.cBtn(menu.button_list[4])  # 点击数据导入
        menu.cBtn(menu.button_list[17])  # 点击提交按钮
        time.sleep(1)
        flag = menu.isElementExist(menu.msg_list[7])
        self.assertTrue(flag, '弹出提示信息')
        if flag:
            msgInfo = menu.getValue(*menu.msg_list[7])
            self.assertIn(menu.valueList[11], msgInfo, '提示导入失败，停留在导入窗口')

    def test_import_5(self):
        '''数据导入点击取消验证'''
        menu = Transfer_Page(self.driver)  # 实例化批量转账页面
        self.login.loginFunc()  # 登录
        menu.intransfer()  # 进入批量转账页面
        time.sleep(3)
        menu.cBtn(menu.button_list[4])  # 点击数据导入
        menu.cBtn(menu.button_list[18])  # 点击提交按钮
        flag = menu.isElementExist(menu.msg_list[12])
        self.assertFalse(flag,'关闭数据导入窗口')

    def test_transfer_1(self):
        '''点击批量转账'''
        menu = Transfer_Page(self.driver)  # 实例化批量转账页面
        self.login.loginFunc()  # 登录
        menu.intransfer()  # 进入批量转账页面
        time.sleep(3)
        menu.cBtn(menu.button_list[5])  # 点击批量转账
        time.sleep(1)
        flag = menu.isElementExist(menu.msg_list[7])
        self.assertTrue(flag, '弹出提示信息')
        if flag:
            msgInfo = menu.getValue(*menu.msg_list[7])
            self.assertIn(menu.valueList[8],msgInfo, '提示信息正确')

    def test_transfer_2(self):
        '''选择一项点击批量转账'''
        menu = Transfer_Page(self.driver)  # 实例化批量转账页面
        self.login.loginFunc()  # 登录
        menu.intransfer()  # 进入批量转账页面
        time.sleep(3)
        menu.cBtn(menu.checkbox_list[1])#选择一项
        menu.cBtn(menu.button_list[5])  # 点击批量转账
        flag = menu.isElementExist(menu.msg_list[13])
        self.assertTrue(flag,'弹出确定支付窗口')

    def test_transfer_3(self):
        '''选择多项点击批量转账'''
        menu = Transfer_Page(self.driver)  # 实例化批量转账页面
        self.login.loginFunc()  # 登录
        menu.intransfer()  # 进入批量转账页面
        time.sleep(3)
        menu.cBtn(menu.checkbox_list[0])#全选
        menu.cBtn(menu.button_list[5])  # 点击批量转账
        flag = menu.isElementExist(menu.msg_list[13])
        self.assertTrue(flag,'弹出确定支付窗口')

    def test_transfer_4(self):
        '''输入错误支付密码批量转账'''
        menu = Transfer_Page(self.driver)  # 实例化批量转账页面
        self.login.loginFunc()  # 登录
        menu.intransfer()  # 进入批量转账页面
        time.sleep(3)
        menu.cBtn(menu.checkbox_list[1])#选择一项
        menu.cBtn(menu.button_list[5])  # 点击批量转账
        menu.inputValue(menu.input_list[6],menu.valueList[3])#输入交易密码
        menu.cBtn(menu.button_list[20])#点击确定按钮
        time.sleep(1)
        flag = menu.isElementExist(menu.msg_list[7])
        self.assertTrue(flag, '支付密码错误')

    def test_transfer_5(self):
        '''输入正确支付密码批量转账'''
        menu = Transfer_Page(self.driver)  # 实例化批量转账页面
        self.login.loginFunc()  # 登录
        menu.intransfer()  # 进入批量转账页面
        time.sleep(3)
        menu.cBtn(menu.checkbox_list[1])  # 选择一项
        menu.cBtn(menu.button_list[5])  # 点击批量转账
        menu.inputValue(menu.input_list[6], menu.valueList[4])  # 输入交易密码
        menu.cBtn(menu.button_list[20])  # 点击确定按钮
        time.sleep(1)
        flag = menu.isElementExist(menu.msg_list[7])
        self.assertTrue(flag, '批量转账成功')

    def test_transfer_6(self):
        '''批量转账点击取消验证'''
        menu = Transfer_Page(self.driver)  # 实例化批量转账页面
        self.login.loginFunc()  # 登录
        menu.intransfer()  # 进入批量转账页面
        time.sleep(3)
        menu.cBtn(menu.checkbox_list[0])#全选
        menu.cBtn(menu.button_list[5])  # 点击批量转账
        menu.cBtn(menu.button_list[19])  # 点击取消按钮
        # time.sleep(1)
        # flag = menu.isElementExist(menu.msg_list[17])
        # self.assertFalse(flag,'关闭支付窗口')

    def test_export(self):
        '''点击导出模板验证'''
        menu = Transfer_Page(self.driver)  # 实例化批量转账页面
        self.login.loginFunc()  # 登录
        menu.intransfer()  # 进入批量转账页面
        time.sleep(3)
        menu.cBtn(menu.button_list[6])  # 点击导出模板
        time.sleep(5)
        assert (os.path.exists('F:\TestDownloads\\银农直联批量转账.xlsx'))  # 检查是否已下载

if __name__ == '__main__':
        pass
