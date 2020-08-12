from appium.webdriver.common.mobileby import MobileBy

from app_homework1.page.basepage import BasePage
from app_homework1.page.setpersonpage import SetPersonPage


class PersonInfoPage(BasePage):
    set_ele = (MobileBy.ID, 'com.tencent.wework:id/h9p')

    def click_setbutton(self):
        self.webdriver_wait(self.set_ele)
        self.find_and_click(self.set_ele)
        return SetPersonPage(self.driver)
