'''
Code description： OtherBank_Page
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

class OtherBank_Page(BasePage):
    '''
    对方银行设置
    '''
    # 银农直联系统
    Silverfarmers = (By.XPATH, eleData.readExcel(14, 3))
    # 银农直联列表
    Silverfarmersul = (By.XPATH, '//*[@id="sidebarTree_23_ul"]')
    # 设置与维护
    set = (By.XPATH, '//*[@id="sidebarTree_33"]')
    # 设置与维护列表
    setul = (By.XPATH, '//*[@id="sidebarTree_36_ul"]')
    # 对方银行
    otherBank = (By.XPATH, eleData.readExcel(234, 3))
    # 对方银行设置页面
    otherBankpage = (By.XPATH, eleData.readExcel(378, 3))
    # 查询条件 开户机构,户名,账号,银行名称
    query_list = [(By.XPATH, eleData.readExcel(379, 3)), (By.XPATH, eleData.readExcel(380, 3)),
                  (By.XPATH, eleData.readExcel(381, 3)),(By.XPATH, eleData.readExcel(382, 3))]
    # 查询数据
    valuesList = [queryData.readExcel(17, 1), queryData.readExcel(18, 1),
                  queryData.readExcel(19, 1), queryData.readExcel(20, 1)]
    #输入框
    input_list = \
        [(By.XPATH, '//*[@id="defaultForm"]/div[1]/div/input'),#银行名称（新增，修改）0
         (By.XPATH, '//*[@id="defaultForm"]/div[2]/div/input'),#户名（新增,修改）1
         (By.XPATH, '//*[@id="defaultForm"]/div[3]/div/input'),#开户机构（新增，修改）2
         (By.XPATH, '//*[@id="defaultForm"]/div[4]/div/input'),#账户号码（新增，修改）3
         (By.XPATH, '//*[@id="transaction_type_select"]'),#联行号（新增，修改）4
         (By.XPATH, eleData.readExcel(423, 3)),#短信接收人（新增）5
         (By.XPATH, eleData.readExcel(424, 3)),#短信接收人手机号（新增）6
         (By.XPATH, eleData.readExcel(425, 3)),#联行号（新增，修改)7
         (By.XPATH, eleData.readExcel(391, 3)),#短信接收人（修改）8
         (By.XPATH, eleData.readExcel(392, 3))]#短信接收人手机号（修改）9
    #点击元素
    button_list = \
         [(By.ID, eleData.readExcel(393, 3)),#查询0
          (By.ID, eleData.readExcel(394, 3)),#新增1
          (By.ID, eleData.readExcel(395, 3)),#修改2
          (By.ID, eleData.readExcel(396, 3)),#删除3
          (By.ID, eleData.readExcel(397, 3)),#查询余额4
          (By.XPATH, eleData.readExcel(398, 3)),#是农商行（修改）5
          (By.XPATH, eleData.readExcel(399, 3)),#否农商行（修改）6
          (By.ID, eleData.readExcel(400, 3)),#提交（新增）7
          (By.ID, eleData.readExcel(401, 3)),#取消（新增）8
          (By.ID, eleData.readExcel(402, 3)),#提交（修改）9
          (By.ID, eleData.readExcel(403, 3)),#取消（修改）10
          (By.XPATH, eleData.readExcel(404, 3)),#确定（删除）11
          (By.XPATH, eleData.readExcel(405, 3))]#取消（删除）12

    # 是否农商行（新增）
    whether = [(By.XPATH, eleData.readExcel(428, 3)),(By.XPATH, eleData.readExcel(429, 3))]
    #选框
    check_box = \
         [(By.XPATH, eleData.readExcel(407, 3)),#修改项0(作废)
          (By.XPATH, eleData.readExcel(408, 3)),#删除项1
          (By.XPATH, eleData.readExcel(409, 3))]#全选2
    #检验
    msg_list = \
         [(By.XPATH, eleData.readExcel(410, 3)),  #右上角验证0
          (By.XPATH, eleData.readExcel(411, 3)),  #新增窗口验证1
          (By.XPATH, eleData.readExcel(412, 3)),  #银行名称为空提示（新增，修改）2
          (By.XPATH, '//*[@id="defaultForm"]/div[2]/div/small'),  #户名为空提示（新增，修改）3
          (By.XPATH, '//*[@id="defaultForm"]/div[3]/div/small'),  #开户机构为空验证（新增，修改）4
          (By.XPATH, '//*[@id="defaultForm"]/div[4]/div/small[1]'),  #账号为空验证（新增）5
          (By.XPATH, '//*[@id="defaultForm"]/div[4]/div/small[2]'),  #账号不规则（新增）6
          (By.XPATH, '//*[@id="defaultForm"]/div[5]/div/small'),  #联行号不规则验证（新增）7
          (By.XPATH, eleData.readExcel(418, 3)),  #短信接收人为空验证(修改）8
          (By.XPATH, eleData.readExcel(419, 3)),  #短信接收人手机号为空验证（修改）9
          (By.XPATH, eleData.readExcel(420, 3)),  #修改窗口验证10
          (By.XPATH, eleData.readExcel(421, 3)),  #删除窗口验证11
          (By.XPATH, eleData.readExcel(422, 3)),  #查询验证12
          (By.XPATH, '/html/body/div[5]'),  # 删除提示13
          (By.XPATH, '/html/body/div[6]'), # 重复验证提示14
          (By.XPATH, '//*[@id="mychart4"]/tbody')] #15
          # 测试数据
    valueList = ['981637672804', '15864901222','测试银行','无相关查询数据','不能为空']
    reason = time.strftime('%Y-%m-%d:%H-%M-%S') + '测试'

    def InotherBankpage(self):
        '''
        进入对方银行设置页面
        :return:
        '''
        leftMenu = self.findElement(*self.menuList[0])  # 左侧菜单栏
        leftMenu.find_element_by_id('sidebarTree_23_a').click()  # 点击银农直联系统
        time.sleep(1)
        Silverfarmersul = self.findElement(*self.Silverfarmersul)
        Silverfarmersul.find_element_by_xpath('//*[@id="sidebarTree_36"]').click()  # 点击设置与维护
        time.sleep(1)
        payul = self.findElement(*self.setul)
        payul.find_element_by_id('sidebarTree_38').click()  # 点击对方银行设置
        time.sleep(1)
        log.logger.info('page[%s] :found the menu [%s] and [%s]' % (
            sys._getframe().f_code.co_name, self.menuList[0], self.setul))

     # 输入查询条件
    def iQueryCondition(self, Accountnamebank, value):
        """
        :param Accountnamebank:
        :param value:
        :return:
        """
        Account_name_bank = self.findElement(*Accountnamebank)
        try:
            Account_name_bank.clear()
            Account_name_bank.send_keys(str(value))
        except Exception:
            log.logger.exception('input value error', exc_info=True)
            raise
        else:
            log.logger.info('[%s] is typing value [%s] ' % (Accountnamebank, value))

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
                self.query_list[0], self.query_list[1], self.query_list[2],self.query_list[3]))

if __name__ == '__main__':
        pass
