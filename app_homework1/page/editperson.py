from appium.webdriver.common.mobileby import MobileBy

from app_homework1.page.basepage import BasePage


class EditPerson(BasePage):
    delperson_ele = (MobileBy.XPATH, "//*[@text='删除成员']")
    confirm_ele = (MobileBy.XPATH, "//*[@text='确定']")

    def click_del(self):
        self.webdriver_wait(self.delperson_ele)
        self.find_and_click(self.delperson_ele)
        self.find_and_click(self.confirm_ele)
        from app_homework1.page.searchpage import SearchPage
        return SearchPage(self.driver)
