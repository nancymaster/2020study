import pytest
import yaml

from app_homework1.page.app import App

with  open('../data/addcontact.yml') as f:
    addcontactdatas =yaml.safe_load(f)
class TestContact:
    def setup_class(self):
        self.app = App()
        self.main = self.app.start().goto_main()

    @pytest.mark.parametrize('name,sex,phone', addcontactdatas)
    def test_addcontact(self, name, sex, phone):
        mypage = self.main.goto_contactlist().addcontact().add_menual().set_name(name).set_sex(sex).set_phone(phone).click_save()
        text = mypage.get_toast()
        assert '成功' in text

