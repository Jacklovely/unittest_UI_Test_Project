'''
Code description：对方银行设置模块 testcase
Create time：
Developer：
'''
import time
from framfriend.test_case.models.myunittest import MyunitTest
from framfriend.test_case.page_obj.otherbank_page import OtherBank_Page

class OtherBank_Tc(MyunitTest):
    '''对方银行设置模块用例'''

    def test_alone_query_1(self):
        """按开户机构条件查询"""
        menu =OtherBank_Page(self.driver) # 实例化对方银行设置页面
        self.login.loginFunc()  # 登录
        menu.InotherBankpage()  # 进入对方银行设置页面
        time.sleep(3)
        menu.inputValue(menu.query_list[0], menu.valuesList[0])
        menu.cBtn(menu.button_list[0])
        Text = menu.getValue(*menu.msg_list[15])
        self.assertIn(menu.valuesList[0], Text, '验证成功')

    def test_alone_query_1_1(self):
        """按不存在开户机构条件查询"""
        menu =OtherBank_Page(self.driver) # 实例化对方银行设置页面
        self.login.loginFunc()  # 登录
        menu.InotherBankpage()  # 进入对方银行设置页面
        time.sleep(3)
        menu.inputValue(menu.query_list[0], menu.valuesList[1])
        menu.cBtn(menu.button_list[0])
        Text = menu.getValue(*menu.msg_list[15])
        self.assertIn(menu.valueList[3], Text, '验证成功')

    def test_alone_query_2(self):
        """按户名条件查询"""
        menu =OtherBank_Page(self.driver) # 实例化对方银行设置页面
        self.login.loginFunc()  # 登录
        menu.InotherBankpage()  # 进入对方银行设置页面
        time.sleep(3)
        menu.inputValue(menu.query_list[1], menu.valuesList[1])
        menu.cBtn(menu.button_list[0])
        Text = menu.getValue(*menu.msg_list[15])
        self.assertIn(menu.valuesList[1], Text, '验证成功')

    def test_alone_query_2_1(self):
        """按不存在户名条件查询"""
        menu =OtherBank_Page(self.driver) # 实例化对方银行设置页面
        self.login.loginFunc()  # 登录
        menu.InotherBankpage()  # 进入对方银行设置页面
        time.sleep(3)
        menu.inputValue(menu.query_list[1], menu.valuesList[0])
        menu.cBtn(menu.button_list[0])
        Text = menu.getValue(*menu.msg_list[15])
        self.assertIn(menu.valueList[3], Text, '验证成功')

    def test_alone_query_3(self):
        """按账号条件查询"""
        menu =OtherBank_Page(self.driver) # 实例化对方银行设置页面
        self.login.loginFunc()  # 登录
        menu.InotherBankpage()  # 进入对方银行设置页面
        time.sleep(3)
        menu.inputValue(menu.query_list[2], menu.valuesList[2])
        menu.cBtn(menu.button_list[0])
        Text = menu.getValue(*menu.msg_list[15])
        self.assertIn(menu.valuesList[2], Text, '验证成功')

    def test_alone_query_3_1(self):
        """按不存在账号条件查询"""
        menu =OtherBank_Page(self.driver) # 实例化对方银行设置页面
        self.login.loginFunc()  # 登录
        menu.InotherBankpage()  # 进入对方银行设置页面
        time.sleep(3)
        menu.inputValue(menu.query_list[2], menu.valueList[0])
        menu.cBtn(menu.button_list[0])
        Text = menu.getValue(*menu.msg_list[15])
        self.assertIn(menu.valueList[3], Text, '验证成功')

    def test_alone_query_4(self):
        """按银行名称条件查询"""
        menu =OtherBank_Page(self.driver) # 实例化对方银行设置页面
        self.login.loginFunc()  # 登录
        menu.InotherBankpage()  # 进入对方银行设置页面
        time.sleep(3)
        menu.inputValue(menu.query_list[3], menu.valuesList[3])
        menu.cBtn(menu.button_list[0])
        Text = menu.getValue(*menu.msg_list[15])
        self.assertIn(menu.valuesList[3], Text, '验证成功')

    def test_alone_query_4(self):
        """按不存在银行名称条件查询"""
        menu = OtherBank_Page(self.driver)  # 实例化对方银行设置页面
        self.login.loginFunc()  # 登录
        menu.InotherBankpage()  # 进入对方银行设置页面
        time.sleep(3)
        menu.inputValue(menu.query_list[3], menu.valueList[0])
        menu.cBtn(menu.button_list[0])
        Text = menu.getValue(*menu.msg_list[15])
        self.assertIn(menu.valueList[3], Text, '验证成功')

    def test_addotherbank_1(self):
        '''点击新增按钮验证'''
        menu = OtherBank_Page(self.driver)  # 实例化对方银行设置页面
        self.login.loginFunc()  # 登录
        menu.InotherBankpage()  # 进入对方银行设置页面
        time.sleep(3)
        menu.cBtn(menu.button_list[1])#点击新增按钮
        time.sleep(1)
        msg = menu.isElementExist(menu.msg_list[1])
        self.assertTrue(msg,'弹出新增窗口')

    def test_addownbank_2(self):
        '''为空提交验证'''
        menu = OtherBank_Page(self.driver)  # 实例化对方银行设置页面
        self.login.loginFunc()  # 登录
        menu.InotherBankpage()  # 进入对方银行设置页面
        time.sleep(3)
        menu.cBtn(menu.button_list[1])  # 点击新增按钮
        menu.cBtn(menu.button_list[7]) #点击提交
        time.sleep(2)
        flag1  = menu.isElementExist(menu.msg_list[2])
        self.assertTrue(flag1,'出现提示信息')
        if flag1:
            msgInfo1 = menu.getValue(*menu.msg_list[2])
            self.assertEqual(msgInfo1,menu.valueList[4],'提示信息正确')
        flag2 = menu.isElementExist(menu.msg_list[3])
        self.assertTrue(flag2, '出现提示信息')
        if flag2:
            msgInfo2 = menu.getValue(*menu.msg_list[3])
            self.assertEqual(msgInfo2,menu.valueList[4],'提示信息正确')
        flag3 = menu.isElementExist(menu.msg_list[4])
        self.assertTrue(flag3, '出现提示信息')
        if flag3:
            msgInfo3 = menu.getValue(*menu.msg_list[4])
            self.assertEqual(msgInfo3,menu.valueList[4],'提示信息正确')
        flag4 = menu.isElementExist(menu.msg_list[5])
        self.assertTrue(flag4, '出现提示信息')
        if flag4:
            msgInfo4 = menu.getValue(*menu.msg_list[5])
            self.assertEqual(msgInfo4,menu.valueList[4],'提示信息正确')


    def test_addotherbank_3(self):
        '''不输入银行名称提交验证'''
        menu = OtherBank_Page(self.driver)  # 实例化对方银行设置页面
        self.login.loginFunc()  # 登录
        menu.InotherBankpage()  # 进入对方银行设置页面
        time.sleep(3)
        menu.cBtn(menu.button_list[1])  # 点击新增按钮
        menu.inputValue(menu.input_list[1],menu.reason)#输入户名
        menu.inputValue(menu.input_list[2], menu.reason)  # 输入开户机构
        menu.inputValue(menu.input_list[5], menu.valueList[0])   #输入账号
        #menu.inputValue(menu.input_list[6], menu.valueList[1])#输入手机号
        menu.cBtn(menu.button_list[7]) #点击提交
        time.sleep(1)
        flag = menu.isElementExist(menu.msg_list[2])
        self.assertTrue(flag, '出现提示信息')
        if flag:
            msgInfo = menu.getValue(*menu.msg_list[2])
            self.assertEqual(msgInfo, '不能为空', '提示信息正确')

    def test_addotherbank_4(self):
        '''不输入户名提交验证'''
        menu = OtherBank_Page(self.driver)  # 实例化对方银行设置页面
        self.login.loginFunc()  # 登录
        menu.InotherBankpage()  # 进入对方银行设置页面
        time.sleep(3)
        menu.cBtn(menu.button_list[1])  # 点击新增按钮
        menu.inputValue(menu.input_list[0], menu.reason)   #输入银行名称
        menu.inputValue(menu.input_list[2], menu.reason)   # 输入开户机构
        menu.inputValue(menu.input_list[5], menu.reason)   #输入短信接收人
        menu.inputValue(menu.input_list[6], menu.valueList[1])#输入手机号
        menu.cBtn(menu.button_list[7]) #点击提交
        time.sleep(1)
        flag = menu.isElementExist(menu.msg_list[3])
        self.assertTrue(flag, '出现提示信息')
        if flag:
            msgInfo = menu.getValue(*menu.msg_list[3])
            self.assertEqual(msgInfo, '不能为空', '提示信息正确')

    def test_addotherbank_5(self):
        '''不输入开户机构提交验证'''
        menu = OtherBank_Page(self.driver)  # 实例化对方银行设置页面
        self.login.loginFunc()  # 登录
        menu.InotherBankpage()  # 进入对方银行设置页面
        time.sleep(3)
        menu.cBtn(menu.button_list[1])  # 点击新增按钮
        menu.inputValue(menu.input_list[0], menu.reason)   #输入银行名称
        menu.inputValue(menu.input_list[1], menu.reason)   # 输入户名
        menu.inputValue(menu.input_list[5], menu.reason)   #输入短信接收人
        menu.inputValue(menu.input_list[6], menu.valueList[1])#输入手机号
        menu.cBtn(menu.button_list[7]) #点击提交
        time.sleep(1)
        flag = menu.isElementExist(menu.msg_list[4])
        self.assertTrue(flag, '出现提示信息')
        if flag:
            msgInfo = menu.getValue(*menu.msg_list[4])
            self.assertEqual(msgInfo, '不能为空', '提示信息正确')

    def test_addotherbank_6(self):
        '''不输入短信接收人提交验证'''
        menu = OtherBank_Page(self.driver)  # 实例化对方银行设置页面
        self.login.loginFunc()  # 登录
        menu.InotherBankpage()  # 进入对方银行设置页面
        time.sleep(3)
        menu.cBtn(menu.button_list[1])  # 点击新增按钮
        menu.inputValue(menu.input_list[0], menu.reason)  # 输入银行名称
        menu.inputValue(menu.input_list[1], menu.reason)  # 输入户名
        menu.inputValue(menu.input_list[2], menu.reason)  # 输入开户机构
        menu.inputValue(menu.input_list[6], menu.valueList[1])  # 输入手机号
        menu.cBtn(menu.button_list[7])  # 点击提交
        time.sleep(1)
        flag = menu.isElementExist(menu.msg_list[5])
        self.assertTrue(flag, '出现提示信息')
        if flag:
            msgInfo = menu.getValue(*menu.msg_list[5])
            self.assertEqual(msgInfo, '不能为空', '提示信息正确')

    def test_addotherbank_7(self):
        '''不输入手机号提交验证'''
        menu = OtherBank_Page(self.driver)  # 实例化对方银行设置页面
        self.login.loginFunc()  # 登录
        menu.InotherBankpage()  # 进入对方银行设置页面
        time.sleep(3)
        menu.cBtn(menu.button_list[1])  # 点击新增按钮
        menu.inputValue(menu.input_list[0], menu.reason)  # 输入银行名称
        menu.inputValue(menu.input_list[1], menu.reason)  # 输入户名
        menu.inputValue(menu.input_list[2], menu.reason)  # 输入开户机构
        menu.inputValue(menu.input_list[5], menu.reason)  # 输入短信接收人
        menu.cBtn(menu.button_list[7])  # 点击提交
        time.sleep(1)
        flag = menu.isElementExist(menu.msg_list[6])
        self.assertTrue(flag, '出现提示信息')
        if flag:
            msgInfo = menu.getValue(*menu.msg_list[6])
            self.assertEqual(msgInfo, '请输入正确的手机号', '提示信息正确')

    def test_addotherbank_8(self):
        '''输入不规则手机号验证'''
        menu = OtherBank_Page(self.driver)  # 实例化对方银行设置页面
        self.login.loginFunc()  # 登录
        menu.InotherBankpage()  # 进入对方银行设置页面
        time.sleep(3)
        menu.cBtn(menu.button_list[1])  # 点击新增按钮
        menu.inputValue(menu.input_list[0], menu.reason)  # 输入银行名称
        menu.inputValue(menu.input_list[1], menu.reason)  # 输入户名
        menu.inputValue(menu.input_list[2], menu.reason)  # 输入开户机构
        menu.inputValue(menu.input_list[5], menu.reason)  # 输入短信接收人
        menu.inputValue(menu.input_list[6], menu.reason)  # 输入手机号
        menu.cBtn(menu.button_list[7])  # 点击提交
        time.sleep(1)
        flag = menu.isElementExist(menu.msg_list[6])
        self.assertTrue(flag, '出现提示信息')
        if flag:
            msgInfo = menu.getValue(*menu.msg_list[6])
            self.assertEqual(msgInfo, '请输入正确的手机号', '提示信息正确')

    def test_addotherbank_9(self):
        '''正确新增验证'''
        menu = OtherBank_Page(self.driver)  # 实例化对方银行设置页面
        self.login.loginFunc()  # 登录
        menu.InotherBankpage()  # 进入对方银行设置页面
        time.sleep(3)
        menu.cBtn(menu.button_list[1])  # 点击新增按钮
        menu.inputValue(menu.input_list[0], menu.reason)  # 输入银行名称
        menu.inputValue(menu.input_list[1], menu.reason)  # 输入户名
        menu.inputValue(menu.input_list[2], menu.reason)  # 输入开户机构
        menu.inputValue(menu.input_list[5], menu.reason)  # 输入短信接收人
        menu.inputValue(menu.input_list[6], menu.valueList[1])  # 输入手机号
        menu.cBtn(menu.whether[0])#是农商行
        menu.cBtn(menu.button_list[7])  # 点击提交
        time.sleep(1.5)
        flag = menu.isElementExist(menu.msg_list[0])
        self.assertTrue(flag, '弹出提示信息')
        if flag:
            msgInfo = menu.getValue(*menu.msg_list[0])
            self.assertEqual(msgInfo, '×\n提示! 新增成功！', '提示信息正确')

    def test_addotherbank_10(self):
        '''重复新增验证'''
        menu = OtherBank_Page(self.driver)  # 实例化对方银行设置页面
        self.login.loginFunc()  # 登录
        menu.InotherBankpage()  # 进入对方银行设置页面
        time.sleep(3)
        menu.cBtn(menu.button_list[1])  # 点击新增按钮
        menu.inputValue(menu.input_list[0], menu.valueList[2])  # 输入银行名称
        menu.inputValue(menu.input_list[1], menu.reason)  # 输入户名
        menu.inputValue(menu.input_list[2], menu.reason)  # 输入开户机构
        menu.inputValue(menu.input_list[5], menu.reason)  # 输入短信接收人
        menu.inputValue(menu.input_list[6], menu.valueList[1])  # 输入手机号
        menu.cBtn(menu.whether[0])#是农商行
        menu.cBtn(menu.button_list[7])  # 点击提交
        time.sleep(1)
        flag = menu.getValue(*menu.msg_list[14])
        self.assertEqual(flag, '×\n提示! 银行名不可以重复，可以使用别名。或该银行账户已存在，请仔细核对')

    def test_addotherbank_13(self):
        '''点击取消验证验证'''
        menu = OtherBank_Page(self.driver)  # 实例化对方银行设置页面
        self.login.loginFunc()  # 登录
        menu.InotherBankpage()  # 进入对方银行设置页面
        time.sleep(3)
        menu.cBtn(menu.button_list[1])  # 点击新增按钮
        menu.cBtn(menu.button_list[8])  # 点击取消
        time.sleep(1)
        flag = menu.isElementExist(menu.msg_list[1])
        self.assertFalse(flag, '关闭新增窗口')

    def test_update_1(self):
        '''点击修改验证'''
        menu = OtherBank_Page(self.driver)  # 实例化对方银行设置页面
        self.login.loginFunc()  # 登录
        menu.InotherBankpage()  # 进入对方银行设置页面
        time.sleep(3)
        menu.cBtn(menu.button_list[2])#点击修改按钮
        time.sleep(1)
        msg = menu.getValue(*menu.msg_list[0])
        self.assertEqual(msg,'×\n提示! 请选中一项内容！', '提示信息正确')

    def test_update_2(self):
        '''选择多项点击修改'''
        menu = OtherBank_Page(self.driver)  # 实例化对方银行设置页面
        self.login.loginFunc()  # 登录
        menu.InotherBankpage()  # 进入对方银行设置页面
        time.sleep(3)
        menu.cBtn(menu.check_box[2])#全选
        menu.cBtn(menu.button_list[2])  # 点击修改按钮
        time.sleep(1)
        msg = menu.getValue(*menu.msg_list[0])
        self.assertEqual(msg, '×\n提示! 请选中一项内容进行操作！', '提示信息正确')

    def test_update_3(self):
        '''选择一项点击修改'''
        menu = OtherBank_Page(self.driver)  # 实例化对方银行设置页面
        self.login.loginFunc()  # 登录
        menu.InotherBankpage()  # 进入对方银行设置页面
        time.sleep(3)
        menu.cBtn(menu.check_box[0])  # 选择一项
        menu.cBtn(menu.button_list[2])  # 点击修改按钮
        time.sleep(1)
        msg = menu.isElementExist(menu.msg_list[10])
        self.assertTrue(msg,'弹出修改窗口')

    def test_update_4(self):
        '''清空必填项点击提交验证'''
        menu = OtherBank_Page(self.driver)  # 实例化对方银行设置页面
        self.login.loginFunc()  # 登录
        menu.InotherBankpage()  # 进入对方银行设置页面
        time.sleep(3)
        menu.cBtn(menu.check_box[0])  # 选择一项
        menu.cBtn(menu.button_list[2])  # 点击修改按钮
        '''清空必填项'''
        menu.clearValue(menu.input_list[0])
        menu.clearValue(menu.input_list[1])
        menu.clearValue(menu.input_list[2])
        menu.clearValue(menu.input_list[8])
        menu.clearValue(menu.input_list[9])
        menu.cBtn(menu.button_list[9])#点击提交按钮
        time.sleep(1)
        flag1  = menu.isElementExist(menu.msg_list[2])
        self.assertTrue(flag1,'出现提示信息')
        if flag1:
            msgInfo1 = menu.getValue(*menu.msg_list[2])
            self.assertEqual(msgInfo1,'不能为空','提示信息正确')
        flag2 = menu.isElementExist(menu.msg_list[3])
        self.assertTrue(flag2, '出现提示信息')
        if flag2:
            msgInfo2 = menu.getValue(*menu.msg_list[3])
            self.assertEqual(msgInfo2, '不能为空','提示信息正确')
        flag3 = menu.isElementExist(menu.msg_list[4])
        self.assertTrue(flag3, '出现提示信息')
        if flag3:
            msgInfo3 = menu.getValue(*menu.msg_list[4])
            self.assertEqual(msgInfo3, '不能为空','提示信息正确')
        flag4 = menu.isElementExist(menu.msg_list[9])
        self.assertTrue(flag4, '出现提示信息')
        if flag4:
            msgInfo4 = menu.getValue(*menu.msg_list[9])
            self.assertEqual(msgInfo4, '请输入正确的手机号','提示信息正确')
        flag5 = menu.isElementExist(menu.msg_list[8])
        self.assertTrue(flag5, '出现提示信息')
        if flag5:
            msgInfo5 = menu.getValue(*menu.msg_list[8])
            self.assertEqual(msgInfo5, '不能为空', '提示信息正确')

    def test_update_5(self):
        '''清空银行名称点击提交验证'''
        menu = OtherBank_Page(self.driver)  # 实例化对方银行设置页面
        self.login.loginFunc()  # 登录
        menu.InotherBankpage()  # 进入对方银行设置页面
        time.sleep(3)
        menu.cBtn(menu.check_box[0])  # 选择一项
        menu.cBtn(menu.button_list[2])  # 点击修改按钮
        menu.clearValue(menu.input_list[0])#清空银行名称
        menu.cBtn(menu.button_list[9])  # 点击提交按钮
        time.sleep(1)
        flag = menu.isElementExist(menu.msg_list[2])
        self.assertTrue(flag, '出现提示信息')
        if flag:
            msgInfo = menu.getValue(*menu.msg_list[2])
            self.assertEqual(msgInfo, '不能为空', '提示信息正确')

    def test_update_6(self):
        '''清空户名点击提交验证'''
        menu = OtherBank_Page(self.driver)  # 实例化对方银行设置页面
        self.login.loginFunc()  # 登录
        menu.InotherBankpage()  # 进入对方银行设置页面
        time.sleep(3)
        menu.cBtn(menu.check_box[0])  # 选择一项
        menu.cBtn(menu.button_list[2])  # 点击修改按钮
        menu.clearValue(menu.input_list[1])#清空户名
        menu.cBtn(menu.button_list[9])  # 点击提交按钮
        time.sleep(1)
        flag = menu.isElementExist(menu.msg_list[3])
        self.assertTrue(flag, '出现提示信息')
        if flag:
            msgInfo = menu.getValue(*menu.msg_list[3])
            self.assertEqual(msgInfo, '不能为空', '提示信息正确')

    def test_update_7(self):
        '''清空开户机构点击提交验证'''
        menu = OtherBank_Page(self.driver)  # 实例化对方银行设置页面
        self.login.loginFunc()  # 登录
        menu.InotherBankpage()  # 进入对方银行设置页面
        time.sleep(3)
        menu.cBtn(menu.check_box[0])  # 选择一项
        menu.cBtn(menu.button_list[2])  # 点击修改按钮
        menu.clearValue(menu.input_list[2])#清空开户机构
        menu.cBtn(menu.button_list[9])  # 点击提交按钮
        time.sleep(1)
        flag = menu.isElementExist(menu.msg_list[4])
        self.assertTrue(flag, '出现提示信息')
        if flag:
            msgInfo = menu.getValue(*menu.msg_list[4])
            self.assertEqual(msgInfo, '不能为空', '提示信息正确')

    def test_update_8(self):
        '''清空短信接收人点击提交验证'''
        menu = OtherBank_Page(self.driver)  # 实例化对方银行设置页面
        self.login.loginFunc()  # 登录
        menu.InotherBankpage()  # 进入对方银行设置页面
        time.sleep(3)
        menu.cBtn(menu.check_box[0])  # 选择一项
        menu.cBtn(menu.button_list[2])  # 点击修改按钮
        menu.clearValue(menu.input_list[8])#清空短信接收人
        menu.cBtn(menu.button_list[9])  # 点击提交按钮
        time.sleep(1)
        flag = menu.isElementExist(menu.msg_list[8])
        self.assertTrue(flag, '出现提示信息')
        if flag:
            msgInfo = menu.getValue(*menu.msg_list[8])
            self.assertEqual(msgInfo, '不能为空', '提示信息正确')

    def test_update_9(self):
        '''清空短信接收人手机号点击提交验证'''
        menu = OtherBank_Page(self.driver)  # 实例化对方银行设置页面
        self.login.loginFunc()  # 登录
        menu.InotherBankpage()  # 进入对方银行设置页面
        time.sleep(3)
        menu.cBtn(menu.check_box[0])  # 选择一项
        menu.cBtn(menu.button_list[2])  # 点击修改按钮
        menu.clearValue(menu.input_list[9])#清空短信接收人手机号
        menu.cBtn(menu.button_list[9])  # 点击提交按钮
        time.sleep(1)
        flag = menu.isElementExist(menu.msg_list[9])
        self.assertTrue(flag, '出现提示信息')
        if flag:
            msgInfo = menu.getValue(*menu.msg_list[9])
            self.assertEqual(msgInfo, '请输入正确的手机号', '提示信息正确')

    def test_update_10(self):
        '''修改输入不规则短信接收人手机号点击提交验证'''
        menu = OtherBank_Page(self.driver)  # 实例化对方银行设置页面
        self.login.loginFunc()  # 登录
        menu.InotherBankpage()  # 进入对方银行设置页面
        time.sleep(3)
        menu.cBtn(menu.check_box[0])  # 选择一项
        menu.cBtn(menu.button_list[2])  # 点击修改按钮
        menu.inputValue(menu.input_list[9],menu.reason)#输入不规则手机号
        menu.cBtn(menu.button_list[9])  # 点击提交按钮
        time.sleep(1)
        flag = menu.isElementExist(menu.msg_list[9])
        self.assertTrue(flag, '出现提示信息')
        if flag:
            msgInfo = menu.getValue(*menu.msg_list[9])
            self.assertEqual(msgInfo, '请输入正确的手机号', '提示信息正确')

    def test_update_11(self):
        '''修改必填项点击提交验证'''
        menu = OtherBank_Page(self.driver)  # 实例化对方银行设置页面
        self.login.loginFunc()  # 登录
        menu.InotherBankpage()  # 进入对方银行设置页面
        time.sleep(3)
        menu.cBtn(menu.check_box[1])  # 选择一项
        menu.cBtn(menu.button_list[2])  # 点击修改按钮
        '''修改必填项'''
        menu.inputValue(menu.input_list[0],menu.reason)
        menu.inputValue(menu.input_list[1], menu.reason)
        menu.inputValue(menu.input_list[2], menu.reason)
        menu.inputValue(menu.input_list[8], menu.reason)
        menu.inputValue(menu.input_list[9], menu.valueList[1])
        menu.cBtn(menu.button_list[9])#点击提交按钮
        time.sleep(1)
        flag = menu.isElementExist(menu.msg_list[0])
        self.assertTrue(flag, '弹出提示信息')
        if flag:
            msgInfo = menu.getValue(*menu.msg_list[0])
            self.assertEqual(msgInfo, '×\n提示! 修改成功！', '提示信息正确')

    def test_update_12(self):
        '''修改输入重复银行名称点击提交验证'''
        menu = OtherBank_Page(self.driver)  # 实例化对方银行设置页面
        self.login.loginFunc()  # 登录
        menu.InotherBankpage()  # 进入对方银行设置页面
        time.sleep(3)
        menu.cBtn(menu.check_box[1])  # 选择一项
        menu.cBtn(menu.button_list[2])  # 点击修改按钮
        '''修改必填项'''
        menu.inputValue(menu.input_list[0],menu.valueList[2])
        menu.inputValue(menu.input_list[1], menu.reason)
        menu.inputValue(menu.input_list[2], menu.reason)
        menu.inputValue(menu.input_list[8], menu.reason)
        menu.inputValue(menu.input_list[9], menu.valueList[1])
        menu.cBtn(menu.button_list[9])#点击提交按钮
        time.sleep(1)
        flag = menu.getValue(*menu.msg_list[14])
        self.assertEqual(flag, '×\n提示! 银行名不可以重复，可以使用别名。或该银行账户已存在，请仔细核对')

    def test_update_13(self):
        '''点击修改取消验证'''
        menu = OtherBank_Page(self.driver)  # 实例化对方银行设置页面
        self.login.loginFunc()  # 登录
        menu.InotherBankpage()  # 进入对方银行设置页面
        time.sleep(3)
        menu.cBtn(menu.check_box[1])  # 选择一项
        menu.cBtn(menu.button_list[2])  # 点击修改按钮
        menu.cBtn(menu.button_list[10])#点击取消按钮
        msg = menu.isElementExist(menu.msg_list[10])
        self.assertFalse(msg,'关闭修改窗口')

    def test_delete_1(self):
        '''点击删除验证'''
        menu = OtherBank_Page(self.driver)  # 实例化对方银行设置页面
        self.login.loginFunc()  # 登录
        menu.InotherBankpage()  # 进入对方银行设置页面
        time.sleep(3)
        menu.cBtn(menu.button_list[3])#点击删除
        time.sleep(1)
        msg = menu.getValue(*menu.msg_list[0])
        self.assertEqual(msg,'×\n提示! 请选中一项内容！', '提示信息正确')

    def test_delete_2(self):
        '''选择一项点击删除验证'''
        menu = OtherBank_Page(self.driver)  # 实例化对方银行设置页面
        self.login.loginFunc()  # 登录
        menu.InotherBankpage()  # 进入对方银行设置页面
        time.sleep(3)
        menu.cBtn(menu.check_box[1])#选择删除项
        menu.cBtn(menu.button_list[3])#点击删除
        time.sleep(1)
        msg = menu.isElementExist(menu.msg_list[11])
        self.assertTrue(msg,'弹出删除窗口')

    def test_delete_3(self):
        '''确定删除验证'''
        menu = OtherBank_Page(self.driver)  # 实例化对方银行设置页面
        self.login.loginFunc()  # 登录
        menu.InotherBankpage()  # 进入对方银行设置页面
        time.sleep(3)
        menu.cBtn(menu.check_box[1])#选择删除项
        menu.cBtn(menu.button_list[3])#点击删除
        menu.cBtn(menu.button_list[11])#点击确定按钮
        time.sleep(1)
        flag = menu.isElementExist(menu.msg_list[13])
        self.assertTrue(flag,'弹出提示信息')
        msg = menu.getValue(*menu.msg_list[13])
        self.assertEqual(msg, '×\n提示! 删除成功！', '提示信息正确')

    def test_delete_4(self):
        '''取消删除验证'''
        menu = OtherBank_Page(self.driver)  # 实例化对方银行设置页面
        self.login.loginFunc()  # 登录
        menu.InotherBankpage()  # 进入对方银行设置页面
        time.sleep(3)
        menu.cBtn(menu.check_box[1])#选择删除项
        menu.cBtn(menu.button_list[3])#点击删除
        menu.cBtn(menu.button_list[12])#点击取消按钮
        # flag = menu.isElementExist(menu.msg_list[11])
        # self.assertFalse(flag,'关闭删除窗口')

if __name__ == '__main__':
        pass
