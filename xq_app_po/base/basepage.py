import logging

from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    driver: WebDriver
    logging.basicConfig(level=logging.INFO)

    _black_list = [
        (MobileBy.ID, "iv_close")
    ]
    _max_err_num = 3
    _err_num = 0

    def __init__(self, driver=None):
        self.driver = driver

    def finds(self, locator):
        logging.info(f"finds elements：{locator}")
        return self.driver.find_elements(*locator)

    def find(self, locator, value: str = None):
        logging.info(f'find:{locator}')
        try:
            # find ele, clear error num
            if isinstance(locator, tuple):
                result = self.driver.find_element(*locator)
            else:
                result = self.driver.find_element(locator, value)
            self._err_num = 0
            return result
        except Exception as e:
            # not find ele, use black_list
            if self._err_num > self._max_err_num:
                # find num max, clear error num and raise
                self._err_num = 0
                raise e
            self._err_num += 1
            for ele in self._black_list:
                # click black_list
                eles = self.finds(ele)
                if len(eles) > 0:
                    eles[0].click()
                    return self.find(locator)
            raise ValueError("元素不在黑名单")

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

