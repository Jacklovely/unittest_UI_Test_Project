'''
Code description： Transfer_Page
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


class Transfer_Page(BasePage):
    '''
    批量转账
    '''
    # 银农直联系统
    Silverfarmers = (By.XPATH, eleData.readExcel(14, 3))
    # 银农直联列表
    Silverfarmersul = (By.XPATH, '//*[@id="sidebarTree_23_ul"]')
    # 转账功能
    pay = (By.XPATH, '//*[@id="sidebarTree_24"]')
    # 转账功能列表
    payul = (By.XPATH, '//*[@id="sidebarTree_24_ul"]')
    # 批量转账
    transfer = (By.XPATH, eleData.readExcel(227, 3))
    #输入框
    input_list = \
        [(By.XPATH,eleData.readExcel(296,3)),#对方户名新增、修改0
         (By.XPATH,eleData.readExcel(297,3)),#对方账号新增、修改1
         (By.XPATH,eleData.readExcel(298,3)),#金额新增、修改2
         (By.XPATH,eleData.readExcel(299,3)),#备注新增、修改3
         (By.XPATH,eleData.readExcel(300,3)),#联行号新增、修改4
         (By.XPATH,eleData.readExcel(301,3)),#开户机构新增、修改5
         (By.XPATH,eleData.readExcel(302,3))]#交易密码6
    #按钮
    button_list = \
        [(By.ID, eleData.readExcel(303, 3)),#查询按钮0
         (By.ID, eleData.readExcel(304, 3)),#新增按钮1
         (By.ID, eleData.readExcel(305, 3)),#修改按钮2
         (By.ID, eleData.readExcel(306, 3)),#删除按钮3
         (By.ID, eleData.readExcel(307, 3)),#数据导入4
         (By.ID, eleData.readExcel(308, 3)),#批量转账5
         (By.ID, eleData.readExcel(309, 3)),#导出模板6
         (By.XPATH, eleData.readExcel(310, 3)),#选择打开银行(新增，修改）7
         (By.XPATH, eleData.readExcel(311, 3)),#选择银行（新增8
         (By.XPATH, eleData.readExcel(312, 3)),#提交（新增）9
         (By.XPATH, eleData.readExcel(313, 3)),#取消（新增）10
         (By.XPATH, eleData.readExcel(314, 3)),#选择银行（修改）11
         (By.ID, eleData.readExcel(315, 3)),#提交（修改）12
         (By.ID, eleData.readExcel(316, 3)),#取消（修改）13
         (By.ID, eleData.readExcel(317, 3)),#确定（删除)14
         (By.XPATH, eleData.readExcel(318, 3)),#取消(删除)15
         (By.ID, eleData.readExcel(319, 3)),#上传16
         (By.ID, eleData.readExcel(320, 3)),#导入数据（提交）17
         (By.ID, eleData.readExcel(321, 3)),#导入数据（取消）18
         (By.XPATH, eleData.readExcel(322, 3)),#确定支付（关闭）19
         (By.XPATH, eleData.readExcel(323, 3)),#确定支付（确定）20
         (By.XPATH, '//*[@id="searchForm"]/div[1]/div/button'),#己方户名21
         (By.XPATH, '//*[@id="searchForm"]/div[1]/div/div/ul/li[4]/a')]#己方户名中一项22
    #验证
    msg_list = \
        [(By.XPATH, eleData.readExcel(324, 3)),#银行存款为空验证0
         (By.XPATH, eleData.readExcel(325, 3)),#对方户名为空验证1
         (By.XPATH, eleData.readExcel(326, 3)),#对方账号为空验证2
         (By.XPATH, eleData.readExcel(327, 3)),#备注为空验证3
         (By.XPATH, eleData.readExcel(328, 3)),#联行号为空验证（新增、修改）4
         (By.XPATH, eleData.readExcel(329, 3)),#开户机构为空验证（新增、修改）5
         (By.XPATH, eleData.readExcel(330, 3)),#金额（修改）为空验证6
         (By.XPATH, eleData.readExcel(331, 3)),#右上角提示7
         (By.XPATH, eleData.readExcel(332, 3)),#查询验证8
         (By.XPATH, eleData.readExcel(333, 3)),#新增窗口9
         (By.XPATH, eleData.readExcel(334, 3)),#修改窗口10
         (By.XPATH, eleData.readExcel(335, 3)),#删除窗口11
         (By.XPATH, eleData.readExcel(336, 3)),#数据导入窗口12
         (By.XPATH, eleData.readExcel(337, 3)),#确定支付窗口13
         (By.XPATH, '//*[@id="defaultForm"]/div[4]/div/small[1]'),#修改账号为空14
         (By.XPATH, '//*[@id="defaultForm"]/div[4]/div/small[2]'),#修改输入错误账号15
         (By.XPATH, '/html/body/div[5]'),#删除验证16
         (By.XPATH, '//*[@id="confirmPayPw"]/div/div'),#关闭转账验证17
         (By.XPATH, '//*[@id="container-fluid"]/div[1]/div/div/div[2]/div[1]/div[2]/div[4]/div[1]/span[1]')]#18
    #选框
    checkbox_list = \
        [(By.XPATH, eleData.readExcel(338, 3)),#全选框0
         (By.XPATH, eleData.readExcel(339, 3)),#修改项1
         (By.XPATH, eleData.readExcel(340, 3))]#删除项2
    # 查询条件 昵称,手机号,登录账号
    query_list = [(By.XPATH,eleData.readExcel(293,3)), (By.XPATH, eleData.readExcel(294, 3)),
                  (By.XPATH, eleData.readExcel(295, 3))]
    # 查询数据
    valuesList = [queryData.readExcel(7, 1), int(queryData.readExcel(8, 1)), queryData.readExcel(9, 1)]
    #测试数据
    valueList = ['test', '123456789123456', '1','123594422111','123456','不能为空','请输入有效的数字','新增成功',
    '请选中一项内容','请选中一项内容进行修改','修改成功','导入数据','删除成功','导入成功','总共 3 条记录']
    reason = time.strftime('%Y-%m-%d:%H-%M-%S') + '测试'

    def intransfer(self):
        '''
        进入批量转账页面
        :return:
        '''
        leftMenu = self.findElement(*self.menuList[0])  # 左侧菜单栏
        leftMenu.find_element_by_id('sidebarTree_23_a').click()  # 点击银农直联系统
        time.sleep(1)
        Silverfarmersul = self.findElement(*self.Silverfarmersul)
        Silverfarmersul.find_element_by_xpath('//*[@id="sidebarTree_24_a"]').click()  # 点击转账功能
        time.sleep(1)
        payul = self.findElement(*self.payul)
        payul.find_element_by_id('sidebarTree_26').click()  # 点击批量转账
        time.sleep(1)
        log.logger.info('page[%s] :found the menu [%s] and [%s]' % (
            sys._getframe().f_code.co_name, self.menuList[0], self.payul))

    #输入查询条件
    def iQueryCondition(self, NameIdOrgan, value):
        """
        :param NameIdOrgan:
        :param value:
        :return:
        """
        name_phone_login = self.findElement(*NameIdOrgan)
        try:
            name_phone_login.clear()
            name_phone_login.send_keys(str(value))
        except Exception:
            log.logger.exception('input value error', exc_info=True)
            raise
        else:
            log.logger.info('[%s] is typing value [%s] ' % (NameIdOrgan, value))

    # 获取条件输入框的内容
    def getInputboxValue(self,*query_list):
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

    def uploadfalse(self):
        '''
        上传
        :return:
        '''
        js = 'document.getElementById("file_input").style.display="block";'
        self.jScript(js)
        self.findElement(*self.button_list[16]).send_keys('F:\TestDownloads\\log.xml')  # 定位上传按钮，添加本地文件
        time.sleep(3)
    def uploadture(self):
        '''
        上传
        :return:
        '''
        js = 'document.getElementById("file_input").style.display="block";'
        self.jScript(js)
        self.findElement(*self.button_list[16]).send_keys('F:\TestDownloads\\银农直联批量转账true.xlsx')  # 定位上传按钮，添加本地文件
        time.sleep(3)

if __name__ == '__main__':
        pass
