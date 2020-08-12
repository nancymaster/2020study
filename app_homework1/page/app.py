from appium import webdriver

from app_homework1.page.basepage import BasePage
from app_homework1.page.mainpage import MainPage


class App(BasePage):
    _package = "com.tencent.wework"
    _activity = ".launch.WwMainActivity"

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
            #desired_caps['settings[waitForIdleTimeout]'] = 0
            # desired_caps['automationName'] = 'UiAutomator2'
            # desired_caps['showChromedriverLog'] = True

            self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        else:
            #self.driver.start_activity(self._package, self._activity)
            self.driver.launch_app()

        self.driver.implicitly_wait(30)
        return self

    def restart(self):
        self.driver.close()
        self.driver.launch_app()
        return self

    def stop(self):
        self.driver.quit()

    def goto_main(self) -> MainPage:
        return MainPage(self.driver)
