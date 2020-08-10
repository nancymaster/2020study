from appium.webdriver.common.mobileby import MobileBy

from app_homework1.page.basepage import BasePage


class ContactAddPage(BasePage):
    def set_name(self, name):
        self.driver.find_element(MobileBy.XPATH,
                                 "//*[contains(@text,'姓名')]/../*[@class='android.widget.EditText']").send_keys(name)
        return self

    def set_sex(self, sex):
        self.driver.find_element(MobileBy.XPATH,
                                 "//*[contains(@text,'性别')]/..//*[@text='男']").click()
        if sex == '男':
            self.driver.find_element(MobileBy.XPATH, "//*[@text='男']").click()
        else:
            self.driver.find_element(MobileBy.XPATH, "//*[@text='女']").click()
        return self

    def set_phone(self, phone):
        self.driver.find_element(MobileBy.XPATH, "//*[@text='手机号']").send_keys(phone)
        return self

    def click_save(self):
        from app_homework1.page.addmenberpage import AddMenberPage
        self.driver.find_element(MobileBy.XPATH,
                                 ' //android.widget.TextView[@text="保存"]').click()
        return AddMenberPage(self.driver)