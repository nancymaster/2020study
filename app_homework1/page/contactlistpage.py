from appium.webdriver.common.mobileby import MobileBy

from app_homework1.page.addmenberpage import AddMenberPage
from app_homework1.page.basepage import BasePage
from app_homework1.page.searchpage import SearchPage


class ContactListPage(BasePage):
    addmenber_text = "添加成员"
    search_ele = (MobileBy.ID, "com.tencent.wework:id/h9z")

    def addcontact(self):
        self.find_and_scroll(self.addmenber_text).click()
        return AddMenberPage(self.driver)

    def search_contact(self):
        self.find_and_click(self.search_ele)
        return SearchPage(self.driver)