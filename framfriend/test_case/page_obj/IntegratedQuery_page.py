'''
Code description： IntegratedQuery_page
Create time：
Developer：
'''
import time
import sys
import logging
from selenium.webdriver.common.by import By
from framfriend.test_case.models.log import Logger
from framfriend.test_case.page_obj.base_page import BasePage, eleData, queryData

log = Logger(__name__, CmdLevel=logging.INFO, FileLevel=logging.INFO)

class IntegratedQuery_page(BasePage):
    '''
    综合查询
    '''
    # 银农直联系统
    Silverfarmers = (By.XPATH, eleData.readExcel(14, 3))
    # 银农直联列表
    Silverfarmersul = (By.XPATH, '//*[@id="sidebarTree_23_ul"]')
    # 转账功能
    pay = (By.XPATH, '//*[@id="sidebarTree_24"]')
    # 转账功能列表
    payul = (By.XPATH, '//*[@id="sidebarTree_24_ul"]')
    # 转账查询
    IntegratedQuery = (By.XPATH, eleData.readExcel(228, 3))
    # 转账查询页面
    IntegratedQuerypage = (By.XPATH, eleData.readExcel(342, 3))
    # 查询条件 己方银行,对方银行,摘要
    query_list = [(By.XPATH, eleData.readExcel(343, 3)), (By.XPATH, eleData.readExcel(344, 3)),
                  (By.XPATH, eleData.readExcel(345, 3))]
    # 查询数据
    valuesList = [queryData.readExcel(10, 1), queryData.readExcel(11, 1), queryData.readExcel(12, 1)]
    #点击元素
    button_list = \
        [(By.XPATH, eleData.readExcel(346, 3)),#开始时间1 0
         (By.XPATH, eleData.readExcel(347, 3)),#开始时间2 1
         (By.XPATH, eleData.readExcel(348, 3)),#查询2
         (By.XPATH, eleData.readExcel(349, 3)),#批量打印3
         (By.XPATH, eleData.readExcel(350, 3)),#切换年4
         (By.XPATH, eleData.readExcel(351, 3)),#切换月5
         (By.XPATH, eleData.readExcel(352, 3)),#选择日6
         (By.XPATH, eleData.readExcel(353, 3)),#确定7
         (By.XPATH, eleData.readExcel(354, 3)),#现在8
         (By.XPATH, eleData.readExcel(355, 3))]#清空9
    # 选框
    checkbox_list = \
        [(By.XPATH, eleData.readExcel(356, 3)),  # 选择一项0
         (By.XPATH, eleData.readExcel(357, 3))]  # 全选1
    #验证
    msg = \
        [(By.XPATH, eleData.readExcel(358, 3)),#单一查询验证
         (By.XPATH, eleData.readExcel(359, 3)),#时间查询验证
         (By.XPATH, eleData.readExcel(360, 3))]#打印验证
    #数据后打印按钮
    dataprint = (By.XPATH, '//*[@id="mychart4"]/tbody/tr[1]/td[13]/a')
    # 数据后刷新按钮
    datarefresh = (By.XPATH, '//*[@id="mychart4"]/tbody/tr[1]/td[15]/a')

    def inIntegratedQuery(self):
        '''
        进入转账查询页面
        :return:
        '''
        leftMenu = self.findElement(*self.menuList[0])  # 左侧菜单栏
        leftMenu.find_element_by_id('sidebarTree_23_a').click()  # 点击银农直联系统
        time.sleep(1)
        Silverfarmersul = self.findElement(*self.Silverfarmersul)
        Silverfarmersul.find_element_by_xpath('//*[@id="sidebarTree_24_a"]').click()  # 点击转账功能
        time.sleep(1)
        payul = self.findElement(*self.payul)
        payul.find_element_by_id('sidebarTree_27').click()  # 点击批量转账查询
        time.sleep(1)
        log.logger.info('page[%s] :found the menu [%s] and [%s]' % (
            sys._getframe().f_code.co_name, self.menuList[0], self.payul))

    #输入查询条件
    def iQueryCondition(self, MeAdverseAbstract, value):
        """
        :param MeAdverseAbstract:
        :param value:
        :return:
        """
        me_adverse_abstract = self.findElement(*MeAdverseAbstract)
        try:
            me_adverse_abstract.clear()
            me_adverse_abstract.send_keys(value)
        except Exception:
            log.logger.exception('input value error', exc_info=True)
            raise
        else:
            log.logger.info('[%s] is typing value [%s] ' % (MeAdverseAbstract, value))

    # 获取条件输入框的内容
    def getInputboxValue(self,*query_list):
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
        except Exception:
            log.logger.exception('reset fail', exc_info=True)
            raise
        else:
            log.logger.info('reset [%s]-[%s]-[%s] success' % (
                self.query_list[0], self.query_list[1], self.query_list[2]))

if __name__ == '__main__':
        pass