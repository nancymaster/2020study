import logging

import yaml
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

from xq_app_po.page.deal_black import deal_black


class BasePage:
    driver: WebDriver
    logging.basicConfig(level=logging.INFO)

    def __init__(self, driver=None):
        self.driver = driver

    @deal_black
    def finds(self, locator):
        logging.info(f"finds elements：{locator}")
        return self.driver.find_elements(*locator)

    @deal_black
    def find(self, locator, value: str = None):
        logging.info(f'find:{locator}')
        # find ele, clear error num
        if isinstance(locator, tuple):
            result = self.driver.find_element(*locator)
        else:
            result = self.driver.find_element(locator, value)
        return result

    def find_and_click(self, locator):
        logging.info('click')
        self.find(locator).click()

    def find_and_sendkeys(self, locator, text):
        logging.info(f'sendkeys: {text}')
        self.find(locator).send_keys(text)

    def find_and_scroll(self, text):
        logging.info(f'scroll find: {text}')
        return self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                        'new UiScrollable'
                                        '(new UiSelector().'
                                        'scrollable(true).'
                                        'instance(0)).'
                                        'scrollIntoView('
                                        'new UiSelector().'
                                        f'text("{text}").instance(0));')

    def webdriver_wait(self, locator, timeout=10):
        logging.info(f'webdriver wait: {locator}, timeout: {timeout}')
        element = WebDriverWait(self.driver, timeout).until(
            lambda x: x.find_element(*locator))
        return element

    def back(self, num=1):
        logging.info(f'back: {num}')
        for i in range(num):
            self.driver.back()

    def set_implicitly_wait(self, time=3):
        self.driver.implicitly_wait(time)

    # use yml to go steps
    def yml_step(self, yml_path):
        with open(yml_path, encoding="utf-8") as f:
            steps = yaml.safe_load(f)
        logging.info(f'读取step.yml: {steps}')

        self.set_implicitly_wait(20)
        for step in steps:
            if "action" in step.keys():
                action = step["action"]
                locator = (step["by"], step["locator"])
                if "click" == action:
                    self.find_and_click(locator)
                if "send" == action:
                    self.find_and_click(locator)
                    self.find_and_sendkeys(locator, step["value"])

