'''
Code description： Menu_Page
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

class SwitchPage(BasePage):
    '''
    风格切换
    '''
    # 基础功能列表
    functionList = (By.ID, eleData.readExcel(18, 3))
    #切换横版、切换竖版、验证
    element = [(By.XPATH, eleData.readExcel(221, 3)),(By.XPATH, eleData.readExcel(222, 3)),
               (By.XPATH, eleData.readExcel(223, 3)), (By.XPATH, eleData.readExcel(224, 3)),
               (By.XPATH, eleData.readExcel(225, 3))]

    def inSwitchPage(self):
        '''
        进入风格切换页面
        :return:
        '''
        leftMenu = self.findElement(*self.menuList[0])  # 左侧菜单栏
        leftMenu.find_element_by_id('sidebarTree_16_a').click()  # 点击基础功能维护
        time.sleep(1)
        menu_list = self.findElement(*self.functionList)
        menu_list.find_element_by_xpath('//*[@id="sidebarTree_21_a"]').click()  # 点击风格切换
        time.sleep(1)
        log.logger.info('page[%s] :found the menu [%s] and [%s]' % (
            sys._getframe().f_code.co_name, self.menuList[0], self.functionList))

    def cBtn(self,button):
        '''
        点击按钮
        :return:
        '''
        btn = self.findElement(*button)
        try:
            btn.click()
        except Exception:
            log.logger.exception('can not the button ',exc_info=True)
            raise
        else:
            log.logger.info(
                'page[%s]:clicking the button [%s]' % (sys._getframe().f_code.co_name,button))

if __name__ == '__main__':
    pass

