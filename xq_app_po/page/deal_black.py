from appium.webdriver.common.mobileby import MobileBy


def deal_black(func):
    def wrapper(*args, **kwargs):
        _black_list = [
            (MobileBy.ID, "iv_close")
        ]
        _max_err_num = 3
        _err_num = 0
        # self arg
        from xq_app_po.base.basepage import BasePage
        instance: BasePage = args[0]
        try:
            result = func(*args, **kwargs)
            _err_num = 0
            instance.set_implicitly_wait(20)
            return result
        except Exception as e:
            instance.set_implicitly_wait(1)
            # not find ele, use black_list
            if _err_num > _max_err_num:
                # find num max, clear error num and raise
                _err_num = 0
                raise e
            _err_num += 1
            for ele in _black_list:
                # click black_list
                eles = instance.finds(ele)
                if len(eles) > 0:
                    eles[0].click()
                    return wrapper(*args, **kwargs)
            raise ValueError("元素不在黑名单")

    return wrapper
