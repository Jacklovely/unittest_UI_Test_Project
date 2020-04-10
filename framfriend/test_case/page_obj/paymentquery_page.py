'''
Code description： parmentquery_page
Create time；
Developer
'''
import time
import sys
import logging
from  selenium.webdriver.common.by import By
from framfriend.test_case.models.log import Logger
from framfriend.test_case.page_obj.base_page import BasePage,eleData
log =Logger(__name__,CmdLevel=logging.INFO,FileLevel=logging.INFO)

class PaymentQuery_page(BasePage):
        '''
        代付结果查询
        '''
        #银农直联系统
        Silverfarmers = (By.XPATH,eleData.readExcel(14,3))
        #银农直联列表
        SilverFarmersul = (By.XPATH,'//*[@id="sidebarTree_23_ul"]')
        #代付功能
        pay = (By.XPATH,'//*[@id="sidebarTree_32"]')
        #代付功能列表
        payul = (By.XPATH,'//*[@id="sidebarTree_32_ul"]')
        #代付结果查询
        paymentquery = (By.XPATH,eleData.readExcel(231,3))
        #代付结果查询页面
        parmentquery_page =(By.XPATH,eleData.readExcel(272,3))

        #点击
        button_list = \
                    [(By.XPATH, eleData.readExcel(770,3)),#己方银行0
                     (By.XPATH, eleData.readExcel(771,3)),#己方银行选项1
                     (By.XPATH, eleData.readExcel(772,3)),#查询2
                     (By.XPATH, eleData.readExcel(773, 3)),#详情3
                     (By.XPATH, eleData.readExcel(774, 3)),#打印4
                     (By.XPATH, eleData.readExcel(775, 3)),#详情内查询5
                     (By.XPATH, eleData.readExcel(776, 3)),#详情内打印6
                     (By.XPATH, eleData.readExcel(777, 3))]#详情内取消7
        input_list = \
                    [(By.XPATH, eleData.readExcel(778, 3)),#摘要0
                     (By.XPATH, eleData.readExcel(779, 3)),#详情内收款账号1
                     (By.XPATH, eleData.readExcel(780, 3)),#详情内收款人2
                     (By.XPATH, eleData.readExcel(781, 3))]#详情内摘要3
        msg_list = \
                    [(By.XPATH, eleData.readExcel(782, 3)),#查询0
                     (By.XPATH, eleData.readExcel(783, 3)),#详情1
                     (By.XPATH, eleData.readExcel(784, 3)),#详情内查询2
                     (By.XPATH, eleData.readExcel(785, 3)),#不存在查询3
                     (By.XPATH, eleData.readExcel(786, 3))]#详情不存在查询4
        #测试数据
        valuelist = ['测试','98032230389911653019','黄岛一','6215210200005034','沂南县蒲汪镇大王庄村股份经济合作社','35170550687795445677']
        #断言数据
        assertlist = ['显示第 1 到第 0 条记录，总共 0 条记录']
        def inparmentquery(self):
            '''
            进入代付结果查询页面
            :return:
            '''
            leftMenu = self.findElement(*self.menuList[0])#左侧菜单栏
            leftMenu.find_element_by_id('sidebarTree_23_a').click()#点击银农直联
            time.sleep(1)
            Silverfarmersul = self.findElement(*self.SilverFarmersul)
            Silverfarmersul.find_element_by_xpath('//*[@id="sidebarTree_32"]').click()
            time.sleep(1)
            paymentul = self.findElement(*self.payul)
            paymentul.find_element_by_id('sidebarTree_34').click()#点击代付结果查询
            time.sleep(1)
            log.logger.info('page[%s]:found the menu [%s]and [%s]'%(
                        sys._getframe().f_code.co_name,self.menuList[0],self.payul))

if __name__ == '__main__':
    pass



