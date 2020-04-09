'''
Code description： parmentquery_page
Create time；
Developer
'''
import time
import sys
import logging
from  selenium.webdriver.common.by import By
from framfriend.test_case.models.log import Logger
from framfriend.test_case.page_obj.base_page import BasePage
Log =Logger(__name__,CmdLevel=logging.INFO,FileLevel=logging.INFO)

class ParmentQuery_page(BasePage):

