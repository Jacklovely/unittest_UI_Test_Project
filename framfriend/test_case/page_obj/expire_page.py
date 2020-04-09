'''
Code description： Expire_Page
Create time：
Developer：
'''
import time
from selenium.webdriver.common.by import By
import logging
import sys
from framfriend.test_case.page_obj.base_page import BasePage, eleData
from framfriend.test_case.models.log import Logger

log = Logger(__name__, CmdLevel=logging.INFO, FileLevel=logging.INFO)

class Expire_Page(BasePage):
    '''
        到期提醒
    '''
    # 合同管理
    contract = (By.XPATH, eleData.readExcel(17, 3))
    # 合同管理列表
    contractul = (By.XPATH, eleData.readExcel(452,3))
    # 选框  全选  选择一项
    check_box = [(By.XPATH, eleData.readExcel(602, 3)), (By.XPATH, eleData.readExcel(603, 3))]
    #所有地区，查看明细
    button = [(By.XPATH,eleData.readExcel(605,3)),(By.XPATH,eleData.readExcel(606,3))]
    # 验证  右上角验证   明细窗口
    msg_list = [(By.XPATH, eleData.readExcel(598, 3)), (By.XPATH, eleData.readExcel(604, 3))]

    def inexpirepage(self):
     '''
     进入到期提醒页面
     :return:
     '''
     leftMenu = self.findElement(*self.menuList[0])  # 左侧菜单栏
     leftMenu.find_element_by_id('sidebarTree_70_a').click()  # 点击合同管理
     time.sleep(1)
     contractul = self.findElement(*self.contractul)
     contractul.find_element_by_id('sidebarTree_74').click()  # 点击到期提醒
     time.sleep(1)
     log.logger.info('page[%s] :found the menu [%s] and [%s]' % (
      sys._getframe().f_code.co_name, self.menuList[0], self.contractul))

if __name__=='__main__':
    pass
