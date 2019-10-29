'''
Code description：机构管理模块 testcase
Create time：
Developer：
'''

import time
from framfriend.test_case.models.myunit import MyunitTest
from framfriend.test_case.page_obj.jg_page import jg

class jg_TC(MyunitTest):
    """机构模块测试用例"""

    #直接点击新增
    def test_addjg_1(self):
        menu = jg(self.driver)# 实例化机构管理页面
        self.login.loginFunc()#登录
        menu.jgPage()#进入机构管理页面
        menu.cBtn(menu.addBtn)#点击新增
        msg = menu.isElementExist(menu.adderr)#提示新增
        self.assertTrue(msg,'弹出提示信息')
        if msg:
            msgInfo = menu.getValue(*menu.adderr)
            self.assertEqual(msgInfo,'×\n提示! 请先选中节点进行新增','提示信息正确')

    #直接点击修改
    def test_updatejg_2(self):
        menu = jg(self.driver)#实例化页面
        self.login.loginFunc()#登录
        menu.jgPage()#进入页面
        menu.cBtn(menu.updateBtn)#点击修改
        msg = menu.isElementExist(menu.updateerr)
        self.assertTrue(msg,'弹出提示信息')
        if msg:
            msgInfo = menu.getValue(*menu.updateerr)
            self.assertEqual(msgInfo,'×\n提示! 请先选中节点进行修改','提示信息正确')

    #直接点击删除
    def test_deletejg_3(self):
        menu = jg(self.driver)
        self.login.loginFunc()
        menu.jgPage()
        menu.cBtn(menu.deleteBtn)
        msg = menu.isElementExist(menu.deleteerr)
        self.assertTrue(msg,'弹出提示信息')
        if msg:
            msgInfo = menu.getValue(*menu.deleteerr)
            self.assertEqual(msgInfo, '×\n提示! 请先选中节点进行删除！', '提示信息正确')

    #点击所有机构
    def test_treeBtn_4(self):
        menu = jg(self.driver)
        self.login.loginFunc()
        menu.jgPage()
        menu.cBtn(menu.treeBtn)
        time.sleep(3)

    #为空新增
    def test_addnulljg_5(self):
        menu = jg(self.driver)
        self.login.loginFunc()
        menu.jgPage()
        menu.cBtn(menu.treeBtn)
        menu.cBtn(menu.addBtn)
        menu.cBtn(menu.addsubmitBtn)
        msg = menu.isElementExist(menu.msg)
        self.assertTrue(msg,'出现提示信息')
        if msg:
            msgInfo = menu.getValue(*menu.msg)
            self.assertEqual(msgInfo, '不能为空', '提示信息正确')

    #不为空新增
    def test_addjg1_6(self):
        menu = jg(self.driver)
        self.login.loginFunc()
        menu.jgPage()
        menu.cBtn(menu.treeBtn)
        menu.cBtn(menu.addBtn)
        time.sleep(2)
        menu.inputValue(menu.eleList[0], menu.reason)
        menu.cBtn(menu.addsubmitBtn)
        time.sleep(1)
        msg = menu.isElementExist(menu.addmsg)
        self.assertTrue(msg,'新增成功！')
        if msg:
            msgInfo = menu.getValue(*menu.addmsg)
            self.assertEqual(msgInfo, '×\n提示! 新增成功！', '提示信息正确')

    #修改为空提交
    def test_updatenull_7(self):
        menu = jg(self.driver)
        self.login.loginFunc()
        menu.jgPage()
        menu.cBtn(menu.tree)
        menu.cBtn(menu.updatedate)
        menu.cBtn(menu.updateBtn)
        time.sleep(2)
        menu.clearValue(menu.eleList[1])
        menu.cBtn(menu.updatesubmitBtn)
        time.sleep(1)
        msg = menu.isElementExist(menu.updatenullmsg)
        self.assertTrue(msg,'出现提示信息')
        if msg:
            msgInfo = menu.getValue(*menu.updatenullmsg)
            self.assertEqual(msgInfo, '不能为空', '提示信息正确')

     #修改机构名称
    def test_updatedata_8(self):
        menu = jg(self.driver)
        self.login.loginFunc()
        menu.jgPage()
        menu.cBtn(menu.tree)
        menu.cBtn(menu.updatedate)
        menu.cBtn(menu.updateBtn)
        time.sleep(2)
        menu.inputValue(menu.eleList[1], menu.reasonupdate)
        menu.cBtn(menu.updatesubmitBtn)
        time.sleep(1)
        msg = menu.isElementExist(menu.updatemsg)
        self.assertTrue(msg,'弹出提示信息')
        if msg:
            msgInfo = menu.getValue(*menu.updatemsg)
            self.assertEqual(msgInfo, '×\n提示! 修改成功！', '提示信息正确')

    #删除机构
    def test_deletedata_9(self):
        menu = jg(self.driver)
        self.login.loginFunc()
        menu.jgPage()
        menu.cBtn(menu.tree)
        menu.cBtn(menu.deletedate)
        menu.cBtn(menu.deleteBtn)
        time.sleep(2)
        menu.cBtn(menu.deletesubmitBtn)
        time.sleep(1)
        msg = menu.isElementExist(menu.deletemsg)
        self.assertTrue(msg,'弹出提示信息')
        if msg:
            msgInfo = menu.getValue(*menu.deletemsg)
            self.assertEqual(msgInfo, '×\n提示! 删除成功！', '提示信息正确')

if __name__ == '__main__':
    pass


