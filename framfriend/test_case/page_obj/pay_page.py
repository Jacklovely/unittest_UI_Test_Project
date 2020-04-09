'''
Code description： Pay_Page
Create time：
Developer：
'''
import time
import sys
import logging
from selenium.webdriver.common.by import By
from framfriend.test_case.models.log import Logger
from framfriend.test_case.page_obj.base_page import BasePage,eleData
log = Logger(__name__, CmdLevel=logging.INFO, FileLevel=logging.INFO)


class Pay_Page(BasePage):
    '''
    单笔支付
    '''
    #银农直联系统
    Silverfarmers = (By.XPATH,eleData.readExcel(14,3))
    #银农直联列表
    Silverfarmersul = (By.XPATH,'//*[@id="sidebarTree_23_ul"]')
    #转账功能
    pay = (By.XPATH,'//*[@id="sidebarTree_24"]')
    #转账功能列表
    payul = (By.XPATH,'//*[@id="sidebarTree_24_ul"]')
    #单笔支付
    singlePay = (By.XPATH,eleData.readExcel(226,3))
    #按钮
    button_list = \
        [(By.XPATH, eleData.readExcel(238, 3)),#村居0
         (By.XPATH, eleData.readExcel(239, 3)),#选择一项村居1
         (By.XPATH, eleData.readExcel(240, 3)),#收款方2
         (By.XPATH, eleData.readExcel(241, 3)),#选择一项收款方3
         (By.XPATH, eleData.readExcel(242, 3)),#添加新收款方4
         (By.XPATH, eleData.readExcel(243, 3)),#开始支付5
         (By.XPATH, eleData.readExcel(244, 3)),#关闭支付6
         (By.XPATH, eleData.readExcel(245, 3))]#确定支付7
    #输入框
    input_list = \
        [(By.XPATH, eleData.readExcel(246, 3)),#收款方名称0
         (By.NAME, eleData.readExcel(247, 3)),#收款方账号1
         (By.NAME, eleData.readExcel(248, 3)),#收款方户名2
         (By.XPATH, eleData.readExcel(249, 3)),#联行号3
         (By.XPATH, eleData.readExcel(250, 3)),#金额4
         (By.XPATH, eleData.readExcel(251, 3)),#摘要5
         (By.XPATH, eleData.readExcel(252, 3))]#支付密码6
    #验证信息
    msg_list = \
        [(By.XPATH, eleData.readExcel(253, 3)),#村居为空提示0
         (By.XPATH, eleData.readExcel(254, 3)),#账号为空提示1
         (By.XPATH, eleData.readExcel(255, 3)),#收款账号为空提示2
         (By.XPATH, eleData.readExcel(256, 3)),#金额为空错误提示3
         (By.XPATH, eleData.readExcel(257, 3)),#摘要为空提示4
         (By.XPATH, eleData.readExcel(258, 3)),#收款账号错误提示5
         (By.XPATH, eleData.readExcel(259, 3)),#收款账号为空提示6
         (By.XPATH, eleData.readExcel(260, 3)),#收款户名为空提示7
         (By.XPATH, eleData.readExcel(261, 3)),#联行号为空错误提示8
         (By.XPATH, eleData.readExcel(262, 3)),#右上提示9
         (By.XPATH, eleData.readExcel(263, 3)),#选择村居验证10
         (By.XPATH, eleData.readExcel(264, 3)),#选择村居验证11
         (By.XPATH, eleData.readExcel(265, 3)),#选择村居验证12
         (By.XPATH, eleData.readExcel(266, 3)),#选择收款方验证13
         (By.XPATH, eleData.readExcel(267, 3)),#选择收款方验证14
         (By.XPATH, eleData.readExcel(268, 3)),#选择收款方验证15
         (By.XPATH, eleData.readExcel(269, 3)),#选择收款方验证16
         (By.XPATH, eleData.readExcel(270, 3)),#收款方为空提示17
         (By.XPATH, eleData.readExcel(271, 3)),#确定支付窗口18
         (By.XPATH, eleData.readExcel(272, 3)),#关闭支付验证19
         (By.XPATH, eleData.readExcel(273, 3)),#点击添加新收款方验证20
         (By.XPATH, '//*[@id="hasntOtherBank"]/div[4]/div/small[2]')]#新增收款方联行号错误
    # 测试数据
    valueList = ['967687572875767575', '811247857857', '1','123456','测试']
    reason = time.strftime('%Y-%m-%d:%H-%M-%S') + '测试'

    def insinglePay(self):
        '''
        进入单笔支付页面
        :return:
        '''
        leftMenu = self.findElement(*self.menuList[0])  # 左侧菜单栏
        leftMenu.find_element_by_id('sidebarTree_23_a').click()  # 点击银农直联系统
        time.sleep(1)
        Silverfarmersul = self.findElement(*self.Silverfarmersul)
        Silverfarmersul.find_element_by_xpath('//*[@id="sidebarTree_24_a"]').click()  # 点击支付功能
        time.sleep(1)
        payul = self.findElement(*self.payul)
        payul.find_element_by_xpath('//*[@id="sidebarTree_25_a"]').click()#点击单笔支付
        time.sleep(1)
        log.logger.info('page[%s] :found the menu [%s] and [%s]' % (
            sys._getframe().f_code.co_name, self.menuList[0], self.payul))

    def cBtn(self, button):
        '''
        点击按钮
        :return:
        '''
        btn = self.findElement(*button)
        try:
            btn.click()
        except Exception:
            log.logger.exception('can not the button ', exc_info=True)
            raise
        else:
            log.logger.info(
                'page[%s]:clicking the button [%s]' % (sys._getframe().f_code.co_name, button))

if __name__ == '__main__':
        pass



