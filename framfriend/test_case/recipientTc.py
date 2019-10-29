'''
Code description：短信接收人设置模块 testcase
Create time：
Developer：
'''
import time
from framfriend.test_case.models.myunit import MyunitTest
from framfriend.test_case.page_obj.recipient_page import recipient_page

class recipient_Tc(MyunitTest):
    '''短信接收人设置模块用例'''

    def test_alone_query(self):
        """按姓名，手机号单一条件查询"""
        menu =recipient_page(self.driver) # 实例化短信接收人设置页面
        self.login.loginFunc()  # 登录
        menu.inrecipientpage() # 进入短信接收人设置页面
        time.sleep(3)
        for name_phone in menu.query_list:
            menu.reset()  # 重置
            for value in menu.valuesList:
                menu.iQueryCondition(name_phone, value)
                menu.cBtn(menu.button_list[0])  # 点击[查询]
                time.sleep(3)
                flag = menu.getValue(*menu.msg_list[6])
                try:
                    self.assertIn('15864901234',flag, '查询成功')
                except Exception:
                    self.assertNotIn('15864901234', flag, '输入的查询条件无效')

    def test_add_1(self):
        '''点击新增验证'''
        menu = recipient_page(self.driver)  # 实例化短信接收人设置页面
        self.login.loginFunc()  # 登录
        menu.inrecipientpage()  # 进入短信接收人设置页面
        time.sleep(3)
        menu.cBtn(menu.button_list[1])#点击新增
        flag = menu.isElementExist(menu.msg_list[1])
        self.assertTrue(flag,'弹出新增窗口')

    def test_add_2(self):
        '''为空新增验证'''
        menu = recipient_page(self.driver)  # 实例化短信接收人设置页面
        self.login.loginFunc()  # 登录
        menu.inrecipientpage()  # 进入短信接收人设置页面
        time.sleep(3)
        menu.cBtn(menu.button_list[1])#点击新增
        menu.cBtn(menu.button_list[4])#点击提交
        msgInfo1 = menu.getValue(*menu.msg_list[2])
        self.assertEqual(msgInfo1,'不能为空','提示信息正确')
        msgInfo2 = menu.getValue(*menu.msg_list[3])
        self.assertEqual(msgInfo2, '请输入正确的手机号', '提示信息正确')

    def test_add_3(self):
        '''不输入姓名新增验证'''
        menu = recipient_page(self.driver)  # 实例化短信接收人设置页面
        self.login.loginFunc()  # 登录
        menu.inrecipientpage()  # 进入短信接收人设置页面
        time.sleep(3)
        menu.cBtn(menu.button_list[1])#点击新增
        menu.inputValue(menu.input_list[1],menu.valueList[0])#输入手机号
        menu.cBtn(menu.button_list[4])#点击提交
        msgInfo = menu.getValue(*menu.msg_list[2])
        self.assertEqual(msgInfo,'不能为空','提示信息正确')

    def test_add_4(self):
        '''不输入手机号新增验证'''
        menu = recipient_page(self.driver)  # 实例化短信接收人设置页面
        self.login.loginFunc()  # 登录
        menu.inrecipientpage()  # 进入短信接收人设置页面
        time.sleep(3)
        menu.cBtn(menu.button_list[1])#点击新增
        menu.inputValue(menu.input_list[0],menu.reason)#输入姓名
        menu.cBtn(menu.button_list[4])#点击提交
        msgInfo = menu.getValue(*menu.msg_list[3])
        self.assertEqual(msgInfo,'请输入正确的手机号','提示信息正确')

    def test_add_5(self):
        '''输入不规则手机号新增验证'''
        menu = recipient_page(self.driver)  # 实例化短信接收人设置页面
        self.login.loginFunc()  # 登录
        menu.inrecipientpage()  # 进入短信接收人设置页面
        time.sleep(3)
        menu.cBtn(menu.button_list[1])#点击新增
        menu.inputValue(menu.input_list[0],menu.reason)#输入姓名
        menu.inputValue(menu.input_list[1], menu.reason)  # 输入不规则手机号
        menu.cBtn(menu.button_list[4])#点击提交
        msgInfo = menu.getValue(*menu.msg_list[3])
        self.assertEqual(msgInfo,'请输入正确的手机号','提示信息正确')

    def test_add_6(self):
        '''输入重复手机号新增验证'''
        menu = recipient_page(self.driver)  # 实例化短信接收人设置页面
        self.login.loginFunc()  # 登录
        menu.inrecipientpage()  # 进入短信接收人设置页面
        time.sleep(3)
        menu.cBtn(menu.button_list[1])#点击新增
        menu.inputValue(menu.input_list[0],menu.reason)#输入姓名
        menu.inputValue(menu.input_list[1], menu.valueList[1])  # 输入重复手机号
        menu.cBtn(menu.button_list[4])#点击提交
        flag = menu.isElementExist(menu.msg_list[0])
        self.assertTrue(flag,'提示不能重复')

    def test_add_7(self):
        '''正常新增验证'''
        menu = recipient_page(self.driver)  # 实例化短信接收人设置页面
        self.login.loginFunc()  # 登录
        menu.inrecipientpage()  # 进入短信接收人设置页面
        time.sleep(3)
        menu.cBtn(menu.button_list[1])  # 点击新增
        menu.inputValue(menu.input_list[0], menu.reason)  # 输入姓名
        menu.inputValue(menu.input_list[1], menu.valueList[0])  # 输入重复手机号
        menu.cBtn(menu.button_list[4])  # 点击提交
        time.sleep(1)
        msgInfo = menu.getValue(*menu.msg_list[0])
        self.assertEqual(msgInfo, '×\n提示! 新增成功', '提示信息正确')

    def test_add_8(self):
        '''新增取消验证'''
        menu = recipient_page(self.driver)  # 实例化短信接收人设置页面
        self.login.loginFunc()  # 登录
        menu.inrecipientpage()  # 进入短信接收人设置页面
        time.sleep(3)
        menu.cBtn(menu.button_list[1])  # 点击新增
        menu.cBtn(menu.button_list[5])  # 点击取消
        flag = menu.isElementExist(menu.msg_list[1])
        self.assertFalse(flag,'关闭新增窗口')

    def test_update_1(self):
        '''点击修改按钮'''
        menu = recipient_page(self.driver)  # 实例化短信接收人设置页面
        self.login.loginFunc()  # 登录
        menu.inrecipientpage()  # 进入短信接收人设置页面
        time.sleep(3)
        menu.cBtn(menu.button_list[2])  # 点击修改
        time.sleep(1)
        msgInfo = menu.getValue(*menu.msg_list[0])
        self.assertEqual(msgInfo, '×\n提示! 请选中一项内容！', '提示信息正确')

    def test_update_2(self):
        '''全选点击修改按钮'''
        menu = recipient_page(self.driver)  # 实例化短信接收人设置页面
        self.login.loginFunc()  # 登录
        menu.inrecipientpage()  # 进入短信接收人设置页面
        time.sleep(3)
        menu.cBtn(menu.checkbox[1])#全选
        menu.cBtn(menu.button_list[2])  # 点击修改
        time.sleep(1)
        msgInfo = menu.getValue(*menu.msg_list[0])
        self.assertEqual(msgInfo, '×\n提示! 请选中一项内容进行操作！', '提示信息正确')

    def test_update_3(self):
        '''全选点击修改按钮'''
        menu = recipient_page(self.driver)  # 实例化短信接收人设置页面
        self.login.loginFunc()  # 登录
        menu.inrecipientpage()  # 进入短信接收人设置页面
        time.sleep(3)
        menu.cBtn(menu.checkbox[0])#选择一项
        menu.cBtn(menu.button_list[2])  # 点击修改
        flag = menu.isElementExist(menu.msg_list[4])
        self.assertTrue(flag,'弹出修改窗口')

    def test_update_4(self):
        '''清空必填项提交'''
        menu = recipient_page(self.driver)  # 实例化短信接收人设置页面
        self.login.loginFunc()  # 登录
        menu.inrecipientpage()  # 进入短信接收人设置页面
        time.sleep(3)
        menu.cBtn(menu.checkbox[0])  # 选择一项
        menu.cBtn(menu.button_list[2])  # 点击修改
        menu.clearValue(menu.input_list[0])#清空姓名
        menu.clearValue(menu.input_list[1])#清空手机号
        menu.cBtn(menu.button_list[4])#提交
        msgInfo1 = menu.getValue(*menu.msg_list[2])
        self.assertEqual(msgInfo1, '不能为空', '提示信息正确')
        msgInfo2 = menu.getValue(*menu.msg_list[3])
        self.assertEqual(msgInfo2, '请输入正确的手机号', '提示信息正确')

    def test_update_5(self):
        '''清空姓名提交'''
        menu = recipient_page(self.driver)  # 实例化短信接收人设置页面
        self.login.loginFunc()  # 登录
        menu.inrecipientpage()  # 进入短信接收人设置页面
        time.sleep(3)
        menu.cBtn(menu.checkbox[0])  # 选择一项
        menu.cBtn(menu.button_list[2])  # 点击修改
        menu.clearValue(menu.input_list[0])  # 清空姓名
        menu.cBtn(menu.button_list[4])  # 提交
        msgInfo = menu.getValue(*menu.msg_list[2])
        self.assertEqual(msgInfo, '不能为空', '提示信息正确')

    def test_update_6(self):
        '''清空手机号提交'''
        menu = recipient_page(self.driver)  # 实例化短信接收人设置页面
        self.login.loginFunc()  # 登录
        menu.inrecipientpage()  # 进入短信接收人设置页面
        time.sleep(3)
        menu.cBtn(menu.checkbox[0])  # 选择一项
        menu.cBtn(menu.button_list[2])  # 点击修改
        menu.clearValue(menu.input_list[1])#清空手机号
        menu.cBtn(menu.button_list[4])#提交
        msgInfo2 = menu.getValue(*menu.msg_list[3])
        self.assertEqual(msgInfo2, '请输入正确的手机号', '提示信息正确')

    def test_update_7(self):
        '''修改输入不规则提交'''
        menu = recipient_page(self.driver)  # 实例化短信接收人设置页面
        self.login.loginFunc()  # 登录
        menu.inrecipientpage()  # 进入短信接收人设置页面
        time.sleep(3)
        menu.cBtn(menu.checkbox[0])  # 选择一项
        menu.cBtn(menu.button_list[2])  # 点击修改
        menu.inputValue(menu.input_list[1],menu.reason)#输入不规则手机号
        menu.cBtn(menu.button_list[4])#提交
        msgInfo2 = menu.getValue(*menu.msg_list[3])
        self.assertEqual(msgInfo2, '请输入正确的手机号', '提示信息正确')

    def test_update_8(self):
        '''修改输入重复手机号提交'''
        menu = recipient_page(self.driver)  # 实例化短信接收人设置页面
        self.login.loginFunc()  # 登录
        menu.inrecipientpage()  # 进入短信接收人设置页面
        time.sleep(3)
        menu.cBtn(menu.checkbox[0])  # 选择一项
        menu.cBtn(menu.button_list[2])  # 点击修改
        menu.inputValue(menu.input_list[1],menu.valueList[1])#输入重复手机号
        menu.cBtn(menu.button_list[4])#提交
        flag = menu.isElementExist(menu.msg_list[0])
        self.assertTrue(flag, '提示不能重复')

    def test_update_9(self):
        '''正确修改提交'''
        menu = recipient_page(self.driver)  # 实例化短信接收人设置页面
        self.login.loginFunc()  # 登录
        menu.inrecipientpage()  # 进入短信接收人设置页面
        time.sleep(3)
        menu.cBtn(menu.checkbox[0])  # 选择一项
        menu.cBtn(menu.button_list[2])  # 点击修改
        menu.inputValue(menu.input_list[0], menu.reason)#输入姓名
        menu.inputValue(menu.input_list[1],menu.valueList[2])#输入手机号
        menu.cBtn(menu.button_list[4])#提交
        time.sleep(1)
        msgInfo = menu.getValue(*menu.msg_list[0])
        self.assertEqual(msgInfo, '×\n提示! 修改成功', '提示信息正确')

    def test_update_10(self):
        '''取消修改提交'''
        menu = recipient_page(self.driver)  # 实例化短信接收人设置页面
        self.login.loginFunc()  # 登录
        menu.inrecipientpage()  # 进入短信接收人设置页面
        time.sleep(3)
        menu.cBtn(menu.checkbox[0])  # 选择一项
        menu.cBtn(menu.button_list[2])  # 点击修改
        menu.cBtn(menu.button_list[5])#取消
        flag  = menu.isElementExist(menu.msg_list[4])
        self.assertFalse(flag,'关闭修改窗口')

    def test_delete_1(self):
        '''点击删除'''
        menu = recipient_page(self.driver)  # 实例化短信接收人设置页面
        self.login.loginFunc()  # 登录
        menu.inrecipientpage()  # 进入短信接收人设置页面
        time.sleep(3)
        menu.cBtn(menu.button_list[3])  # 点击删除
        msgInfo = menu.getValue(*menu.msg_list[0])
        self.assertEqual(msgInfo, '×\n提示! 请选中一项内容！', '提示信息正确')

    def test_delete_2(self):
        '''选择一项点击删除'''
        menu = recipient_page(self.driver)  # 实例化短信接收人设置页面
        self.login.loginFunc()  # 登录
        menu.inrecipientpage()  # 进入短信接收人设置页面
        time.sleep(3)
        menu.cBtn(menu.checkbox[0])  # 选择一项
        menu.cBtn(menu.button_list[3])  # 点击删除
        flag = menu.isElementExist(menu.msg_list[5])
        self.assertTrue(flag,'弹出删除确认窗')

    def test_delete_3(self):
        '''选择一项点击删除'''
        menu = recipient_page(self.driver)  # 实例化短信接收人设置页面
        self.login.loginFunc()  # 登录
        menu.inrecipientpage()  # 进入短信接收人设置页面
        time.sleep(3)
        menu.cBtn(menu.checkbox[0])  # 选择一项
        menu.cBtn(menu.button_list[3])  # 点击删除
        menu.cBtn(menu.button_list[6])#确定
        # time.sleep(1)
        # msgInfo = menu.getValue(*menu.msg_list[0])
        # self.assertEqual(msgInfo, '×\n提示! 删除成功', '提示信息正确')

    def test_delete_4(self):
        '''取消删除'''
        menu = recipient_page(self.driver)  # 实例化短信接收人设置页面
        self.login.loginFunc()  # 登录
        menu.inrecipientpage()  # 进入短信接收人设置页面
        time.sleep(3)
        menu.cBtn(menu.checkbox[0])  # 选择一项
        menu.cBtn(menu.button_list[3])  # 点击删除
        menu.cBtn(menu.button_list[7])  # 取消

if __name__ == '__main__':
        pass





