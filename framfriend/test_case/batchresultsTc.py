'''
Code description：批量转账查询模块 testcase
Create time：
Developer：
'''
import os
import time
from framfriend.test_case.models.myunit import MyunitTest
from framfriend.test_case.page_obj.batchResults_page import BatchResults_Page

class BatchResult_Tc(MyunitTest):
    '''批量转账查询模块用例'''

    def test_query_1(self):
        """验证查询功能"""
        menu = BatchResults_Page(self.driver)  # 实例化批量转账查询页面
        self.login.loginFunc()  # 登录
        menu.inbatchResults()  # 进入批量转账查询页面
        time.sleep(3)
        '''选择时间'''
        menu.cBtn(menu.button_list[0])#选择开始
        #menu.cBtn(menu.button_list[4])#切换年
        menu.cBtn(menu.button_list[5])#切换月
        menu.cBtn(menu.button_list[6])#选择日
        #time.sleep(3)
        menu.cBtn(menu.button_list[7])  # 确定
        time.sleep(2)
        menu.cBtn(menu.button_list[1])#选择截止
        menu.cBtn(menu.button_list[8])  # 现在
        # menu.cBtn(menu.button_list[5])#切换月
        # menu.cBtn(menu.button_list[6])#选择日
        # time.sleep(2)
        # menu.cBtn(menu.button_list[7])#确定
        # # menu.cBtn(menu.button_list[1])  # 选择截止
        # # menu.cBtn(menu.button_list[6])  # 选择日
        # # menu.cBtn(menu.button_list[7])  # 确定
        time.sleep(2)
        menu.cBtn(menu.button_list[2])#点击查询按钮
        time.sleep(1)
        msgInfo = menu.getValue(*menu.msg_list[0])
        self.assertEqual(msgInfo, '显示第 1 到第 1 条记录，总共 1 条记录', '提示信息正确')

    def test_details_1(self):
        """验证点击详情功能"""
        menu = BatchResults_Page(self.driver)  # 实例化批量转账查询页面
        self.login.loginFunc()  # 登录
        menu.inbatchResults()  # 进入批量转账查询页面
        time.sleep(2)
        menu.cBtn(menu.button_list[3])#点击查看详情
        time.sleep(1)
        flag = menu.isElementExist(menu.msg_list[1])
        self.assertTrue(flag,'弹出提示信息')
        if flag:
            msgInfo = menu.getValue(*menu.msg_list[1])
            self.assertEqual(msgInfo,'×\n提示! 请选中一项内容！', '提示信息正确')

    def test_details_2(self):
        """全选点击详情功能验证"""
        menu = BatchResults_Page(self.driver)  # 实例化批量转账查询页面
        self.login.loginFunc()  # 登录
        menu.inbatchResults()  # 进入批量转账查询页面
        time.sleep(2)
        menu.cBtn(menu.checkbox[1])#全选
        menu.cBtn(menu.button_list[3])#点击查看详情
        time.sleep(1)
        flag = menu.isElementExist(menu.msg_list[1])
        self.assertTrue(flag,'弹出提示信息')
        if flag:
            msgInfo = menu.getValue(*menu.msg_list[1])
            self.assertEqual(msgInfo,'×\n提示! 请选中一项内容进行操作！', '提示信息正确')

    def test_details_3(self):
        """全选点击详情功能验证"""
        menu = BatchResults_Page(self.driver)  # 实例化批量转账查询页面
        self.login.loginFunc()  # 登录
        menu.inbatchResults()  # 进入批量转账查询页面
        time.sleep(2)
        menu.cBtn(menu.checkbox[0])#单选
        menu.cBtn(menu.button_list[3])  # 点击查看详情
        time.sleep(1)
        flag = menu.isElementExist(menu.msg_list[2])
        self.assertTrue(flag, '弹出详情窗口')

    def test_details_4(self):
        """详情关闭验证"""
        menu = BatchResults_Page(self.driver)  # 实例化批量转账查询页面
        self.login.loginFunc()  # 登录
        menu.inbatchResults()  # 进入批量转账查询页面
        time.sleep(2)
        menu.cBtn(menu.checkbox[0])#单选
        menu.cBtn(menu.button_list[3])  # 点击查看详情
        menu.cBtn(menu.button_list[10])#点击关闭按钮
        time.sleep(1)
        flag = menu.isElementExist(menu.msg_list[2])
        self.assertFalse(flag, '关闭详情窗口')

if __name__=='__main__':
    pass