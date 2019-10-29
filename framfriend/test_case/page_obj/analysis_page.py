'''
Code description： analysis_page
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

class analysis_page(BasePage):
    '''
        年限分析
    '''
    # 合同管理
    contract = (By.XPATH, eleData.readExcel(17, 3))
    # 合同管理列表
    contractul = (By.XPATH, eleData.readExcel(452,3))
    #点击
    button_list = [(By.XPATH, eleData.readExcel(641, 3)),#所有地区
                   (By.XPATH, eleData.readExcel(642, 3)),#查询
                   (By.XPATH, eleData.readExcel(643, 3))]#查看明细
    #时间控件
    time_list = [(By.XPATH, eleData.readExcel(644, 3)),#签订年度
                 (By.XPATH, eleData.readExcel(645, 3)),#前年
                 (By.XPATH, eleData.readExcel(646, 3)),#点击
                 (By.XPATH, eleData.readExcel(647, 3)),#2018
                 (By.XPATH, eleData.readExcel(648, 3))]#确定
    #选择框
    checkbox = [(By.XPATH, eleData.readExcel(649, 3)),#全选
                (By.XPATH, eleData.readExcel(650, 3))]#一项
    #验证
    msg_list = [(By.XPATH, eleData.readExcel(651, 3)),#查询验证
                (By.XPATH, eleData.readExcel(652, 3)),#右上角验证
                (By.XPATH, eleData.readExcel(653, 3))]#明细窗口

    def inanalysispage(self):
     '''
     进入年限分析页面
     :return:
     '''
     leftMenu = self.findElement(*self.menuList[0])  # 左侧菜单栏
     leftMenu.find_element_by_id('sidebarTree_70_a').click()  # 点击合同管理
     time.sleep(1)
     contractul = self.findElement(*self.contractul)
     contractul.find_element_by_id('sidebarTree_76').click()  # 点击年限分析
     time.sleep(1)
     log.logger.info('page[%s] :found the menu [%s] and [%s]' % (
      sys._getframe().f_code.co_name, self.menuList[0], self.contractul))

if __name__=='__main__':
    pass

