from appium import webdriver

from app_homework1.page.mainpage import MainPage


class App:
    def start(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        # desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = 'emulator-5554'
        desired_caps['noReset'] = 'true'
        desired_caps['appPackage'] = 'com.tencent.wework'
        desired_caps['appActivity'] = '.launch.WwMainActivity'
        desired_caps['skipServerInstallation'] = 'true'
        desired_caps['skipDeviceInitialization'] = 'true'
        desired_caps['settings[waitForIdleTimeout]'] = 0
        # desired_caps['automationName'] = 'UiAutomator2'
        desired_caps['showChromedriverLog'] = True

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)
        return self

    def restart(self):
        self.driver.close()
        self.driver.launch_app()
        return self

    def stop(self):
        self.driver.quit()

    def goto_main(self):
        return MainPage(self.driver)
