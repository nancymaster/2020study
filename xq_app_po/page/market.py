from appium.webdriver.common.mobileby import MobileBy

from xq_app_po.base.basepage import BasePage
from xq_app_po.page.search import SearchPage


class MarketPage(BasePage):
    _search_ele = (MobileBy.ID, "action_search")

    def click_search(self):
        self.find_and_click(self._search_ele)
        return SearchPage(self.driver)
