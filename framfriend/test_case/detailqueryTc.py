'''
Code description：银行流水查询模块 testcase
Create time：
Developer：
'''
import os
import time
from framfriend.test_case.models.myunittest import MyunitTest
from framfriend.test_case.page_obj.detailquery_page import DetailQuery_Page

class DetailQuery_Tc(MyunitTest):
    '''银行流水查询模块用例'''

    def test_query_1(self):
        """点击查询按钮"""
        menu = DetailQuery_Page(self.driver)  # 实例化综合模块页面
        self.login.loginFunc()  # 登录
        menu.indetailQuery()  # 进入综合模块页面
        time.sleep(3)
        menu.cBtn(menu.button_list[2])#点击查询
        time.sleep(1)
        flag = menu.isElementExist(menu.msg[0])
        self.assertTrue(flag,'弹出提示信息')
        if flag:
            msgInfo = menu.getValue(*menu.msg[0])
            self.assertEqual(msgInfo, '×\n提示! 请选择截止时间', '提示信息正确')

    def test_query_2(self):
        '''开始时间，结束时间查询'''
        menu = DetailQuery_Page(self.driver)  # 实例化综合模块页面
        self.login.loginFunc()  # 登录
        menu.indetailQuery()  # 进入综合模块页面
        time.sleep(3)
        menu.cBtn(menu.button_list[2])  # 点击查询
        time.sleep(1)
        flag = menu.isElementExist(menu.msg[0])
        self.assertTrue(flag, '弹出提示信息')

    def test_query_3(self):
        '''验证选择银行'''
        menu = DetailQuery_Page(self.driver)  # 实例化综合模块页面
        self.login.loginFunc()  # 登录
        menu.indetailQuery()  # 进入综合模块页面
        time.sleep(3)
        menu.cBtn(menu.button_list[0])
        menu.cBtn(menu.button_list[1])#选择银行
        time.sleep(1)
        msg = menu.getValue(*menu.button_list[0])
        self.assertEqual(msg, '沂南县蒲汪镇经管统计站\n ', '提示信息正确')

    def test_query_4(self):
        '''验证点击打印'''
        menu = DetailQuery_Page(self.driver)  # 实例化综合模块页面
        self.login.loginFunc()  # 登录
        menu.indetailQuery()  # 进入综合模块页面
        time.sleep(3)
        menu.cBtn(menu.button_list[3])
        time.sleep(1)
        # flag = menu.isElementExist(menu.msg[1])
        # self.assertTrue(flag,'弹出打印页面')

    def test_export(self):
        '''点击导出验证'''
        menu = DetailQuery_Page(self.driver)  # 实例化综合模块页面
        self.login.loginFunc()  # 登录
        menu.indetailQuery()  # 进入综合模块页面
        time.sleep(3)
        menu.cBtn(menu.button_list[4])  # 点击导出模板
        time.sleep(5)
        assert (os.path.exists('F:\TestDownloads\\交易明细表.xlsx'))  # 检查是否已下载

if __name__ == '__main__':
    pass
