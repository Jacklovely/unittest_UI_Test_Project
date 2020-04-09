'''
Code description： Receipt_Page
Create time：
Developer：
'''
import time
from selenium.webdriver.common.by import By
import logging
import sys
from framfriend.test_case.page_obj.base_page import BasePage, eleData, queryData
from framfriend.test_case.models.log import Logger

log = Logger(__name__, CmdLevel=logging.INFO, FileLevel=logging.INFO)

class Receipt_Page(BasePage):
    '''
        合同收款
    '''
    # 合同管理
    contract = (By.XPATH, eleData.readExcel(17, 3))
    # 合同管理列表
    contractul = (By.XPATH, eleData.readExcel(452,3))
    #查询数据
    valuesList = [int(queryData.readExcel(27, 1)), (queryData.readExcel(28, 1)),
                  queryData.readExcel(29, 1),int(queryData.readExcel(30, 1))]
    # 查询条件 合同号,合同名称,客户名称，经办人
    query_list = [(By.XPATH, eleData.readExcel(585, 3)), (By.XPATH, eleData.readExcel(586, 3)),
                  (By.XPATH, eleData.readExcel(587, 3)), (By.XPATH, eleData.readExcel(588, 3))]
    #时间控件
    time_list = [(By.XPATH, eleData.readExcel(589, 3)), #签订时间始0
                 (By.XPATH, eleData.readExcel(590, 3)), #前一年1
                 (By.XPATH, eleData.readExcel(591, 3)), #选择日2
                 (By.XPATH, eleData.readExcel(592, 3)), #签订时间止3
                 (By.XPATH, eleData.readExcel(593, 3)), #前一月4
                 (By.XPATH, eleData.readExcel(594, 3)), #选择日5
                 (By.XPATH, eleData.readExcel(595, 3))] #确定6

    #点击  查询   查看明细
    button_list = [(By.XPATH, eleData.readExcel(596, 3)),(By.XPATH, eleData.readExcel(597, 3))]
    #验证  右上角验证   条件查询验证   时间查询验证，明细窗口
    msg_list = [(By.XPATH, eleData.readExcel(598, 3)),(By.XPATH, eleData.readExcel(599, 3)),
                (By.XPATH, eleData.readExcel(600, 3)),(By.XPATH, eleData.readExcel(601, 3))]
    #选框  全选  选择一项
    check_box = [(By.XPATH, eleData.readExcel(602, 3)),(By.XPATH, eleData.readExcel(603, 3))]

    def inreceiptpage(self):
     '''
     进入合同收款页面
     :return:
     '''
     leftMenu = self.findElement(*self.menuList[0])  # 左侧菜单栏
     leftMenu.find_element_by_id('sidebarTree_70_a').click()  # 点击合同管理
     time.sleep(1)
     contractul = self.findElement(*self.contractul)
     contractul.find_element_by_id('sidebarTree_73').click()  # 点击合同收款
     time.sleep(1)
     log.logger.info('page[%s] :found the menu [%s] and [%s]' % (
      sys._getframe().f_code.co_name, self.menuList[0], self.contractul))

    # 输入查询条件
    def iQueryCondition(self, contractinformation, value):
     """
     :param contractinformation:
     :param value:
     :return:
     """
     contract_information = self.findElement(*contractinformation)
     try:
      contract_information.clear()
      contract_information.send_keys(str(value))
     except Exception:
      log.logger.exception('input value error', exc_info=True)
      raise
     else:
      log.logger.info('[%s] is typing value [%s] ' % (contractinformation, value))

    # 获取条件输入框的内容
    def getInputboxValue(self, *query_list):
     '''

     :param query_list:
     :return:
     '''
     try:
      get_query_text = self.findElement(*query_list)
      text = get_query_text.get_attribute('value')
     except Exception:
      log.logger.exception('get value of element fail', exc_info=True)
      raise
     else:
      log.logger.info('get value [%s] of element [%s] success' % (query_list, text))
      return text

    # 重置功能的重写
    def reset(self):
     """

     :return:
     """
     try:
      self.findElement(*self.query_list[0]).clear()
      self.findElement(*self.query_list[1]).clear()
      self.findElement(*self.query_list[2]).clear()
      self.findElement(*self.query_list[3]).clear()
     except Exception:
      log.logger.exception('reset fail', exc_info=True)
      raise
     else:
      log.logger.info('reset [%s]-[%s]-[%s]-[%s] success' % (
       self.query_list[0], self.query_list[1], self.query_list[2], self.query_list[3]))

if __name__=='__main__':
    pass
