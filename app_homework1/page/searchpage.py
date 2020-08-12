from appium.webdriver.common.mobileby import MobileBy

from app_homework1.page.basepage import BasePage
from app_homework1.page.context import Context
from app_homework1.page.personinfopage import PersonInfoPage


class SearchPage(BasePage):
    search_input_ele = (MobileBy.ID, 'com.tencent.wework:id/fxc')
    # search_result_ele = (MobileBy.XPATH, '')

    def search_result(self, text):
        return self.find_eles((MobileBy.XPATH, f"//*[@text='{text}']"), 3)

    def search_name(self, text):
        self.find_and_sendkeys(self.search_input_ele, text)
        search_result = self.search_result(text)
        setattr(Context, "search_result", search_result)
        if len(search_result) < 2:
            print("没有这个联系人")
            return
        else:
            search_result[1].click()
        return PersonInfoPage(self.driver)

