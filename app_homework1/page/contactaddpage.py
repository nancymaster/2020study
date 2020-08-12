from appium.webdriver.common.mobileby import MobileBy

from app_homework1.page.basepage import BasePage


class ContactAddPage(BasePage):
    name_element = (MobileBy.XPATH,
                    "//*[contains(@text,'姓名')]/../*[@class='android.widget.EditText']")
    sex_element = (MobileBy.XPATH,
                   "//*[contains(@text,'性别')]/..//*[@text='男']")
    male_ele = (MobileBy.XPATH, "//*[@text='男']")
    female_ele = (MobileBy.XPATH, "//*[@text='女']")
    phone_ele = (MobileBy.XPATH, "//*[@text='手机号']")
    save_ele = (MobileBy.XPATH,'//android.widget.TextView[@text="保存"]')

    def set_name(self, name):
        self.find_and_sendkeys(self.name_element, name)
        return self

    def set_sex(self, sex):
        self.find_and_click(self.sex_element)
        if sex == '男':
            self.find_and_click(self.male_ele)
        else:
            self.find_and_click(self.female_ele)
        return self

    def set_phone(self, phone):
        self.find_and_sendkeys(self.phone_ele, phone)
        return self

    def click_save(self):
        from app_homework1.page.addmenberpage import AddMenberPage
        self.find_and_click(self.save_ele)
        return AddMenberPage(self.driver)