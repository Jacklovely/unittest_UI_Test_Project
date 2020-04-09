'''
Code description： GeneralLedger_Page
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

class GeneralLedger_Page(BasePage):
    '''
        总账
    '''
    # 合同管理
    contract = (By.XPATH, eleData.readExcel(17, 3))
    # 合同管理列表
    contractul = (By.XPATH, eleData.readExcel(452,3))
    #合同台账列表
    accountsul = (By.XPATH, eleData.readExcel(692,3))
    # 统计
    statistics = (By.XPATH, eleData.readExcel(469, 3))
    #点击
    button_list = [(By.XPATH, eleData.readExcel(693,3)),#所有地区0
                   (By.XPATH, eleData.readExcel(694,3)),#合同主体1
                   (By.XPATH, eleData.readExcel(695,3)),#招标方式2
                   (By.XPATH, eleData.readExcel(696,3)),#收款状态3
                   (By.XPATH, eleData.readExcel(697,3))]#查询4
    #合同主体
    contractsubject = [(By.XPATH, eleData.readExcel(698, 3)),#请选择
                       (By.XPATH, eleData.readExcel(699, 3)),#房屋租赁
                       (By.XPATH, eleData.readExcel(700, 3)),#场地租赁
                       (By.XPATH, eleData.readExcel(701, 3)),#土地承包
                       (By.XPATH, eleData.readExcel(702, 3)),#资产
                       (By.XPATH, eleData.readExcel(703, 3))]#建地
    #招标方式
    tender = [(By.XPATH, eleData.readExcel(704, 3)),#请选择
              (By.XPATH, eleData.readExcel(705, 3)),#公开协作
              (By.XPATH, eleData.readExcel(706, 3)),#公开竞标
              (By.XPATH, eleData.readExcel(707, 3)),#其他
              (By.XPATH, eleData.readExcel(708, 3)),#招投标
              (By.XPATH, eleData.readExcel(709, 3))]#拍卖
    # 收款状态
    paymentstatus = [(By.XPATH, eleData.readExcel(710, 3)),  # 请选择
                     (By.XPATH, eleData.readExcel(711, 3)),  # 正常履约
                     (By.XPATH, eleData.readExcel(712, 3)),  # 已终止
                     (By.XPATH, eleData.readExcel(713, 3)),  # 超期未收
                     (By.XPATH, eleData.readExcel(714, 3))]  # 待收款
    #时间控件
    time_list = [(By.XPATH, eleData.readExcel(715, 3)),#签订年度
                 (By.XPATH, eleData.readExcel(716, 3)),#前一年
                 (By.XPATH, eleData.readExcel(717, 3)),#点击
                 (By.XPATH, eleData.readExcel(718, 3)),#2018
                 (By.XPATH, eleData.readExcel(719, 3))]#确定
    #验证
    msgInfo = (By.XPATH, eleData.readExcel(720, 3))

    def ingeneralledgerpage(self):
        '''
        进入总账页面
        :return:
        '''
        leftMenu = self.findElement(*self.menuList[0])  # 左侧菜单栏
        leftMenu.find_element_by_id('sidebarTree_70_a').click()  # 点击合同管理
        ele = self.findElement(*self.statistics)  # 定位到元素
        self.driver.execute_script('arguments[0].scrollIntoView(false)', ele)
        time.sleep(1)
        contractul = self.findElement(*self.contractul)
        contractul.find_element_by_id('sidebarTree_79_a').click()  # 点击合同台账
        accountsul = self.findElement(*self.contractul)
        accountsul.find_element_by_id('sidebarTree_80').click() #总账
        time.sleep(1)
        log.logger.info('page[%s] :found the menu [%s] and [%s]' % (
            sys._getframe().f_code.co_name, self.menuList[0], self.contractul))

    # 合同主体，招标方式，收款状态下拉选项
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


if __name__=='__main__':
    pass
