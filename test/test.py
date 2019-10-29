import unittest

import time
from idlelib import browser

from selenium import webdriver
from selenium.webdriver.support.ui import Select

class Test(unittest.TestCase):
    def setUp(self):
        '''启动浏览器'''
        self.dr = webdriver.Chrome()
        self.dr.maximize_window()

    def testName(self):
        self.dr.get('http://localhost:8080/farmfriend/login/exit.do')
        time.sleep(3)
        '''登录'''
        self.dr.find_element_by_id('loginName').send_keys('admin')
        self.dr.find_element_by_id('password').send_keys('666666')
        Select(self.dr.find_element_by_xpath('//*[@id="accounts_select"]')).select_by_value('00102001')
        self.dr.find_element_by_xpath('//*[@id="login-middle"]/div/div[2]/form/p[5]/input').click()

        time.sleep(3)
        menu = self.dr.find_element_by_id('sidebar-nav')
        menu.find_element_by_id('sidebarTree_16_a').click()
        ul = self.dr.find_element_by_id('sidebarTree_16_ul')
        ul.find_element_by_id('sidebarTree_18_a').click()
        time.sleep(3)
        main = self.dr.find_element_by_xpath('//*[@id="wrapper"]/div[2]/div[1]')
        main.find_element_by_xpath('//*[@id="searchForm"]/div[1]/input').send_keys('测试')
        main.find_element_by_xpath('//*[@id="searchForm"]/div[2]/input').send_keys('15566595533	')
        main.find_element_by_xpath('//*[@id="searchForm"]/div[3]/input').send_keys('test')
        role = main.find_element_by_id('role_id')
        Select(role).select_by_value('cd40e89572b747eb80b3670646217275')
        main.find_element_by_xpath('//*[@id="defaultUserInfo"]').click()
        main.find_element_by_xpath('//*[@id="addUserInfo"]').click()
        add = self.dr.find_element_by_xpath('//*[@id="addDate"]/div/div')
        add.find_element_by_xpath('//*[@id="defaultForm"]/div[1]/div/input').send_keys('t')
        add.find_element_by_xpath('//*[@id="defaultForm"]/div[2]/div/input').send_keys('111')
        add.find_element_by_xpath('//*[@id="defaultForm"]/div[3]/div/input').send_keys('y')
        add.find_element_by_xpath('//*[@id="defaultForm"]/div[4]/div/input').send_keys('666666')
        add.find_element_by_xpath('//*[@id="defaultForm"]/div[5]/div/input').send_keys('15066595533')
        gender = add.find_element_by_xpath('//*[@id="defaultForm"]/div[6]/div/select')
        Select(gender).select_by_value('2')
        add.find_element_by_xpath('//*[@id="defaultForm"]/div[7]/div/input[1]').click()
        jg = self.dr.find_element_by_xpath('//*[@id="orgDig"]/div/div')
        jggl=jg.find_element_by_xpath('//*[@id="orgDig"]/div/div/div[2]/div')
        jgglul = jggl.find_element_by_xpath('//*[@id="tree"]')
        jgglul.find_element_by_xpath('//*[@id="tree_1_switch"]').click()
        jgul = jggl.find_element_by_xpath('//*[@id="tree_1_ul"]')
        jgul.find_element_by_xpath('//*[@id="tree_15_a"]').click()
        jg.find_element_by_xpath('//*[@id="addOrg"]').click()
        js = add.find_element_by_xpath('//*[@id="defaultForm"]/div[8]/div/select')
        Select(js).select_by_value('cd40e89572b747eb80b3670646217275')
        add.find_element_by_xpath('//*[@id="addUserInfoConfig"]').click()

    def tearDown(self):
        time.sleep(5)
        title = self.dr.find_element_by_xpath('//*[@id="wrapper"]')
        cs = title.find_element_by_xpath('//*[@id="wrapper"]/nav')
        div = cs.find_element_by_xpath('//*[@id="navbar-menu"]')
        divul = div.find_element_by_xpath('//*[@id="navbar-menu"]/ul')
        divul.find_element_by_css_selector('#navbar-menu > ul > li').click()
        ul = div.find_element_by_xpath('//*[@id="navbar-menu"]/ul/li/ul')
        ul.find_element_by_xpath('//*[@id="navbar-menu"]/ul/li/ul/li[4]').click()
        tc = self.dr.find_element_by_xpath('//*[@id="myModal"]')
        ck = tc.find_element_by_xpath('//*[@id="myModal"]/div/div')
        ck1 = ck.find_element_by_xpath('//*[@id="myModal"]/div/div/div[3]')
        ck1.find_element_by_xpath('//*[@id="exits"]').click()
        for x in range(5):
            print(msg5 = menu.isElementExist(menu.button_list[6]))
if __name__ == "__main__":
    unittest.main()



