'''
Code description： Issuing_Page
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


class Issuing_Page(BasePage):
    '''
    母子账号代付
    '''
    #银农直联系统
    Silverfarmers = (By.XPATH,eleData.readExcel(14,3))
    #银农直联列表
    Silverfarmersul = (By.XPATH,'//*[@id="sidebarTree_23_ul"]')
    #代付功能
    pay = (By.XPATH,'//*[@id="sidebarTree_32"]')
    #代付功能列表
    payul = (By.XPATH,'//*[@id="sidebarTree_32_ul"]')
    #母子账号代付
    issuing = (By.XPATH,eleData.readExcel(230,3))
    #母子账号代付页面
    issuingpage = (By.XPATH,eleData.readExcel(272,3))
    #按钮
    button_list = \
        [(By.XPATH, eleData.readExcel(722, 3)),  #己方银行0
         (By.XPATH, '//*[@id="searchForm"]/div[1]/div/div/ul/li[2]'),#1
         (By.XPATH, eleData.readExcel(723, 3)),  # 查询2
         (By.XPATH, eleData.readExcel(724, 3)),  # 新增3
         (By.XPATH, eleData.readExcel(725, 3)),  # 修改4
         (By.XPATH, eleData.readExcel(726, 3)),  # 删除5
         (By.XPATH, eleData.readExcel(727, 3)),  # 数据导入6
         (By.XPATH, eleData.readExcel(728, 3)),  # 批量代付7
         (By.XPATH, eleData.readExcel(729, 3)),  # 导出模板8
         (By.XPATH, eleData.readExcel(730, 3)),  # 新增内银行9
         (By.XPATH, eleData.readExcel(731, 3)),  # 提交10
         (By.XPATH, eleData.readExcel(732, 3)),  # 取消11
         (By.XPATH, eleData.readExcel(733, 3)),  # 卡，折12
         (By.XPATH, eleData.readExcel(734, 3)),  # 修改提交13
         (By.XPATH, eleData.readExcel(735, 3)),  # 修改取消14
         (By.XPATH, eleData.readExcel(736, 3)),  # 删除确定按钮15
         (By.XPATH, eleData.readExcel(737, 3)),  # 删除消按钮16
         (By.XPATH, eleData.readExcel(738, 3)),  # 数据导入提交17
         (By.XPATH, eleData.readExcel(739, 3)),  # 数据导入取消18
         (By.XPATH, eleData.readExcel(740, 3)),  # 关闭支付19
         (By.XPATH, eleData.readExcel(741, 3)), # 确定支付20
         (By.XPATH, '//*[@id="defaultForm"]/div[1]/div/div/div/ul/li[2]'),#新增银行21
         (By.XPATH, '//*[@id="defaultForm"]/div[1]/div/div/div/ul/li[3]'),#修改银行22
         (By.ID, 'file_input')]#上传23

    #输入框
    input_list = \
        [(By.XPATH, eleData.readExcel(742, 3)),  #收款人0
         (By.XPATH, eleData.readExcel(743, 3)),  # 收款账号1
         (By.XPATH, eleData.readExcel(744, 3)),  # 摘要2
         (By.XPATH, eleData.readExcel(745, 3)),  #收款人3
         (By.XPATH, eleData.readExcel(746, 3)),  # 收款账号4
         (By.XPATH, eleData.readExcel(747, 3)),  # 金额5
         (By.XPATH, eleData.readExcel(748, 3)),  #备注6
         (By.XPATH, eleData.readExcel(749, 3)),  # 全选7
         (By.XPATH, eleData.readExcel(750, 3)), # 第一项8
         (By.XPATH, eleData.readExcel(751, 3)), #支付输入9
         (By.XPATH, '//*[@id="mychart1"]/tbody/tr[2]/td[1]/input')]#第二项10

    #验证信息
    msg_list = \
        [(By.XPATH, eleData.readExcel(752, 3)),  #右上提示0
         (By.XPATH, eleData.readExcel(753, 3)),  #查询验证1
         (By.XPATH, eleData.readExcel(754, 3)),  #新增窗口验证2
         (By.XPATH, eleData.readExcel(755, 3)),  #修改窗口验证3
         (By.XPATH, eleData.readExcel(756, 3)),  #删除窗口窗口4
         (By.XPATH, eleData.readExcel(757, 3)),  #数据导入5
         (By.XPATH, eleData.readExcel(758, 3)),  #批量代付6
         (By.XPATH, eleData.readExcel(759, 3)),  # 查询失败7
         (By.XPATH, eleData.readExcel(760, 3)),  # 新增银行不能为空8
         (By.XPATH, eleData.readExcel(761, 3)),  # 新增收款人不能为空9
         (By.XPATH, eleData.readExcel(762, 3)),  # 新增金额不能为空10
         (By.XPATH, eleData.readExcel(763, 3)),  # 新增摘要不能为空11
         (By.XPATH, eleData.readExcel(764, 3)),  # 修改账号不能为空12
         (By.XPATH, eleData.readExcel(765, 3)),  # 修改金额不能为空13
         (By.XPATH, eleData.readExcel(766, 3)),  # 修改账号非数字14
         (By.XPATH, eleData.readExcel(767, 3)),  # 新增账号非数字15
         (By.XPATH, eleData.readExcel(768, 3)),  #修改成功提示16
         (By.XPATH, eleData.readExcel(769, 3))]  #删除成功提示17

    #上传
    uploaddata = (By.ID,'file_input')
    # 测试数据
    valueList = ['测试', '98032230389911653019', '123456','黄岛一','6215210200005034','1','2',
                 '不能为空','请输入有效的数字','新增成功','请选中一项内容','请选中一项内容进行修改',
                 '修改成功','测试','98032230389911653019','2020-06-22测试','折(P)','导入失败','导入成功',
                 '密码输入错误','代付成功']
    reason = time.strftime('%Y-%m-%d') + '测试'

    def inissuing(self):
        '''
        进入母子代付页面
        :return:
        '''
        leftMenu = self.findElement(*self.menuList[0])  # 左侧菜单栏
        leftMenu.find_element_by_id('sidebarTree_23_a').click()  # 点击银农直联系统
        time.sleep(1)
        Silverfarmersul = self.findElement(*self.Silverfarmersul)
        Silverfarmersul.find_element_by_xpath('//*[@id="sidebarTree_32"]').click()  # 点击代付功能
        time.sleep(1)
        payul = self.findElement(*self.payul)
        payul.find_element_by_id('sidebarTree_33').click()  # 点击母子代付
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

    def uploadfalse(self):
        '''
        上传
        :return:
        '''
        js = 'document.getElementById("file_input").style.display="block";'
        self.jScript(js)
        self.findElement(*self.button_list[23]).send_keys('F:\TestDownloads\\log.xml')  # 定位上传按钮，添加本地文件
        time.sleep(3)

    def uploadtrue(self):
        '''
        上传
        :return:
        '''
        js = 'document.getElementById("file_input").style.display="block";'
        self.jScript(js)
        self.findElement(*self.button_list[23]).send_keys('F:\TestDownloads\\银农直联代付模板True.xlsx')  # 定位上传按钮，添加本地文件
        time.sleep(3)

if __name__ == '__main__':
        pass
