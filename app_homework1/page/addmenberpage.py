from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait

from app_homework1.page.basepage import BasePage
from app_homework1.page.contactaddpage import ContactAddPage


class AddMenberPage(BasePage):
    add_manual_element = (MobileBy.XPATH,
                          '//android.widget.TextView[@text="手动输入添加"]')

    def add_menual(self):
        self.find_and_click(self.add_manual_element)
        return ContactAddPage(self.driver)

    def get_toast(self):
        element = self.webdriver_wait(self.toast_ele)
        return element.text