from appium.webdriver.common.mobileby import MobileBy

from .basepage import BasePage
from ..page.search import Search


class Main(BasePage):
    def goto_search_page(self):
        self.find(MobileBy.ID, "tv_search").click()
        return Search(self._driver)