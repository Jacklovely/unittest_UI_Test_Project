'''
Code description：save all driver info
Create time：
Developer：
'''
import time

from selenium import webdriver
import logging
import sys
from framfriend.test_case.models.log import Logger

log = Logger(__name__, CmdLevel=logging.INFO, FileLevel=logging.INFO)
class WDriver(object):

    # Firefox driver
    def fireFoxDriver(self):
        """

        :return:
        """
        try:
            self.driver = webdriver.Firefox()
        except Exception as e:
            log.logger.exception('FireFoxDriverServer.exe executable needs to be in PATH. Please download!', exc_info=True)
            raise e
        else:
            log.logger.info('%s:found the Firefox driver [%s] successed !' %(sys._getframe().f_code.co_name,self.driver))
            return self.driver

    # chrom driver
    def chromeDriver(self):
        """

        :return:
        """
        try:
            chromeOptions = webdriver.ChromeOptions()
            prefs = {"download.default_directory": "F:\\TestDownloads"}
            chromeOptions.add_experimental_option("prefs", prefs)
            self.driver = webdriver.Chrome(options=chromeOptions)
            time.sleep(10)

        except Exception as e:
            log.logger.exception('ChromeDriverServer.exe executable needs to be in PATH. Please download!',
                                 exc_info=True)
            raise e
        else:
            log.logger.info('%s:found the chrome driver [%s] successed !' % (sys._getframe().f_code.co_name, self.driver))
            return self.driver


    # Ie driver
    def ieDriver(self):
        """

        :return:
        """
        try:
            self.driver = webdriver.Ie()
        except Exception as e:
            log.logger.exception('IEDriverServer.exe executable needs to be in PATH. Please download!',
                                 exc_info=True)
            raise e
        else:
            log.logger.info('%s:found the IE driver [%s] successed !' % (sys._getframe().f_code.co_name, self.driver))
            return self.driver


if __name__ == '__main__':
    WDrive=WDriver()
    WDrive.chromeDriver()

