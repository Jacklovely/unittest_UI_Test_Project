'''
Code description：菜单管理模块 testcase
Create time：
Developer：
'''
import time
from framfriend.test_case.models.myunittest import MyunitTest
from framfriend.test_case.page_obj.menu_page import Menu_Page

class Menu_Tc(MyunitTest):
    '''菜单管理模块用例'''
    def test_addmenu_1(self):
        '''点击新增按钮'''
        menu = Menu_Page(self.driver) #实例化菜单管理页面
        self.login.loginFunc() #登录
        menu.inmenuPage() #进入菜单管理页面
        time.sleep(2)
        menu.cBtn(menu.button_list[0])#点击新增按钮
        msg1 = menu.isElementExist(menu.addmenu_list[0])
        self.assertTrue(msg1,'弹出新增窗口')#验证

    def test_addmenu_2(self):
        '''不输入必填项提交'''
        menu = Menu_Page(self.driver) #实例化菜单管理页面
        self.login.loginFunc()#登录
        menu.inmenuPage()#进入菜单管理页面
        time.sleep(2)
        menu.cBtn(menu.button_list[0])#点击新增按钮
        menu.cBtn(menu.button_list[6])#点击提交按钮
        msg2 = menu.isElementExist(menu.addmenu_list[5])
        self.assertTrue(msg2,'出现提示信息')#验证
        if msg2:
            msgInfo = menu.getValue(*menu.addmenu_list[5])
            self.assertEqual(msgInfo, '不能为空', '提示信息正确')

    def test_addmenu_3(self):
        '''错误输入排序'''
        menu = Menu_Page(self.driver) #实例化菜单管理页面
        self.login.loginFunc()  # 登录
        menu.inmenuPage()  # 进入菜单管理页面
        time.sleep(2)
        menu.cBtn(menu.button_list[0])#点击新增按钮
        menu.inputValue(menu.addmenu_list[4],menu.reason)#输入排序
        msg3 = menu.isElementExist(menu.addmenu_list[6])
        self.assertTrue(msg3,'出现提示信息')#验证
        if msg3:
            msgInfo = menu.getValue(*menu.addmenu_list[6])
            self.assertEqual(msgInfo, '请输入有效的数字', '提示信息正确')

    def test_addmenu_4(self):
        '''输入必填项点击新增'''
        menu = Menu_Page(self.driver) #实例化菜单管理页面
        self.login.loginFunc()  # 登录
        menu.inmenuPage()  # 进入菜单管理页面
        time.sleep(2)
        menu.cBtn(menu.additem[0])
        menu.cBtn(menu.additem[1])# 点击新增项
        menu.cBtn(menu.button_list[0])#点击新增按钮
        menu.inputValue(menu.addmenu_list[1],menu.reason)#输入菜单名称
        menu.cBtn(menu.button_list[6])#点击提交按钮
        time.sleep(1)
        msg4 = menu.isElementExist(menu.msgbox)
        self.assertTrue(msg4,'新增成功！')
        if msg4:
            msgInfo = menu.getValue(*menu.msgbox)
            self.assertEqual(msgInfo, '×\n提示! 新增成功！', '提示信息正确')

    def test_addmenu_5(self):
        '''点击取消关闭窗口'''
        menu = Menu_Page(self.driver)  # 实例化菜单管理页面
        self.login.loginFunc()  # 登录
        menu.inmenuPage()  # 进入菜单管理页面
        time.sleep(2)
        menu.cBtn(menu.additem[0])
        menu.cBtn(menu.additem[1])  # 点击新增项
        menu.cBtn(menu.button_list[0])#点击新增按钮
        menu.cBtn(menu.button_list[7])#点击取消按钮
        msg5 = menu.isElementExist(menu.addmenu_list[0])
        self.assertFalse(msg5,'关闭窗口')

    def test_updatemenu_1(self):
        '''点击修改按钮'''
        menu = Menu_Page(self.driver)  # 实例化菜单管理页面
        self.login.loginFunc()  # 登录
        menu.inmenuPage()  # 进入菜单管理页面
        time.sleep(2)
        menu.cBtn(menu.button_list[1])#点击修改按钮
        time.sleep(1)
        msg1 = menu.isElementExist(menu.msgbox)
        self.assertTrue(msg1,'弹出提示信息')
        if msg1:
            msgInfo = menu.getValue(*menu.msgbox)
            self.assertEqual(msgInfo, '×\n提示! 请先选中节点！', '提示信息正确')

    def test_updatemanu_2(self):
        '''选中节点点击修改按钮'''
        menu = Menu_Page(self.driver)  # 实例化菜单管理页面
        self.login.loginFunc()  # 登录
        menu.inmenuPage()  # 进入菜单管理页面
        time.sleep(2)
        menu.cBtn(menu.additem[0])
        menu.cBtn(menu.additem[1])
        menu.cBtn(menu.additem[2])
        menu.cBtn(menu.additem[3])
        menu.cBtn(menu.deletemenu_list[2])  # 选中节点
        menu.cBtn(menu.button_list[1])#点击修改按钮
        msg2 = menu.isElementExist(menu.updatemenu_list[0])
        self.assertTrue(msg2,'弹出修改窗口')

    def test_updatemenu_3(self):
        '''清空必填项提交验证'''
        menu = Menu_Page(self.driver)  # 实例化菜单管理页面
        self.login.loginFunc()  # 登录
        menu.inmenuPage()  # 进入菜单管理页面
        time.sleep(2)
        menu.cBtn(menu.additem[0])
        menu.cBtn(menu.additem[1])
        menu.cBtn(menu.additem[2])
        menu.cBtn(menu.additem[3])
        menu.cBtn(menu.deletemenu_list[2])  # 选中节点
        menu.cBtn(menu.button_list[1])  # 点击修改按钮
        menu.clearValue(menu.updatemenu_list[1])#清空必填项
        menu.cBtn(menu.button_list[8])#点击提交按钮
        msg3 = menu.isElementExist(menu.updatemenu_list[5])
        self.assertTrue(msg3,'出现提示信息')
        if msg3:
            msgInfo = menu.getValue(*menu.updatemenu_list[5])
            self.assertEqual(msgInfo, '不能为空', '提示信息正确')

    def test_updatemenu_4(self):
        '''错误输入排序'''
        menu = Menu_Page(self.driver)  # 实例化菜单管理页面
        self.login.loginFunc()  # 登录
        menu.inmenuPage()  # 进入菜单管理页面
        time.sleep(2)
        menu.cBtn(menu.additem[0])
        menu.cBtn(menu.additem[1])
        menu.cBtn(menu.additem[2])
        menu.cBtn(menu.additem[3])
        menu.cBtn(menu.deletemenu_list[2])  # 选中节点
        menu.cBtn(menu.button_list[1])  # 点击修改按钮
        menu.clearValue(menu.updatemenu_list[4])
        menu.inputValue(menu.updatemenu_list[4],menu.reason)#修改排序
        msg4 = menu.isElementExist(menu.updatemenu_list[6])
        self.assertTrue(msg4,'出现提示信息')
        if msg4:
            msgInfo = menu.getValue(*menu.updatemenu_list[6])
            self.assertEqual(msgInfo, '请输入有效的数字', '提示信息正确')

    def test_updatemenu_5(self):
        '''正确修改提交'''
        menu = Menu_Page(self.driver)  # 实例化菜单管理页面
        self.login.loginFunc()  # 登录
        menu.inmenuPage()  # 进入菜单管理页面
        time.sleep(2)
        menu.cBtn(menu.additem[0])
        menu.cBtn(menu.additem[1])
        menu.cBtn(menu.additem[2])
        menu.cBtn(menu.additem[3])
        menu.cBtn(menu.deletemenu_list[2])  # 选中节点
        menu.cBtn(menu.button_list[1])  # 点击修改按钮
        '''输入修改内容'''
        menu.inputValue(menu.updatemenu_list[1], menu.reason)
        menu.inputValue(menu.updatemenu_list[2], menu.valueList[0])
        menu.inputValue(menu.updatemenu_list[3], menu.valueList[1])
        menu.inputValue(menu.updatemenu_list[4], menu.valueList[2])
        menu.cBtn(menu.button_list[8])  # 点击提交按钮
        time.sleep(1)
        msg5 = menu.isElementExist(menu.msgbox)
        self.assertTrue(msg5,'修改成功！')
        if msg5:
            msgInfo = menu.getValue(*menu.msgbox)
            self.assertEqual(msgInfo, '×\n提示! 修改成功！', '提示信息正确')

    def test_updatemenu_6(self):
        '''点击取消按钮'''
        menu = Menu_Page(self.driver)  # 实例化菜单管理页面
        self.login.loginFunc()  # 登录
        menu.inmenuPage()  # 进入菜单管理页面
        time.sleep(2)
        menu.cBtn(menu.additem[0])
        menu.cBtn(menu.additem[1])
        menu.cBtn(menu.additem[2])
        menu.cBtn(menu.additem[3])
        menu.cBtn(menu.deletemenu_list[2])  # 选中节点
        menu.cBtn(menu.button_list[1])  # 点击修改按钮
        menu.cBtn(menu.button_list[9])#点击取消按钮
        msg6  = menu.isElementExist(menu.updatemenu_list[0])
        self.assertFalse(msg6,'关闭窗口')

    def test_deletemenu_1(self):
        '''点击删除按钮'''
        menu = Menu_Page(self.driver)  # 实例化菜单管理页面
        self.login.loginFunc()  # 登录
        menu.inmenuPage()  # 进入菜单管理页面
        time.sleep(2)
        menu.cBtn(menu.button_list[2])
        msg1 = menu.isElementExist(menu.msgbox)
        self.assertTrue(msg1,'弹出提示信息')
        if msg1:
            msgInfo = menu.getValue(*menu.msgbox)
            self.assertEqual(msgInfo, '×\n提示! 请先选中节点！', '提示信息正确')

    def test_deletemenu_2(self):
        '''选中节点点击删除'''
        menu = Menu_Page(self.driver)  # 实例化菜单管理页面
        self.login.loginFunc()  # 登录
        menu.inmenuPage()  # 进入菜单管理页面
        time.sleep(2)
        menu.cBtn(menu.additem[0])
        menu.cBtn(menu.additem[1])
        menu.cBtn(menu.additem[2])
        menu.cBtn(menu.additem[3])
        menu.cBtn(menu.deletemenu_list[2])  # 选中节点
        menu.cBtn(menu.button_list[2])#点击删除按钮
        msg2 = menu.isElementExist(menu.deletemenu_list[1])
        self.assertTrue(msg2,'弹出删除提示')

    def test_deletemenu_3(self):
        '''确定删除'''
        menu = Menu_Page(self.driver)  # 实例化菜单管理页面
        self.login.loginFunc()  # 登录
        menu.inmenuPage()  # 进入菜单管理页面
        time.sleep(2)
        menu.cBtn(menu.additem[0])
        menu.cBtn(menu.additem[1])
        menu.cBtn(menu.additem[2])
        menu.cBtn(menu.additem[3])
        menu.cBtn(menu.deletemenu_list[2])  # 选中节点
        menu.cBtn(menu.button_list[2])  # 点击删除按钮
        menu.cBtn(menu.button_list[10])#点击提交按钮
        time.sleep(1)
        msg3 = menu.isElementExist(menu.msgbox)
        self.assertTrue(msg3,'弹出提示信息')
        if msg3:
            msgInfo = menu.getValue(*menu.msgbox)
            self.assertEqual(msgInfo, '×\n提示! 删除成功！', '提示信息正确')

    def test_deletemenu_4(self):
        '''取消删除'''
        menu = Menu_Page(self.driver)  # 实例化菜单管理页面
        self.login.loginFunc()  # 登录
        menu.inmenuPage()  # 进入菜单管理页面
        time.sleep(2)
        menu.cBtn(menu.additem[0])
        menu.cBtn(menu.additem[1])
        menu.cBtn(menu.additem[2])
        menu.cBtn(menu.additem[3])
        menu.cBtn(menu.deletemenu_list[2])  # 选中节点
        menu.cBtn(menu.button_list[2])  # 点击删除按钮
        menu.cBtn(menu.button_list[11])  # 点击取消按钮
        msg4 = menu.isElementExist(menu.deletemenu_list[1])
        self.assertFalse(msg4,'关闭窗口')

if __name__=='__main__':
    pass