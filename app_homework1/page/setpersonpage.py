from appium.webdriver.common.mobileby import MobileBy

from app_homework1.page.basepage import BasePage
from app_homework1.page.editperson import EditPerson


class SetPersonPage(BasePage):
    editperson_ele = (MobileBy.XPATH, "//*[@text='编辑成员']")

    def click_edit(self):
        self.find_and_click(self.editperson_ele)
        return EditPerson(self.driver)