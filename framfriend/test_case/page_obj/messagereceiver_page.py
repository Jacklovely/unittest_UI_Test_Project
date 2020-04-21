'''
Code description： MessagerEceiver_Page
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

class MessagerEceiver_Page(BasePage):
    '''
        预警短信接收人
    '''
    # 合同管理
    contract = (By.XPATH, eleData.readExcel(17, 3))
    # 合同管理列表
    contractul = (By.XPATH, eleData.readExcel(452,3))
    valueList = (13764901222)
    reason = time.strftime('%Y-%m-%d:%H-%M-%S') + '测试'
    #查询数据
    valuesList = [(queryData.readExcel(31, 1)),(queryData.readExcel(32, 1))]
    # 查询条件 姓名  备注
    query_list = [(By.XPATH, eleData.readExcel(607,3)), (By.XPATH, eleData.readExcel(608,3))]
    # 断言数据
    assertlist = ['显示第 1 到第 0 条记录，总共 0 条记录',
                  '请选择一项查看',
                  '测试',
                  '测试人员',
                  '手机号不能为空',
                  '不能为空',
                  '请输入正确的手机号',
                  '新增成功！',
                  '请选中一项内容！',
                  '请选中一项内容进行操作！',
                  '修改成功！',
                  '删除成功！']
    #输入框
    input_list = [(By.XPATH, eleData.readExcel(609,3)),#姓名（增0
                  (By.XPATH, eleData.readExcel(610,3)),#手机号（增1
                  (By.XPATH, eleData.readExcel(611,3)),#备注（增2
                  (By.XPATH, eleData.readExcel(612,3)),#姓名（改3
                  (By.XPATH, eleData.readExcel(613,3)),#手机号（改4
                  (By.XPATH, eleData.readExcel(614,3))]#备注（改5
    #选择框  全选  一项
    checkbox = [(By.XPATH, eleData.readExcel(615,3)),(By.XPATH, eleData.readExcel(616,3))]
    #点击
    button_list = [(By.XPATH, eleData.readExcel(617,3)),#查询0
                   (By.XPATH, eleData.readExcel(618,3)),#新增1
                   (By.XPATH, eleData.readExcel(619,3)),#修改2
                   (By.XPATH, eleData.readExcel(620,3)),#删除3
                   (By.XPATH, eleData.readExcel(621,3)),#新增提交4
                   (By.XPATH, eleData.readExcel(622,3)),#新增取消5
                   (By.XPATH, eleData.readExcel(623,3)),#修改提交6
                   (By.XPATH, eleData.readExcel(624,3)),#修改取消7
                   (By.XPATH, eleData.readExcel(625,3)),#删除确定8
                   (By.XPATH, eleData.readExcel(626,3))]#删除取消9
    #验证
    msg_list = [(By.XPATH, eleData.readExcel(627,3)),#右上角验证0
                (By.XPATH, eleData.readExcel(628,3)),#查询验证1
                (By.XPATH, eleData.readExcel(629,3)),#新增窗口2
                (By.XPATH, eleData.readExcel(630,3)),#修改窗口3
                (By.XPATH, eleData.readExcel(631,3)),#删除窗口4
                (By.XPATH, eleData.readExcel(632,3)),#为空验证5
                (By.XPATH, eleData.readExcel(633,3)),#不正规手机号验证（增6
                (By.XPATH, eleData.readExcel(634,3)),#手机号为空（增7
                (By.XPATH, eleData.readExcel(635,3)),#姓名为空提示（增8
                (By.XPATH, eleData.readExcel(636,3)),#姓名为空提示（改9
                (By.XPATH, eleData.readExcel(637,3)),#手机号为空（改10
                (By.XPATH, eleData.readExcel(638,3)),#不规则手机号（改11
                (By.XPATH, eleData.readExcel(639,3)),#备注为空（改12
                (By.XPATH, eleData.readExcel(640, 3)),#删除验证13
                (By.XPATH, eleData.readExcel(600, 3))]#错误查询验证14

    def inmessagereceiverpage(self):
     '''
     进入预警短信接收人页面
     :return:
     '''
     leftMenu = self.findElement(*self.menuList[0])  # 左侧菜单栏
     leftMenu.find_element_by_id('sidebarTree_74_a').click()  # 点击合同管理
     time.sleep(1)
     contractul = self.findElement(*self.contractul)
     contractul.find_element_by_id('sidebarTree_79').click()  # 点击预警短信接收人
     time.sleep(1)
     log.logger.info('page[%s] :found the menu [%s] and [%s]' % (
      sys._getframe().f_code.co_name, self.menuList[0], self.contractul))

    def iQueryCondition(self, messagereceiver, value):
     """
     :param contractinformation:
     :param value:
     :return:
     """
     message_receiver = self.findElement(*messagereceiver)
     try:
      message_receiver.clear()
      message_receiver.send_keys(str(value))
     except Exception:
      log.logger.exception('input value error', exc_info=True)
      raise
     else:
      log.logger.info('[%s] is typing value [%s] ' % (messagereceiver, value))

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
      log.logger.info('reset [%s]-[%s]success' % (
       self.query_list[0], self.query_list[1]))

    #键盘删除
    def keydelete(self):
        '''

        :return:
        '''
        for keydelete1 in range(25):
            self.findElement(*self.input_list[3]).send_keys(Keys.BACK_SPACE)
            self.findElement(*self.input_list[4]).send_keys(Keys.BACK_SPACE)
            self.findElement(*self.input_list[5]).send_keys(Keys.BACK_SPACE)


if __name__=='__main__':
    pass



