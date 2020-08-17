from xq_app_po.base.app import App


class TestMarket:
    def setup_class(self):
        self.app = App()

    def teardown_class(self):
        self.app.stop()

    def test_market(self):
        self.app.start().goto_main().goto_market()

def wrapper(fun):
    def hello(*args, **kwargs):
        print("1")
        fun(*args, **kwargs)
        print("2")
    return hello


def test_tmp1():
    tmp2()

@wrapper
def tmp2():
    print("tmp2")