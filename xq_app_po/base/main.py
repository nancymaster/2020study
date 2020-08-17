from appium.webdriver.common.mobileby import MobileBy

from .basepage import BasePage
from ..page.market import MarketPage
from ..page.search import SearchPage


class MainPage(BasePage):
    _search_ele = (MobileBy.ID, "tv_search")
    _market_ele = (MobileBy.XPATH, "//*[@resource-id='android:id/tabs']//*[@text='行情']")
    _edit_ele = (MobileBy.ID, "post_status")

    def goto_search_page(self):
        self.find_and_click(self._search_ele)
        return SearchPage(self.driver)

    def goto_market(self):
        #self.driver.implicitly_wait(5)
        self.find_and_click(self._edit_ele)  # 伪造黑名单
        self.find_and_click(self._market_ele)
        return MarketPage(self.driver)
