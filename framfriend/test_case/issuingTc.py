'''
Code description：批量代付模块 testcase
Create time：
Developer：
'''
import os
import time

from selenium.webdriver.support.select import Select

from framfriend.test_case.models.myunittest import MyunitTest
from framfriend.test_case.page_obj.issuing_page import Issuing_Page

class Issuing_Tc(MyunitTest):
    '''母子代付模块用例'''
    def test_singlePay_1(self):
        '''正确条件己方户名查询'''
        menu = Issuing_Page(self.driver)  # 实例化母子代付页面
        self.login.loginFunc()  # 登录
        menu.inissuing() # 进入母子代付页面
        time.sleep(3)
        menu.cBtn(menu.button_list[0])
        menu.cBtn(menu.button_list[1])#输入查询条件
        menu.cBtn(menu.button_list[2])#点击查询按钮
        Text = menu.getValue(*menu.msg_list[1])
        self.assertIn('沂南县蒲汪镇经管统计站', Text, '提示信息正确')

    def test_singlePay_2(self):
        '''错误条件收款人查询'''
        menu = Issuing_Page(self.driver)  # 实例化批量代付页面
        self.login.loginFunc()  # 登录
        menu.inissuing() # 进入批量代付页面
        time.sleep(3)
        menu.inputValue(menu.input_list[0],menu.valueList[1])#输入查询条件
        menu.cBtn(menu.button_list[2])#点击查询按钮
        time.sleep(2)
        Text = menu.getValue(*menu.msg_list[7])
        self.assertIn('显示第 1 到第 0 条记录，总共 0 条记录', Text, '提示信息正确')

    def test_singlePay_3(self):
        '''正确条件收款人查询'''
        menu = Issuing_Page(self.driver)  # 实例化批量代付页面
        self.login.loginFunc()  # 登录
        menu.inissuing() # 进入批量代付页面
        menu.inputValue(menu.input_list[0], menu.valueList[3])  # 输入查询条件
        menu.cBtn(menu.button_list[2])  # 点击查询按钮
        time.sleep(2)
        Text = menu.getValue(*menu.msg_list[1])
        self.assertIn('黄岛一', Text, '提示信息正确')

    def test_singlePay_4(self):
        '''错误收款账号查询'''
        menu = Issuing_Page(self.driver)  # 实例化批量代付页面
        self.login.loginFunc()  # 登录
        menu.inissuing()  # 进入批量代付页面
        menu.inputValue(menu.input_list[1], menu.valueList[3])  # 输入查询条件
        menu.cBtn(menu.button_list[2])  # 点击查询按钮
        time.sleep(2)
        Text = menu.getValue(*menu.msg_list[7])
        self.assertIn('显示第 1 到第 0 条记录，总共 0 条记录', Text, '提示信息正确')

    def test_singlePay_5(self):
        '''正确收款账号查询'''
        menu = Issuing_Page(self.driver)  # 实例化批量代付页面
        self.login.loginFunc()  # 登录
        menu.inissuing()  # 进入批量代付页面
        time.sleep(3)
        menu.cBtn(menu.button_list[2])#点击批量代付
        menu.inputValue(menu.input_list[1], menu.valueList[4])  # 输入查询条件
        menu.cBtn(menu.button_list[2])  # 点击查询按钮
        time.sleep(2)
        Text = menu.getValue(*menu.msg_list[1])
        self.assertIn('6215210200005034', Text, '提示信息正确')

    def test_singlePay_6(self):
        '''错误摘要查询'''
        menu = Issuing_Page(self.driver)  # 实例化批量代付页面
        self.login.loginFunc()  # 登录
        menu.inissuing()  # 进入批量代付页面
        time.sleep(3)
        menu.cBtn(menu.button_list[2])#点击批量代付
        menu.inputValue(menu.input_list[2], menu.valueList[3])  # 输入查询条件
        menu.cBtn(menu.button_list[2])  # 点击查询按钮
        time.sleep(2)
        Text = menu.getValue(*menu.msg_list[7])
        self.assertIn('显示第 1 到第 0 条记录，总共 0 条记录', Text, '提示信息正确')

    def test_singlePay_7(self):
        '''正确摘要查询'''
        menu = Issuing_Page(self.driver)  # 实例化批量代付页面
        self.login.loginFunc()  # 登录
        menu.inissuing()  # 进入批量代付页面
        time.sleep(3)
        menu.cBtn(menu.button_list[2])#点击批量代付
        menu.inputValue(menu.input_list[2], menu.valueList[0])  # 输入查询条件
        menu.cBtn(menu.button_list[2])  # 点击查询按钮
        time.sleep(2)
        Text = menu.getValue(*menu.msg_list[1])
        self.assertIn('测试', Text, '提示信息正确')

    def test_singlePay_8(self):
        '''点击新增验证'''
        menu = Issuing_Page(self.driver)  # 实例化批量代付页面
        self.login.loginFunc()  # 登录
        menu.inissuing()  # 进入批量代付页面
        time.sleep(3)
        menu.cBtn(menu.button_list[2])#点击批量代付
        menu.cBtn(menu.button_list[3])#点击新增
        msg8_1 = menu.isElementExist(menu.msg_list[2])
        self.assertTrue(msg8_1, '弹出新增窗口')

    def test_singlePay_9(self):
        '''为空新增校验'''
        menu = Issuing_Page(self.driver)  # 实例化批量代付页面
        self.login.loginFunc()  # 登录
        menu.inissuing()  # 进入批量代付页面
        time.sleep(3)
        menu.cBtn(menu.button_list[2])#点击批量代付
        menu.cBtn(menu.button_list[3])#点击新增按钮
        menu.cBtn(menu.button_list[10])#点击提交
        msg9_1 = menu.getValue(*menu.msg_list[8])
        self.assertIn(menu.valueList[7], msg9_1, '提示信息正确')
        msg9_2 = menu.getValue(*menu.msg_list[9])
        self.assertIn(menu.valueList[7], msg9_2, '提示信息正确')
        msg9_3 = menu.getValue(*menu.msg_list[10])
        self.assertIn(menu.valueList[8], msg9_3, '提示信息正确')
        msg9_4 = menu.getValue(*menu.msg_list[11])
        self.assertIn(menu.valueList[7], msg9_4, '提示信息正确')

    def test_singlePay_10(self):
        '''不选择银行新增'''
        menu = Issuing_Page(self.driver)  # 实例化批量代付页面
        self.login.loginFunc()  # 登录
        menu.inissuing()  # 进入批量代付页面
        time.sleep(3)
        menu.cBtn(menu.button_list[2])  # 点击批量代付
        menu.cBtn(menu.button_list[3])#点击新增按钮
        '''输入其他项'''
        time.sleep(1)
        menu.inputValue(menu.input_list[3],menu.valueList[3])
        menu.inputValue(menu.input_list[4], menu.valueList[4])
        menu.inputValue(menu.input_list[5], menu.valueList[5])
        menu.inputValue(menu.input_list[6],menu.valueList[0])
        card = self.driver.find_element_by_xpath('//*[@id="defaultForm"]/div[7]/div/select')
        Select(card).select_by_value('C')  # 获取下拉选
        menu.cBtn(menu.button_list[10])#提交
        time.sleep(1)
        msg10_1 = menu.getValue(*menu.msg_list[8])
        self.assertIn(menu.valueList[7], msg10_1, '提示信息正确')

    def test_singlePay_11(self):
        '''不输入收款人新增'''
        menu = Issuing_Page(self.driver)  # 实例化批量代付页面
        self.login.loginFunc()  # 登录
        menu.inissuing()  # 进入批量代付页面
        time.sleep(3)
        menu.cBtn(menu.button_list[2])  # 点击批量代付
        menu.cBtn(menu.button_list[3])  # 点击新增按钮
        '''输入其他项'''
        time.sleep(1)
        menu.cBtn(menu.button_list[9])
        menu.cBtn(menu.button_list[21])
        #menu.inputValue(menu.input_list[3], menu.valueList[3])
        menu.inputValue(menu.input_list[4], menu.valueList[4])
        menu.inputValue(menu.input_list[5], menu.valueList[5])
        menu.inputValue(menu.input_list[6], menu.valueList[0])
        card = self.driver.find_element_by_xpath('//*[@id="defaultForm"]/div[7]/div/select')
        Select(card).select_by_value('C')  # 获取下拉选
        menu.cBtn(menu.button_list[10])  # 提交
        time.sleep(1)
        msg11_1 = menu.getValue(*menu.msg_list[9])
        self.assertIn(menu.valueList[7], msg11_1, '提示信息正确')

    def test_singlePay_12(self):
        '''不输入金额新增'''
        menu = Issuing_Page(self.driver)  # 实例化批量代付页面
        self.login.loginFunc()  # 登录
        menu.inissuing()  # 进入批量代付页面
        time.sleep(3)
        menu.cBtn(menu.button_list[2])  # 点击批量代付
        menu.cBtn(menu.button_list[3])  # 点击新增按钮
        '''输入其他项'''
        time.sleep(1)
        menu.cBtn(menu.button_list[9])
        menu.cBtn(menu.button_list[21])
        menu.inputValue(menu.input_list[3], menu.valueList[3])
        menu.inputValue(menu.input_list[4], menu.valueList[4])
        #menu.inputValue(menu.input_list[5], menu.valueList[5])
        menu.inputValue(menu.input_list[6], menu.valueList[0])
        card = self.driver.find_element_by_xpath('//*[@id="defaultForm"]/div[7]/div/select')
        Select(card).select_by_value('C')  # 获取下拉选
        menu.cBtn(menu.button_list[10])  # 提交
        time.sleep(1)
        msg12_1 = menu.getValue(*menu.msg_list[10])
        self.assertIn(menu.valueList[8], msg12_1, '提示信息正确')

    def test_singlePay_13(self):
        '''不输入摘要新增'''
        menu = Issuing_Page(self.driver)  # 实例化批量代付页面
        self.login.loginFunc()  # 登录
        menu.inissuing()  # 进入批量代付页面
        time.sleep(3)
        menu.cBtn(menu.button_list[2])  # 点击批量代付
        menu.cBtn(menu.button_list[3])  # 点击新增按钮
        '''输入其他项'''
        time.sleep(1)
        menu.cBtn(menu.button_list[9])
        menu.cBtn(menu.button_list[21])
        menu.inputValue(menu.input_list[3], menu.valueList[3])
        menu.inputValue(menu.input_list[4], menu.valueList[4])
        menu.inputValue(menu.input_list[5], menu.valueList[5])
        #menu.inputValue(menu.input_list[6], menu.valueList[0])
        card = self.driver.find_element_by_xpath('//*[@id="defaultForm"]/div[7]/div/select')
        Select(card).select_by_value('C')  # 获取下拉选
        menu.cBtn(menu.button_list[10])  # 提交
        time.sleep(1)
        msg13_1 = menu.getValue(*menu.msg_list[11])
        self.assertIn(menu.valueList[7], msg13_1, '提示信息正确')

    def test_singlePay_14(self):
        '''输入不规则账号新增'''
        menu = Issuing_Page(self.driver)  # 实例化批量代付页面
        self.login.loginFunc()  # 登录
        menu.inissuing()  # 进入批量代付页面
        time.sleep(3)
        menu.cBtn(menu.button_list[2])  # 点击批量代付
        menu.cBtn(menu.button_list[3])  # 点击新增按钮
        '''输入其他项'''
        time.sleep(1)
        menu.cBtn(menu.button_list[9])
        menu.cBtn(menu.button_list[21])
        menu.inputValue(menu.input_list[3], menu.valueList[3])
        menu.inputValue(menu.input_list[4], menu.valueList[3])
        menu.inputValue(menu.input_list[5], menu.valueList[5])
        menu.inputValue(menu.input_list[6], menu.valueList[0])
        card = self.driver.find_element_by_xpath('//*[@id="defaultForm"]/div[7]/div/select')
        Select(card).select_by_value('C')  # 获取下拉选
        menu.cBtn(menu.button_list[10])  # 提交
        time.sleep(1)
        msg14_1 = menu.getValue(*menu.msg_list[15])
        self.assertIn(menu.valueList[8], msg14_1, '提示信息正确')

    def test_singlePay_15(self):
        '''输入不规则金额新增'''
        menu = Issuing_Page(self.driver)  # 实例化批量代付页面
        self.login.loginFunc()  # 登录
        menu.inissuing()  # 进入批量代付页面
        time.sleep(3)
        menu.cBtn(menu.button_list[2])  # 点击批量代付
        menu.cBtn(menu.button_list[3])  # 点击新增按钮
        '''输入其他项'''
        time.sleep(1)
        menu.cBtn(menu.button_list[9])
        menu.cBtn(menu.button_list[21])
        menu.inputValue(menu.input_list[3], menu.valueList[3])
        menu.inputValue(menu.input_list[4], menu.valueList[4])
        menu.inputValue(menu.input_list[5], menu.valueList[3])
        menu.inputValue(menu.input_list[6], menu.valueList[0])
        card = self.driver.find_element_by_xpath('//*[@id="defaultForm"]/div[7]/div/select')
        Select(card).select_by_value('C')  # 获取下拉选
        menu.cBtn(menu.button_list[10])  # 提交
        time.sleep(1)
        msg15_1 = menu.getValue(*menu.msg_list[10])
        self.assertIn(menu.valueList[8], msg15_1, '提示信息正确')

    def test_singlePay_16(self):
        '''新增代付'''
        menu = Issuing_Page(self.driver)  # 实例化批量代付页面
        self.login.loginFunc()  # 登录
        menu.inissuing()  # 进入批量代付页面
        time.sleep(3)
        menu.cBtn(menu.button_list[2])  # 点击批量代付
        menu.cBtn(menu.button_list[3])  # 点击新增按钮
        '''输入其他项'''
        time.sleep(1)
        menu.cBtn(menu.button_list[9])
        menu.cBtn(menu.button_list[21])
        menu.inputValue(menu.input_list[3], menu.valueList[3])
        menu.inputValue(menu.input_list[4], menu.valueList[4])
        menu.inputValue(menu.input_list[5], menu.valueList[5])
        menu.inputValue(menu.input_list[6], menu.valueList[0])
        card = self.driver.find_element_by_xpath('//*[@id="defaultForm"]/div[7]/div/select')
        Select(card).select_by_value('C')  # 获取下拉选
        menu.cBtn(menu.button_list[10])  # 提交
        time.sleep(1)
        msg16_1 = menu.getValue(*menu.msg_list[0])
        self.assertIn(menu.valueList[9], msg16_1, '提示信息正确')

    def test_singlePay_17(self):
        '''取消新增代付'''
        menu = Issuing_Page(self.driver)  # 实例化批量代付页面
        self.login.loginFunc()  # 登录
        menu.inissuing()  # 进入批量代付页面
        time.sleep(3)
        menu.cBtn(menu.button_list[2])  # 点击批量代付
        menu.cBtn(menu.button_list[3])  # 点击新增按钮
        menu.cBtn(menu.button_list[11]) #取消新增
        msg17_1 = menu.isElementExist(menu.msg_list[2])
        self.assertFalse(msg17_1, '关闭新增窗口')

    def test_singlePay_18(self):
        '''点击修改'''
        menu = Issuing_Page(self.driver)  # 实例化批量代付页面
        self.login.loginFunc()  # 登录
        menu.inissuing()  # 进入批量代付页面
        time.sleep(3)
        menu.cBtn(menu.button_list[2])  # 点击批量代付
        menu.cBtn(menu.button_list[4])  # 点击修改按钮
        msg18_1 = menu.getValue(*menu.msg_list[0])
        self.assertIn(menu.valueList[10], msg18_1, '提示信息正确')

    def test_singlePay_19(self):
        '''全选点击修改'''
        menu = Issuing_Page(self.driver)  # 实例化批量代付页面
        self.login.loginFunc()  # 登录
        menu.inissuing()  # 进入批量代付页面
        time.sleep(3)
        menu.cBtn(menu.button_list[2])  # 点击批量代付
        menu.cBtn(menu.input_list[7]) #全选
        menu.cBtn(menu.button_list[4])  # 点击修改按钮
        msg19_1 = menu.getValue(*menu.msg_list[0])
        self.assertIn(menu.valueList[11], msg19_1, '提示信息正确')

    def test_singlePay_20(self):
        '''一项点击修改'''
        menu = Issuing_Page(self.driver)  # 实例化批量代付页面
        self.login.loginFunc()  # 登录
        menu.inissuing()  # 进入批量代付页面
        time.sleep(3)
        menu.cBtn(menu.button_list[2])  # 点击批量代付
        time.sleep(1)
        menu.cBtn(menu.input_list[8]) #选择一项
        menu.cBtn(menu.button_list[4])  # 点击修改按钮
        msg20_1 = menu.isElementExist(menu.msg_list[3])
        self.assertTrue(msg20_1, '弹出修改窗口')

    def test_singlePay_21(self):
        '''修改清空所有项提交'''
        menu = Issuing_Page(self.driver)  # 实例化批量代付页面
        self.login.loginFunc()  # 登录
        menu.inissuing()  # 进入批量代付页面
        time.sleep(3)
        menu.cBtn(menu.button_list[2])  # 点击批量代付
        time.sleep(1)
        menu.cBtn(menu.input_list[8]) #选择一项
        menu.cBtn(menu.button_list[4])  # 点击修改按钮
        menu.clearValue(menu.input_list[3])
        menu.clearValue(menu.input_list[4])
        menu.clearValue(menu.input_list[5])
        menu.clearValue(menu.input_list[6])
        menu.cBtn(menu.button_list[13])#提交
        time.sleep(1)
        msg21_1 = menu.getValue(*menu.msg_list[9])
        self.assertIn(menu.valueList[7], msg21_1, '提示信息正确')
        msg21_2 = menu.getValue(*menu.msg_list[12])
        self.assertIn(menu.valueList[7], msg21_2, '提示信息正确')
        msg21_3 = menu.getValue(*menu.msg_list[13])
        self.assertIn(menu.valueList[8], msg21_3, '提示信息正确')

    def test_singlePay_22(self):
        '''修改清空收款人提交'''
        menu = Issuing_Page(self.driver)  # 实例化批量代付页面
        self.login.loginFunc()  # 登录
        menu.inissuing()  # 进入批量代付页面
        time.sleep(3)
        menu.cBtn(menu.button_list[2])  # 点击批量代付
        time.sleep(1)
        menu.cBtn(menu.input_list[8]) #选择一项
        menu.cBtn(menu.button_list[4])  # 点击修改按钮
        menu.clearValue(menu.input_list[3])
        menu.cBtn(menu.button_list[13])#提交
        time.sleep(1)
        msg22_1 = menu.getValue(*menu.msg_list[9])
        self.assertIn(menu.valueList[7], msg22_1, '提示信息正确')

    def test_singlePay_23(self):
        '''修改清空账号提交'''
        menu = Issuing_Page(self.driver)  # 实例化批量代付页面
        self.login.loginFunc()  # 登录
        menu.inissuing()  # 进入批量代付页面
        time.sleep(3)
        menu.cBtn(menu.button_list[2])  # 点击批量代付
        time.sleep(1)
        menu.cBtn(menu.input_list[8]) #选择一项
        menu.cBtn(menu.button_list[4])  # 点击修改按钮
        menu.clearValue(menu.input_list[4])
        menu.cBtn(menu.button_list[13])#提交
        time.sleep(1)
        msg23_1 = menu.getValue(*menu.msg_list[12])
        self.assertIn(menu.valueList[7], msg23_1, '提示信息正确')

    def test_singlePay_24(self):
        '''修改清空金额提交'''
        menu = Issuing_Page(self.driver)  # 实例化批量代付页面
        self.login.loginFunc()  # 登录
        menu.inissuing()  # 进入批量代付页面
        time.sleep(3)
        menu.cBtn(menu.button_list[2])  # 点击批量代付
        time.sleep(1)
        menu.cBtn(menu.input_list[8]) #选择一项
        menu.cBtn(menu.button_list[4])  # 点击修改按钮
        menu.clearValue(menu.input_list[5])
        menu.cBtn(menu.button_list[13])#提交
        time.sleep(1)
        msg24_1 = menu.getValue(*menu.msg_list[13])
        self.assertIn(menu.valueList[8], msg24_1, '提示信息正确')

    def test_singlePay_25(self):
        '''修改转出银行'''
        menu = Issuing_Page(self.driver)#实例化代付页面
        self.login.loginFunc()#登录
        menu.inissuing()#进入母子代付界面
        time.sleep(2)
        menu.cBtn(menu.button_list[2])#点击母子代付
        time.sleep(1)
        menu.cBtn(menu.input_list[8])#选择一项
        menu.cBtn(menu.button_list[4])  # 点击修改按钮
        menu.cBtn(menu.button_list[9])
        menu.cBtn(menu.button_list[22])
        menu.cBtn(menu.button_list[13])#提交
        msg25_1 = menu.getValue(*menu.msg_list[16])
        self.assertIn(menu.valueList[12],msg25_1,'提示信息正确')

    def test_singlePay_26(self):
        '''修改收款人'''
        menu = Issuing_Page(self.driver)#实例化代付页面
        self.login.loginFunc()#登录
        menu.inissuing()#进入母子代付界面
        time.sleep(2)
        menu.cBtn(menu.button_list[2])#点击母子代付
        time.sleep(1)
        menu.cBtn(menu.input_list[8])#选择一项
        menu.cBtn(menu.button_list[4])  # 点击修改按钮
        menu.inputValue(menu.input_list[3],menu.valueList[0])
        menu.cBtn(menu.button_list[13])#提交
        msg26_1 = menu.getValue(*menu.msg_list[16])
        self.assertIn(menu.valueList[12],msg26_1,'提示信息正确')
        msg26_2 = menu.getValue(*menu.msg_list[1])
        self.assertIn(menu.valueList[13],msg26_2,'提示信息正确')

    def test_singlePay_27(self):
        '''修改收款账号'''
        menu = Issuing_Page(self.driver)  # 实例化代付页面
        self.login.loginFunc()  # 登录
        menu.inissuing()  # 进入母子代付界面
        time.sleep(2)
        menu.cBtn(menu.button_list[2])  # 点击母子代付
        time.sleep(1)
        menu.cBtn(menu.input_list[8])  # 选择一项
        menu.cBtn(menu.button_list[4])  # 点击修改按钮
        menu.inputValue(menu.input_list[4], menu.valueList[1])
        menu.cBtn(menu.button_list[13])  # 提交
        msg27_1 = menu.getValue(*menu.msg_list[16])
        self.assertIn(menu.valueList[12], msg27_1, '提示信息正确')
        time.sleep(1)
        msg27_2 = menu.getValue(*menu.msg_list[1])
        self.assertIn(menu.valueList[14], msg27_2, '提示信息正确')

    def test_singlePay_28(self):
        '''修改收款金额'''
        menu = Issuing_Page(self.driver)  # 实例化代付页面
        self.login.loginFunc()  # 登录
        menu.inissuing()  # 进入母子代付界面
        time.sleep(2)
        menu.cBtn(menu.button_list[2])  # 点击母子代付
        time.sleep(1)
        menu.cBtn(menu.input_list[8])  # 选择一项
        menu.cBtn(menu.button_list[4])  # 点击修改按钮
        menu.inputValue(menu.input_list[5], menu.valueList[6])
        menu.cBtn(menu.button_list[13])  # 提交
        msg28_1 = menu.getValue(*menu.msg_list[16])
        self.assertIn(menu.valueList[12], msg28_1, '提示信息正确')

    def test_singlePay_29(self):
        '''修改不规则收款账号'''
        menu = Issuing_Page(self.driver)  # 实例化代付页面
        self.login.loginFunc()  # 登录
        menu.inissuing()  # 进入母子代付界面
        time.sleep(2)
        menu.cBtn(menu.button_list[2])  # 点击母子代付
        time.sleep(1)
        menu.cBtn(menu.input_list[8])  # 选择一项
        menu.cBtn(menu.button_list[4])  # 点击修改按钮
        menu.inputValue(menu.input_list[4], menu.valueList[0])
        menu.cBtn(menu.button_list[13])  # 提交
        msg29_1 = menu.getValue(*menu.msg_list[14])
        self.assertIn(menu.valueList[8], msg29_1, '提示信息正确')

    def test_singlePay_30(self):
        '''修改不规则金额'''
        menu = Issuing_Page(self.driver)  # 实例化代付页面
        self.login.loginFunc()  # 登录
        menu.inissuing()  # 进入母子代付界面
        time.sleep(2)
        menu.cBtn(menu.button_list[2])  # 点击母子代付
        time.sleep(1)
        menu.cBtn(menu.input_list[8])  # 选择一项
        menu.cBtn(menu.button_list[4])  # 点击修改按钮
        menu.inputValue(menu.input_list[5], menu.valueList[0])
        menu.cBtn(menu.button_list[13])  # 提交
        msg30_1 = menu.getValue(*menu.msg_list[13])
        self.assertIn(menu.valueList[8], msg30_1, '提示信息正确')

    def test_singlePay_31(self):
        '''修改摘要'''
        menu = Issuing_Page(self.driver)  # 实例化代付页面
        self.login.loginFunc()  # 登录
        menu.inissuing()  # 进入母子代付界面
        time.sleep(2)
        menu.cBtn(menu.button_list[2])  # 点击母子代付
        time.sleep(1)
        menu.cBtn(menu.input_list[8])  # 选择一项
        menu.cBtn(menu.button_list[4])  # 点击修改按钮
        menu.inputValue(menu.input_list[6], menu.reason)
        menu.cBtn(menu.button_list[13])  # 提交
        msg31_1 = menu.getValue(*menu.msg_list[16])
        self.assertIn(menu.valueList[12], msg31_1, '提示信息正确')
        msg31_2 = menu.getValue(*menu.msg_list[1])
        self.assertIn(menu.valueList[15],msg31_2,'提示信息正确')

    def test_singlePay_32(self):
        '''修改折卡'''
        menu = Issuing_Page(self.driver)  # 实例化代付页面
        self.login.loginFunc()  # 登录
        menu.inissuing()  # 进入母子代付界面
        time.sleep(2)
        menu.cBtn(menu.button_list[2])  # 点击母子代付
        time.sleep(1)
        menu.cBtn(menu.input_list[8])  # 选择一项
        menu.cBtn(menu.button_list[4])  # 点击修改按钮
        card = self.driver.find_element_by_xpath('//*[@id="defaultForm"]/div[7]/div/select')
        Select(card).select_by_value('P')  # 获取下拉选
        menu.cBtn(menu.button_list[13])  # 提交
        msg32_1 = menu.getValue(*menu.msg_list[16])
        self.assertIn(menu.valueList[12], msg32_1, '提示信息正确')
        msg32_2 = menu.getValue(*menu.msg_list[1])
        self.assertIn(menu.valueList[16], msg32_2, '提示信息正确')

    def test_singlePay_33(self):
        '''取消修改'''
        menu = Issuing_Page(self.driver)  # 实例化代付页面
        self.login.loginFunc()  # 登录
        menu.inissuing()  # 进入母子代付界面
        time.sleep(2)
        menu.cBtn(menu.button_list[2])  # 点击母子代付
        time.sleep(1)
        menu.cBtn(menu.input_list[8])  # 选择一项
        menu.cBtn(menu.button_list[4])  # 点击修改按钮
        menu.cBtn(menu.button_list[14]) #点击取消
        msg33_1 = menu.isElementExist(menu.msg_list[3])
        self.assertFalse(msg33_1, '关闭修改窗口')

    def test_singlePay_34(self):
        '''点击删除'''
        menu = Issuing_Page(self.driver)  # 实例化代付页面
        self.login.loginFunc()  # 登录
        menu.inissuing()  # 进入母子代付界面
        time.sleep(2)
        menu.cBtn(menu.button_list[2])  # 点击母子代付
        time.sleep(1)
        menu.cBtn(menu.button_list[5]) #点击删除
        msg34_1 = menu.getValue(*menu.msg_list[0])
        self.assertIn(menu.valueList[10], msg34_1, '提示信息正确')

    def test_singlePay_35(self):
        '''一项点击删除'''
        menu = Issuing_Page(self.driver)  # 实例化代付页面
        self.login.loginFunc()  # 登录
        menu.inissuing()  # 进入母子代付界面
        time.sleep(2)
        menu.cBtn(menu.button_list[2])  # 点击母子代付
        time.sleep(1)
        menu.cBtn(menu.input_list[8])  # 选择一项
        menu.cBtn(menu.button_list[5]) #点击删除
        msg35_1 = menu.isElementExist(menu.msg_list[4])
        self.assertTrue(msg35_1, '弹出删除提示窗口')

    def test_singlePay_36(self):
        '''一项确定删除'''
        menu = Issuing_Page(self.driver)  # 实例化代付页面
        self.login.loginFunc()  # 登录
        menu.inissuing()  # 进入母子代付界面
        time.sleep(2)
        menu.cBtn(menu.button_list[2])  # 点击母子代付
        time.sleep(1)
        menu.cBtn(menu.input_list[8])  # 选择一项
        menu.cBtn(menu.button_list[5]) #点击删除
        menu.cBtn(menu.button_list[15])#确定删除
        msg36_1 = menu.isElementExist(menu.msg_list[17])
        self.assertTrue(msg36_1, '弹出删除成功信息')

    def test_singlePay_37(self):
        '''取消删除'''
        menu = Issuing_Page(self.driver)  # 实例化代付页面
        self.login.loginFunc()  # 登录
        menu.inissuing()  # 进入母子代付界面
        time.sleep(2)
        menu.cBtn(menu.button_list[2])  # 点击母子代付
        time.sleep(1)
        menu.cBtn(menu.input_list[8])  # 选择一项
        menu.cBtn(menu.button_list[5]) #点击删除
        menu.cBtn(menu.button_list[16])#取消删除

    def test_singlePay_38(self):
        '''导出模板'''
        menu = Issuing_Page(self.driver)  # 实例化代付页面
        self.login.loginFunc()  # 登录
        menu.inissuing()  # 进入母子代付界面
        time.sleep(2)
        menu.cBtn(menu.button_list[2])  # 点击母子代付
        time.sleep(1)
        menu.cBtn(menu.button_list[8]) #点击导出模板
        assert (os.path.exists('F:\TestDownloads\\银农直联代付模板.xlsx'))  # 检查是否已下载

    def test_singlePay_39(self):
        '''数据导入'''
        menu = Issuing_Page(self.driver)  # 实例化代付页面
        self.login.loginFunc()  # 登录
        menu.inissuing()  # 进入母子代付界面
        time.sleep(2)
        menu.cBtn(menu.button_list[2])  # 点击母子代付
        time.sleep(1)
        menu.cBtn(menu.button_list[6]) #点击数据导入
        msg39_1 = menu.isElementExist(menu.msg_list[5])
        self.assertTrue(msg39_1, '弹出数据导入窗口')

    def test_singlePay_40(self):
        '''错误文件数据导入'''
        menu = Issuing_Page(self.driver)  # 实例化代付页面
        self.login.loginFunc()  # 登录
        menu.inissuing()  # 进入母子代付界面
        time.sleep(2)
        menu.cBtn(menu.button_list[2])  # 点击母子代付
        time.sleep(1)
        menu.cBtn(menu.button_list[6])  # 点击数据导入
        menu.uploadfalse()
        menu.cBtn(menu.button_list[17])  # 点击提交
        msgInfo = menu.getValue(*menu.msg_list[17])
        self.assertIn(menu.valueList[17], msgInfo, '提示导入失败，停留在导入窗口')

    def test_singlePay_41(self):
        '''为空数据导入'''
        menu = Issuing_Page(self.driver)  # 实例化代付页面
        self.login.loginFunc()  # 登录
        menu.inissuing()  # 进入母子代付界面
        time.sleep(2)
        menu.cBtn(menu.button_list[2])  # 点击母子代付
        time.sleep(1)
        menu.cBtn(menu.button_list[6])  # 点击数据导入
        menu.cBtn(menu.button_list[17])  # 点击提交
        msgInfo = menu.getValue(*menu.msg_list[17])
        self.assertIn(menu.valueList[17], msgInfo, '提示导入失败，停留在导入窗口')

    def test_singlePay_42(self):
        '''正确数据导入'''
        menu = Issuing_Page(self.driver)  # 实例化代付页面
        self.login.loginFunc()  # 登录
        menu.inissuing()  # 进入母子代付界面
        time.sleep(2)
        menu.cBtn(menu.button_list[2])  # 点击母子代付
        time.sleep(1)
        menu.cBtn(menu.button_list[6])  # 点击数据导入
        menu.uploadtrue()
        menu.cBtn(menu.button_list[17])  # 点击提交
        time.sleep(2)
        msgInfo = menu.getValue(*menu.msg_list[0])
        self.assertIn(menu.valueList[18], msgInfo, '提示信息正确')

    def test_singlePay_43(self):
        '''点击批量代付'''
        menu = Issuing_Page(self.driver)  # 实例化代付页面
        self.login.loginFunc()  # 登录
        menu.inissuing()  # 进入母子代付界面
        time.sleep(2)
        menu.cBtn(menu.button_list[2])  # 点击母子代付
        time.sleep(1)
        menu.cBtn(menu.button_list[7])  # 点击批量代付
        msgInfo = menu.getValue(*menu.msg_list[0])
        self.assertIn(menu.valueList[10], msgInfo, '提示信息正确')

    def test_singlePay_44(self):
        '''一项点击批量代付'''
        menu = Issuing_Page(self.driver)  # 实例化代付页面
        self.login.loginFunc()  # 登录
        menu.inissuing()  # 进入母子代付界面
        time.sleep(2)
        menu.cBtn(menu.button_list[2])  # 点击母子代付
        time.sleep(1)
        menu.cBtn(menu.input_list[8])  # 选择一项
        menu.cBtn(menu.input_list[10])  # 选择二项
        menu.cBtn(menu.button_list[7])  # 点击批量代付
        msgInfo = menu.isElementExist(menu.msg_list[6])
        self.assertTrue(msgInfo, '弹出批量代付窗口')

    def test_singlePay_45(self):
        '''错误密码支付'''
        menu = Issuing_Page(self.driver)  # 实例化代付页面
        self.login.loginFunc()  # 登录
        menu.inissuing()  # 进入母子代付界面
        time.sleep(2)
        menu.cBtn(menu.button_list[2])  # 点击母子代付
        time.sleep(1)
        menu.cBtn(menu.input_list[8])  # 选择一项
        menu.cBtn(menu.input_list[10])  # 选择二项
        menu.cBtn(menu.button_list[7])  # 点击批量代付
        menu.inputValue(menu.input_list[9], menu.valueList[4])  # 输入交易密码
        menu.cBtn(menu.button_list[20])#确定支付
        time.sleep(2)
        msgInfo = menu.getValue(*menu.msg_list[16])
        self.assertIn(menu.valueList[19], msgInfo, '提示信息正确')

    def test_singlePay_46(self):
        '''正确密码支付'''
        menu = Issuing_Page(self.driver)  # 实例化代付页面
        self.login.loginFunc()  # 登录
        menu.inissuing()  # 进入母子代付界面
        time.sleep(2)
        menu.cBtn(menu.button_list[2])  # 点击母子代付
        time.sleep(1)
        menu.cBtn(menu.input_list[8])  # 选择一项
        menu.cBtn(menu.input_list[10])  # 选择二项
        menu.cBtn(menu.button_list[7])  # 点击批量代付
        menu.inputValue(menu.input_list[9], menu.valueList[2])  # 输入交易密码
        menu.cBtn(menu.button_list[20])#确定支付
        time.sleep(2)
        msgInfo = menu.getValue(*menu.msg_list[16])
        self.assertIn(menu.valueList[20], msgInfo, '提示信息正确')

    def test_singlePay_47(self):
        '''取消密码支付'''
        menu = Issuing_Page(self.driver)  # 实例化代付页面
        self.login.loginFunc()  # 登录
        menu.inissuing()  # 进入母子代付界面
        time.sleep(2)
        menu.cBtn(menu.button_list[2])  # 点击母子代付
        time.sleep(1)
        menu.cBtn(menu.input_list[8])  # 选择一项
        menu.cBtn(menu.input_list[10])  # 选择二项
        menu.cBtn(menu.button_list[7])  # 点击批量代付
        menu.cBtn(menu.button_list[19])#取消支付

if __name__ == '__main__':
        pass