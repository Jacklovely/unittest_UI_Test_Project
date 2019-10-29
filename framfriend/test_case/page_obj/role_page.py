'''
Code description： role_page
Create time：
Developer：
'''
import time
from selenium.webdriver.common.by import By
import logging
import sys
from framfriend.test_case.page_obj.base_page import BasePage, eleData, queryData
from framfriend.test_case.models.log import Logger
log = Logger(__name__, CmdLevel=logging.INFO, FileLevel=logging.INFO)

class rolePage(BasePage):
    '''
        角色管理
    '''

    # 查询数据
    valuesList = [queryData.readExcel(4, 1), int(queryData.readExcel(5, 1)), queryData.readExcel(6, 1)]
    # 测试数据
    reason = time.strftime('%Y-%m-%d:%H:%M:%S') + '测试'
    valueList = ['testname', '1', 'test']
    # 基础功能列表
    functionList = (By.ID, eleData.readExcel(18, 3))
    # 角色管理页面
    rolepage = (By.XPATH, eleData.readExcel(119, 3))
    # 查询条件 角色,表示位,描述
    query_list = [(By.XPATH, eleData.readExcel(120, 3)), (By.XPATH, eleData.readExcel(121, 3)),
                  (By.XPATH, eleData.readExcel(122, 3))]
    #所有按钮
    button_list = \
        [(By.ID, eleData.readExcel(123, 3)),#查询按钮0
         (By.ID, eleData.readExcel(124, 3)),#新增按钮1
         (By.ID, eleData.readExcel(125, 3)),#修改按钮2
         (By.ID, eleData.readExcel(126, 3)),#菜单分配按钮3
         (By.ID, eleData.readExcel(127, 3)),#按钮分配按钮4
         (By.ID, eleData.readExcel(128, 3)),#新增提交按钮5
         (By.ID, eleData.readExcel(129, 3)),#新增取消按钮6
         (By.ID, eleData.readExcel(130, 3)),#修改，菜单、按钮分配提交按钮7
         (By.ID, eleData.readExcel(131, 3)),#修改，菜单、按钮分配取消按钮8
         (By.ID, eleData.readExcel(132, 3)),#选择分配菜单9
         (By.ID, eleData.readExcel(133, 3)),#按钮新增10
         (By.ID, eleData.readExcel(134, 3)),#按钮修改11
         (By.ID, eleData.readExcel(135, 3)),#按钮删除12
         (By.ID, eleData.readExcel(136, 3)),#按钮分配功能开发展开13
         (By.LINK_TEXT, eleData.readExcel(137, 3))]#选择页面14
    #查询验证
    query_msg = \
         [(By.XPATH, eleData.readExcel(138, 3)),
          (By.XPATH, eleData.readExcel(139, 3)) ]
    #新增角色
    addrole_list = \
        [(By.XPATH, eleData.readExcel(140, 3)),#角色名称输入框0
         (By.XPATH, eleData.readExcel(141, 3)),#表示位输入框1
         (By.XPATH, eleData.readExcel(142, 3)),#描述输入框2
         (By.CSS_SELECTOR, eleData.readExcel(143, 3)),#角色名称为空提示3
         (By.CSS_SELECTOR, eleData.readExcel(144, 3)),#表示位为空提示4
         (By.CSS_SELECTOR, eleData.readExcel(145, 3)),#描述为空提示5
         (By.XPATH, eleData.readExcel(146, 3))]#新增成功提示6
    #修改角色
    updaterole_list = \
        [(By.XPATH, eleData.readExcel(147, 3)),#修改项0
         (By.XPATH, eleData.readExcel(148, 3)),#全选框1
         (By.XPATH, eleData.readExcel(149, 3)),#角色名称输入框2
         (By.XPATH, eleData.readExcel(150, 3)),#表示位输入框3
         (By.XPATH, eleData.readExcel(151, 3)),#描述输入框4
         (By.CSS_SELECTOR, eleData.readExcel(152, 3)),#角色名称为空提示5
         (By.CSS_SELECTOR, eleData.readExcel(153, 3)),#表示位为空提示6
         (By.CSS_SELECTOR, eleData.readExcel(154, 3)),#描述为空提示7
         (By.XPATH, eleData.readExcel(155, 3))]#修改成功提示8
    #按钮分配
    buttonAssigned_list = \
         [(By.XPATH, eleData.readExcel(156, 3)),#按钮分配窗口0
          (By.XPATH, eleData.readExcel(157, 3)),#新增按钮名称输入框1
          (By.XPATH, eleData.readExcel(158, 3)),#新增英文名称输入框2
          (By.XPATH, eleData.readExcel(159, 3)),#新增表示位输入框3
          (By.XPATH, eleData.readExcel(160, 3)),#新增按钮图标输入框4
          (By.XPATH, eleData.readExcel(161, 3)),#新增描述输入框5
          (By.XPATH, eleData.readExcel(162, 3)),#新增提交按钮6
          (By.XPATH, eleData.readExcel(163, 3)),#新增取消按钮7
          (By.XPATH, eleData.readExcel(164, 3)),#新增按钮窗口8
          (By.XPATH, eleData.readExcel(165, 3)),#修改项9
          (By.XPATH, eleData.readExcel(166, 3)),#全选框10
          (By.XPATH, eleData.readExcel(167, 3)),#修改按钮名称输入框11
          (By.XPATH, eleData.readExcel(168, 3)),#修改英文名称输入框12
          (By.XPATH, eleData.readExcel(169, 3)),#修改表示位输入框13
          (By.XPATH, eleData.readExcel(170, 3)),#修改按钮图标输入框14
          (By.XPATH, eleData.readExcel(171, 3)),#修改描述输入框15
          (By.XPATH, eleData.readExcel(172, 3)),#修改提交按钮16
          (By.XPATH, eleData.readExcel(173, 3)),#修改取消按钮17
          (By.XPATH, eleData.readExcel(174, 3)),#修改按钮窗口18
          (By.XPATH, eleData.readExcel(175, 3)),#删除框19
          (By.XPATH, eleData.readExcel(176, 3)),#删除确定按钮20
          (By.XPATH, eleData.readExcel(177, 3)),#删除取消按钮21
          (By.XPATH, eleData.readExcel(178, 3)),#删除项22
          (By.XPATH, eleData.readExcel(179, 3)),#新增按钮名称为空提示23
          (By.XPATH, eleData.readExcel(180, 3)),#新增英文名称为空提示24
          (By.XPATH, eleData.readExcel(181, 3)),#新增表示位为空提示25
          (By.XPATH, eleData.readExcel(182, 3)),#新增按钮图标为空提示26
          (By.XPATH, eleData.readExcel(183, 3)),#新增描述为空提示27
          (By.XPATH, eleData.readExcel(184, 3)),#修改按钮名称为空提示28
          (By.XPATH, eleData.readExcel(185, 3)),#修改英文名称为空提示29
          (By.XPATH, eleData.readExcel(186, 3)),#修改表示位为空提示30
          (By.XPATH, eleData.readExcel(187, 3)),#修改按钮图标为空提示31
          (By.XPATH, eleData.readExcel(188, 3)),#修改描述为空提示32
          (By.XPATH, eleData.readExcel(189, 3))]#关闭按钮分配验证33

    def inrolePage(self):
        '''
        进入角色管理页面
        :return:
        '''
        leftMenu = self.findElement(*self.menuList[0])#左侧菜单栏
        leftMenu.find_element_by_id('sidebarTree_16_a').click()#点击基础功能
        time.sleep(1)
        userList = self.findElement(*self.functionList)
        userList.find_element_by_xpath('//*[@id="sidebarTree_19_a"]').click()#点击角色管理
        time.sleep(1)
        log.logger.info('page [%s] :found the menu [%s] and [%s]' % (
        sys._getframe().f_code.co_name, self.menuList[0], self.functionList))

    #输入查询条件
    def iQueryCondition(self, roleshowdescribe, value):
        '''
        :param roleshowdescribe:
        :param value:
        :return:
        '''
        role_show_describe = self.findElement(*roleshowdescribe)
        try:
            role_show_describe.clear()
            role_show_describe.send_keys(str(value))
        except Exception:
            log.logger.exception('input value error', exc_info=True)
            raise
        else:
            log.logger.info('[%s] is typing value [%s] ' % (roleshowdescribe, value))

    #获取条件输入框内容
    def getInputboxValue(self,*query_list):
        '''
        :param query_list:
        :return:
        '''
        try:
            get_query_text = self.findElement(*query_list)
            text = get_query_text.get_attribute('value')
        except Exception:
            log.logger.exception('get value of element fail',exc_info=True)
            raise
        else:
            log.logger.info('get value[%s] of element[%s] success'%(query_list,text))
            return text

    #重置功能的重写
    def reset(self):
        '''

        :return:
        '''
        try:
            self.findElement(*self.query_list[0]).clear()
            self.findElement(*self.query_list[1]).clear()
            self.findElement(*self.query_list[2]).clear()
        except Exception:
            log.logger.exception('reset fail',exc_info=True)
            raise
        else:
            log.logger.info('reset [%s]-[%s]-[%s] success'%(
                self.query_list[0],self.query_list[1],self.query_list[2]))

    #点击按钮
    def cBtn(self,button):
        btn = self.findElement(*button)
        try:
            btn.click()
        except Exception:
            log.logger.exception('can not the button',exc_info=True)
            raise
        else:
            log.logger.info(
                'page [%s] :clicking the button [%s]' % (sys._getframe().f_code.co_name ,button))

    #清空输入项
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
