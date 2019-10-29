import time
import unittest
from telnetlib import EC

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class Test(unittest.TestCase):
    def setUp(self):
        '''启动浏览器'''
        self.dr = webdriver.Chrome()
        self.dr.maximize_window()

    def test1(self):
        self.dr.get('http://www.baidu.com')
        #输入js 字段
        loc = (By.ID,'kw')
        WebDriverWait(self.dr,10).until(EC.visibility_of_element_located(loc)) # 显式等待元素可定位
        time.sleep(0.3)
        self.dr.find_element(*loc).send_keys('js',Keys.ENTER) # 键盘操作，enter 键
        loc = (By.XPATH,'//*[@id="5001"]/div[1]/h3/a[1]')
        WebDriverWait(self.dr,10).until(EC.visibility_of_element_located(loc)) # 等待元素可见，可以定位
        ele = self.dr.find_element(*loc) # 定位到元素
        self.dr.execute_script('arguments[0].scrollIntoView(false)',ele)
        time.sleep(3)
        # self.dr.execute_script('window.scrollTo(0,document.body.scrollHeight)') # 滚动到页面底部
        # time.sleep(3)
        # self.dr.execute_script('window.scrollTo(document.body.scrollHeight,0)') #滚动到页面顶部
        # time.sleep(3)
        # ele.click()
        # self.dr.quit()
