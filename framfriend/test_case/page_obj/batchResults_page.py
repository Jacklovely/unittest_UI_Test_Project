'''
Code description： BatchResults_Page
Create time：
Developer：
'''
import time
import sys
import logging
from selenium.webdriver.common.by import By
from framfriend.test_case.models.log import Logger
from framfriend.test_case.page_obj.base_page import BasePage, eleData

log = Logger(__name__, CmdLevel=logging.INFO, FileLevel=logging.INFO)

class BatchResults_Page(BasePage):
    '''
    批量转账查询
    '''
    # 银农直联系统
    Silverfarmers = (By.XPATH, eleData.readExcel(14, 3))
    # 银农直联列表
    Silverfarmersul = (By.XPATH, '//*[@id="sidebarTree_23_ul"]')
    # 转账功能
    pay = (By.XPATH, '//*[@id="sidebarTree_24"]')
    # 转账功能列表
    payul = (By.XPATH, '//*[@id="sidebarTree_24_ul"]')
    # 批量转账查询
    batchResults = (By.XPATH, eleData.readExcel(229, 3))
    # 批量转账查询页面
    batchResultspage = (By.XPATH, eleData.readExcel(342, 3))

    #点击元素
    button_list = \
        [(By.XPATH, eleData.readExcel(368, 3)),  #查询日期始0
         (By.XPATH, eleData.readExcel(369, 3)),  #查询日期止1
         (By.ID, eleData.readExcel(370, 3)),  #查询2
         (By.ID, eleData.readExcel(371, 3)),  #查看详情3
         (By.XPATH, eleData.readExcel(350, 3)),  # 切换年4
         (By.XPATH, eleData.readExcel(351, 3)),  # 切换月5
         (By.XPATH, eleData.readExcel(352, 3)),  # 选择日6
         (By.XPATH, eleData.readExcel(353, 3)),  # 确定7
         (By.XPATH, eleData.readExcel(354, 3)),  # 现在8
         (By.XPATH, eleData.readExcel(355, 3)),  # 清空9
         (By.XPATH, '//*[@id="closeSqlConfig"]')]  #详情关闭10
    #验证
    msg_list = \
         [(By.XPATH, eleData.readExcel(372, 3)),#查询验证0
          (By.XPATH, eleData.readExcel(373, 3)),#右上角验证1
          (By.XPATH, eleData.readExcel(374, 3))]#详情窗口验证2
    #选框
    checkbox = \
        [(By.XPATH, eleData.readExcel(375, 3)),#单选
         (By.XPATH, eleData.readExcel(376, 3))]#全选

    def inbatchResults(self):
        '''
        进入批量转账查询页面
        :return:
        '''
        leftMenu = self.findElement(*self.menuList[0])  # 左侧菜单栏
        leftMenu.find_element_by_id('sidebarTree_23_a').click()  # 点击银农直联系统
        time.sleep(1)
        Silverfarmersul = self.findElement(*self.Silverfarmersul)
        Silverfarmersul.find_element_by_xpath('//*[@id="sidebarTree_24_a"]').click()  # 点击转账功能
        time.sleep(1)
        payul = self.findElement(*self.payul)
        payul.find_element_by_id('sidebarTree_28').click()  # 点击批量转账查询
        time.sleep(1)
        log.logger.info('page[%s] :found the menu [%s] and [%s]' % (
            sys._getframe().f_code.co_name, self.menuList[0], self.payul))

if __name__=='__main__':
    pass