from xq_app_po.base.app import App


class TestMarket:
    def setup_class(self):
        self.app = App()

    def teardown_class(self):
        self.app.stop()

    def test_market(self):
        self.app.start().goto_main().goto_market()