from appium import webdriver
from .basepage import BasePage
from .main import MainPage


class App(BasePage):
    _package = "com.xueqiu.android"
    _activity = ".view.WelcomeActivityAlias"

    def start(self):
        if self.driver is None:
            desired_caps = {}
            desired_caps['platformName'] = 'Android'
            # desired_caps['platformVersion'] = '6.0'
            desired_caps['deviceName'] = 'emulator-5554'
            desired_caps['noReset'] = 'true'
            desired_caps['appPackage'] = self._package
            desired_caps['appActivity'] = self._activity
            desired_caps['skipServerInstallation'] = 'true'
            desired_caps['skipDeviceInitialization'] = 'true'
            # desired_caps['settings[waitForIdleTimeout]'] = 0
            # desired_caps['automationName'] = 'UiAutomator2'
            desired_caps['showChromedriverLog'] = True

            self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
            self.driver.implicitly_wait(30)
        else:
            self.driver.start_activity(self._package, self._activity)

        return self

    def stop(self):
        self.driver.quit()

    def goto_main(self) -> MainPage:
        return MainPage(self.driver)
