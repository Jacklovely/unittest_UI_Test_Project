'''
Code description: 代付结果查询 testcase
Create time :
Developer:
'''
import  os
import time
from selenium.webdriver.support.select import Select
from framfriend.test_case.models.myunit import MyunitTest
from framfriend.test_case.page_obj.paymentquery_page import PaymentQuery_page

class PaymentQuery_TC(MyunitTest):
    '''代付结果查询'''
    def test_paymentquery_1(self):
        '''己方银行查询'''
        menu = PaymentQuery_page(self.driver)#实例化代付结果查询页面
        self.login.loginFunc()#登录
        menu.inparmentquery()#进入代付结果查询页面
        time.sleep(2)
        menu.cBtn(menu.button_list[0])
        menu.cBtn(menu.button_list[1])
        menu.cBtn(menu.button_list[2])#点击查询按钮
        msgInfo = menu.getValue(*menu.msg_list[0])
        self.assertIn(menu.valuelist[5],msgInfo,'提示信息正确')

    def test_paymentquery_2(self):
        '''代付类型查询'''
        menu = PaymentQuery_page(self.driver)#实例化代付结果查询页面
        self.login.loginFunc()#登录
        menu.inparmentquery()#进入代付结果查询页面
        time.sleep(2)
        stype = self.driver.find_element_by_xpath('//*[@id="searchForm"]/div[2]/select')
        Select(stype).select_by_value('0')
        menu.cBtn(menu.button_list[2])#点击查询按钮
        msgInfo = menu.getValue(*menu.msg_list[0])
        self.assertIn(menu.valuelist[5],msgInfo,'提示信息正确')

    def test_paymentquery_3(self):
        '''摘要查询'''
        menu = PaymentQuery_page(self.driver)#实例化代付结果查询页面
        self.login.loginFunc()#登录
        menu.inparmentquery()#进入代付结果查询页面
        time.sleep(2)
        menu.inputValue(menu.input_list[0],menu.valuelist[0])
        menu.cBtn(menu.button_list[2])#点击查询按钮
        msgInfo = menu.getValue(*menu.msg_list[0])
        self.assertIn(menu.valuelist[0],msgInfo,'提示信息正确')

    def test_paymentquery_4(self):
        '''摘要不存在查询'''
        menu = PaymentQuery_page(self.driver)#实例化代付结果查询页面
        self.login.loginFunc()#登录
        menu.inparmentquery()#进入代付结果查询页面
        time.sleep(2)
        menu.inputValue(menu.input_list[0],menu.valuelist[1])
        menu.cBtn(menu.button_list[2])#点击查询按钮
        time.sleep(2)
        msgInfo = menu.getValue(*menu.msg_list[3])
        self.assertIn(menu.assertlist[0],msgInfo,'提示信息正确')

    def test_paymentquery_5(self):
        '''点击详情'''
        menu = PaymentQuery_page(self.driver)#实例化代付结果查询页面
        self.login.loginFunc()#登录
        menu.inparmentquery()#进入代付结果查询页面
        time.sleep(2)
        menu.cBtn(menu.button_list[3])#点击详情按钮
        msgInfo = menu.isElementExist(menu.msg_list[1])
        self.assertTrue(msgInfo,'弹出详情窗口')

    def test_paymentquery_6(self):
        '''点击打印'''
        menu = PaymentQuery_page(self.driver)#实例化代付结果查询页面
        self.login.loginFunc()#登录
        menu.inparmentquery()#进入代付结果查询页面
        time.sleep(2)
        menu.cBtn(menu.button_list[4])#点击打印按钮

    def test_paymentquery_7(self):
        '''详情收款账号错误查询'''
        menu = PaymentQuery_page(self.driver)#实例化代付结果查询页面
        self.login.loginFunc()#登录
        menu.inparmentquery()#进入代付结果查询页面
        time.sleep(2)
        menu.cBtn(menu.button_list[3])#点击详情按钮
        time.sleep(2)
        menu.inputValue((menu.input_list[1]),menu.valuelist[1])
        menu.cBtn((menu.button_list[5]))
        time.sleep(1)
        msgInfo = menu.getValue(*menu.msg_list[4])
        self.assertIn(menu.assertlist[0],msgInfo,'提示信息正确')

    def test_paymentquery_8(self):
        '''详情收款账号正确查询'''
        menu = PaymentQuery_page(self.driver)#实例化代付结果查询页面
        self.login.loginFunc()#登录
        menu.inparmentquery()#进入代付结果查询页面
        time.sleep(2)
        menu.cBtn(menu.button_list[3])#点击详情按钮
        time.sleep(2)
        menu.inputValue((menu.input_list[1]),menu.valuelist[3])
        menu.cBtn((menu.button_list[5]))
        time.sleep(1)
        msgInfo = menu.getValue(*menu.msg_list[2])
        self.assertIn(menu.valuelist[3],msgInfo,'提示信息正确')

    def test_paymentquery_9(self):
        '''详情收款人错误查询'''
        menu = PaymentQuery_page(self.driver)#实例化代付结果查询页面
        self.login.loginFunc()#登录
        menu.inparmentquery()#进入代付结果查询页面
        time.sleep(2)
        menu.cBtn(menu.button_list[3])#点击详情按钮
        time.sleep(2)
        menu.inputValue((menu.input_list[2]),menu.valuelist[1])
        menu.cBtn((menu.button_list[5]))
        time.sleep(1)
        msgInfo = menu.getValue(*menu.msg_list[4])
        self.assertIn(menu.assertlist[0],msgInfo,'提示信息正确')

    def test_paymentquery_10(self):
        '''详情收款人正确查询'''
        menu = PaymentQuery_page(self.driver)#实例化代付结果查询页面
        self.login.loginFunc()#登录
        menu.inparmentquery()#进入代付结果查询页面
        time.sleep(2)
        menu.cBtn(menu.button_list[3])#点击详情按钮
        time.sleep(2)
        menu.inputValue((menu.input_list[2]),menu.valuelist[2])
        menu.cBtn((menu.button_list[5]))
        time.sleep(1)
        msgInfo = menu.getValue(*menu.msg_list[2])
        self.assertIn(menu.valuelist[2],msgInfo,'提示信息正确')

    def test_paymentquery_11(self):
        '''详情摘要错误查询'''
        menu = PaymentQuery_page(self.driver)#实例化代付结果查询页面
        self.login.loginFunc()#登录
        menu.inparmentquery()#进入代付结果查询页面
        time.sleep(2)
        menu.cBtn(menu.button_list[3])#点击详情按钮
        time.sleep(2)
        menu.inputValue((menu.input_list[3]),menu.valuelist[2])
        menu.cBtn((menu.button_list[5]))
        time.sleep(1)
        msgInfo = menu.getValue(*menu.msg_list[4])
        self.assertIn(menu.assertlist[0],msgInfo,'提示信息正确')

    def test_paymentquery_12(self):
        '''详情摘要正确查询'''
        menu = PaymentQuery_page(self.driver)#实例化代付结果查询页面
        self.login.loginFunc()#登录
        menu.inparmentquery()#进入代付结果查询页面
        time.sleep(2)
        menu.cBtn(menu.button_list[3])#点击详情按钮
        time.sleep(2)
        menu.inputValue((menu.input_list[3]),menu.valuelist[0])
        menu.cBtn((menu.button_list[5]))
        time.sleep(1)
        msgInfo = menu.getValue(*menu.msg_list[2])
        self.assertIn(menu.valuelist[0],msgInfo,'提示信息正确')

    def test_paymentquery_13(self):
        '''详情内打印'''
        menu = PaymentQuery_page(self.driver)#实例化代付结果查询页面
        self.login.loginFunc()#登录
        menu.inparmentquery()#进入代付结果查询页面
        time.sleep(2)
        menu.cBtn(menu.button_list[3])#点击详情按钮
        time.sleep(2)
        menu.cBtn((menu.button_list[6]))

    def test_paymentquery_14(self):
        '''详情内取消'''
        menu = PaymentQuery_page(self.driver)#实例化代付结果查询页面
        self.login.loginFunc()#登录
        menu.inparmentquery()#进入代付结果查询页面
        time.sleep(2)
        menu.cBtn(menu.button_list[3])#点击详情按钮
        time.sleep(2)
        menu.cBtn((menu.button_list[7]))
        time.sleep(2)
        msgInfo = menu.isElementExist(menu.msg_list[1])
        self.assertFalse(msgInfo,'弹出详情窗口')


if __name__ == '__main__':
    pass