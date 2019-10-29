'''
Code description： menu_page
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


class menu_Page(BasePage):
    '''
    菜单管理
    '''
    #测试数据
    valueList = ['test1','test2','5']
    reason =time.strftime('%Y-%m-%d:%H-%M-%S')+'测试'
    # 基础功能列表
    functionList = (By.ID, eleData.readExcel(18, 3))
    #菜单管理页面
    menupage = (By.XPATH,eleData.readExcel(190, 3))
    #按钮
    button_list = \
        [(By.ID, eleData.readExcel(191, 3)),#新增按钮0
         (By.ID, eleData.readExcel(192, 3)),#修改按钮1
         (By.ID, eleData.readExcel(193, 3)),#删除按钮2
         (By.ID, eleData.readExcel(194, 3)),#功能开发展开3
         (By.ID, eleData.readExcel(195, 3)),#银农直联展开4
         (By.ID, eleData.readExcel(196, 3)),#合同管理展开5
         (By.ID, eleData.readExcel(197, 3)),#新增提交按钮6
         (By.ID, eleData.readExcel(198, 3)),#新增取消按钮7
         (By.ID, eleData.readExcel(199, 3)),#修改提交按钮8
         (By.ID, eleData.readExcel(200, 3)),#修改取消按钮9
         (By.ID, eleData.readExcel(201, 3)),#删除提交按钮10
         (By.ID, eleData.readExcel(202, 3))]#删除取消按钮11
    #新增菜单
    addmenu_list = \
        [(By.XPATH, eleData.readExcel(203, 3)),#新增菜单窗口0
         (By.XPATH, eleData.readExcel(204, 3)),#菜单名称输入框1
         (By.XPATH, eleData.readExcel(205, 3)),#图标输入框2
         (By.XPATH, eleData.readExcel(206, 3)),#跳转地址输入框3
         (By.XPATH, eleData.readExcel(207, 3)),#排序输入框4
         (By.XPATH, eleData.readExcel(208, 3)),#菜单名称为空提示5
         (By.XPATH, eleData.readExcel(209, 3))]#排序输入错误提示6
    #修改菜单
    updatemenu_list = \
        [(By.XPATH, eleData.readExcel(210, 3)),#修改菜单窗口0
         (By.XPATH, eleData.readExcel(211, 3)),#修改菜单名称输入框1
         (By.XPATH, eleData.readExcel(212, 3)),#修改图标输入框2
         (By.XPATH, eleData.readExcel(213, 3)),#修改跳转地址输入框3
         (By.XPATH, eleData.readExcel(214, 3)),#修改排序输入框4
         (By.XPATH, eleData.readExcel(215, 3)),#修改菜单名称为空提示5
         (By.XPATH, eleData.readExcel(216, 3)),#修改排序输入错误提示6
         (By.XPATH, eleData.readExcel(217, 3))]#修改项7
    #删除菜单
    deletemenu_list = [(By.XPATH, eleData.readExcel(218,3)),#删除项0
                       (By.XPATH, eleData.readExcel(219,3)),#删除窗口1
                       (By.XPATH, '//*[@id="tree_5_a"]')]#选中项2
    #提示信息
    msgbox = (By.XPATH, eleData.readExcel(220,3))#提示信息
    #新增项
    additem = [(By.XPATH,'//*[@id="tree_2_switch"]'),(By.XPATH,'//*[@id="tree_3_span"]'),
               (By.XPATH,'//*[@id="tree_3_switch"]'),(By.XPATH,'//*[@id="tree_4_switch"]')]
    #修改项
    updateitem = (By.ID,'tree_3_switch')
    def inmenuPage(self):
        '''
        进入菜单管理页面
        :return:
        '''
        leftMenu = self.findElement(*self.menuList[0])#左侧菜单栏
        leftMenu.find_element_by_id('sidebarTree_16').click()#点击基础功能维护
        time.sleep(1)
        menu_list = self.findElement(*self.functionList)
        menu_list.find_element_by_id('sidebarTree_20_a').click()#点击菜单管理
        time.sleep(1)
        log.logger.info('page[%s] :found the menu [%s] and [%s]'%(
            sys._getframe().f_code.co_name,self.menuList[0],self.functionList))

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

    def clearValue(self, clear):
        '''
        清空输入项
        :param clear:
        :return:
        '''
        input_clear = self.findElement(*clear)
        try:
            input_clear.clear()
        except Exception:
            log.logger.exception(
                'can not clear input', exc_info=True)
        else:
            log.logger.info(
                'page [%s] :clearing input [%s]' % (sys._getframe().f_code.co_name, clear))

if __name__ == '__main__':
    pass

