'''
Code description： user_page
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

class userPage(BasePage):
    '''
        用户管理
    '''
    #查询数据
    valuesList = [queryData.readExcel(1, 1), int(queryData.readExcel(2, 1)), queryData.readExcel(3, 1)]
    # 测试新增数据
    reason = time.strftime('%Y-%m-%d:%H:%M:%S') + '测试'
    valueList = ['testname','name', 'test11', '123456', '15864901722','12345678a.']

    #基础功能列表
    functionList = (By.ID, eleData.readExcel(18, 3))
    #机构管理
    usergl = (By.ID, eleData.readExcel(20, 3))
    #用户管理页面
    userpage = (By.XPATH,eleData.readExcel(47,3))
    #查询条件 昵称,手机号,登录账号
    query_list = [(By.XPATH, eleData.readExcel(48,3)),(By.XPATH, eleData.readExcel(49,3)),
                  (By.XPATH, eleData.readExcel(50,3))]

    #全部按钮
    button_list = \
        [(By.ID, eleData.readExcel(52,3)),#查询按钮0
         (By.ID, eleData.readExcel(53,3)),#新增按钮1
         (By.ID, eleData.readExcel(54,3)),#修改按钮2
         (By.ID, eleData.readExcel(55,3)),#删除按钮3
         (By.ID, eleData.readExcel(56,3)),#机构分配按钮4
         (By.ID, eleData.readExcel(57,3)),#账套分配按钮5
         (By.ID, eleData.readExcel(58,3)),#权限分配按钮6
         (By.ID, eleData.readExcel(59,3)),#地区分配按钮7
         (By.ID, eleData.readExcel(60,3)),#新增提交按钮8
         (By.ID, eleData.readExcel(61,3)),#新增取消按钮9
         (By.ID, eleData.readExcel(62,3)),#修改提交按钮10
         (By.ID, eleData.readExcel(63,3)),#修改取消按钮11
         (By.ID, eleData.readExcel(64,3)),#删除确定按钮12
         (By.XPATH, eleData.readExcel(65,3)),#删除取消按钮13
         (By.ID, eleData.readExcel(66,3)),#机构，账套，权限，地区提交按钮14
         (By.ID, eleData.readExcel(66, 3)),#机构，账套，权限，地区取消按钮15
         (By.XPATH, eleData.readExcel(68, 3)),#机构分配所有展开按钮16
         (By.LINK_TEXT, eleData.readExcel(69, 3)),#选择机构17
         (By.XPATH, eleData.readExcel(72, 3)),#账套全选按钮18
         (By.XPATH, eleData.readExcel(75, 3)),#权限全选按钮19
         (By.LINK_TEXT, eleData.readExcel(78, 3))]#选择地区20

    #角色成功验证
    querymsg = \
         [(By.XPATH,eleData.readExcel(79,3)),#角色验证
          (By.XPATH,eleData.readExcel(80,3))]#昵称,手机号，登录账号验证

    #新增用户
    addinput = \
        [(By.XPATH,eleData.readExcel(81,3)),#用户名0
         (By.XPATH,eleData.readExcel(82,3)),#昵称1
         (By.XPATH,eleData.readExcel(83,3)),#登录账号2
         (By.XPATH,eleData.readExcel(84,3)),#密码3
         (By.XPATH,eleData.readExcel(85,3)),#手机号4
         (By.XPATH,eleData.readExcel(86,3)),#所属机构5
         (By.ID,eleData.readExcel(87,3)),#选择机构6
         (By.XPATH,eleData.readExcel(88,3)),#用户名为空提示7
         (By.XPATH,eleData.readExcel(89,3)),#昵称为空提示8
         (By.XPATH,eleData.readExcel(90,3)),#登录账号为空提示9
         (By.XPATH,eleData.readExcel(91,3)),#密码为空提示10
         (By.XPATH,eleData.readExcel(92,3)),#手机号为空提示11
         (By.XPATH,eleData.readExcel(93,3)),#手机号格式不正确12
         (By.XPATH,eleData.readExcel(94,3)),#新增成功提示13
         (By.ID, eleData.readExcel(95, 3)),#所属机构提交按钮14
         (By.ID, eleData.readExcel(96, 3)),#所属机构取消按钮15
         (By.NAME, eleData.readExcel(97,3))]#角色16

    #修改用户
    updateuser = \
        [(By.XPATH, eleData.readExcel(98, 3)),#不选择修改项点击修改提示0
         (By.XPATH, eleData.readExcel(99, 3)),#选择多项修改项点击修改提示1
         (By.XPATH, eleData.readExcel(100, 3)),#全选框2
         (By.XPATH, eleData.readExcel(101, 3)),#选择一项3
         (By.XPATH, eleData.readExcel(102, 3)),#登录账号4
         (By.XPATH, eleData.readExcel(103, 3)),#登录密码5
         (By.XPATH, eleData.readExcel(104, 3)),#登录账号为空提示6
         (By.XPATH, eleData.readExcel(105, 3)),#登录密码为空提示7
         (By.XPATH, eleData.readExcel(106, 3)),#修改成功提示8
         (By.XPATH, eleData.readExcel(107, 3)),#修改登录账号成功验证9
         (By.XPATH, eleData.readExcel(108, 3)),#修改性别成功验证10
         (By.XPATH, eleData.readExcel(109, 3))]#修改角色成功验证11

    #删除用户
    deleteuser = \
        [(By.XPATH, eleData.readExcel(110, 3)),#点击删除提示0
         (By.XPATH, eleData.readExcel(111, 3)),#删除成功提示1
         (By.XPATH, eleData.readExcel(112, 3)),#删除项2
         (By.XPATH, eleData.readExcel(113, 3))]#删除验证3

    #分配
    allot = \
        [(By.XPATH, eleData.readExcel(114, 3)),#不选择分配项点击。。分配提示0
         (By.XPATH, eleData.readExcel(115, 3)),#选择多项分配项点击。。分配提示1
         (By.XPATH, eleData.readExcel(116, 3)),#分配成功提示2
         (By.XPATH, eleData.readExcel(117, 3)),#机构分配成功验证3
         (By.XPATH, eleData.readExcel(118, 3))]#地区分配成功验证4

    #用户管理
    def inuserpage(self):
        '''
        进入用户管理页面
        :return:
        '''

        leftMenu = self.findElement(*self.menuList[0])#左侧菜单栏
        leftMenu.find_element_by_id('sidebarTree_16_a').click()#点击基础功能
        time.sleep(1)
        userList = self.findElement(*self.functionList)
        userList.find_element_by_xpath('//*[@id="sidebarTree_18_a"]').click()#点击用户管理
        time.sleep(1)
        log.logger.info('page [%s] :found the menu [%s] and [%s]' % (
        sys._getframe().f_code.co_name, self.menuList[0], self.functionList))

    #输入查询条件
    def iQueryCondition(self, NamePhonelogin, value):
        """
        :param NamePhonelogin:
        :param value:
        :return:
        """
        name_phone_login = self.findElement(*NamePhonelogin)
        try:
            name_phone_login.clear()
            name_phone_login.send_keys(str(value))
        except Exception:
            log.logger.exception('input value error', exc_info=True)
            raise
        else:
            log.logger.info('[%s] is typing value [%s] ' % (NamePhonelogin, value))

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
        except Exception:
            log.logger.exception('reset fail', exc_info=True)
            raise
        else:
            log.logger.info('reset [%s]-[%s]-[%s] success' % (
                self.query_list[0], self.query_list[1], self.query_list[2]))

    # 点击按钮
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

if __name__ == '__main__':
    pass

