'''
Code description：年限分析模块 testcase
Create time：
Developer：
'''
import time
from framfriend.test_case.models.myunit import MyunitTest
from framfriend.test_case.page_obj.analysis_page import analysis_page

class analysis_Tc(MyunitTest):
    '''年限分析模块用例'''
    def test_contract_query_1(self):
        '''查询'''
        menu = analysis_page(self.driver)  # 实例化年限分析页面
        self.login.loginFunc()  # 登录
        menu.inanalysispage()  # 进入年限分析页面
        time.sleep(2)
        menu.cBtn(menu.button_list[0])
        menu.cBtn(menu.time_list[0])
        menu.cBtn(menu.time_list[1])
        for i in range(5):
            menu.cBtn(menu.time_list[2])
        menu.cBtn(menu.time_list[3])
        menu.cBtn(menu.time_list[4])
        menu.cBtn(menu.button_list[1])
        time.sleep(1)
        msgInfo = menu.getValue(*menu.msg_list[0])
        self.assertEqual(msgInfo,'显示第 1 到第 10 条记录，总共 67 条记录','查询成功')

    def test_click_detail_1(self):
        '''点击明细'''
        menu = analysis_page(self.driver)  # 实例化年限分析页面
        self.login.loginFunc()  # 登录
        menu.inanalysispage()  # 进入年限分析页面
        time.sleep(2)
        menu.cBtn(menu.button_list[0])
        menu.cBtn(menu.button_list[2])
        time.sleep(1)
        msgInfo = menu.getValue(*menu.msg_list[1])
        self.assertEqual(msgInfo, '×\n提示! 请选择一项查看','提示信息正确')

    def test_click_detail_2(self):
        '''全选点击明细'''
        menu = analysis_page(self.driver)  # 实例化年限分析页面
        self.login.loginFunc()  # 登录
        menu.inanalysispage()  # 进入年限分析页面
        time.sleep(2)
        menu.cBtn(menu.button_list[0])
        menu.cBtn(menu.checkbox[0])
        menu.cBtn(menu.button_list[2])
        time.sleep(1)
        msgInfo = menu.getValue(*menu.msg_list[1])
        self.assertEqual(msgInfo, '×\n提示! 请选择一项查看','提示信息正确')

    def test_click_detail_3(self):
        '''选择一项点击明细'''
        menu = analysis_page(self.driver)  # 实例化年限分析页面
        self.login.loginFunc()  # 登录
        menu.inanalysispage()  # 进入年限分析页面
        time.sleep(2)
        menu.cBtn(menu.button_list[0])
        menu.cBtn(menu.checkbox[1])
        menu.cBtn(menu.button_list[2])
        time.sleep(1)
        msg = menu.isElementExist(menu.msg_list[2])
        self.assertTrue(msg,'弹出明细窗口')

if __name__=='__main__':
    pass


