import pytest
import yaml
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait

with  open('../data/addcontact.yml') as f:
    addcontactdatas =yaml.safe_load(f)
'''
联系人用例
'''
class TestContact:
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        #desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = 'emulator-5554'
        desired_caps['noReset'] = 'true'
        desired_caps['appPackage'] = 'com.tencent.wework'
        desired_caps['appActivity'] = '.launch.WwMainActivity'
        desired_caps['skipServerInstallation'] = 'true'
        desired_caps['skipDeviceInitialization'] = 'true'
        desired_caps['settings[waitForIdleTimeout]'] = 0
       # desired_caps['automationName'] = 'UiAutomator2'

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)


    @pytest.mark.parametrize('name,sex,phone',addcontactdatas)
    def test_addcontact(self,name,sex,phone):
        '''
        打开应用-》点击通讯录-》添加成员-》输入用户名手机号性别-》点保存-》验证成功
        :return:
        '''
        self.driver.find_element(MobileBy.XPATH,
                                 '//android.widget.TextView[@text="通讯录"]').click()
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable'
                                 '(new UiSelector().'
                                 'scrollable(true).'
                                 'instance(0)).'
                                 'scrollIntoView('
                                 'new UiSelector().'
                                 'text("添加成员").instance(0));').click()
        self.driver.find_element(MobileBy.XPATH,
                                 '//android.widget.TextView[@text="手动输入添加"]').click()
        self.driver.find_element(MobileBy.XPATH,
                                 "//*[contains(@text,'姓名')]/../*[@class='android.widget.EditText']").send_keys(name)
        self.driver.find_element(MobileBy.XPATH,
                                 "//*[contains(@text,'性别')]/..//*[@text='男']").click()
        if sex == '男':
            self.driver.find_element(MobileBy.XPATH, "//*[@text='男']").click()
        else:
            self.driver.find_element(MobileBy.XPATH, "//*[@text='女']").click()

        self.driver.find_element(MobileBy.XPATH,"//*[@text='手机号']").send_keys(phone)
        self.driver.find_element(MobileBy.XPATH,
                                 ' //android.widget.TextView[@text="保存"]').click()
        element = WebDriverWait(self.driver, 30).until(lambda x: x.find_element(MobileBy.XPATH,
                                                                                "//*[@class='android.widget.Toast']"))
        result = element.text
        print(result)
        assert '添加成功' in result


    def test_delcontact(self):
        '''
                打开应用-》点击通讯录-》搜索成员-》点击成员-》编辑-》删除-》验证成功
                :return:
                '''
        self.driver.find_element(MobileBy.XPATH,
                                 '//android.widget.TextView[@text="通讯录"]').click()

    def teardown(self):
        self.driver.quit()