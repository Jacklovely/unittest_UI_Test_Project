'''
Code description： issuing_page
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


class issuing_Page(BasePage):
    '''
    批量代付
    '''
    #银农直联系统
    Silverfarmers = (By.XPATH,eleData.readExcel(14,3))
    #银农直联列表
    Silverfarmersul = (By.XPATH,'//*[@id="sidebarTree_23_ul"]')
    #代付功能
    pay = (By.XPATH,'//*[@id="sidebarTree_29"]')
    #支付功能列表
    payul = (By.XPATH,'//*[@id="sidebarTree_29_ul"]')
    #批量代付
    issuing = (By.XPATH,eleData.readExcel(231,3))
    #批量代付页面
    issuingpage = (By.XPATH,eleData.readExcel(274,3))
    #按钮
    button_list = \
        [(By.ID, eleData.readExcel(275, 3)),#查询按钮0
         (By.ID, eleData.readExcel(276, 3)),#模板导出1
         (By.ID, eleData.readExcel(277, 3)),#批量代发2
         (By.XPATH, eleData.readExcel(278, 3)),#上传3
         (By.ID, eleData.readExcel(279, 3)),#提交4
         (By.ID, eleData.readExcel(280, 3)),#取消5
         (By.XPATH, eleData.readExcel(281, 3))]#查询结果6
    #输入框
    input_list = \
        [(By.XPATH, eleData.readExcel(282, 3)),#备注查询框0
         (By.XPATH, eleData.readExcel(283, 3)),#导入备注框1
         (By.XPATH, eleData.readExcel(284, 3))]#导入交易密码框2
    #验证信息
    msg_list = \
        [(By.XPATH, eleData.readExcel(285, 3)),#查询验证0
         (By.XPATH, eleData.readExcel(286, 3)),#导入备注为空提示1
         (By.XPATH, eleData.readExcel(287, 3)),#导入交易密码为空提示2
         (By.XPATH, eleData.readExcel(288, 3)),#右上角提示3
         (By.XPATH, eleData.readExcel(289, 3)),#批量代发窗口4
         (By.XPATH, eleData.readExcel(290, 3)),#上传文档验证5
         (By.XPATH, eleData.readExcel(291, 3))]#批量代发详情窗口6
    #上传
    uploaddata = (By.ID,'file_input')
    # 测试数据
    valueList = ['工资代发', '98032230389911653019', '123456']
    reason = time.strftime('%Y-%m-%d:%H-%M-%S') + '测试'

    def inissuing(self):
        '''
        进入批量代付页面
        :return:
        '''
        leftMenu = self.findElement(*self.menuList[0])  # 左侧菜单栏
        leftMenu.find_element_by_id('sidebarTree_23_a').click()  # 点击银农直联系统
        time.sleep(1)
        Silverfarmersul = self.findElement(*self.Silverfarmersul)
        Silverfarmersul.find_element_by_xpath('//*[@id="sidebarTree_29"]').click()  # 点击代付功能
        time.sleep(1)
        payul = self.findElement(*self.payul)
        payul.find_element_by_id('sidebarTree_31').click()  # 点击批量代付
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

    def upload(self):
        '''
        上传
        :return:
        '''
        js = 'document.getElementById("file_input").style.display="block";'
        self.jScript(js)
        self.findElement(*self.uploaddata).send_keys('E:\\MyDownloads\\20190923034151.xls')  # 定位上传按钮，添加本地文件
        time.sleep(3)

if __name__ == '__main__':
        pass
