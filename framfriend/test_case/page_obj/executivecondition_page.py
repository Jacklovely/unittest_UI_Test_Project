'''
Code description： executivecondition_page
Create time：
Developer：
'''
import time
from selenium.webdriver.common.by import By
import logging
import sys

from selenium.webdriver.common.keys import Keys

from framfriend.test_case.page_obj.base_page import BasePage, eleData, queryData
from framfriend.test_case.models.log import Logger

log = Logger(__name__, CmdLevel=logging.INFO, FileLevel=logging.INFO)

class executivecondition_page(BasePage):
    '''
        执行情况
    '''
    # 合同管理
    contract = (By.XPATH, eleData.readExcel(17, 3))
    # 合同管理列表
    contractul = (By.XPATH, eleData.readExcel(452,3))
    #点击
    button_list = [(By.XPATH, eleData.readExcel(654, 3)),#所有地区
                   (By.XPATH, eleData.readExcel(655, 3)),#查询
                   (By.XPATH, eleData.readExcel(656, 3))]#查看明细
    #选择框
    checkbox = [(By.XPATH, eleData.readExcel(657, 3)),#全选0
                (By.XPATH, eleData.readExcel(658, 3)),#一项1
                (By.XPATH, eleData.readExcel(659, 3)),#履约2
                (By.XPATH, eleData.readExcel(660, 3)),#超期3
                (By.XPATH, eleData.readExcel(661, 3)),#终止4
                (By.XPATH, eleData.readExcel(662, 3))]#待收款5
    #验证
    msg_list = [(By.XPATH, eleData.readExcel(663, 3)),#查询验证
                (By.XPATH, eleData.readExcel(664, 3)),#右上角验证
                (By.XPATH, eleData.readExcel(665, 3))]#明细窗口

    def inexecutiveconditionpage(self):
     '''
     进入执行情况页面
     :return:
     '''
     leftMenu = self.findElement(*self.menuList[0])  # 左侧菜单栏
     leftMenu.find_element_by_id('sidebarTree_70_a').click()  # 点击合同管理
     time.sleep(1)
     contractul = self.findElement(*self.contractul)
     contractul.find_element_by_id('sidebarTree_78').click()  # 点击执行情况
     time.sleep(1)
     log.logger.info('page[%s] :found the menu [%s] and [%s]' % (
      sys._getframe().f_code.co_name, self.menuList[0], self.contractul))

if __name__=='__main__':
    pass
