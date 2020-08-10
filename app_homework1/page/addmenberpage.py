from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait

from app_homework1.page.basepage import BasePage
from app_homework1.page.contactaddpage import ContactAddPage


class AddMenberPage(BasePage):
    def add_menual(self):
        self.driver.find_element(MobileBy.XPATH,
                                 '//android.widget.TextView[@text="手动输入添加"]').click()
        return ContactAddPage(self.driver)

    def get_toast(self):
        element = WebDriverWait(self.driver, 30).until(lambda x: x.find_element(MobileBy.XPATH,
                                                                       "//*[@class='android.widget.Toast']"))
        return element.text