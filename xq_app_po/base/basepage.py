import logging

from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    driver: WebDriver
    logging.basicConfig(level=logging.INFO)

    def __init__(self, driver=None):
        self.driver = driver

    def find(self, locator, value: str = None):
        logging.info(f'find:{locator}')
        if isinstance(locator, tuple):
            return self.driver.find_element(*locator)
        else:
            return self.driver.find_element(locator, value)

    def find_eles(self, locator):
        logging.info(f"find eles：{locator}")
        return self.driver.find_elements(*locator)

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


