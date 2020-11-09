#_*_ coding:utf-8 _*_
import configparser
import os.path
from framework.logger_record import LoggerRecord
from selenium import webdriver

logger = LoggerRecord("BrowserEngine").getlog()
print("BrowserEngine logger为%s" % logger)

class BrowserEngine(object):
    dir = os.path.dirname(os.path.abspath('.'))
    chrome_driver_path = dir + '/tools/chromedriver.exe'

    def __init__(self):
        pass

    def open_browser(self):
        config = configparser.ConfigParser()
        file_path = os.path.dirname(os.getcwd()) + '/config/config.ini'
        config.read(file_path, encoding='utf-8')

        browser = config.get("browserType", "browserName")
        print(browser)
        url = config.get("testServer", "URL")
        print(url)
        logger.info("You had select %s browser" % browser)
        logger.info("The test server url is : %s" % url)

        if browser == 'Chrome':
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument('--no-sandbox')
            driver = webdriver.Chrome(options=chrome_options)
            logger.info("Start Chrome browser.")

        elif browser == 'Firefox':
            driver = webdriver.Firefox()
            logger.info("Start firefox browser.")

        elif browser == 'IE':
            driver = webdriver.Ie()
            logger.info("Start IE browser.")

        driver.get(url)
        logger.info("Open url: %s" % url)
        driver.maximize_window()
        logger.info("Maximize the current window.")
        driver.implicitly_wait(10)
        logger.info("Set implicitly wait 10 seconds")
        return driver

    def quit_browser(self):
        logger.info("Now, close and quit the browser")
        self.open_browser().quit()



