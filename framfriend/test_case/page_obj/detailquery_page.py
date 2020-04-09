'''
Code description： DetailQuery_Page
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

class DetailQuery_Page(BasePage):
    '''
    银行流水查询
    '''
    # 银农直联系统
    Silverfarmers = (By.XPATH, eleData.readExcel(14, 3))
    # 银农直联列表
    Silverfarmersul = (By.XPATH, '//*[@id="sidebarTree_23_ul"]')
    # 综合查询
    detailQuery = (By.XPATH, eleData.readExcel(232, 3))
    # 综合查询页面
    detailQuerypage = (By.XPATH, eleData.readExcel(342, 3))

    #点击元素
    button_list = \
        [(By.XPATH, eleData.readExcel(361, 3)),#打开选择银行0
         (By.XPATH, eleData.readExcel(362, 3)),#选择银行1
         (By.XPATH, eleData.readExcel(363, 3)),#查询2
         (By.XPATH, eleData.readExcel(364, 3)),#打印3
         (By.XPATH, eleData.readExcel(365, 3))]#导出4
    #验证
    msg = \
        [(By.XPATH, eleData.readExcel(366, 3)),#查询验证0
         (By.XPATH, eleData.readExcel(367, 3))]#打印验证1

    def indetailQuery(self):
        '''
        进入综合查询页面
        :return:
        '''
        leftMenu = self.findElement(*self.menuList[0])  # 左侧菜单栏
        leftMenu.find_element_by_id('sidebarTree_23_a').click()  # 点击银农直联系统
        time.sleep(1)
        Silverfarmersul = self.findElement(*self.Silverfarmersul)
        Silverfarmersul.find_element_by_xpath('//*[@id="sidebarTree_36_span"]').click()  # 点击综合查询
        time.sleep(1)
        log.logger.info('page[%s] :found the menu [%s] and [%s]' % (
            sys._getframe().f_code.co_name, self.menuList[0], self.Silverfarmersul))

if __name__=='__main__':
    pass