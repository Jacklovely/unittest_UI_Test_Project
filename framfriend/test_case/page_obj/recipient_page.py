'''
Code description： Recipient_Page
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

class Recipient_Page(BasePage):
    '''
    短信接收人设置
    '''
    # 银农直联系统
    Silverfarmers = (By.XPATH, eleData.readExcel(14, 3))
    # 银农直联列表
    Silverfarmersul = (By.XPATH, '//*[@id="sidebarTree_23_ul"]')
    # 设置与维护
    set = (By.XPATH, '//*[@id="sidebarTree_33"]')
    # 设置与维护列表
    setul = (By.XPATH, '//*[@id="sidebarTree_33_ul"]')
    # 短信接收人设置
    recipient = (By.XPATH, eleData.readExcel(236, 3))
    # 短信接收人设置页面
    recipientpage = (By.XPATH, eleData.readExcel(378, 3))
    # 查询条件 姓名，手机号
    query_list = [(By.XPATH, eleData.readExcel(430, 3)), (By.XPATH, eleData.readExcel(431, 3))]
    # 查询数据
    valuesList = [queryData.readExcel(21, 1), queryData.readExcel(22, 1)]
    #输入框
    input_list = \
        [(By.XPATH, eleData.readExcel(432, 3)),#姓名（增改）0
         (By.XPATH, eleData.readExcel(433, 3)),#手机号（增改）1
         (By.XPATH, eleData.readExcel(434, 3))]#备注（增改）2
    #点击
    button_list = \
        [(By.XPATH, eleData.readExcel(435, 3)),#查询0
         (By.XPATH, eleData.readExcel(436, 3)),#新增1
         (By.XPATH, eleData.readExcel(437, 3)),#修改2
         (By.XPATH, eleData.readExcel(438, 3)),#删除3
         (By.XPATH, eleData.readExcel(439, 3)),#提交（增改）4
         (By.XPATH, eleData.readExcel(440, 3)),#取消（增改）5
         (By.XPATH, eleData.readExcel(441, 3)),#确定（删除）6
         (By.XPATH, eleData.readExcel(442, 3))]#取消（删除）7
    #选择框
    checkbox = [(By.XPATH, eleData.readExcel(443, 3)),#选择一项0
                (By.XPATH, eleData.readExcel(444, 3))]#全选1
    #验证
    msg_list = \
         [(By.XPATH, eleData.readExcel(445, 3)),#右上角验证0
          (By.XPATH, eleData.readExcel(446, 3)),#新增窗口验证1
          (By.XPATH, eleData.readExcel(447, 3)),#姓名为空提示（增改）2
          (By.XPATH, eleData.readExcel(448, 3)),#手机号为空提示（增改）3
          (By.XPATH, eleData.readExcel(449, 3)),#修改窗口验证4
          (By.XPATH, eleData.readExcel(450, 3)),#删除窗口验证5
          (By.XPATH, eleData.readExcel(451, 3))]#查询验证6
    # 测试数据
    valueList = ['15864901222','18560703375','13764901222']
    reason = time.strftime('%Y-%m-%d:%H-%M-%S') + '测试'

    def inrecipientpage(self):
        '''
        进入对方银行设置页面
        :return:
        '''
        leftMenu = self.findElement(*self.menuList[0])  # 左侧菜单栏
        leftMenu.find_element_by_id('sidebarTree_23_a').click()  # 点击银农直联系统
        time.sleep(1)
        Silverfarmersul = self.findElement(*self.Silverfarmersul)
        Silverfarmersul.find_element_by_xpath('//*[@id="sidebarTree_33"]').click()  # 点击设置与维护
        time.sleep(1)
        setul = self.findElement(*self.setul)
        setul.find_element_by_id('sidebarTree_37_a').click()  # 点击短信接收人设置
        time.sleep(1)
        log.logger.info('page[%s] :found the menu [%s] and [%s]' % (
            sys._getframe().f_code.co_name, self.menuList[0], self.setul))

    # 输入查询条件
    def iQueryCondition(self, namephone, value):
        """
        :param namephone:
        :param value:
        :return:
        """
        name_phone = self.findElement(*namephone)
        try:
            name_phone.clear()
            name_phone.send_keys(str(value))
        except Exception:
            log.logger.exception('input value error', exc_info=True)
            raise
        else:
            log.logger.info('[%s] is typing value [%s] ' % (namephone, value))

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
        except Exception:
            log.logger.exception('reset fail', exc_info=True)
            raise
        else:
            log.logger.info('reset [%s]-[%s] success' % (
                self.query_list[0], self.query_list[1]))


if __name__ == '__main__':
    pass