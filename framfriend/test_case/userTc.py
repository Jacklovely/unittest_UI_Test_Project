'''
Code description：用户管理模块 testcase
Create time：
Developer：
'''

import time

from selenium.webdriver.support.select import Select
from framfriend.test_case.models.myunit import MyunitTest
from framfriend.test_case.page_obj.user_page import UserPage

class User_TC(MyunitTest):
    """用户模块测试用例"""

    def test_alone_query_1(self):
        """按昵称,手机号码，登录账号单一条件查询"""
        menu = UserPage(self.driver)  # 实例化用户管理页面
        self.login.loginFunc()  # 登录
        menu.inUserPage()  # 进入用户管理页面
        time.sleep(3)
        for name_phone_login in menu.query_list:
            menu.reset()  # 重置
            for value in menu.valuesList:
                menu.iQueryCondition(name_phone_login, value)
                menu.cBtn(menu.button_list[0])  # 点击[查询]
                time.sleep(3)
                flag = menu.getValue(*menu.querymsg[1])
                try:
                    self.assertEqual('显示第 1 到第 1 条记录，总共 1 条记录', flag, '查询成功')
                except Exception:
                    self.assertEqual('显示第 1 到第 0 条记录，总共 0 条记录', flag, '查询不到')

    def test_alone_query_2(self):
        """按角色类型单一查询"""
        menu = UserPage(self.driver) # 实例化用户管理页面
        self.login.loginFunc() # 登录
        menu.inUserPage()  # 进入用户管理页面
        time.sleep(3)
        role = self.driver.find_element_by_id('role_id')
        Select(role).select_by_value('0fea1af336204e7d8dd2d63768751253')#获取下拉选
        menu.cBtn(menu.button_list[0])  # 点击[查询]
        time.sleep(1)
        flag = menu.isElementExist(menu.querymsg[0])# 判断查询成功
        self.assertTrue(flag, '验证信息')
        if flag:
            msgInfo = menu.getValue(*menu.querymsg[0])
            self.assertEqual(msgInfo, '代理中心负责人', '提示信息正确')

    def testadduser_1(self):
        '''为空新增用户:'''
        menu = UserPage(self.driver) # 实例化用户管理页面
        self.login.loginFunc() # 登录
        menu.inUserPage()  # 进入用户管理页面
        time.sleep(3)
        menu.cBtn(menu.button_list[1])
        menu.cBtn(menu.button_list[8])
        msg1 = menu.isElementExist(menu.addinput[7])
        self.assertTrue(msg1,'出现提示信息')
        if msg1:
            msgInfo1 = menu.getValue(*menu.addinput[7])
            self.assertEqual(msgInfo1, '不能为空', '提示信息正确')
        msg2 = menu.isElementExist(menu.addinput[8])
        self.assertTrue(msg2,'出现提示信息')
        if msg2:
            msgInfo2 = menu.getValue(*menu.addinput[8])
            self.assertEqual(msgInfo2, '不能为空', '提示信息正确')
        msg3 = menu.isElementExist(menu.addinput[9])
        self.assertTrue(msg3, '出现提示信息')
        if msg3:
            msgInfo3 = menu.getValue(*menu.addinput[9])
            self.assertEqual(msgInfo3, '不能为空', '提示信息正确')
        msg4 = menu.isElementExist(menu.addinput[10])
        self.assertTrue(msg4, '出现提示信息')
        if msg4:
            msgInfo4 = menu.getValue(*menu.addinput[10])
            self.assertEqual(msgInfo4, '不能为空', '提示信息正确')
        msg5 = menu.isElementExist(menu.addinput[11])
        self.assertTrue(msg5, '不能为空')
        if msg5:
            msgInfo5 = menu.getValue(*menu.addinput[11])
            self.assertEqual(msgInfo5, '不能为空', '提示信息正确')

    def testadduser_2(self):
        ''' 用户名为空新增'''
        menu = UserPage(self.driver)#实例化用户管理页面
        self.login.loginFunc()#登录
        menu.inUserPage()#进入用户管理页面
        time.sleep(3)
        menu.cBtn(menu.button_list[1])
        '''输入其他必填项'''
        menu.inputValue(menu.addinput[1], menu.valueList[1])
        menu.inputValue(menu.addinput[2], menu.valueList[2])
        menu.inputValue(menu.addinput[3], menu.valueList[3])
        menu.inputValue(menu.addinput[4], menu.valueList[4])
        menu.cBtn(menu.button_list[8])
        time.sleep(1)
        msg1 = menu.isElementExist(menu.addinput[7])
        self.assertTrue(msg1,'出现提示信息')#验证
        if msg1:
            msgInfo = menu.getValue(*menu.addinput[7])
            self.assertEqual(msgInfo, '不能为空', '提示信息正确')

    def testadduser_3(self):
        ''' 昵称为空新增'''
        menu = UserPage(self.driver)  # 实例化用户管理页面
        self.login.loginFunc()  # 登录
        menu.inUserPage()  # 进入用户管理页面
        time.sleep(3)
        menu.cBtn(menu.button_list[1])
        menu.inputValue(menu.addinput[0], menu.valueList[0])
        menu.inputValue(menu.addinput[2], menu.valueList[2])
        menu.inputValue(menu.addinput[3], menu.valueList[3])
        menu.inputValue(menu.addinput[4], menu.valueList[4])
        menu.cBtn(menu.button_list[8])
        time.sleep(1)
        msg2 = menu.isElementExist(menu.addinput[8])
        self.assertTrue(msg2, '出现提示信息')#验证
        if msg2:
            msgInfo = menu.getValue(*menu.addinput[8])
            self.assertEqual(msgInfo, '不能为空', '提示信息正确')

    def testadduser_4(self):
        ''' 登录账号为空新增'''
        menu = UserPage(self.driver)  # 实例化用户管理页面
        self.login.loginFunc()  # 登录
        menu.inUserPage()  # 进入用户管理页面
        time.sleep(3)
        menu.cBtn(menu.button_list[1])
        menu.inputValue(menu.addinput[0], menu.valueList[0])
        menu.inputValue(menu.addinput[1], menu.valueList[1])
        menu.inputValue(menu.addinput[3], menu.valueList[3])
        menu.inputValue(menu.addinput[4], menu.valueList[4])
        menu.cBtn(menu.button_list[8])
        time.sleep(1)
        msg3 = menu.isElementExist(menu.addinput[9])
        self.assertTrue(msg3, '出现提示信息')#验证
        if msg3:
            msgInfo = menu.getValue(*menu.addinput[9])
            self.assertEqual(msgInfo, '不能为空', '提示信息正确')

    def testadduser_5(self):
        ''' 密码为空新增'''
        menu = UserPage(self.driver)  # 实例化用户管理页面
        self.login.loginFunc()  # 登录
        menu.inUserPage()  # 进入用户管理页面
        time.sleep(3)
        menu.cBtn(menu.button_list[1])
        menu.inputValue(menu.addinput[0], menu.valueList[0])
        menu.inputValue(menu.addinput[1], menu.valueList[1])
        menu.inputValue(menu.addinput[2], menu.valueList[2])
        menu.inputValue(menu.addinput[4], menu.valueList[4])
        menu.cBtn(menu.button_list[8])
        time.sleep(1)
        msg4 = menu.isElementExist(menu.addinput[10])
        self.assertTrue(msg4, '出现提示信息')#验证
        if msg4:
            msgInfo = menu.getValue(*menu.addinput[10])
            self.assertEqual(msgInfo, '不能为空', '提示信息正确')

    def testadduser_6(self):
        ''' 手机号为空新增'''
        menu = UserPage(self.driver)  # 实例化用户管理页面
        self.login.loginFunc()  # 登录
        menu.inUserPage()  # 进入用户管理页面
        time.sleep(3)
        menu.cBtn(menu.button_list[1])
        menu.inputValue(menu.addinput[0], menu.valueList[0])
        menu.inputValue(menu.addinput[1], menu.valueList[1])
        menu.inputValue(menu.addinput[2], menu.valueList[2])
        menu.inputValue(menu.addinput[3], menu.valueList[3])
        menu.cBtn(menu.button_list[8])
        time.sleep(1)
        msg5 = menu.isElementExist(menu.addinput[11])
        self.assertTrue(msg5, '出现提示信息')#验证
        if msg5:
            msgInfo = menu.getValue(*menu.addinput[11])
            self.assertEqual(msgInfo, '不能为空', '提示信息正确')

    def testadduser_7(self):
        ''' 手机号格式不正确新增'''
        menu = UserPage(self.driver)  # 实例化用户管理页面
        self.login.loginFunc()  # 登录
        menu.inUserPage()  # 进入用户管理页面
        time.sleep(3)
        menu.cBtn(menu.button_list[1])
        menu.inputValue(menu.addinput[0], menu.valueList[0])
        menu.inputValue(menu.addinput[1], menu.valueList[1])
        menu.inputValue(menu.addinput[2], menu.valueList[2])
        menu.inputValue(menu.addinput[3], menu.valueList[3])
        menu.inputValue(menu.addinput[4], menu.valueList[5])
        menu.cBtn(menu.button_list[8])
        time.sleep(1)
        msg6 = menu.isElementExist(menu.addinput[12])
        self.assertTrue(msg6, '出现提示信息')#验证
        if msg6:
            msgInfo = menu.getValue(*menu.addinput[12])
            self.assertEqual(msgInfo, '请输入正确的手机号', '提示信息正确')

    def testadduser_8(self):
        ''' 正确输入新增成功'''
        menu = UserPage(self.driver)  # 实例化用户管理页面
        self.login.loginFunc()  # 登录
        menu.inUserPage()  # 进入用户管理页面
        time.sleep(3)
        menu.cBtn(menu.button_list[1])
        menu.inputValue(menu.addinput[0], menu.valueList[0])
        menu.inputValue(menu.addinput[1], menu.valueList[1])
        menu.inputValue(menu.addinput[2], menu.valueList[2])
        menu.inputValue(menu.addinput[3], menu.valueList[3])
        menu.inputValue(menu.addinput[4], menu.valueList[4])
        menu.cBtn(menu.button_list[8])
        time.sleep(1)
        msg7 = menu.isElementExist(menu.addinput[13])
        self.assertTrue(msg7, '弹出提示信息')#验证
        if msg7:
            msgInfo = menu.getValue(*menu.addinput[13])
            self.assertEqual(msgInfo, '×\n提示! 新增成功！', '提示信息正确')

    def testadduser_9(self):
        ''' 验证选择所属机构'''
        menu = UserPage(self.driver)  # 实例化用户管理页面
        self.login.loginFunc()  # 登录
        menu.inUserPage()  # 进入用户管理页面
        time.sleep(3)
        menu.cBtn(menu.button_list[1])
        menu.cBtn(menu.addinput[5])
        menu.cBtn(menu.addinput[6])#选择机构
        time.sleep(1)
        menu.cBtn(menu.addinput[14])#提交
        time.sleep(2)
        # msg8 = menu.isElementExist(menu.addinput[5])
        # self.assertTrue(msg8, '验证信息')  # 验证

    def testadduser_10(self):
        ''' 验证选择角色'''
        menu = UserPage(self.driver)  # 实例化用户管理页面
        self.login.loginFunc()  # 登录
        menu.inUserPage()  # 进入用户管理页面
        time.sleep(3)
        menu.cBtn(menu.button_list[1])
        role = self.driver.find_element_by_name('roleId')
        Select(role).select_by_value('0fea1af336204e7d8dd2d63768751253')  # 获取下拉选
        # msg9 = menu.isElementExist(menu.addinput[14])
        # self.assertTrue(msg9,'代理中心负责人')#验证

    def testupdateuser_1(self):
        '''验证点击修改按钮'''
        menu = UserPage(self.driver)  # 实例化用户管理页面
        self.login.loginFunc()  # 登录
        menu.inUserPage()  # 进入用户管理页面
        time.sleep(3)
        menu.cBtn(menu.button_list[2])
        time.sleep(1)
        msg1 = menu.isElementExist(menu.updateuser[0])
        self.assertTrue(msg1,'弹出提示信息')
        if msg1:
            msgInfo = menu.getValue(*menu.updateuser[0])
            self.assertEqual(msgInfo, '×\n提示! 请选中一项内容！', '提示信息正确')

    def testupdateuser_2(self):
        '''验证选择多项点击修改按钮'''
        menu = UserPage(self.driver)  # 实例化用户管理页面
        self.login.loginFunc()  # 登录
        menu.inUserPage()  # 进入用户管理页面
        time.sleep(3)
        menu.cBtn(menu.updateuser[2])
        menu.cBtn(menu.button_list[2])
        time.sleep(1)
        msg2 = menu.isElementExist(menu.updateuser[1])
        self.assertTrue(msg2, '弹出提示信息')
        if msg2:
            msgInfo = menu.getValue(*menu.updateuser[1])
            self.assertEqual(msgInfo, '×\n提示! 请选中一项内容进行操作！', '提示信息正确')

    def testupdateuser_3(self):
        '''验证删除修改必填项点击提交'''
        menu = UserPage(self.driver)  # 实例化用户管理页面
        self.login.loginFunc()  # 登录
        menu.inUserPage()  # 进入用户管理页面
        time.sleep(3)
        menu.cBtn(menu.updateuser[3])#选择一项
        menu.cBtn(menu.button_list[2])#点击修改按钮
        menu.clearValue(menu.updateuser[4])#清空登录账号
        menu.clearValue(menu.updateuser[5])#清空登录密码
        menu.cBtn(menu.button_list[10])#点击修改提交按钮
        msg3 = menu.isElementExist(menu.updateuser[6])
        self.assertTrue(msg3,'出现提示信息')
        if msg3:
            msgInfo1 = menu.getValue(*menu.updateuser[6])
            self.assertEqual(msgInfo1, '不能为空', '提示信息正确')
        msg3_1 = menu.isElementExist(menu.updateuser[7])
        self.assertTrue(msg3_1,'出现提示信息')
        if msg3_1:
            msgInfo2 = menu.getValue(*menu.updateuser[7])
            self.assertEqual(msgInfo2, '不能为空', '提示信息正确')

    def testupdateuser_4(self):
        '''验证修改登录账号点击提交'''
        menu = UserPage(self.driver)  # 实例化用户管理页面
        self.login.loginFunc()  # 登录
        menu.inUserPage()  # 进入用户管理页面
        time.sleep(3)
        menu.cBtn(menu.updateuser[3])#选择一项
        menu.cBtn(menu.button_list[2])#点击修改按钮
        menu.inputValue(menu.updateuser[4], menu.valueList[4])#修改登录账号
        menu.cBtn(menu.button_list[10])#点击提交
        '''验证'''
        time.sleep(1)
        msg4 = menu.isElementExist(menu.updateuser[8])
        self.assertTrue(msg4,'弹出提示信息')
        if msg4:
            msgInfo1 = menu.getValue(*menu.updateuser[8])
            self.assertEqual(msgInfo1, '×\n提示! 修改成功！', '提示信息正确')
        msg4_1 = menu.isElementExist(menu.updateuser[9])
        self.assertTrue(msg4_1,'页面显示验证')
        if msg4_1:
            msgInfo2 = menu.getValue(*menu.updateuser[9])
            self.assertEqual(msgInfo2, '15864901722', '显示信息正确')

    def testupdateuser_5(self):
        '''验证修改登录密码点击提交'''
        menu = UserPage(self.driver)  # 实例化用户管理页面
        self.login.loginFunc()  # 登录
        menu.inUserPage()  # 进入用户管理页面
        time.sleep(3)
        menu.cBtn(menu.updateuser[3])#选择一项
        menu.cBtn(menu.button_list[2])#点击修改按钮
        menu.inputValue(menu.updateuser[5], menu.valueList[3])#修改登录密码
        menu.cBtn(menu.button_list[10])#点击提交
        time.sleep(1)
        msg5 = menu.isElementExist(menu.updateuser[8])
        self.assertTrue(msg5, '弹出提示信息')
        if msg5:
            msgInfo = menu.getValue(*menu.updateuser[8])
            self.assertEqual(msgInfo, '×\n提示! 修改成功！', '提示信息正确')

    def testupdateuser_6(self):
        '''验证修改性别，角色提交'''
        menu = UserPage(self.driver)  # 实例化用户管理页面
        self.login.loginFunc()  # 登录
        menu.inUserPage()  # 进入用户管理页面
        time.sleep(3)
        menu.cBtn(menu.updateuser[3])#选择一项
        menu.cBtn(menu.button_list[2])#点击修改按钮
        sex = self.driver.find_element_by_name('sex')
        Select(sex).select_by_value('2')  # 获取下拉选
        time.sleep(1)
        role = self.driver.find_element_by_xpath('//*[@id="upDateForm"]/div[7]/div/select')
        Select(role).select_by_value('0fea1af336204e7d8dd2d63768751253')  # 获取下拉选
        menu.cBtn(menu.button_list[10])#点击提交
        '''验证'''
        time.sleep(1)
        msg6_1 = menu.isElementExist(menu.updateuser[10])
        self.assertTrue(msg6_1,'页面显示验证')
        if msg6_1:
            msgInfo1 = menu.getValue(*menu.updateuser[10])
            self.assertEqual(msgInfo1, '女', '显示信息正确')
        msg6_2 = menu.isElementExist(menu.updateuser[11])
        self.assertTrue(msg6_2,'页面显示验证')
        if msg6_2:
            msgInfo2 = menu.getValue(*menu.updateuser[11])
            self.assertEqual(msgInfo2, '代理中心负责人', '显示信息正确')
        msg6_3 = menu.isElementExist(menu.updateuser[8])
        self.assertTrue(msg6_3, '弹出提示信息')
        if msg6_3:
            msgInfo3 = menu.getValue(*menu.updateuser[8])
            self.assertEqual(msgInfo3, '×\n提示! 修改成功！', '提示信息正确')

    def testdeleteuser_1(self):
        '''点击删除按钮'''
        menu = UserPage(self.driver)  # 实例化用户管理页面
        self.login.loginFunc()  # 登录
        menu.inUserPage()  # 进入用户管理页面
        time.sleep(3)
        menu.cBtn(menu.button_list[3])#点击删除按钮
        msg1 = menu.isElementExist(menu.deleteuser[0])
        self.assertTrue(msg1,'弹出提示信息')#验证
        if msg1:
            msgInfo = menu.getValue(*menu.deleteuser[0])
            self.assertEqual(msgInfo, '×\n提示! 请选中一项内容！', '提示信息正确')
    """
    def testdeleteuser_2(self):
        '''选择一项点击删除验证'''
        menu = UserPage(self.driver)  # 实例化用户管理页面
        self.login.loginFunc()  # 登录
        menu.inUserPage()  # 进入用户管理页面
        time.sleep(3)
        menu.cBtn(menu.deleteuser[2])#选择删除项
        menu.cBtn(menu.button_list[3])  # 点击删除按钮
        menu.cBtn(menu.button_list[12])#点击确定按钮
        '''验证'''
        time.sleep(1)
        msg2_1 = menu.isElementExist(menu.deleteuser[1])
        self.assertTrue(msg2_1,'弹出提示信息')
        if msg2_1:
            msgInfo = menu.getValue(*menu.deleteuser[1])
            self.assertEqual(msgInfo, '×\n提示! 删除成功！', '提示信息正确')
     """
    def testorgan_1(self):
        '''点击机构分配'''
        menu = UserPage(self.driver)  # 实例化用户管理页面
        self.login.loginFunc()  # 登录
        menu.inUserPage()  # 进入用户管理页面
        time.sleep(2)
        menu.cBtn(menu.button_list[4])#点击机构分配
        msg1 = menu.isElementExist(menu.allot[0])
        self.assertTrue(msg1,'弹出提示信息')#验证
        if msg1:
            msgInfo = menu.getValue(*menu.allot[0])
            self.assertEqual(msgInfo, '×\n提示! 请选中一项内容！', '提示信息正确')

    def testorgan_2(self):
        '''选择多项点击机构分配'''
        menu = UserPage(self.driver)  # 实例化用户管理页面
        self.login.loginFunc()  # 登录
        menu.inUserPage()  # 进入用户管理页面
        time.sleep(2)
        menu.cBtn(menu.updateuser[2])#选择多项
        menu.cBtn(menu.button_list[4])#点击机构分配
        time.sleep(1)
        msg2 = menu.isElementExist(menu.allot[1])
        self.assertTrue(msg2,'弹出提示信息')#验证
        if msg2:
            msgInfo = menu.getValue(*menu.allot[1])
            self.assertEqual(msgInfo, '×\n提示! 请选中一项内容进行操作！', '提示信息正确')

    def testorgan_3(self):
        '''选择一项点击机构分配'''
        menu = UserPage(self.driver)  # 实例化用户管理页面
        self.login.loginFunc()  # 登录
        menu.inUserPage()  # 进入用户管理页面
        time.sleep(2)
        menu.cBtn(menu.updateuser[3])  # 选择一项
        menu.cBtn(menu.button_list[4])  # 点击机构分配
        menu.cBtn(menu.button_list[16])
        menu.cBtn(menu.button_list[17])#选择机构
        menu.cBtn(menu.button_list[14])#提交
        time.sleep(1)
        msg3 = menu.isElementExist(menu.allot[2])
        self.assertTrue(msg3,'弹出提示信息')
        if msg3:
            msgInfo1 = menu.getValue(*menu.allot[2])
            self.assertEqual(msgInfo1, '×\n提示! 分配成功！', '提示信息正确')
        msg3_1 = menu.isElementExist(menu.allot[3])
        self.assertTrue(msg3_1,'显示验证')
        if msg3_1:
            msgInfo2 = menu.getValue(*menu.allot[3])
            self.assertEqual(msgInfo2, '淄川区', '显示信息正确')

    def testaccount_1(self):
        '''点击账套分配'''
        menu = UserPage(self.driver)  # 实例化用户管理页面
        self.login.loginFunc()  # 登录
        menu.inUserPage()  # 进入用户管理页面
        time.sleep(2)
        menu.cBtn(menu.button_list[5])  # 点击账套分配
        time.sleep(1)
        msg1 = menu.isElementExist(menu.allot[0])
        self.assertTrue(msg1,'弹出提示信息')
        if msg1:
            msgInfo = menu.getValue(*menu.allot[0])
            self.assertEqual(msgInfo, '×\n提示! 请选中一项内容！', '提示信息正确')

    def testaccount_2(self):
        '''选中多项点击账套分配'''
        menu = UserPage(self.driver)  # 实例化用户管理页面
        self.login.loginFunc()  # 登录
        menu.inUserPage()  # 进入用户管理页面
        time.sleep(2)
        menu.cBtn(menu.updateuser[2])  # 选择多项
        menu.cBtn(menu.button_list[5])  # 点击账套分配
        time.sleep(1)
        msg2 = menu.isElementExist(menu.allot[1])
        self.assertTrue(msg2, '弹出提示信息')  # 验证
        if msg2:
            msgInfo = menu.getValue(*menu.allot[1])
            self.assertEqual(msgInfo, '×\n提示! 请选中一项内容进行操作！', '提示信息正确')

    def testaccount_3(self):
        '''选择一项点击账套分配'''
        menu = UserPage(self.driver)  # 实例化用户管理页面
        self.login.loginFunc()  # 登录
        menu.inUserPage()  # 进入用户管理页面
        time.sleep(2)
        menu.cBtn(menu.updateuser[3])  # 选择一项
        menu.cBtn(menu.button_list[5])  # 点击账套分配
        menu.cBtn(menu.button_list[18])  #选择账套
        menu.cBtn(menu.button_list[14])#提交
        time.sleep(1)
        msg3 = menu.isElementExist(menu.allot[2])
        self.assertTrue(msg3, '弹出提示信息')
        if msg3:
            msgInfo = menu.getValue(*menu.allot[2])
            self.assertEqual(msgInfo, '×\n提示! 分配成功！', '提示信息正确')

    def testlimits_1(self):
        ''' 点击权限分配'''
        menu = UserPage(self.driver)  # 实例化用户管理页面
        self.login.loginFunc()  # 登录
        menu.inUserPage()  # 进入用户管理页面
        time.sleep(2)
        menu.cBtn(menu.button_list[6])  # 点击账套分配
        time.sleep(1)
        msg1 = menu.isElementExist(menu.allot[0])
        self.assertTrue(msg1,'弹出提示信息')
        if msg1:
            msgInfo = menu.getValue(*menu.allot[0])
            self.assertEqual(msgInfo, '×\n提示! 请选中一项内容！', '提示信息正确')

    def testlimits_2(self):
        '''选中多项点击权限分配'''
        menu = UserPage(self.driver)  # 实例化用户管理页面
        self.login.loginFunc()  # 登录
        menu.inUserPage()  # 进入用户管理页面
        time.sleep(2)
        menu.cBtn(menu.updateuser[2])  # 选择多项
        menu.cBtn(menu.button_list[6])  # 点击权限分配
        time.sleep(1)
        msg2 = menu.isElementExist(menu.allot[1])
        self.assertTrue(msg2, '弹出提示信息')  # 验证
        if msg2:
            msgInfo = menu.getValue(*menu.allot[1])
            self.assertEqual(msgInfo, '×\n提示! 请选中一项内容进行操作！', '提示信息正确')

    def testlimits_3(self):
        '''选择一项点击权限分配'''
        menu = UserPage(self.driver)  # 实例化用户管理页面
        self.login.loginFunc()  # 登录
        menu.inUserPage()  # 进入用户管理页面
        time.sleep(2)
        menu.cBtn(menu.updateuser[3])  # 选择一项
        menu.cBtn(menu.button_list[6])  # 点击权限分配
        menu.cBtn(menu.button_list[19])#选择权限
        menu.cBtn(menu.button_list[14])#提交
        time.sleep(1)
        msg3 = menu.isElementExist(menu.allot[2])
        self.assertTrue(msg3,'弹出提示信息')
        if msg3:
            msgInfo = menu.getValue(*menu.allot[2])
            self.assertEqual(msgInfo, '×\n提示! 分配成功！', '提示信息正确')

    def testarea_1(self):
        '''点击地区分配'''
        menu = UserPage(self.driver)  # 实例化用户管理页面
        self.login.loginFunc()  # 登录
        menu.inUserPage()  # 进入用户管理页面
        time.sleep(2)
        menu.cBtn(menu.button_list[7])  # 点击地区分配
        time.sleep(1)
        msg1 = menu.isElementExist(menu.allot[0])
        self.assertTrue(msg1, '弹出提示信息')
        if msg1:
            msgInfo = menu.getValue(*menu.allot[0])
            self.assertEqual(msgInfo, '×\n提示! 请选中一项内容！', '提示信息正确')

    def testarea_2(self):
        '''选中多项点击地区分配'''
        menu = UserPage(self.driver)  # 实例化用户管理页面
        self.login.loginFunc()  # 登录
        menu.inUserPage()  # 进入用户管理页面
        time.sleep(2)
        menu.cBtn(menu.updateuser[2])  # 选择多项
        menu.cBtn(menu.button_list[7])  # 点击地区分配
        time.sleep(1)
        msg2 = menu.isElementExist(menu.allot[1])
        self.assertTrue(msg2, '弹出提示信息')  # 验证
        if msg2:
            msgInfo = menu.getValue(*menu.allot[1])
            self.assertEqual(msgInfo, '×\n提示! 请选中一项内容进行操作！', '提示信息正确')

    def testarea_3(self):
        '''选择一项点击地区分配'''
        menu = UserPage(self.driver)  # 实例化用户管理页面
        self.login.loginFunc()  # 登录
        menu.inUserPage()  # 进入用户管理页面
        time.sleep(2)
        menu.cBtn(menu.updateuser[3])  # 选择一项
        menu.cBtn(menu.button_list[7])  # 点击地区分配
        menu.cBtn(menu.button_list[20])  # 选择地区
        menu.cBtn(menu.button_list[14])  # 提交
        time.sleep(1)
        msg3_1 = menu.isElementExist(menu.allot[2])
        self.assertTrue(msg3_1, '弹出提示信息')
        if msg3_1:
            msgInfo1 = menu.getValue(*menu.allot[2])
            self.assertEqual(msgInfo1, '×\n提示! 分配成功！', '提示信息正确')
        msg3_2 = menu.isElementExist(menu.allot[4])
        self.assertTrue(msg3_2,'页面显示验证')
        if msg3_2:
            msgInfo2 = menu.getValue(*menu.allot[4])
            self.assertEqual(msgInfo2, '所有地区', '提示信息正确')

if __name__ == '__main__':
    pass








