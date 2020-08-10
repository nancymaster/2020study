from appium.webdriver.common.mobileby import MobileBy

from app_homework1.page.contactlistpage import ContactListPage


class MainPage:
    def __init__(self, driver):
        self.driver = driver

    def goto_contactlist(self):
        self.driver.find_element(MobileBy.XPATH,
                                 '//android.widget.TextView[@text="通讯录"]').click()
        return ContactListPage(self.driver)

    def goto_workbench(self):
        pass

