import pytest
import yaml

from app_homework1.page.app import App
from app_homework1.page.context import Context
from app_homework1.page.getdata import Datas

addcontactdatas = Datas().get_data('addcontact')
delcontactdatas = Datas().get_data('delcontactdatas')

class TestContact:
    def setup_class(self):
        self.app = App()
        self.main = self.app.start().goto_main()

    def teardown(self):
        self.app.back()

    @pytest.mark.parametrize('name,sex,phone', addcontactdatas)
    def test_addcontact(self, name, sex, phone):
        mypage = self.main.goto_contactlist().addcontact().add_menual().set_name(name).set_sex(sex).set_phone(phone).click_save()
        text = mypage.get_toast()
        assert '成功' in text


    @pytest.mark.parametrize('name', delcontactdatas)
    def test_delcontact(self, name):
        result_after = self.main.goto_contactlist().search_contact().search_name(name).click_setbutton()\
            .click_edit().click_del().search_result(name)

        result_before = getattr(Context, "search_result")
        assert len(result_before) - 1 == len(result_after)

