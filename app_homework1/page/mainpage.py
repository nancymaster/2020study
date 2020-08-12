from appium.webdriver.common.mobileby import MobileBy

from app_homework1.page.basepage import BasePage
from app_homework1.page.contactlistpage import ContactListPage


class MainPage(BasePage):
    contactlist = (MobileBy.XPATH,
                   '//android.widget.TextView[@text="通讯录"]')

    def goto_contactlist(self):
        self.find_and_click(self.contactlist)
        return ContactListPage(self.driver)

    def goto_workbench(self):
        pass

