from appium.webdriver.common.mobileby import MobileBy

from ..base.basepage import BasePage


class SearchPage(BasePage):
    _search_ele = (MobileBy.ID, 'search_input_text')
    _searchst_ele = (MobileBy.ID, 'name')
    _price_ele = (MobileBy.ID, "current_price")

    def search_text(self, key):
        self.find_and_sendkeys(self._search_ele, key)
        self.find_and_click(self._searchst_ele)
        return self

    def get_price(self, key):
        price = self.find(self._price_ele).text
        return float(price)
