import base64
import os
import time
import unittest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='emulator-5554',
    language='en',
    locale='US'
)

appium_server_url = 'http://localhost:4723'

class TestAppium(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()

    def test_find_battery(self) -> None:
        self.driver.activate_app('com.gof.china')
        time.sleep(2)
        self.driver.update_settings({"fixImageTemplatescale": True})
        self.driver.implicitly_wait(10)

        current_dir = os.path.dirname(os.path.abspath(__file__))
        town_img = os.path.join(current_dir, "mei8.png")
        with open(town_img, 'rb') as png_file:
            b64_town_img = base64.b64encode(png_file.read()).decode('UTF-8')
        self.driver.find_element(AppiumBy.IMAGE, b64_town_img).click()

        # el = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="城镇"]')
        # el.click()
        time.sleep(20)

if __name__ == '__main__':
    unittest.main()