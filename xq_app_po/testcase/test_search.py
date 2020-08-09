import pytest
from xq_app_po.base.app import App


class TestSearch:
    def setup(self):
        self.main = App().start().main()


    def test_search(self):
        price = self.main.goto_search_page().search("alibaba").get_price("BABA")
        assert price > 200