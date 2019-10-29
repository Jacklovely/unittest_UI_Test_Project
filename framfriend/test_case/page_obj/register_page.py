'''
Code description： register_page
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

class register_page(BasePage):
    '''
        合同登记
    '''
    #查询数据
    valuesList = [queryData.readExcel(23, 1), (queryData.readExcel(24, 1)),
                  queryData.readExcel(25, 1),(queryData.readExcel(26, 1))]

    # 测试新增数据
    reason = time.strftime('%Y-%m-%d:%H:%M:%S') + '测试'
    reason1 = time.strftime('%Y%m%d%H%M%S')
    valueList = ['10000','test','1','10-1','6535456754434556766','PZ07']

    # 合同管理
    contract = (By.XPATH, eleData.readExcel(17, 3))
    # 合同管理列表
    contractul = (By.XPATH, eleData.readExcel(452,3))
    # 合同登记
    register = (By.XPATH, eleData.readExcel(453, 3))
    #合同登记页面
    registerpage = (By.XPATH,eleData.readExcel(473,3))
    #输入框
    input_list = \
         [(By.XPATH, eleData.readExcel(478, 3)),#合同编号0
          (By.XPATH, eleData.readExcel(479, 3)),#合同名称1
          (By.XPATH, eleData.readExcel(480, 3)),#客户名称2
          (By.XPATH, eleData.readExcel(481, 3)),#承租方3
          (By.XPATH, eleData.readExcel(482, 3)),#村委名4
          (By.XPATH, eleData.readExcel(483, 3)),#合同总额5
          (By.XPATH, eleData.readExcel(484, 3)),#收款金额6
          (By.XPATH, eleData.readExcel(485, 3)),#收款日期7
          (By.XPATH, eleData.readExcel(486, 3)),#合同年限8
          (By.XPATH, eleData.readExcel(487, 3)),#经营方式9
          (By.XPATH, eleData.readExcel(488, 3)),#账号10
          (By.XPATH, eleData.readExcel(489, 3)),#备注11
          (By.XPATH, eleData.readExcel(490, 3)),#自定义收款金额12
          (By.XPATH, eleData.readExcel(491, 3)),#合同明细名称13
          (By.XPATH, eleData.readExcel(492, 3)),#合同明细数量14
          (By.XPATH, eleData.readExcel(493, 3)),#明细修改金额15
          (By.XPATH, eleData.readExcel(494, 3)),#节点名称（增16
          (By.XPATH, eleData.readExcel(495, 3)),#短信接收人（增17
          (By.XPATH, eleData.readExcel(496, 3)),#手机号（增18
          (By.XPATH, eleData.readExcel(497, 3)),#节点名称（改19
          (By.XPATH, eleData.readExcel(498, 3)),#短信接收人（改20
          (By.XPATH, eleData.readExcel(499, 3)),#手机号（改21
          (By.XPATH, '//*[@id="defaultForm"]/div[18]/div/input')]#账号（改22

    #点击元素
    button_list = \
         [(By.XPATH, eleData.readExcel(500, 3)),#节点新增0
          (By.XPATH, eleData.readExcel(501, 3)),#节点修改1
          (By.XPATH, eleData.readExcel(502, 3)),#节点删除2
          (By.XPATH, eleData.readExcel(503, 3)),#查询3
          (By.XPATH, eleData.readExcel(504, 3)),#新增4
          (By.XPATH, eleData.readExcel(505, 3)),#修改5
          (By.XPATH, eleData.readExcel(506, 3)),#查看明细6
          (By.XPATH, eleData.readExcel(507, 3)),#查看明细2 7
          (By.XPATH, eleData.readExcel(508, 3)),#删除8
          (By.XPATH, eleData.readExcel(509, 3)),#模板导出9
          (By.XPATH, eleData.readExcel(510, 3)),#数据导入10
          (By.XPATH, eleData.readExcel(511, 3)),#图片上传11
          (By.XPATH, eleData.readExcel(512, 3)),#提交12
          (By.XPATH, eleData.readExcel(513, 3)),#取消13
          (By.XPATH, eleData.readExcel(514, 3)),#修改（提交14
          (By.XPATH, eleData.readExcel(515, 3)),#修改（取消15
          (By.XPATH, eleData.readExcel(516, 3)),#明细刷新16
          (By.XPATH, eleData.readExcel(517, 3)),#明细修改17
          (By.XPATH, eleData.readExcel(518, 3)),#明细关闭18
          (By.XPATH, eleData.readExcel(519, 3)),#明细修改（提交19
          (By.XPATH, eleData.readExcel(520, 3)),#明细修改（关闭20
          (By.XPATH, eleData.readExcel(521, 3)),#删除（确定21
          (By.XPATH, eleData.readExcel(522, 3)),#删除（取消22
          (By.XPATH, eleData.readExcel(523, 3)),#数据导入（上传23
          (By.XPATH, eleData.readExcel(524, 3)),#数据导入（提交24
          (By.XPATH, eleData.readExcel(525, 3))]#数据导入（取消25

    #节点
    nodebutton_list = \
          [(By.XPATH, '//*[@id="addAddVillage"]'),#提交0
           (By.XPATH, '//*[@id="closeAddVillage"]'),#取消1
           (By.XPATH, '//*[@id="edit_updateVillage"]'),#提交（改2
           (By.XPATH, '//*[@id="close_updateVillage"]'),#取消（改3
           (By.XPATH,'//*[@id="edit_deleteVillage"]'),#确定(删除4
           (By.XPATH, '//*[@id="close_deleteVillage"]'),#取消（删除5
           (By.XPATH, '//*[@id="tree_6_span"]')]#太和社区6

    #日期控件
    time_list = \
         [(By.XPATH, eleData.readExcel(526, 3)),#开始时间0
          (By.XPATH, eleData.readExcel(527, 3)),#截止时间1
          (By.XPATH, eleData.readExcel(528, 3)),#切换年2
          (By.XPATH, eleData.readExcel(529, 3)),#切换月3
          (By.XPATH, eleData.readExcel(530, 3)),#选择日4
          (By.XPATH, eleData.readExcel(531, 3)),#清空5
          (By.XPATH, eleData.readExcel(532, 3)),#现在6
          (By.XPATH, eleData.readExcel(533, 3)),#确定7
          (By.XPATH, '//*[@id="jedate"]/div[4]/div[2]/span[2]')]#明细修改日期8
    #选择
    choose_list = \
         [(By.XPATH, eleData.readExcel(534, 3)),#所有地区0
          (By.XPATH, eleData.readExcel(535, 3)),#展开所有地区1
          (By.XPATH, eleData.readExcel(536, 3)),#展开洪山镇2
          (By.XPATH, eleData.readExcel(537, 3)),#洪山镇中一项3
          (By.XPATH, eleData.readExcel(538, 3)),#洪山镇4
          (By.XPATH, eleData.readExcel(539, 3)),#全选5
          (By.XPATH, eleData.readExcel(540, 3)),#选择一项6
          (By.XPATH, eleData.readExcel(541, 3)),#签订日期7
          (By.XPATH, eleData.readExcel(542, 3)),#租赁年限始8
          (By.XPATH, eleData.readExcel(543, 3)),#租赁年限止9
          (By.XPATH, eleData.readExcel(544, 3)),#应收日期10
          (By.XPATH, eleData.readExcel(545, 3)),#明细内已收日期11
          (By.XPATH, '//*[@id="mychart5"]/thead/tr/th[1]/div[1]/input'), # 明细全选12
          (By.XPATH, '//*[@id="mychart5"]/tbody/tr[1]/td[1]/input'), # 明细选择一项13
          (By.XPATH, '//*[@id="mychart1"]/tbody/tr[10]/td[1]/input')]#删除项14
    #验证
    msg_list = \
        [(By.XPATH, eleData.readExcel(546, 3)),  #右上角验证0
         (By.XPATH, eleData.readExcel(547, 3)),  #节点名称验证1
         (By.XPATH, eleData.readExcel(548, 3)),  #短信接收人验证2
         (By.XPATH, eleData.readExcel(549, 3)),  #手机号验证3
         (By.XPATH, eleData.readExcel(550, 3)),  #合同编号为空验证4
         (By.XPATH, eleData.readExcel(551, 3)),  #合同名称为空验证5
         (By.XPATH, eleData.readExcel(552, 3)),  #客户名称为空验证6
         (By.XPATH, eleData.readExcel(553, 3)),  #签订日期为空验证7
         (By.XPATH, eleData.readExcel(554, 3)),  #租赁年限1为空验证8
         (By.XPATH, eleData.readExcel(555, 3)),  #租赁年限2为空验证9
         (By.XPATH, eleData.readExcel(556, 3)),  #承租方为空验证10
         (By.XPATH, eleData.readExcel(557, 3)),  #合同总额为空验证11
         (By.XPATH, eleData.readExcel(558, 3)),  #合同总额数字验证12
         (By.XPATH, eleData.readExcel(559, 3)),  #收款金额为空验证13
         (By.XPATH, eleData.readExcel(560, 3)),  #收款金额数字验证14
         (By.XPATH, eleData.readExcel(561, 3)),  #收款日期为空验证15
         (By.XPATH, eleData.readExcel(562, 3)),  #合同年限为空验证16
         (By.XPATH, eleData.readExcel(563, 3)),  #经营方式为空验证17
         (By.XPATH, eleData.readExcel(564, 3)),  #账号为空验证18
         (By.XPATH, eleData.readExcel(565, 3)),  #账号数字验证19
         (By.XPATH, eleData.readExcel(566, 3)),  #村委名为空验证20
         (By.XPATH, eleData.readExcel(567, 3)),  #新增节点窗口21
         (By.XPATH, eleData.readExcel(568, 3)),  #修改节点窗口22
         (By.XPATH, eleData.readExcel(569, 3)),  #删除节点窗口23
         (By.XPATH, eleData.readExcel(570, 3)),  #新增合同窗口24
         (By.XPATH, eleData.readExcel(571, 3)),  #修改合同窗口25
         (By.XPATH, eleData.readExcel(572, 3)),  #查看明细窗口26
         (By.XPATH, eleData.readExcel(573, 3)),  #明细中修改窗口27
         (By.XPATH, eleData.readExcel(574, 3)),  #删除合同窗口28
         (By.XPATH, eleData.readExcel(575, 3)),  #数据导入窗口29
         (By.XPATH, eleData.readExcel(576, 3)),  #单一查询验证30
         (By.XPATH, eleData.readExcel(577, 3)),  #时间查询验证31
         (By.XPATH, eleData.readExcel(578, 3)),  #明细不完整验证32
         (By.XPATH, eleData.readExcel(579, 3)),  #上传图片验证33
         (By.CSS_SELECTOR, eleData.readExcel(580, 3)),  #合同号重复验证34
         (By.XPATH, eleData.readExcel(581, 3)),  #合同账号为空验证35
         (By.XPATH, eleData.readExcel(582, 3)),  #合同账号非数字验证36
         (By.XPATH, eleData.readExcel(583, 3)),  #明细刷新修改验证37
         (By.XPATH, eleData.readExcel(584, 3))]  #明细页面记录38

    #合同类型选项
    contractTypeNum = [(By.XPATH,'//*[@id="defaultForm"]/div[2]/div/select/option[1]'),#收款
                     (By.XPATH, '//*[@id="defaultForm"]/div[2]/div/select/option[2]')]#付款
    #合同主体选项
    contractsubjectNum = [(By.XPATH, '//*[@id="defaultForm"]/div[4]/div/select/option[1]'),#房屋租赁
                          (By.XPATH, '//*[@id="defaultForm"]/div[4]/div/select/option[2]'),#场地租赁
                          (By.XPATH, '//*[@id="defaultForm"]/div[4]/div/select/option[3]'),#土地承包
                          (By.XPATH, '//*[@id="defaultForm"]/div[4]/div/select/option[4]'),#资产
                          (By.XPATH, '//*[@id="defaultForm"]/div[4]/div/select/option[5]')]#建地
    #招标方式
    tenderNum = [(By.XPATH, '//*[@id="defaultForm"]/div[5]/div/select/option[1]'),#公开协作
              (By.XPATH, '//*[@id="defaultForm"]/div[5]/div/select/option[2]'),#公开竞标
              (By.XPATH, '//*[@id="defaultForm"]/div[5]/div/select/option[3]'),#其他
              (By.XPATH, '//*[@id="defaultForm"]/div[5]/div/select/option[4]'),#招投标
              (By.XPATH, '//*[@id="defaultForm"]/div[5]/div/select/option[5]')]#拍卖
    #收款方式
    Billing_methodNum = [(By.XPATH, '//*[@id="defaultForm"]/div[13]/div/select/option[1]'),#按年
                         (By.XPATH, '//*[@id="defaultForm"]/div[13]/div/select/option[2]'),#按半年
                         (By.XPATH, '//*[@id="defaultForm"]/div[13]/div/select/option[3]'),#按月
                         (By.XPATH, '//*[@id="defaultForm"]/div[13]/div/select/option[4]')]#自定义
    #明细修改状态
    contract_statesNum = [(By.XPATH, '//*[@id="defaultForm"]/div[2]/div/select/option[1]'),# 已收款
                       (By.XPATH, '//*[@id="defaultForm"]/div[2]/div/select/option[2]'),# 未收款
                       (By.XPATH, '//*[@id="defaultForm"]/div[2]/div/select/option[3]'),# 待收款
                       (By.XPATH, '//*[@id="defaultForm"]/div[2]/div/select/option[4]'),# 已收不足
                       (By.XPATH, '//*[@id="defaultForm"]/div[2]/div/select/option[5]'),# 超期不足
                       (By.XPATH, '//*[@id="defaultForm"]/div[2]/div/select/option[6]')]# 超期收款
    #自定义合同
    Customcontract = (By.XPATH, '//*[@id="addContractDetail"]')
    #添加明细
    Adddetail = (By.XPATH,'//*[@id="mingxi"]/div')
    #合同类型
    contract_type = (By.XPATH, '//*[@id="defaultForm"]/div[2]/div/select')
    #合同主体
    contract_subject = (By.XPATH,'//*[@id="defaultForm"]/div[4]/div/select')
    #招标方式
    tender = (By.XPATH,'//*[@id="defaultForm"]/div[5]/div/select')
    #收款方式
    Billing_method =(By.XPATH, '//*[@id="defaultForm"]/div[13]/div/select')
    #明细修改状态
    contract_states = (By.XPATH,'//*[@id="defaultForm"]/div[2]/div/select' )
    #查询条件 合同号,合同名称,客户名称，经办人
    query_list = [(By.XPATH, eleData.readExcel(474,3)),(By.XPATH, eleData.readExcel(475,3)),
                  (By.XPATH, eleData.readExcel(476,3)),(By.XPATH, eleData.readExcel(477,3))]
    # 删除图片
    deleteimg = (By.XPATH, '//*[@id="fileUploadContent1"]/div/div[3]/div[2]/i')

    def inregisterpage(self):
     '''
     进入合同登记页面
     :return:
     '''
     leftMenu = self.findElement(*self.menuList[0])  # 左侧菜单栏
     leftMenu.find_element_by_id('sidebarTree_70_a').click()  # 点击合同管理
     time.sleep(1)
     contractul = self.findElement(*self.contractul)
     contractul.find_element_by_id('sidebarTree_71_a').click()  # 点击合同登记
     time.sleep(1)
     log.logger.info('page[%s] :found the menu [%s] and [%s]' % (
      sys._getframe().f_code.co_name, self.menuList[0], self.contractul))

    # 输入查询条件
    def iQueryCondition(self, contractinformation, value):
     """
     :param contractinformation:
     :param value:
     :return:
     """
     contract_information = self.findElement(*contractinformation)
     try:
      contract_information.clear()
      contract_information.send_keys(str(value))
     except Exception:
      log.logger.exception('input value error', exc_info=True)
      raise
     else:
      log.logger.info('[%s] is typing value [%s] ' % (contractinformation, value))

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
      self.findElement(*self.query_list[3]).clear()
     except Exception:
      log.logger.exception('reset fail', exc_info=True)
      raise
     else:
      log.logger.info('reset [%s]-[%s]-[%s]-[%s] success' % (
       self.query_list[0], self.query_list[1], self.query_list[2], self.query_list[3]))

   # 合同类型/合同主体/招标方式/收款方式下拉选项
    def contractTypeLevelOption(self, *xpathList):
        """

        :param xpath_list:
        :return:
        """
        try:
            contract_type_level = self.findElement(*xpathList)
            text = contract_type_level.text
        except Exception:
            log.logger.exception('get element contract type/level item text fail', exc_info=True)
            raise
        else:
            log.logger.info('get element [%s] contract type/level item text [%s] fail' % (xpathList, text))
            return text, contract_type_level

    def upload(self):
        '''
        上传
        :return:
        '''
        d = self.driver.find_element_by_xpath('//*[@id="picture"]/div[1]/input[1]')
        self.driver.execute_script('arguments[0].removeAttribute(\"style\")', d)
        list = [r'E:\\MyDownloads\\Wallpaper.jpg',
                r'E:\\MyDownloads\\Wallpaper1.jpg',
                r'E:\\MyDownloads\\Wallpaper2.jpg']
        for listimage in list:
            self.findElement(*self.button_list[11]).send_keys(listimage)  # 定位上传按钮，添加本地文件

    #键盘删除
    def keydelete(self):
        '''

        :return:
        '''
        for keydelete1 in range(15):
            self.findElement(*self.input_list[0]).send_keys(Keys.BACK_SPACE)
            self.findElement(*self.input_list[1]).send_keys(Keys.BACK_SPACE)
            self.findElement(*self.input_list[2]).send_keys(Keys.BACK_SPACE)
            self.findElement(*self.input_list[3]).send_keys(Keys.BACK_SPACE)
            self.findElement(*self.input_list[5]).send_keys(Keys.BACK_SPACE)
            self.findElement(*self.input_list[6]).send_keys(Keys.BACK_SPACE)
            self.findElement(*self.input_list[7]).send_keys(Keys.BACK_SPACE)
            self.findElement(*self.input_list[8]).send_keys(Keys.BACK_SPACE)
            self.findElement(*self.input_list[9]).send_keys(Keys.BACK_SPACE)
            self.findElement(*self.input_list[22]).send_keys(Keys.BACK_SPACE)

    # 聚焦元素
    def scroll_jujiao(self,jujiao):
        self.driver.switch_to.frame(self.driver.find_element_by_id('drawIframeXX'))
        jiao = self.findElement(*jujiao)
        try:
            self.driver.execute_script("arguments[0].scrollIntoView(false)", jiao)
        except Exception:
            log.logger.exception(
                'can not jujiao the element', exc_info=True)
        else:
            log.logger.info(
                'page [%s] :jujiao the element [%s]' % (sys._getframe().f_code.co_name, jujiao))

    def uploadFalse(self):
        '''
        上传错误文件
        :return:
        '''
        js = 'document.getElementById("file_input").style.display="block";'
        self.jScript(js)
        self.findElement(*self.button_list[23]).send_keys('E:\\MyDownloads\\20190923034151.xls')  # 定位上传按钮，添加本地文件
        time.sleep(3)

    def uploadTrue(self):
        '''
        上传正确文件
        :return:
        '''
        js = 'document.getElementById("file_input").style.display="block";'
        self.jScript(js)
        self.findElement(*self.button_list[23]).send_keys('E:\\MyDownloads\\合同导入.xlsx')  # 定位上传按钮，添加本地文件
        time.sleep(3)

if __name__=='__main__':
    pass


