'''
Code description:paydetailedquery_page
Create time
Developer:
'''
import time
import sys
import logging
from selenium.webdriver.common.by import By
from framfriend.test_case.models.log import Logger
from framfriend.test_case.page_obj.base_page import BasePage,eleData
log = Logger(__name__,CmdLevel=logging.INFO,FileLevel=logging.INFO)

class PayDetailedQuery_Page(BasePage):
        '''
        代付明细查询
        '''
        # 银农直联系统
        Silverfarmers = (By.XPATH, eleData.readExcel(14, 3))
        # 银农直联列表
        SilverFarmersul = (By.XPATH, '//*[@id="sidebarTree_23_ul"]')
        # 代付功能
        pay = (By.XPATH, '//*[@id="sidebarTree_32"]')
        # 代付功能列表
        payul = (By.XPATH, '//*[@id="sidebarTree_32_ul"]')
        # 代付结果查询
        paymentquery = (By.XPATH, eleData.readExcel(231, 3))
        # 代付结果查询页面
        parmentquery_page = (By.XPATH, eleData.readExcel(272, 3))

        #点击
        button_list = \
                    [(By.XPATH, eleData.readExcel(787, 3)),#己方银行0
                     (By.XPATH, eleData.readExcel(788, 3)),#己方银行一项1
                     (By.XPATH, eleData.readExcel(789, 3))]#查询2
        input_list = \
                    [(By.XPATH, eleData.readExcel(790, 3)),  #收款账号0
                     (By.XPATH, eleData.readExcel(791, 3)),  # 收款人1
                     (By.XPATH, eleData.readExcel(792, 3))]  # 摘要2
        msg_list = \
                    [(By.XPATH, eleData.readExcel(793, 3)),#存在查询
                     (By.XPATH, eleData.readExcel(794, 3))]#不存在查询
        #测试数据
        valuelist = ['测试', '98032230389911653019', '黄岛一', '6215210200005034', '沂南县蒲汪镇大王庄村股份经济合作社',
                     '35170550687795445677']
        # 断言数据
        assertlist = ['显示第 1 到第 0 条记录，总共 0 条记录']


        def inpaydetailedquery(self):
            '''
            进入代付结果查询页面
            :return:
            '''
            leftMenu = self.findElement(*self.menuList[0])  # 左侧菜单栏
            leftMenu.find_element_by_id('sidebarTree_23_a').click()  # 点击银农直联
            time.sleep(1)
            Silverfarmersul = self.findElement(*self.SilverFarmersul)
            Silverfarmersul.find_element_by_xpath('//*[@id="sidebarTree_32"]').click()
            time.sleep(1)
            detailedul = self.findElement(*self.payul)
            detailedul.find_element_by_id('sidebarTree_35').click()  # 点击代付明细查询
            time.sleep(1)
            log.logger.info('page[%s]:found the menu [%s]and [%s]' % (
                sys._getframe().f_code.co_name, self.menuList[0], self.payul))


if __name__ == '__main__':
    pass
