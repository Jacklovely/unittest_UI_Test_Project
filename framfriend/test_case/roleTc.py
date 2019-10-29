'''
Code description：角色管理模块 testcase
Create time：
Developer：
'''
import time
from framfriend.test_case.models.myunit import MyunitTest
from framfriend.test_case.page_obj.role_page import rolePage

class role_TC(MyunitTest):
    """角色模块测试用例"""

    def test_alone_query_(self):
        '''按角色、表示位、描述单一条件查询'''
        menu = rolePage(self.driver)#实例化角色管理页面
        self.login.loginFunc()#登录
        menu.inrolePage()#进入角色管理页面
        time.sleep(3)
        for role_show_describe in menu.query_list:
            menu.reset()#重置
            for value in menu.valuesList:
                menu.iQueryCondition(role_show_describe,value)
                menu.cBtn(menu.button_list[0])
                time.sleep(2)
                flag = menu.getValue(*menu.query_msg[1])
                try:
                    self.assertIn('管理员', flag, '查询成功')
                except Exception:
                    self.assertNotIn('管理员', flag, '查询条件无效')

    def testaddrole_1(self):
        '''为空新增角色验证'''
        menu = rolePage(self.driver)  # 实例化角色管理页面
        self.login.loginFunc()  # 登录
        menu.inrolePage()  # 进入角色管理页面
        time.sleep(3)
        menu.cBtn(menu.button_list[1])#点击新增按钮
        menu.cBtn(menu.button_list[5])#点击新增提交按钮
        msg1_1 = menu.isElementExist(menu.addrole_list[3])
        self.assertTrue(msg1_1,'出现提示信息')
        if msg1_1:
            msgInfo1 = menu.getValue(*menu.addrole_list[3])
            self.assertEqual(msgInfo1, '不能为空', '提示信息正确')
        msg1_2 = menu.isElementExist(menu.addrole_list[4])
        self.assertTrue(msg1_2,'出现提示信息')
        if msg1_2:
            msgInfo2 = menu.getValue(*menu.addrole_list[4])
            self.assertEqual(msgInfo2, '不能为空', '提示信息正确')
        msg1_3 = menu.isElementExist(menu.addrole_list[5])
        self.assertTrue(msg1_3,'出现提示信息')
        if msg1_3:
            msgInfo3 = menu.getValue(*menu.addrole_list[5])
            self.assertEqual(msgInfo3, '不能为空', '提示信息正确')

    def testaddrole_2(self):
        '''角色为空验证'''
        menu = rolePage(self.driver)  # 实例化角色管理页面
        self.login.loginFunc()  # 登录
        menu.inrolePage()  # 进入角色管理页面
        time.sleep(3)
        menu.cBtn(menu.button_list[1])#点击新增
        menu.inputValue(menu.addrole_list[1],menu.valueList[1])#输入表示位
        menu.inputValue(menu.addrole_list[2],menu.valueList[2])#输入描述
        menu.cBtn(menu.button_list[5])#点击提交
        msg2 = menu.isElementExist(menu.addrole_list[3])#提示验证
        self.assertTrue(msg2,'出现提示信息')
        if msg2:
            msgInfo = menu.getValue(*menu.addrole_list[3])
            self.assertEqual(msgInfo, '不能为空', '提示信息正确')

    def testaddrole_3(self):
        '''表示位为空验证'''
        menu = rolePage(self.driver) # 实例化角色管理页面
        self.login.loginFunc() #登录
        menu.inrolePage() #进入角色管理页面
        time.sleep(2)
        menu.cBtn(menu.button_list[1])#点击新增按钮
        menu.inputValue(menu.addrole_list[0],menu.valueList[0])#输入角色名称
        menu.inputValue(menu.addrole_list[2],menu.valueList[2])#输入描述
        menu.cBtn(menu.button_list[5])#点击提交
        msg3 = menu.isElementExist(menu.addrole_list[4])#提示验证
        self.assertTrue(msg3,'出现提示信息')
        if msg3:
            msgInfo = menu.getValue(*menu.addrole_list[4])
            self.assertEqual(msgInfo, '不能为空', '提示信息正确')

    def testaddrole_4(self):
        '''描述为空验证'''
        menu = rolePage(self.driver)  # 实例化角色管理页面
        self.login.loginFunc()  # 登录
        menu.inrolePage()  # 进入角色管理页面
        time.sleep(2)
        menu.cBtn(menu.button_list[1])#点击新增按钮
        menu.inputValue(menu.addrole_list[0],menu.valueList[0])#输入角色名称
        menu.inputValue(menu.addrole_list[1],menu.valueList[1])#输入表示位
        menu.cBtn(menu.button_list[5])#点击提交按钮
        msg4 = menu.isElementExist(menu.addrole_list[5])#提示验证
        self.assertTrue(msg4,'出现提示信息')
        if msg4:
            msgInfo = menu.getValue(*menu.addrole_list[5])
            self.assertEqual(msgInfo, '不能为空', '提示信息正确')

    def testaddrole_5(self):
        '''新增成功验证'''
        menu = rolePage(self.driver)  # 实例化角色管理页面
        self.login.loginFunc()  # 登录
        menu.inrolePage()  # 进入角色管理页面
        time.sleep(2)
        menu.cBtn(menu.button_list[1])  # 点击新增按钮
        menu.inputValue(menu.addrole_list[0], menu.valueList[0])  # 输入角色名称
        menu.inputValue(menu.addrole_list[1], menu.valueList[1])  # 输入表示位
        menu.inputValue(menu.addrole_list[2], menu.valueList[2])  # 输入描述
        menu.cBtn(menu.button_list[5])#点击提交
        time.sleep(1)
        msg5 = menu.isElementExist(menu.addrole_list[6])#提示验证
        self.assertTrue(msg5,'新增成功！')
        if msg5:
            msgInfo = menu.getValue(*menu.addrole_list[6])
            self.assertEqual(msgInfo, '×\n提示! 新增成功！', '提示信息正确')

    def testupdaterole_1(self):
        '''点击修改验证'''
        menu = rolePage(self.driver)  # 实例化角色管理页面
        self.login.loginFunc()  # 登录
        menu.inrolePage()  # 进入角色管理页面
        time.sleep(2)
        menu.cBtn(menu.button_list[2]) #点击修改按钮
        time.sleep(1)
        msg1 = menu.isElementExist(menu.updaterole_list[8])#提示验证
        self.assertTrue(msg1, '弹出提示信息')
        if msg1:
            msgInfo = menu.getValue(*menu.updaterole_list[8])
            self.assertEqual(msgInfo, '×\n提示! 请选中一项内容', '提示信息正确')

    def testupdaterole_2(self):
        '''选中多项点击修改按钮'''
        menu = rolePage(self.driver)  # 实例化角色管理页面
        self.login.loginFunc()  # 登录
        menu.inrolePage()  # 进入角色管理页面
        time.sleep(2)
        menu.cBtn(menu.updaterole_list[1])#全选
        menu.cBtn(menu.button_list[2])#点击修改按钮
        msg2 = menu.isElementExist(menu.updaterole_list[8])#提示验证
        self.assertTrue(msg2, '弹出提示信息')
        if msg2:
            msgInfo = menu.getValue(*menu.updaterole_list[8])
            self.assertEqual(msgInfo, '×\n提示! 请选中一项内容进行修改', '提示信息正确')

    def testupdaterole_3(self):
        '''删除已有数据提交'''
        menu = rolePage(self.driver)  # 实例化角色管理页面
        self.login.loginFunc()  # 登录
        menu.inrolePage()  # 进入角色管理页面
        time.sleep(2)
        menu.cBtn(menu.updaterole_list[0])#选中修改项
        menu.cBtn(menu.button_list[2])  # 点击修改按钮
        '''清空数据'''
        menu.clearValue(menu.updaterole_list[2])
        menu.clearValue(menu.updaterole_list[3])
        menu.clearValue(menu.updaterole_list[4])
        menu.cBtn(menu.button_list[7])#点击提交按钮
        msg3_1 = menu.isElementExist(menu.updaterole_list[5])
        self.assertTrue(msg3_1, '出现提示信息')
        if msg3_1:
            msgInfo = menu.getValue(*menu.updaterole_list[5])
            self.assertEqual(msgInfo, '不能为空', '提示信息正确')
        msg3_2 = menu.isElementExist(menu.updaterole_list[6])
        self.assertTrue(msg3_2, '出现提示信息')
        if msg3_2:
            msgInfo2 = menu.getValue(*menu.updaterole_list[6])
            self.assertEqual(msgInfo2, '不能为空', '提示信息正确')
        msg3_3 = menu.isElementExist(menu.updaterole_list[7])
        self.assertTrue(msg3_3, '出现提示信息')
        if msg3_3:
            msgInfo3 = menu.getValue(*menu.updaterole_list[7])
            self.assertEqual(msgInfo3, '不能为空', '提示信息正确')

    def testupdaterole_4(self):
        '''修改必填项验证'''
        menu = rolePage(self.driver)  # 实例化角色管理页面
        self.login.loginFunc()  # 登录
        menu.inrolePage()  # 进入角色管理页面
        time.sleep(2)
        menu.cBtn(menu.updaterole_list[0])  # 选中修改项
        menu.cBtn(menu.button_list[2])  # 点击修改按钮
        menu.inputValue(menu.updaterole_list[2],menu.valueList[0])#修改角色名称
        menu.inputValue(menu.updaterole_list[3],menu.valueList[1])  # 修改表示位
        menu.inputValue(menu.updaterole_list[4],menu.valueList[2])  # 修改描述
        menu.cBtn(menu.button_list[7])  # 点击提交按钮
        time.sleep(1)
        msg4 = menu.isElementExist(menu.updaterole_list[8])#提示验证
        self.assertTrue(msg4, '弹出提示信息')
        if msg4:
            msgInfo = menu.getValue(*menu.updaterole_list[8])
            self.assertEqual(msgInfo, '×\n提示! 修改成功！', '提示信息正确')

    def testmenuAssignment_1(self):
        '''点击菜单分配'''
        menu = rolePage(self.driver)  # 实例化角色管理页面
        self.login.loginFunc()  # 登录
        menu.inrolePage()  # 进入角色管理页面
        time.sleep(2)
        menu.cBtn(menu.button_list[3])#点击菜单分配
        time.sleep(1)
        msg = menu.isElementExist(menu.updaterole_list[8])#提示验证
        self.assertTrue(msg, '弹出提示信息')
        if msg:
            msgInfo = menu.getValue(*menu.updaterole_list[8])
            self.assertEqual(msgInfo, '×\n提示! 请选中一项内容', '提示信息正确')

    def testmenuAssignment_2(self):
        '''选中多项点击菜单分配'''
        menu = rolePage(self.driver)  # 实例化角色管理页面
        self.login.loginFunc()  # 登录
        menu.inrolePage()  # 进入角色管理页面
        time.sleep(2)
        menu.cBtn(menu.updaterole_list[1])  # 全选
        menu.cBtn(menu.button_list[3])#点击菜单分配
        time.sleep(1)
        msg = menu.isElementExist(menu.updaterole_list[8])#提示验证
        self.assertTrue(msg, '弹出提示信息')
        if msg:
            msgInfo = menu.getValue(*menu.updaterole_list[8])
            self.assertEqual(msgInfo, '×\n提示! 请选中一项内容进行操作', '提示信息正确')

    def testmenuAssignment_3(self):
        '''选中一项点击菜单分配'''
        menu = rolePage(self.driver)  # 实例化角色管理页面
        self.login.loginFunc()  # 登录
        menu.inrolePage()  # 进入角色管理页面
        time.sleep(2)
        menu.cBtn(menu.updaterole_list[0])#选中一项
        menu.cBtn(menu.button_list[3])#点击菜单分配
        menu.cBtn(menu.button_list[9])#选中分配菜单
        menu.cBtn(menu.button_list[7])#点击提交按钮
        time.sleep(1)
        msg = menu.isElementExist(menu.updaterole_list[8])
        self.assertTrue(msg,'弹出提示信息')
        if msg:
            msgInfo = menu.getValue(*menu.updaterole_list[8])
            self.assertEqual(msgInfo, '×\n提示! 操作成功！', '提示信息正确')

    def testbuttonAssigned_1(self):
        '''点击按钮分配'''
        menu = rolePage(self.driver)# 实例化角色管理页面
        self.login.loginFunc()  # 登录
        menu.inrolePage()  # 进入角色管理页面
        time.sleep(2)
        menu.cBtn(menu.button_list[4])#点击按钮分配
        time.sleep(1)
        msg = menu.isElementExist(menu.updaterole_list[8])  # 提示验证
        self.assertTrue(msg, '弹出提示信息')
        if msg:
            msgInfo = menu.getValue(*menu.updaterole_list[8])
            self.assertEqual(msgInfo, '×\n提示! 请选中一项内容', '提示信息正确')

    def testbuttonAssigned_2(self):
        '''选中多项点击按钮分配'''
        menu = rolePage(self.driver)  # 实例化角色管理页面
        self.login.loginFunc()  # 登录
        menu.inrolePage()  # 进入角色管理页面
        time.sleep(2)
        menu.cBtn(menu.updaterole_list[1])  # 全选
        menu.cBtn(menu.button_list[4])  # 点击按钮分配
        time.sleep(1)
        msg = menu.isElementExist(menu.updaterole_list[8])  # 提示验证
        self.assertTrue(msg, '弹出提示信息')
        if msg:
            msgInfo = menu.getValue(*menu.updaterole_list[8])
            self.assertEqual(msgInfo, '×\n提示! 请选中一项内容进行操作', '提示信息正确')

    def testbuttonAssigned_3(self):
        '''选中一项点击按钮分配'''
        menu = rolePage(self.driver)  # 实例化角色管理页面
        self.login.loginFunc()  # 登录
        menu.inrolePage()  # 进入角色管理页面
        time.sleep(2)
        menu.cBtn(menu.updaterole_list[0])#选择一项
        menu.cBtn(menu.button_list[4])#点击按钮分配
        msg3 = menu.isElementExist(menu.buttonAssigned_list[0])#窗口验证
        self.assertTrue(msg3,'窗口验证')

    def testbuttonAssigned_4(self):
        '''点击新增按钮'''
        menu = rolePage(self.driver)  # 实例化角色管理页面
        self.login.loginFunc()  # 登录
        menu.inrolePage()  # 进入角色管理页面
        time.sleep(2)
        menu.cBtn(menu.updaterole_list[0])  # 选择一项
        menu.cBtn(menu.button_list[4])  # 点击按钮分配
        menu.cBtn(menu.button_list[10])#点击按钮新增
        msg4 = menu.isElementExist(menu.updaterole_list[8])#提示验证
        self.assertTrue(msg4,'请先选中节点')

    def testbuttonAssigned_5(self):
        '''选中节点点击新增按钮'''
        menu = rolePage(self.driver)  # 实例化角色管理页面
        self.login.loginFunc()  # 登录
        menu.inrolePage()  # 进入角色管理页面
        time.sleep(2)
        menu.cBtn(menu.updaterole_list[0])  # 选择一项
        menu.cBtn(menu.button_list[4])  # 点击按钮分配
        menu.cBtn(menu.button_list[13])
        menu.cBtn(menu.button_list[14])#选择节点
        menu.cBtn(menu.button_list[10])  # 点击按钮新增
        msg5 = menu.isElementExist(menu.buttonAssigned_list[8])#窗口验证
        self.assertTrue(msg5,'新增按钮窗口')

    def testbuttonAssigned_6(self):
        '''新增按钮不输入必填项点击提交按钮'''
        menu = rolePage(self.driver)  # 实例化角色管理页面
        self.login.loginFunc()  # 登录
        menu.inrolePage()  # 进入角色管理页面
        time.sleep(2)
        menu.cBtn(menu.updaterole_list[0])  # 选择一项
        menu.cBtn(menu.button_list[4])  # 点击按钮分配
        menu.cBtn(menu.button_list[13])
        menu.cBtn(menu.button_list[14])  # 选择节点
        menu.cBtn(menu.button_list[10])  # 点击按钮新增
        menu.cBtn(menu.buttonAssigned_list[6])#点击提交按钮
        msg6_1 = menu.isElementExist(menu.buttonAssigned_list[23])
        self.assertTrue(msg6_1,'出现提示信息')
        if msg6_1:
            msgInfo = menu.getValue(*menu.buttonAssigned_list[23])
            self.assertEqual(msgInfo, '不能为空', '提示信息正确')
        msg6_2 = menu.isElementExist(menu.buttonAssigned_list[24])
        self.assertTrue(msg6_2, '出现提示信息')
        if msg6_2:
            msgInfo2 = menu.getValue(*menu.buttonAssigned_list[24])
            self.assertEqual(msgInfo2, '不能为空', '提示信息正确')
        msg6_3 = menu.isElementExist(menu.buttonAssigned_list[25])
        self.assertTrue(msg6_3, '出现提示信息')
        if msg6_3:
            msgInfo3 = menu.getValue(*menu.buttonAssigned_list[25])
            self.assertEqual(msgInfo3, '不能为空', '提示信息正确')
        msg6_4 = menu.isElementExist(menu.buttonAssigned_list[26])
        self.assertTrue(msg6_4, '出现提示信息')
        if msg6_4:
            msgInfo4 = menu.getValue(*menu.buttonAssigned_list[26])
            self.assertEqual(msgInfo4, '不能为空', '提示信息正确')
        msg6_5 = menu.isElementExist(menu.buttonAssigned_list[27])
        self.assertTrue(msg6_5, '出现提示信息')
        if msg6_5:
            msgInfo5 = menu.getValue(*menu.buttonAssigned_list[27])
            self.assertEqual(msgInfo5, '不能为空', '提示信息正确')

    def testbuttonAssigned_7(self):
        '''新增按钮不输入按钮名称点击提交按钮'''
        menu = rolePage(self.driver)  # 实例化角色管理页面
        self.login.loginFunc()  # 登录
        menu.inrolePage()  # 进入角色管理页面
        time.sleep(2)
        menu.cBtn(menu.updaterole_list[0])  # 选择一项
        menu.cBtn(menu.button_list[4])  # 点击按钮分配
        menu.cBtn(menu.button_list[13])
        menu.cBtn(menu.button_list[14])  # 选择节点
        menu.cBtn(menu.button_list[10])  # 点击按钮新增
        '''输入按钮英文名称，表示位，图标，描述'''
        menu.inputValue(menu.buttonAssigned_list[2],menu.valueList[0])
        menu.inputValue(menu.buttonAssigned_list[3], menu.valueList[1])
        menu.inputValue(menu.buttonAssigned_list[4], menu.valueList[2])
        menu.inputValue(menu.buttonAssigned_list[5], menu.valueList[1])
        menu.cBtn(menu.buttonAssigned_list[6])  # 点击提交按钮
        msg7 = menu.isElementExist(menu.buttonAssigned_list[23])#提示验证
        self.assertTrue(msg7, '出现提示信息')
        if msg7:
            msgInfo = menu.getValue(*menu.buttonAssigned_list[23])
            self.assertEqual(msgInfo, '不能为空', '提示信息正确')

    def testbuttonAssigned_8(self):
        '''新增按钮不输入英文名称点击提交按钮'''
        menu = rolePage(self.driver)  # 实例化角色管理页面
        self.login.loginFunc()  # 登录
        menu.inrolePage()  # 进入角色管理页面
        time.sleep(2)
        menu.cBtn(menu.updaterole_list[0])  # 选择一项
        menu.cBtn(menu.button_list[4])  # 点击按钮分配
        menu.cBtn(menu.button_list[13])
        menu.cBtn(menu.button_list[14])  # 选择节点
        menu.cBtn(menu.button_list[10])  # 点击按钮新增
        '''输入按钮名称，表示位，图标，描述'''
        menu.inputValue(menu.buttonAssigned_list[1],menu.valueList[0])
        menu.inputValue(menu.buttonAssigned_list[3], menu.valueList[1])
        menu.inputValue(menu.buttonAssigned_list[4], menu.valueList[2])
        menu.inputValue(menu.buttonAssigned_list[5], menu.valueList[1])
        menu.cBtn(menu.buttonAssigned_list[6])  # 点击提交按钮
        msg8 = menu.isElementExist(menu.buttonAssigned_list[24])#提示验证
        self.assertTrue(msg8, '出现提示信息')
        if msg8:
            msgInfo = menu.getValue(*menu.buttonAssigned_list[24])
            self.assertEqual(msgInfo, '不能为空', '提示信息正确')

    def testbuttonAssigned_9(self):
        '''新增按钮不输入表示位点击提交按钮'''
        menu = rolePage(self.driver)  # 实例化角色管理页面
        self.login.loginFunc()  # 登录
        menu.inrolePage()  # 进入角色管理页面
        time.sleep(2)
        menu.cBtn(menu.updaterole_list[0])  # 选择一项
        menu.cBtn(menu.button_list[4])  # 点击按钮分配
        menu.cBtn(menu.button_list[13])
        menu.cBtn(menu.button_list[14])  # 选择节点
        menu.cBtn(menu.button_list[10])  # 点击按钮新增
        '''输入按钮英文名称，按钮名称，图标，描述'''
        menu.inputValue(menu.buttonAssigned_list[1],menu.valueList[0])
        menu.inputValue(menu.buttonAssigned_list[2], menu.valueList[0])
        menu.inputValue(menu.buttonAssigned_list[4], menu.valueList[2])
        menu.inputValue(menu.buttonAssigned_list[5], menu.valueList[1])
        menu.cBtn(menu.buttonAssigned_list[6])  # 点击提交按钮
        msg9 = menu.isElementExist(menu.buttonAssigned_list[25])#提示验证
        self.assertTrue(msg9, '出现提示信息')
        if msg9:
            msgInfo = menu.getValue(*menu.buttonAssigned_list[25])
            self.assertEqual(msgInfo, '不能为空', '提示信息正确')

    def testbuttonAssigned_10(self):
        '''新增按钮不输入图标点击提交按钮'''
        menu = rolePage(self.driver)  # 实例化角色管理页面
        self.login.loginFunc()  # 登录
        menu.inrolePage()  # 进入角色管理页面
        time.sleep(2)
        menu.cBtn(menu.updaterole_list[0])  # 选择一项
        menu.cBtn(menu.button_list[4])  # 点击按钮分配
        menu.cBtn(menu.button_list[13])
        menu.cBtn(menu.button_list[14])  # 选择节点
        menu.cBtn(menu.button_list[10])  # 点击按钮新增
        '''输入按钮英文名称，表示位，按钮名称，描述'''
        menu.inputValue(menu.buttonAssigned_list[1],menu.valueList[0])
        menu.inputValue(menu.buttonAssigned_list[2], menu.valueList[0])
        menu.inputValue(menu.buttonAssigned_list[3], menu.valueList[1])
        menu.inputValue(menu.buttonAssigned_list[5], menu.valueList[1])
        menu.cBtn(menu.buttonAssigned_list[6])  # 点击提交按钮
        msg10 = menu.isElementExist(menu.buttonAssigned_list[26])#提示验证
        self.assertTrue(msg10, '出现提示信息')
        if msg10:
            msgInfo = menu.getValue(*menu.buttonAssigned_list[26])
            self.assertEqual(msgInfo, '不能为空', '提示信息正确')

    def testbuttonAssigned_11(self):
        '''新增按钮不输入描述点击提交按钮'''
        menu = rolePage(self.driver)  # 实例化角色管理页面
        self.login.loginFunc()  # 登录
        menu.inrolePage()  # 进入角色管理页面
        time.sleep(2)
        menu.cBtn(menu.updaterole_list[0])  # 选择一项
        menu.cBtn(menu.button_list[4])  # 点击按钮分配
        menu.cBtn(menu.button_list[13])
        menu.cBtn(menu.button_list[14])  # 选择节点
        menu.cBtn(menu.button_list[10])  # 点击按钮新增
        '''输入按钮英文名称，表示位，按钮名称，图标'''
        menu.inputValue(menu.buttonAssigned_list[1],menu.valueList[0])
        menu.inputValue(menu.buttonAssigned_list[2], menu.valueList[0])
        menu.inputValue(menu.buttonAssigned_list[3], menu.valueList[1])
        menu.inputValue(menu.buttonAssigned_list[4], menu.valueList[1])
        menu.cBtn(menu.buttonAssigned_list[6])  # 点击提交按钮
        msg11 = menu.isElementExist(menu.buttonAssigned_list[27])#提示验证
        self.assertTrue(msg11, '出现提示信息')
        if msg11:
            msgInfo = menu.getValue(*menu.buttonAssigned_list[27])
            self.assertEqual(msgInfo, '不能为空', '提示信息正确')

    def testbuttonAssigned_12(self):
        '''正常输入点击提交按钮'''
        menu = rolePage(self.driver)  # 实例化角色管理页面
        self.login.loginFunc()  # 登录
        menu.inrolePage()  # 进入角色管理页面
        time.sleep(2)
        menu.cBtn(menu.updaterole_list[0])  # 选择一项
        menu.cBtn(menu.button_list[4])  # 点击按钮分配
        menu.cBtn(menu.button_list[13])
        menu.cBtn(menu.button_list[14])  # 选择节点
        menu.cBtn(menu.button_list[10])  # 点击按钮新增
        '''输入按钮英文名称，表示位，按钮名称，图标，描述'''
        menu.inputValue(menu.buttonAssigned_list[1],menu.valueList[0])
        menu.inputValue(menu.buttonAssigned_list[2], menu.valueList[0])
        menu.inputValue(menu.buttonAssigned_list[3], menu.valueList[1])
        menu.inputValue(menu.buttonAssigned_list[4], menu.valueList[1])
        menu.inputValue(menu.buttonAssigned_list[5], menu.valueList[0])
        menu.cBtn(menu.buttonAssigned_list[6])  # 点击提交按钮
        time.sleep(1)
        msg12 = menu.isElementExist(menu.updaterole_list[8])#提示验证
        self.assertTrue(msg12, '新增成功！')

    def testbuttonAssigned_13(self):
        '''点击修改按钮'''
        menu = rolePage(self.driver)  # 实例化角色管理页面
        self.login.loginFunc()  # 登录
        menu.inrolePage()  # 进入角色管理页面
        time.sleep(2)
        menu.cBtn(menu.updaterole_list[0])  # 选择一项
        menu.cBtn(menu.button_list[4])  # 点击按钮分配
        menu.cBtn(menu.button_list[11])#点击按钮修改
        time.sleep(1)
        msg13 = menu.isElementExist(menu.updaterole_list[8])
        self.assertTrue(msg13,'请选中一项内容！')

    def testbuttonAssigned_14(self):
        '''选中多项点击修改按钮'''
        menu = rolePage(self.driver)  # 实例化角色管理页面
        self.login.loginFunc()  # 登录
        menu.inrolePage()  # 进入角色管理页面
        time.sleep(2)
        menu.cBtn(menu.updaterole_list[0])  # 选择一项
        menu.cBtn(menu.button_list[4])  # 点击按钮分配
        menu.cBtn(menu.button_list[13])
        menu.cBtn(menu.button_list[14])  # 选择节点
        menu.cBtn(menu.buttonAssigned_list[10])#选中多项
        menu.cBtn(menu.button_list[11])#点击按钮修改
        msg14 = menu.isElementExist(menu.updaterole_list[8])
        self.assertTrue(msg14,'请选中一项内容进行操作！')

    def testbuttonAssigned_15(self):
        '''选中一项点击修改按钮'''
        menu = rolePage(self.driver)  # 实例化角色管理页面
        self.login.loginFunc()  # 登录
        menu.inrolePage()  # 进入角色管理页面
        time.sleep(2)
        menu.cBtn(menu.updaterole_list[0])  # 选择一项
        menu.cBtn(menu.button_list[4])  # 点击按钮分配
        menu.cBtn(menu.button_list[13])
        menu.cBtn(menu.button_list[14])  # 选择节点
        menu.cBtn(menu.buttonAssigned_list[9])#选中一项
        menu.cBtn(menu.button_list[11])#点击按钮修改
        msg15 = menu.isElementExist(menu.buttonAssigned_list[18])
        self.assertTrue(msg15,'弹出修改按钮窗口')#验证

    def testbuttonAssigned_16(self):
        '''修改清空按钮必填项点击提交验证'''
        menu = rolePage(self.driver)  # 实例化角色管理页面
        self.login.loginFunc()  # 登录
        menu.inrolePage()  # 进入角色管理页面
        time.sleep(2)
        menu.cBtn(menu.updaterole_list[0])  # 选择一项
        menu.cBtn(menu.button_list[4])  # 点击按钮分配
        menu.cBtn(menu.button_list[13])
        menu.cBtn(menu.button_list[14])  # 选择节点
        menu.cBtn(menu.buttonAssigned_list[9])#选中一项
        menu.cBtn(menu.button_list[11])#点击按钮修改
        '''清空必填项'''
        menu.clearValue(menu.buttonAssigned_list[11])
        menu.clearValue(menu.buttonAssigned_list[12])
        menu.clearValue(menu.buttonAssigned_list[13])
        menu.clearValue(menu.buttonAssigned_list[14])
        menu.clearValue(menu.buttonAssigned_list[15])
        menu.cBtn(menu.buttonAssigned_list[16])#点击提交
        '''提示验证'''
        msg16_1 = menu.isElementExist(menu.buttonAssigned_list[28])
        self.assertTrue(msg16_1, '出现提示信息')
        if msg16_1:
            msgInfo1 = menu.getValue(*menu.buttonAssigned_list[28])
            self.assertEqual(msgInfo1, '不能为空', '提示信息正确')
        msg16_2 = menu.isElementExist(menu.buttonAssigned_list[29])
        self.assertTrue(msg16_2, '出现提示信息')
        if msg16_2:
            msgInfo2 = menu.getValue(*menu.buttonAssigned_list[29])
            self.assertEqual(msgInfo2, '不能为空', '提示信息正确')
        msg16_3 = menu.isElementExist(menu.buttonAssigned_list[30])
        self.assertTrue(msg16_3, '出现提示信息')
        if msg16_3:
            msgInfo3 = menu.getValue(*menu.buttonAssigned_list[30])
            self.assertEqual(msgInfo3, '不能为空', '提示信息正确')
        msg16_4 = menu.isElementExist(menu.buttonAssigned_list[31])
        self.assertTrue(msg16_4, '出现提示信息')
        if msg16_4:
            msgInfo4 = menu.getValue(*menu.buttonAssigned_list[31])
            self.assertEqual(msgInfo4, '不能为空', '提示信息正确')
        msg16_5 = menu.isElementExist(menu.buttonAssigned_list[32])
        self.assertTrue(msg16_5, '出现提示信息')
        if msg16_5:
            msgInfo5 = menu.getValue(*menu.buttonAssigned_list[32])
            self.assertEqual(msgInfo5, '不能为空', '提示信息正确')

    def testbuttonAssigned_17(self):
        '''修改必填项点击提交验证'''
        menu = rolePage(self.driver)  # 实例化角色管理页面
        self.login.loginFunc()  # 登录
        menu.inrolePage()  # 进入角色管理页面
        time.sleep(2)
        menu.cBtn(menu.updaterole_list[0])  # 选择一项
        menu.cBtn(menu.button_list[4])  # 点击按钮分配
        menu.cBtn(menu.button_list[13])
        menu.cBtn(menu.button_list[14])  # 选择节点
        menu.cBtn(menu.buttonAssigned_list[9])#选中一项
        menu.cBtn(menu.button_list[11])#点击按钮修改
        '''修改必填项'''
        menu.inputValue(menu.buttonAssigned_list[11],menu.valueList[0])
        menu.inputValue(menu.buttonAssigned_list[12], menu.valueList[0])
        menu.inputValue(menu.buttonAssigned_list[13], menu.valueList[1])
        menu.inputValue(menu.buttonAssigned_list[14], menu.valueList[1])
        menu.inputValue(menu.buttonAssigned_list[15], menu.valueList[0])
        menu.cBtn(menu.buttonAssigned_list[16])#点击提交
        msg17 = menu.isElementExist(menu.updaterole_list[8])
        self.assertTrue(msg17,'修改成功！')

    def testbuttonAssigned_18(self):
        '''点击删除按钮'''
        menu = rolePage(self.driver)  # 实例化角色管理页面
        self.login.loginFunc()  # 登录
        menu.inrolePage()  # 进入角色管理页面
        time.sleep(2)
        menu.cBtn(menu.updaterole_list[0])  # 选择一项
        menu.cBtn(menu.button_list[4])  # 点击按钮分配
        menu.cBtn(menu.button_list[12]) #d点击删除按钮
        msg18 = menu.isElementExist(menu.updaterole_list[8])
        self.assertTrue(msg18,'请选中一项内容！')

    def testbuttonAssigned_19(self):
        '''选中删除项点击删除按钮'''
        menu = rolePage(self.driver)  # 实例化角色管理页面
        self.login.loginFunc()  # 登录
        menu.inrolePage()  # 进入角色管理页面
        time.sleep(2)
        menu.cBtn(menu.updaterole_list[0])  # 选择一项
        menu.cBtn(menu.button_list[4])  # 点击按钮分配
        menu.cBtn(menu.button_list[13])
        menu.cBtn(menu.button_list[14])  # 选择节点
        menu.cBtn(menu.buttonAssigned_list[22])#选中一项
        menu.cBtn(menu.button_list[12])#点击按钮删除
        msg19 = menu.isElementExist(menu.buttonAssigned_list[19])
        self.assertTrue(msg19,'弹出删除提示框')

    def testbuttonAssigned_20(self):
        '''删除按钮'''
        menu = rolePage(self.driver)  # 实例化角色管理页面
        self.login.loginFunc()  # 登录
        menu.inrolePage()  # 进入角色管理页面
        time.sleep(2)
        menu.cBtn(menu.updaterole_list[0])  # 选择一项
        menu.cBtn(menu.button_list[4])  # 点击按钮分配
        menu.cBtn(menu.button_list[13])
        menu.cBtn(menu.button_list[14])  # 选择节点
        menu.cBtn(menu.buttonAssigned_list[22])#选中一项
        menu.cBtn(menu.button_list[12])#点击按钮删除
        menu.cBtn(menu.buttonAssigned_list[20])#点击确定按钮
        msg20 = menu.isElementExist(menu.updaterole_list[8])
        self.assertTrue(msg20, '删除成功！')

    def testbuttonAssigned_21(self):
        '''关闭按钮'''
        menu = rolePage(self.driver)  # 实例化角色管理页面
        self.login.loginFunc()  # 登录
        menu.inrolePage()  # 进入角色管理页面
        time.sleep(2)
        menu.cBtn(menu.updaterole_list[0])  # 选择一项
        menu.cBtn(menu.button_list[4])  # 点击按钮分配
        menu.cBtn(menu.button_list[8])#点击关闭按钮
        msg21 = menu.isElementExist(menu.buttonAssigned_list[0])
        self.assertFalse(msg21, '关闭窗口')

if __name__ == '__main__':
    pass






