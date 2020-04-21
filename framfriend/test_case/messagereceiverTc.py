'''
Code description：预警短信接收人模块 testcase
Create time：
Developer：
'''
import time
from framfriend.test_case.models.myunit import MyunitTest
from framfriend.test_case.page_obj.messagereceiver_page import MessagerEceiver_Page

class MessagerEceiver_Tc(MyunitTest):
    '''预警短信接收人模块用例'''

    def test_alone_query_1_1(self):
        """正确姓名查询"""
        menu = MessagerEceiver_Page(self.driver)  # 实例化预警短信接收人页面
        self.login.loginFunc()  # 登录
        menu.inmessagereceiverpage()  # 进入预警短信接收人页面
        time.sleep(3)
        menu.inputValue(menu.query_list[0],menu.valuesList[0])
        menu.cBtn(menu.button_list[0])  # 点击[查询]
        time.sleep(3)
        flag = menu.getValue(*menu.msg_list[1])
        self.assertIn(menu.assertlist[2],flag, '查询成功')

    def test_alone_query_1_2(self):
        """错误姓名查询"""
        menu = MessagerEceiver_Page(self.driver)  # 实例化预警短信接收人页面
        self.login.loginFunc()  # 登录
        menu.inmessagereceiverpage()  # 进入预警短信接收人页面
        time.sleep(3)
        menu.inputValue(menu.query_list[0],menu.valuesList[1])
        menu.cBtn(menu.button_list[0])  # 点击[查询]
        time.sleep(3)
        flag = menu.getValue(*menu.msg_list[14])
        self.assertIn(menu.assertlist[0],flag, '查询成功')

    def test_alone_query_1_3(self):
        """正确备注查询"""
        menu = MessagerEceiver_Page(self.driver)  # 实例化预警短信接收人页面
        self.login.loginFunc()  # 登录
        menu.inmessagereceiverpage()  # 进入预警短信接收人页面
        time.sleep(3)
        menu.inputValue(menu.query_list[1],menu.valuesList[1])
        menu.cBtn(menu.button_list[0])  # 点击[查询]
        time.sleep(3)
        flag = menu.getValue(*menu.msg_list[1])
        self.assertIn(menu.assertlist[3],flag, '查询成功')

    def test_alone_query_1_4(self):
        """错误备注查询"""
        menu = MessagerEceiver_Page(self.driver)  # 实例化预警短信接收人页面
        self.login.loginFunc()  # 登录
        menu.inmessagereceiverpage()  # 进入预警短信接收人页面
        time.sleep(3)
        menu.inputValue(menu.query_list[1],menu.reason)
        menu.cBtn(menu.button_list[0])  # 点击[查询]
        time.sleep(3)
        flag = menu.getValue(*menu.msg_list[14])
        self.assertIn(menu.assertlist[0],flag, '查询成功')

    def test_add_receiver_1(self):
        '''点击新增接收人'''
        menu = MessagerEceiver_Page(self.driver)  # 实例化预警短信接收人页面
        self.login.loginFunc()  # 登录
        menu.inmessagereceiverpage()  # 进入预警短信接收人页面
        time.sleep(3)
        menu.cBtn(menu.button_list[1])#点击新增
        time.sleep(1)
        msg = menu.isElementExist(menu.msg_list[2])
        self.assertTrue(msg,'弹出新增接收人窗口')

    def test_add_receiver_2(self):
        '''为空新增接收人'''
        menu = MessagerEceiver_Page(self.driver)  # 实例化预警短信接收人页面
        self.login.loginFunc()  # 登录
        menu.inmessagereceiverpage()  # 进入预警短信接收人页面
        time.sleep(3)
        menu.cBtn(menu.button_list[1])#点击新增
        menu.cBtn(menu.button_list[4])#提交
        time.sleep(1)
        msgInfo = menu.getValue(*menu.msg_list[5])
        self.assertIn(menu.assertlist[4],msgInfo,'提示信息正确')

    def test_add_receiver_3(self):
        '''不输入姓名新增接收人'''
        menu = MessagerEceiver_Page(self.driver)  # 实例化预警短信接收人页面
        self.login.loginFunc()  # 登录
        menu.inmessagereceiverpage()  # 进入预警短信接收人页面
        time.sleep(3)
        menu.cBtn(menu.button_list[1])#点击新增
        menu.inputValue(menu.input_list[1],menu.valueList)
        menu.inputValue(menu.input_list[2],menu.reason)
        menu.cBtn(menu.button_list[4])  # 提交
        msgInfo= menu.getValue(*menu.msg_list[8])
        self.assertIn(menu.assertlist[5],msgInfo,'提示信息正确')

    def test_add_receiver_4(self):
        '''不输入手机号新增接收人'''
        menu = MessagerEceiver_Page(self.driver)  # 实例化预警短信接收人页面
        self.login.loginFunc()  # 登录
        menu.inmessagereceiverpage()  # 进入预警短信接收人页面
        time.sleep(3)
        menu.cBtn(menu.button_list[1])#点击新增
        menu.inputValue(menu.input_list[0],menu.reason)
        menu.inputValue(menu.input_list[2],menu.reason)
        menu.cBtn(menu.button_list[4])  # 提交
        msg = menu.isElementExist(menu.msg_list[0])
        self.assertTrue(msg)
        msgInfo = menu.getValue(*menu.msg_list[5])
        self.assertIn(menu.assertlist[4], msgInfo, '提示信息正确')

    def test_add_receiver_5(self):
        '''输入不规则手机号新增接收人'''
        menu = MessagerEceiver_Page(self.driver)  # 实例化预警短信接收人页面
        self.login.loginFunc()  # 登录
        menu.inmessagereceiverpage()  # 进入预警短信接收人页面
        time.sleep(3)
        menu.cBtn(menu.button_list[1])#点击新增
        menu.inputValue(menu.input_list[0], menu.reason)
        menu.inputValue(menu.input_list[1], menu.reason)
        menu.inputValue(menu.input_list[2], menu.reason)
        menu.cBtn(menu.button_list[4])  # 提交
        msgInfo= menu.getValue(*menu.msg_list[6])
        self.assertEqual(menu.assertlist[6],msgInfo,'提示信息正确')

    def test_add_receiver_6(self):
        '''正常新增接收人'''
        menu = MessagerEceiver_Page(self.driver)  # 实例化预警短信接收人页面
        self.login.loginFunc()  # 登录
        menu.inmessagereceiverpage()  # 进入预警短信接收人页面
        time.sleep(3)
        menu.cBtn(menu.button_list[1])  # 点击新增
        menu.inputValue(menu.input_list[0], menu.reason)
        menu.inputValue(menu.input_list[1], menu.valueList)
        menu.inputValue(menu.input_list[2], menu.reason)
        menu.cBtn(menu.button_list[4])  # 提交
        time.sleep(1)
        msgInfo = menu.getValue(*menu.msg_list[0])
        self.assertIn(menu.assertlist[7],msgInfo,'提示信息正确')

    def test_add_receiver_7(self):
        '''取消新增接收人'''
        menu = MessagerEceiver_Page(self.driver)  # 实例化预警短信接收人页面
        self.login.loginFunc()  # 登录
        menu.inmessagereceiverpage()  # 进入预警短信接收人页面
        time.sleep(3)
        menu.cBtn(menu.button_list[1])  # 点击新增
        menu.cBtn(menu.button_list[5])  # 取消
        msg = menu.isElementExist(menu.msg_list[2])
        self.assertFalse(msg,'关闭窗口')

    def test_update_receiver_1(self):
        '''点击修改接收人'''
        menu = MessagerEceiver_Page(self.driver)  # 实例化预警短信接收人页面
        self.login.loginFunc()  # 登录
        menu.inmessagereceiverpage()  # 进入预警短信接收人页面
        time.sleep(3)
        menu.cBtn(menu.button_list[2])  # 点击修改
        time.sleep(1)
        msgInfo = menu.getValue(*menu.msg_list[0])
        self.assertIn(menu.assertlist[8],msgInfo,'提示信息正确')

    def test_update_receiver_2(self):
        '''全选点击修改接收人'''
        menu = MessagerEceiver_Page(self.driver)  # 实例化预警短信接收人页面
        self.login.loginFunc()  # 登录
        menu.inmessagereceiverpage()  # 进入预警短信接收人页面
        time.sleep(3)
        menu.cBtn(menu.checkbox[0])#全选
        menu.cBtn(menu.button_list[2])  # 点击修改
        time.sleep(1)
        msgInfo = menu.getValue(*menu.msg_list[0])
        self.assertIn(menu.assertlist[9],msgInfo,'提示信息正确')

    def test_update_receiver_3(self):
        '''选择一项点击修改接收人'''
        menu = MessagerEceiver_Page(self.driver)  # 实例化预警短信接收人页面
        self.login.loginFunc()  # 登录
        menu.inmessagereceiverpage()  # 进入预警短信接收人页面
        time.sleep(3)
        menu.cBtn(menu.checkbox[1])#选择一项
        menu.cBtn(menu.button_list[2])  # 点击修改
        time.sleep(1)
        msg = menu.isElementExist(menu.msg_list[3])
        self.assertTrue(msg,'弹出修改窗口')

    def test_update_receiver_4(self):
        '''为空修改接收人'''
        menu = MessagerEceiver_Page(self.driver)  # 实例化预警短信接收人页面
        self.login.loginFunc()  # 登录
        menu.inmessagereceiverpage()  # 进入预警短信接收人页面
        time.sleep(3)
        menu.cBtn(menu.checkbox[1])  # 选择一项
        menu.cBtn(menu.button_list[2])  # 点击修改
        '''清空必填项'''
        menu.keydelete()
        menu.cBtn(menu.button_list[6])#提交
        time.sleep(1)
        msgInfo1 = menu.getValue(*menu.msg_list[9])
        self.assertEqual(msgInfo1,'不能为空','提示信息正确')
        msgInfo2 = menu.getValue(*menu.msg_list[10])
        self.assertEqual(msgInfo2, '不能为空', '提示信息正确')
        msgInfo3 = menu.getValue(*menu.msg_list[12])
        self.assertEqual(msgInfo3, '不能为空', '提示信息正确')

    def test_update_receiver_5(self):
        '''不输入姓名修改接收人'''
        menu = MessagerEceiver_Page(self.driver)  # 实例化预警短信接收人页面
        self.login.loginFunc()  # 登录
        menu.inmessagereceiverpage()  # 进入预警短信接收人页面
        time.sleep(3)
        menu.cBtn(menu.checkbox[1])  # 选择一项
        menu.cBtn(menu.button_list[2])  # 点击修改
        menu.keydelete()
        menu.inputValue(menu.input_list[4],menu.valueList)#手机号
        menu.inputValue(menu.input_list[5],menu.reason)#备注
        menu.cBtn(menu.button_list[6])#提交
        time.sleep(1)
        msgInfo = menu.getValue(*menu.msg_list[9])
        self.assertEqual(msgInfo,menu.assertlist[5],'提示信息正确')

    def test_update_receiver_6(self):
        '''不输入手机号修改接收人'''
        menu = MessagerEceiver_Page(self.driver)  # 实例化预警短信接收人页面
        self.login.loginFunc()  # 登录
        menu.inmessagereceiverpage()  # 进入预警短信接收人页面
        time.sleep(3)
        menu.cBtn(menu.checkbox[1])  # 选择一项
        menu.cBtn(menu.button_list[2])  # 点击修改
        menu.keydelete()
        menu.inputValue(menu.input_list[3],menu.reason)#姓名
        menu.inputValue(menu.input_list[5],menu.reason)#备注
        menu.cBtn(menu.button_list[6])#提交
        time.sleep(1)
        msgInfo = menu.getValue(*menu.msg_list[10])
        self.assertEqual(msgInfo,menu.assertlist[5],'提示信息正确')

    def test_update_receiver_7(self):
        '''不输入备注修改接收人'''
        menu = MessagerEceiver_Page(self.driver)  # 实例化预警短信接收人页面
        self.login.loginFunc()  # 登录
        menu.inmessagereceiverpage()  # 进入预警短信接收人页面
        time.sleep(3)
        menu.cBtn(menu.checkbox[1])  # 选择一项
        menu.cBtn(menu.button_list[2])  # 点击修改
        menu.keydelete()
        menu.inputValue(menu.input_list[3],menu.reason)#姓名
        menu.inputValue(menu.input_list[4],menu.valueList)#手机号
        menu.cBtn(menu.button_list[6])#提交
        time.sleep(1)
        msgInfo = menu.getValue(*menu.msg_list[12])
        self.assertEqual(msgInfo,menu.assertlist[5],'提示信息正确')

    def test_update_receiver_8(self):
        '''输入不规则手机号修改接收人'''
        menu = MessagerEceiver_Page(self.driver)  # 实例化预警短信接收人页面
        self.login.loginFunc()  # 登录
        menu.inmessagereceiverpage()  # 进入预警短信接收人页面
        time.sleep(3)
        menu.cBtn(menu.checkbox[1])  # 选择一项
        menu.cBtn(menu.button_list[2])  # 点击修改
        menu.keydelete()
        menu.inputValue(menu.input_list[3],menu.reason)#姓名
        menu.inputValue(menu.input_list[4],menu.reason)#手机号
        menu.inputValue(menu.input_list[5], menu.reason) # 备注
        menu.cBtn(menu.button_list[6])#提交
        time.sleep(1)
        msgInfo = menu.getValue(*menu.msg_list[11])
        self.assertEqual(msgInfo,menu.assertlist[6],'提示信息正确')

    def test_update_receiver_9(self):
        '''正常修改接收人'''
        menu = MessagerEceiver_Page(self.driver)  # 实例化预警短信接收人页面
        self.login.loginFunc()  # 登录
        menu.inmessagereceiverpage()  # 进入预警短信接收人页面
        time.sleep(3)
        menu.cBtn(menu.checkbox[1])  # 选择一项
        menu.cBtn(menu.button_list[2])  # 点击修改
        menu.keydelete()
        menu.inputValue(menu.input_list[3],menu.reason)#姓名
        menu.inputValue(menu.input_list[4],menu.valueList)#手机号
        menu.inputValue(menu.input_list[5], menu.reason) # 备注
        menu.cBtn(menu.button_list[6])#提交
        time.sleep(1)
        msgInfo = menu.getValue(*menu.msg_list[0])
        self.assertIn(menu.assertlist[10],msgInfo,'提示信息正确')

    def test_update_receiver_10(self):
        '''关闭修改接收人'''
        menu = MessagerEceiver_Page(self.driver)  # 实例化预警短信接收人页面
        self.login.loginFunc()  # 登录
        menu.inmessagereceiverpage()  # 进入预警短信接收人页面
        time.sleep(3)
        menu.cBtn(menu.checkbox[1])  # 选择一项
        menu.cBtn(menu.button_list[2])  # 点击修改
        menu.cBtn(menu.button_list[7])#取消
        msg = menu.isElementExist(menu.msg_list[3])
        self.assertFalse(msg,'关闭修改窗口')

    def test_delete_receiver_1(self):
        '''点击删除接收人'''
        menu = MessagerEceiver_Page(self.driver)  # 实例化预警短信接收人页面
        self.login.loginFunc()  # 登录
        menu.inmessagereceiverpage()  # 进入预警短信接收人页面
        time.sleep(3)
        menu.cBtn(menu.button_list[3])  # 删除
        time.sleep(1)
        msgInfo = menu.getValue(*menu.msg_list[0])
        self.assertIn(menu.assertlist[8],msgInfo,'提示信息正确')

    def test_delete_receiver_2(self):
        '''删除接收人'''
        menu = MessagerEceiver_Page(self.driver)  # 实例化预警短信接收人页面
        self.login.loginFunc()  # 登录
        menu.inmessagereceiverpage()  # 进入预警短信接收人页面
        time.sleep(3)
        menu.cBtn(menu.checkbox[1])
        menu.cBtn(menu.button_list[3])  # 删除
        time.sleep(1)
        msg = menu.isElementExist(menu.msg_list[4])
        self.assertTrue(msg, '弹出删除窗口')

    def test_delete_receiver_3(self):
        '''确定删除接收人'''
        menu = MessagerEceiver_Page(self.driver)  # 实例化预警短信接收人页面
        self.login.loginFunc()  # 登录
        menu.inmessagereceiverpage()  # 进入预警短信接收人页面
        time.sleep(3)
        menu.cBtn(menu.checkbox[1])
        menu.cBtn(menu.button_list[3])  # 删除
        menu.cBtn(menu.button_list[8]) #确定
        time.sleep(1)
        msgInfo = menu.getValue(*menu.msg_list[13])
        self.assertIn(menu.assertlist[11],msgInfo, '提示信息正确')

    def test_delete_receiver_4(self):
        '''取消删除接收人'''
        menu = MessagerEceiver_Page(self.driver)  # 实例化预警短信接收人页面
        self.login.loginFunc()  # 登录
        menu.inmessagereceiverpage()  # 进入预警短信接收人页面
        time.sleep(3)
        menu.cBtn(menu.checkbox[1])
        menu.cBtn(menu.button_list[3])  # 删除
        menu.cBtn(menu.button_list[9]) #取消
        time.sleep(1)
        # msg = menu.isElementExist(menu.msg_list[4])
        # self.assertFalse(msg,'关闭删除窗口')

if __name__=='__main__':
    pass

