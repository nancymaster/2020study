from appium.webdriver.common.mobileby import MobileBy

from app_homework1.page.addmenberpage import AddMenberPage
from app_homework1.page.basepage import BasePage


class ContactListPage(BasePage):
    def addcontact(self):
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable'
                                 '(new UiSelector().'
                                 'scrollable(true).'
                                 'instance(0)).'
                                 'scrollIntoView('
                                 'new UiSelector().'
                                 'text("添加成员").instance(0));').click()
        return AddMenberPage(self.driver)

    def search_contact(self):
        pass