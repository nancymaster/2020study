from appium.webdriver.common.mobileby import MobileBy

from ..base.basepage import BasePage


class Search(BasePage):
    def search(self, key):
        self.find(MobileBy.ID, 'search_input_text').send_keys(key)
        self.find(MobileBy.ID, 'name').click()
        return self

    def get_price(self, key):
        price = self.find(MobileBy.ID, "current_price").text
        return float(price)
