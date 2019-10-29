'''
Code description：单笔支付模块 testcase
Create time：
Developer：
'''
import time
from framfriend.test_case.models.myunit import MyunitTest
from framfriend.test_case.page_obj.pay_page import pay_Page

class pay_Tc(MyunitTest):
    '''单笔支付模块用例'''

    def test_singlePay_1(self):
        '''选择村居验证'''
        menu = pay_Page(self.driver)  # 实例化单笔支付页面
        self.login.loginFunc()  # 登录
        menu.insinglePay() # 进入单笔支付页面
        time.sleep(2)
        menu.cBtn(menu.button_list[0])
        menu.cBtn(menu.button_list[1])#选择村居
        msg1_1 = menu.isElementExist(menu.msg_list[10])
        self.assertTrue(msg1_1,'显示账号')
        msg1_2 = menu.isElementExist(menu.msg_list[11])
        self.assertTrue(msg1_2,'显示户名')
        msg1_3 = menu.isElementExist(menu.msg_list[12])
        self.assertTrue(msg1_3,'显示联行号')

    def test_singlePay_2(self):
        '''选择收款方验证'''
        menu = pay_Page(self.driver)  # 实例化单笔支付页面
        self.login.loginFunc()  # 登录
        menu.insinglePay() # 进入单笔支付页面
        time.sleep(2)
        menu.cBtn(menu.button_list[0])
        menu.cBtn(menu.button_list[1])#选择村居
        menu.cBtn(menu.button_list[2])
        menu.cBtn(menu.button_list[3])#选择收款方
        msg2_1 = menu.isElementExist(menu.msg_list[13])
        self.assertTrue(msg2_1, '显示收款账号')
        msg2_2 = menu.isElementExist(menu.msg_list[14])
        self.assertTrue(msg2_2, '显示户名')
        msg2_3 = menu.isElementExist(menu.msg_list[15])
        self.assertTrue(msg2_3, '显示联行号')
        msg2_4 = menu.isElementExist(menu.msg_list[16])
        self.assertTrue(msg2_4, '显示是否农商行')

    def test_singlePay_3(self):
        '''不输入内容点击开始支付验证'''
        menu = pay_Page(self.driver)  # 实例化单笔支付页面
        self.login.loginFunc()  # 登录
        menu.insinglePay()  # 进入单笔支付页面
        time.sleep(2)
        menu.cBtn(menu.button_list[5])#点击开始支付
        msg3_1 = menu.isElementExist(menu.msg_list[0])
        if msg3_1:
            msgInfo3 = menu.getValue(*menu.msg_list[0])
            self.assertEqual(msgInfo3,'不能为空','提示信息正确')
        msg3_2 = menu.isElementExist(menu.msg_list[3])
        self.assertTrue(msg3_2, '出现提示信息')
        if msg3_2:
            msgInfo4 = menu.getValue(*menu.msg_list[3])
            self.assertEqual(msgInfo4,'请输入有效的数字','提示信息正确')
        msg3_3 = menu.isElementExist(menu.msg_list[4])
        self.assertTrue(msg3_3, '出现提示信息')
        if msg3_3:
            msgInfo5 = menu.getValue(*menu.msg_list[4])
            self.assertEqual(msgInfo5,'不能为空','提示信息正确')

    def test_singlePay_4(self):
        '''不选择村居点击开始支付验证'''
        menu = pay_Page(self.driver)  # 实例化单笔支付页面
        self.login.loginFunc()  # 登录
        menu.insinglePay()  # 进入单笔支付页面
        time.sleep(2)
        menu.inputValue(menu.input_list[4],menu.valueList[2])
        menu.inputValue(menu.input_list[5],menu.reason)
        menu.cBtn(menu.button_list[5])#点击开始支付
        msg4_1 = menu.isElementExist(menu.msg_list[0])
        self.assertTrue(msg4_1, '出现提示信息')
        if msg4_1:
            msgInfo1 = menu.getValue(*menu.msg_list[0])
            self.assertEqual(msgInfo1,'不能为空','提示信息正确')

    def test_singlePay_5(self):
            '''不选择收款方点击开始支付验证'''
            menu = pay_Page(self.driver)  # 实例化单笔支付页面
            self.login.loginFunc()  # 登录
            menu.insinglePay()  # 进入单笔支付页面
            time.sleep(2)
            menu.cBtn(menu.button_list[0])
            menu.cBtn(menu.button_list[1])  # 选择村居
            menu.inputValue(menu.input_list[4], menu.valueList[2])#输入金额
            menu.inputValue(menu.input_list[5], menu.reason)#输入摘要
            menu.cBtn(menu.button_list[5])  # 点击开始支付
            msg5_1 = menu.isElementExist(menu.msg_list[17])
            self.assertTrue(msg5_1, '收款方出现提示信息')
            if msg5_1:
                msgInfo1 = menu.getValue(*menu.msg_list[17])
                self.assertEqual(msgInfo1, '不能为空', '提示信息正确')

    def test_singlePay_6(self):
        '''不输入金额点击开始支付验证'''
        menu = pay_Page(self.driver)  # 实例化单笔支付页面
        self.login.loginFunc()  # 登录
        menu.insinglePay()  # 进入单笔支付页面
        time.sleep(2)
        menu.cBtn(menu.button_list[0])
        menu.cBtn(menu.button_list[1])  # 选择村居
        menu.cBtn(menu.button_list[2])
        menu.cBtn(menu.button_list[3])  # 选择收款方
        menu.inputValue(menu.input_list[5], menu.reason)  # 输入摘要
        menu.cBtn(menu.button_list[5])  # 点击开始支付
        msg6_1 = menu.isElementExist(menu.msg_list[3])
        self.assertTrue(msg6_1, '金额出现提醒信息')
        if msg6_1:
            msgInfo = menu.getValue(*menu.msg_list[3])
            self.assertEqual(msgInfo, '请输入有效的数字', '提示信息正确')

    def test_singlePay_7(self):
        '''不输入摘要点击开始支付验证'''
        menu = pay_Page(self.driver)  # 实例化单笔支付页面
        self.login.loginFunc()  # 登录
        menu.insinglePay()  # 进入单笔支付页面
        time.sleep(2)
        menu.cBtn(menu.button_list[0])
        menu.cBtn(menu.button_list[1])  # 选择村居
        menu.cBtn(menu.button_list[2])
        menu.cBtn(menu.button_list[3])  # 选择收款方
        menu.inputValue(menu.input_list[4], menu.valueList[2])  # 输入金额
        menu.cBtn(menu.button_list[5])  # 点击开始支付
        msg7_1 = menu.isElementExist(menu.msg_list[4])
        self.assertTrue(msg7_1, '摘要出现提示信息')
        if msg7_1:
            msgInfo = menu.getValue(*menu.msg_list[4])
            self.assertEqual(msgInfo, '不能为空', '提示信息正确')

    def test_singlePay_8(self):
        '''输入错误金额点击开始支付验证'''
        menu = pay_Page(self.driver)  # 实例化单笔支付页面
        self.login.loginFunc()  # 登录
        menu.insinglePay()  # 进入单笔支付页面
        time.sleep(2)
        menu.cBtn(menu.button_list[0])
        menu.cBtn(menu.button_list[1])  # 选择村居
        menu.cBtn(menu.button_list[2])
        menu.cBtn(menu.button_list[3])  # 选择收款方
        menu.inputValue(menu.input_list[4], menu.reason)  # 输入错误金额
        menu.inputValue(menu.input_list[5], menu.reason)  # 输入摘要
        menu.cBtn(menu.button_list[5])  # 点击开始支付
        msg8_1 = menu.isElementExist(menu.msg_list[3])
        self.assertTrue(msg8_1, '金额出现提示信息')
        if msg8_1:
            msgInfo = menu.getValue(*menu.msg_list[3])
            self.assertEqual(msgInfo, '请输入有效的数字', '提示信息正确')

    def test_singlePay_9(self):
        '''正确输入点击开始支付验证'''
        menu = pay_Page(self.driver)  # 实例化单笔支付页面
        self.login.loginFunc()  # 登录
        menu.insinglePay()  # 进入单笔支付页面
        time.sleep(2)
        menu.cBtn(menu.button_list[0])
        menu.cBtn(menu.button_list[1])  # 选择村居
        menu.cBtn(menu.button_list[2])
        menu.cBtn(menu.button_list[3])  # 选择收款方
        menu.inputValue(menu.input_list[4], menu.valueList[2])  # 输入金额
        menu.inputValue(menu.input_list[5], menu.reason)  # 输入摘要
        menu.cBtn(menu.button_list[5])  # 点击开始支付
        msg9_1 = menu.isElementExist(menu.msg_list[18])
        self.assertTrue(msg9_1, '弹出确认支付窗口')

    def test_singlePay_10(self):
        '''不输入支付密码确定验证'''
        menu = pay_Page(self.driver)  # 实例化单笔支付页面
        self.login.loginFunc()  # 登录
        menu.insinglePay()  # 进入单笔支付页面
        time.sleep(2)
        menu.cBtn(menu.button_list[0])
        menu.cBtn(menu.button_list[1])  # 选择村居
        menu.cBtn(menu.button_list[2])
        menu.cBtn(menu.button_list[3])  # 选择收款方
        menu.inputValue(menu.input_list[4], menu.valueList[2])  # 输入金额
        menu.inputValue(menu.input_list[5], menu.reason)  # 输入摘要
        menu.cBtn(menu.button_list[5])  # 点击开始支付
        menu.cBtn(menu.button_list[7])#点击确定按钮
        msg10_1 = menu.isElementExist(menu.msg_list[9])
        self.assertTrue(msg10_1, '提示信息')

    def test_singlePay_11(self):
        '''输入错误支付密码确定验证'''
        menu = pay_Page(self.driver)  # 实例化单笔支付页面
        self.login.loginFunc()  # 登录
        menu.insinglePay()  # 进入单笔支付页面
        time.sleep(2)
        menu.cBtn(menu.button_list[0])
        menu.cBtn(menu.button_list[1])  # 选择村居
        menu.cBtn(menu.button_list[2])
        menu.cBtn(menu.button_list[3])  # 选择收款方
        menu.inputValue(menu.input_list[4], menu.valueList[2])  # 输入金额
        menu.inputValue(menu.input_list[5], menu.reason)  # 输入摘要
        menu.cBtn(menu.button_list[5])  # 点击开始支付
        menu.inputValue(menu.input_list[6],menu.valueList[2])#输入错误密码验证
        menu.cBtn(menu.button_list[7])  # 点击确定按钮
        msg11_1 = menu.isElementExist(menu.msg_list[9])
        self.assertTrue(msg11_1, '提示信息')

    def test_singlePay_12(self):
        '''输入正确支付密码确定验证'''
        menu = pay_Page(self.driver)  # 实例化单笔支付页面
        self.login.loginFunc()  # 登录
        menu.insinglePay()  # 进入单笔支付页面
        time.sleep(2)
        menu.cBtn(menu.button_list[0])
        menu.cBtn(menu.button_list[1])  # 选择村居
        menu.cBtn(menu.button_list[2])
        menu.cBtn(menu.button_list[3])  # 选择收款方
        menu.inputValue(menu.input_list[4], menu.valueList[2])  # 输入金额
        menu.inputValue(menu.input_list[5], menu.reason)  # 输入摘要
        menu.cBtn(menu.button_list[5])  # 点击开始支付
        menu.inputValue(menu.input_list[6], menu.valueList[3])  # 输入密码
        menu.cBtn(menu.button_list[7])  # 点击确定按钮
        msg12_1 = menu.isElementExist(menu.msg_list[9])
        self.assertTrue(msg12_1, '提示信息')

    def test_singlePay_13(self):
        '''关闭支付验证'''
        menu = pay_Page(self.driver)  # 实例化单笔支付页面
        self.login.loginFunc()  # 登录
        menu.insinglePay()  # 进入单笔支付页面
        time.sleep(2)
        menu.cBtn(menu.button_list[0])
        menu.cBtn(menu.button_list[1])  # 选择村居
        menu.cBtn(menu.button_list[2])
        menu.cBtn(menu.button_list[3])  # 选择收款方
        menu.inputValue(menu.input_list[4], menu.valueList[2])  # 输入金额
        menu.inputValue(menu.input_list[5], menu.reason)  # 输入摘要
        menu.cBtn(menu.button_list[5])  # 点击开始支付
        menu.inputValue(menu.input_list[6], menu.valueList[3])  # 输入密码
        menu.cBtn(menu.button_list[6])  # 点击关闭按钮
        msg13_1 = menu.isElementExist(menu.msg_list[19])
        self.assertTrue(msg13_1, '关闭支付窗口')

    def test_singlePay_14(self):
        '''点击添加新收款方验证'''
        menu = pay_Page(self.driver)  # 实例化单笔支付页面
        self.login.loginFunc()  # 登录
        menu.insinglePay()  # 进入单笔支付页面
        time.sleep(2)
        menu.cBtn(menu.button_list[4])#点击添加新收款方
        msg14_1 = menu.isElementExist(menu.msg_list[20])
        self.assertTrue(msg14_1, '窗口验证')

    def test_singlePay_15(self):
        '''不输入新收款方内容支付验证'''
        menu = pay_Page(self.driver)  # 实例化单笔支付页面
        self.login.loginFunc()  # 登录
        menu.insinglePay()  # 进入单笔支付页面
        time.sleep(2)
        menu.cBtn(menu.button_list[0])
        menu.cBtn(menu.button_list[1])  # 选择村居
        menu.cBtn(menu.button_list[4])  # 点击添加新收款方
        menu.inputValue(menu.input_list[4], menu.valueList[2])  # 输入金额
        menu.inputValue(menu.input_list[5], menu.reason)  # 输入摘要
        menu.cBtn(menu.button_list[5])  # 点击开始支付
        msg15_2 = menu.isElementExist(menu.msg_list[6])
        self.assertTrue(msg15_2,'收款账号出现提示信息')
        if msg15_2:
            msgInfo2 = menu.getValue(*menu.msg_list[6])
            self.assertEqual(msgInfo2, '不能为空', '提示信息正确')
        msg15_3 = menu.isElementExist(menu.msg_list[7])
        self.assertTrue(msg15_3,'收款户名出现提示信息')
        if msg15_3:
            msgInfo3 = menu.getValue(*menu.msg_list[7])
            self.assertEqual(msgInfo3, '不能为空', '提示信息正确')
        msg15_4 = menu.isElementExist(menu.msg_list[8])
        self.assertTrue(msg15_4,'联行号出现提示信息')
        if msg15_4:
            msgInfo4 = menu.getValue(*menu.msg_list[8])
            self.assertEqual(msgInfo4, '不能为空', '提示信息正确')

    def test_singlePay_16(self):
        '''不输入新收款方账号支付验证'''
        menu = pay_Page(self.driver)  # 实例化单笔支付页面
        self.login.loginFunc()  # 登录
        menu.insinglePay()  # 进入单笔支付页面
        time.sleep(2)
        menu.cBtn(menu.button_list[0])
        menu.cBtn(menu.button_list[1])  # 选择村居
        menu.cBtn(menu.button_list[4])  # 点击添加新收款方
        menu.inputValue(menu.input_list[2], menu.reason)  # 输入户名
        menu.inputValue(menu.input_list[3], menu.valueList[1])  # 输入联行号
        menu.inputValue(menu.input_list[4], menu.valueList[2])  # 输入金额
        menu.inputValue(menu.input_list[5], menu.reason)  # 输入摘要
        menu.cBtn(menu.button_list[5])  # 点击开始支付
        msg15_2 = menu.isElementExist(menu.msg_list[6])
        self.assertTrue(msg15_2, '收款账号出现提示信息')
        if msg15_2:
            msgInfo2 = menu.getValue(*menu.msg_list[6])
            self.assertEqual(msgInfo2, '不能为空', '提示信息正确')

    def test_singlePay_17(self):
        '''输入不规则新收款方账号支付验证'''
        menu = pay_Page(self.driver)  # 实例化单笔支付页面
        self.login.loginFunc()  # 登录
        menu.insinglePay()  # 进入单笔支付页面
        time.sleep(2)
        menu.cBtn(menu.button_list[0])
        menu.cBtn(menu.button_list[1])  # 选择村居
        menu.cBtn(menu.button_list[4])  # 点击添加新收款方
        menu.inputValue(menu.input_list[1], menu.reason)  # 输入账号
        menu.inputValue(menu.input_list[2], menu.reason)  # 输入户名
        menu.inputValue(menu.input_list[3], menu.valueList[1])  # 输入联行号
        menu.inputValue(menu.input_list[4], menu.valueList[2])  # 输入金额
        menu.inputValue(menu.input_list[5], menu.reason)  # 输入摘要
        menu.cBtn(menu.button_list[5])  # 点击开始支付
        msg15_2 = menu.isElementExist(menu.msg_list[5])
        self.assertTrue(msg15_2, '收款账号出现提示信息')
        if msg15_2:
            msgInfo2 = menu.getValue(*menu.msg_list[5])
            self.assertEqual(msgInfo2, '请输入有效的数字', '提示信息正确')

    def test_singlePay_18(self):
        '''不输入新收款方户名支付验证'''
        menu = pay_Page(self.driver)  # 实例化单笔支付页面
        self.login.loginFunc()  # 登录
        menu.insinglePay()  # 进入单笔支付页面
        time.sleep(2)
        menu.cBtn(menu.button_list[0])
        menu.cBtn(menu.button_list[1])  # 选择村居
        menu.cBtn(menu.button_list[4])  # 点击添加新收款方
        menu.inputValue(menu.input_list[1], menu.valueList[0])  # 输入账号
        menu.inputValue(menu.input_list[3], menu.valueList[1])  # 输入联行号
        menu.inputValue(menu.input_list[4], menu.valueList[2])  # 输入金额
        menu.inputValue(menu.input_list[5], menu.reason)  # 输入摘要
        menu.cBtn(menu.button_list[5])  # 点击开始支付
        msg18_1 = menu.isElementExist(menu.msg_list[7])
        self.assertTrue(msg18_1, '收款户名提示信息')
        if msg18_1:
            msgInfo = menu.getValue(*menu.msg_list[7])
            self.assertEqual(msgInfo, '不能为空', '提示信息正确')

    def test_singlePay_20(self):
        '''输入错误新增联行号支付验证'''
        menu = pay_Page(self.driver)  # 实例化单笔支付页面
        self.login.loginFunc()  # 登录
        menu.insinglePay()  # 进入单笔支付页面
        time.sleep(2)
        menu.cBtn(menu.button_list[0])
        menu.cBtn(menu.button_list[1])  # 选择村居
        menu.cBtn(menu.button_list[4])  # 点击添加新收款方
        menu.inputValue(menu.input_list[1], menu.valueList[0])  # 输入新增账号
        menu.inputValue(menu.input_list[2], menu.reason)  # 输入户名
        menu.inputValue(menu.input_list[3], menu.reason)  # 输入错误联行号
        menu.inputValue(menu.input_list[4], menu.valueList[2])  # 输入金额
        menu.inputValue(menu.input_list[5], menu.reason)  # 输入摘要
        menu.cBtn(menu.button_list[5])  # 点击开始支付
        msg20_1 = menu.isElementExist(menu.msg_list[21])
        self.assertTrue(msg20_1, '联行号错误信息')
        if msg20_1:
            msgInfo = menu.getValue(*menu.msg_list[21])
            self.assertEqual(msgInfo, '请输入有效的数字', '提示信息正确')

if __name__ == '__main__':
    pass