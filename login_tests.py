import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import xmlrunner

class LoginTests(unittest.TestCase):

    baseURL = "https://zoloto585.ru/"
    testcard = "1120000057829130"
    testphone = "79162001459"

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def test_login_by_card(self):
        driver = self.driver
        driver.get(self.baseURL)
        driver.find_element_by_css_selector("#app>header>div.section.header-middle>div>div.header-middle__login>div.header-middle__login-block>div>a:nth-child(1)").click()
        input_cardnumber_element = driver.find_element_by_name("cardNumber")
        input_cardnumber_element.click()
        input_cardnumber_element.send_keys(Keys.HOME + self.testcard)
        driver.find_element_by_css_selector("button.reg-card-content__form-btn").click()
        self.assertEqual(self.testcard, driver.find_element_by_css_selector("#app>header>div.section.header-middle>div>div.header-middle__login>div.header-middle__login-block>div.auth>div.card").text)

    def test_login_by_phone(self):
        driver = self.driver
        driver.get("https://zoloto585.ru")
        driver.find_element_by_css_selector("#app>header>div.section.header-middle>div>div.header-middle__login>div.header-middle__login-block>div>a:nth-child(1)").click()
        driver.find_element_by_css_selector("#app>div.v--modal-overlay>div.v--modal-box.v--modal>div>div.reg-card-content__form>form>div:nth-child(4)>a").click()
        input_phone_element = driver.find_element_by_name("phone")
        input_phone_element.click()
        input_phone_element.send_keys(Keys.HOME + self.testphone)
        driver.find_element_by_css_selector("button.reg-card-content__form-btn").click()
        self.assertEqual(self.testcard, driver.find_element_by_css_selector("#app>header>div.section.header-middle>div>div.header-middle__login>div.header-middle__login-block>div.auth>div.card").text)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'))