import logging
import sys
import time
from selenium.webdriver.common.by import By
from framfriend.test_case.page_obj.base_page import  BasePage, eleData
from framfriend.test_case.models.log import Logger
log = Logger(__name__, CmdLevel=logging.INFO, FileLevel=logging.INFO)
class Jg(BasePage):
    '''

    '''
    #左侧菜单栏
    #leftMenu = (By.XPATH, eleData.readExcel(11,3))
    #基础功能
    #jcgn = (By.ID, eleData.readExcel(12, 3))
    #基础功能列表
    functionList = (By.ID, eleData.readExcel(18, 3))
    #机构管理
    Jggl = (By.ID, eleData.readExcel(19, 3))
    #机构页面
    JgPage = (By.XPATH, eleData.readExcel(24, 3))
    #新增机构按钮
    addBtn = (By.ID, eleData.readExcel(25, 3))
    #修改机构按钮
    updateBtn = (By.ID, eleData.readExcel(26, 3))
    #删除机构按钮
    deleteBtn = (By.ID, eleData.readExcel(27, 3))
    tree = (By.ID,'tree_1_switch')
    #所有机构按钮
    treeBtn = (By.ID, eleData.readExcel(28, 3))
    #新增机构窗口
    addck = (By.ID, eleData.readExcel(29, 3))
    #新增机构信息
    addmsg = (By.XPATH, eleData.readExcel(30, 3))
    #机构名称输入框（新增）
    #addJgname = (By.XPATH, eleData.readExcel(31, 3))
    #为空信息提示
    msg = (By.XPATH, eleData.readExcel(32, 3))
    #提交按钮
    addsubmitBtn = (By.ID, eleData.readExcel(33, 3))
    #取消按钮
    AddcancelBtn = (By.XPATH,eleData.readExcel(34,3))
    #修改窗口
    updateck = (By.XPATH,eleData.readExcel(35,3))
    #机构修改信息
    updatemsg = (By.XPATH,eleData.readExcel(36,3))
    #机构名称输入框（修改）
    #updateJgname = (By.XPATH,eleData.readExcel(37,3))
    #修改为空提示
    updatenullmsg = (By.XPATH,'//*[@id="upDateForm"]/div/div/small')
    #提交按钮（修改）
    updatesubmitBtn = (By.ID,eleData.readExcel(38,3))
    #取消按钮（修改）
    updatecancelBtn = (By.ID,eleData.readExcel(39,3))
    #删除窗口
    deleteck = (By.XPATH,eleData.readExcel(40,3))
    #删除信息
    deletemsg = (By.XPATH,eleData.readExcel(41,3))
    #提交按钮（删除）
    deletesubmitBtn = (By.ID,eleData.readExcel(42,3))
    #取消按钮（删除）
    deletecancelBtn = (By.ID,eleData.readExcel(43,3))
    #单点新增提示
    adderr = (By.XPATH,eleData.readExcel(44,3))
    #单点修改提示
    updateerr = (By.XPATH,eleData.readExcel(45,3))
    #单点删除提示
    deleteerr = (By.XPATH,eleData.readExcel(46,3))
    #修改项
    updatedate = (By.ID,'tree_2_span')
    #删除项
    deletedate = (By.ID,'tree_2_span')

    #机构管理必填项
    eleList = \
        [(By.XPATH, eleData.readExcel(31, 3)), # 新增机构名称
         (By.XPATH, eleData.readExcel(37,3))] # 修改机构名称
    #测试新增数据
    reason = time.strftime('%Y-%m-%d:%H:%M:%S') + '测试'
    #valueList = [reason, reason + 'name', 'test', '2018-09-10', '2018-09-10', '00:00:00', '23:59:59']
    #测试修改数据
    reasonupdate = time.strftime('%Y-%m-%d:%H:%M:%S') + '测试修改'
    #valueListupdate = [reason, reason + 'name', 'test', '2018-09-10', '2018-09-10', '00:00:00', '23:59:59']

    #进入机构页面
    def JgPage(self):
        '''
        :return:
        '''
        leftMenu = self.findElement(*self.menuList[0])
        leftMenu.find_element_by_id('sidebarTree_16_a').click()
        #gnMenu = self.findElement(*self.menuList[2]).click()
        time.sleep(1)
        JgList = self.findElement(*self.functionList)
        JgList.find_element_by_xpath('//*[@id="sidebarTree_17_a"]').click()
        time.sleep(1)
        log.logger.info('page [%s] :found the menu [%s] and [%s]' % (sys._getframe().f_code.co_name, self.menuList[0], self.functionList))

    #点击按钮
    def cBtn(self,button):
        btn = self.findElement(*button)
        try:
            btn.click()
        except Exception:
            log.logger.exception(
                'can not click the button' ,exc_info=True)
        else:
            log.logger.info(
                'page [%s] :clicking the button [%s]' % (sys._getframe().f_code.co_name ,button))
    # 输入一组数据
    def inputGroupValue(self, element_list, value_list,value_listupdate):
        """

        :param element_list: 一组元素列表
        :param value_list: 一组数据列表
        :return: none
        """
        for eleLen in range(len(element_list)):
            try:
                self.inputValue(element_list[eleLen], value_list[eleLen])
                self.inputValue(element_list[eleLen], value_listupdate[eleLen])
            except Exception:
                log.logger.exception('element [%s] type value [%s] wrong !' %(element_list[eleLen], value_list[eleLen]))
                raise
            else:
                log.logger.info('element [%s] is typing value [%s]' %(element_list[eleLen], value_list[eleLen]))
    def clearValue(self,clear):
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

if __name__=='__main__':
    pass
