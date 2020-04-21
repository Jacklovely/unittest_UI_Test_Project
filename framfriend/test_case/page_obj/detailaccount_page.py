'''
Code description： DetailAccount_Page
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

class DetailAccount_Page(BasePage):
    '''
        明细账
    '''
    # 合同管理
    contract = (By.XPATH, eleData.readExcel(17, 3))
    # 合同管理列表
    contractul = (By.XPATH, eleData.readExcel(452,3))
    #合同台账列表
    accountsul = (By.XPATH, eleData.readExcel(692,3))
    # 统计
    statistics = (By.XPATH, eleData.readExcel(469, 3))
    # 查询数据
    valuesList = [queryData.readExcel(33, 1), (queryData.readExcel(34, 1)),
                  queryData.readExcel(35, 1), queryData.readExcel(36, 1)]
    # 查询条件 合同号,合同名称,客户名称，合同年限
    query_list = [(By.XPATH, eleData.readExcel(668, 3)), (By.XPATH, eleData.readExcel(669, 3)),
                  (By.XPATH, eleData.readExcel(670, 3)), (By.XPATH, eleData.readExcel(671, 3))]
    #点击  所有地区  查询  第一条数据查看
    button_list = [(By.XPATH, eleData.readExcel(666, 3)),
                   (By.XPATH, eleData.readExcel(667, 3)),
                   (By.XPATH,'//*[@id="mychart1"]/tbody/tr[1]/td[11]/a'),
                   (By.XPATH, '//*[@id="hand_man"]'),#经手人
                   (By.XPATH, '//*[@id="searchForm"]/div[7]/select')]#收款状态
    #经手人
    handledby = [(By.XPATH, eleData.readExcel(672, 3)),#请选择
                 (By.XPATH, eleData.readExcel(673, 3)),#管理员
                 (By.XPATH, eleData.readExcel(674, 3)),#曲盼盼
                 (By.XPATH, eleData.readExcel(675, 3)),#孙宏
                 (By.XPATH, eleData.readExcel(676, 3))]#刘佳
    #收款状态
    paymentstatus = [(By.XPATH, eleData.readExcel(677, 3)),#请选择
                     (By.XPATH, eleData.readExcel(678, 3)),#正常履约
                     (By.XPATH, eleData.readExcel(679, 3)),#已终止
                     (By.XPATH, eleData.readExcel(680, 3)),#超期未收
                     (By.XPATH, eleData.readExcel(681, 3))]#待收款
    #时间控件
    time_list = [(By.XPATH, eleData.readExcel(682, 3)),#签订日期始0
                 (By.XPATH, eleData.readExcel(683, 3)),#签订日期止1
                 (By.XPATH, eleData.readExcel(684, 3)),#前一年2
                 (By.XPATH, eleData.readExcel(685, 3)),#选择日3
                 (By.XPATH, eleData.readExcel(686, 3)),#前一月4
                 (By.XPATH, eleData.readExcel(687, 3)),#选择日5
                 (By.XPATH, eleData.readExcel(688, 3))]#确定6
    #验证
    msg_list = [(By.XPATH, eleData.readExcel(689, 3)),#查询验证
                (By.XPATH, eleData.readExcel(690, 3)),#时间查询验证
                (By.XPATH, eleData.readExcel(691, 3))]#明细窗口
    assertlist = ['显示第 1 到第 0 条记录，总共 0 条记录',
                  '显示第 1 到第 5 条记录，总共 5 条记录',
                  '显示第 1 到第 10 条记录，总共 294 条记录'
                  ]
    def indetailaccountpage(self):
        '''
        进入明细账页面
        :return:
        '''
        leftMenu = self.findElement(*self.menuList[0])  # 左侧菜单栏
        leftMenu.find_element_by_id('sidebarTree_74_a').click()  # 点击合同管理
        time.sleep(1)
        ele = self.findElement(*self.statistics)  # 定位到元素
        self.driver.execute_script('arguments[0].scrollIntoView(false)', ele)
        time.sleep(1)
        contractul = self.findElement(*self.contractul)
        contractul.find_element_by_id('sidebarTree_83_a').click()  # 点击合同台账
        time.sleep(2)
        accountsul = self.findElement(*self.contractul)
        accountsul.find_element_by_id('sidebarTree_85').click() # 明细账
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

    # 经手人，收款状态下拉选项
    def contractOption(self, *xpathList):
        """
        :param xpath_list:
        :return:
        """
        try:
            contract_option = self.findElement(*xpathList)
            text = contract_option.text
        except Exception:
            log.logger.exception('get element contract_option item text fail', exc_info=True)
            raise
        else:
            log.logger.info('get element [%s] contract_option item text [%s] fail' % (xpathList, text))
            return text, contract_option

if __name__ == '__main__':
    pass


