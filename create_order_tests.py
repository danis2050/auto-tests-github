import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class AddToBasketTests(unittest.TestCase):

    baseURL = "https://zoloto585.ru/"
    testcard = "1120000057829130"
    testphone = "79162001459"

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def test_create_order_for_ring(self):
        driver = self.driver
        driver.get(self.baseURL)
        driver.find_element_by_css_selector("#choose-city>span").click()
        driver.find_element_by_xpath("(//a[contains(text(),'Москва')])[2]").click()
        self.assertEqual("МОСКВА", driver.find_element_by_css_selector("#choose-city>span").text)
        driver.find_element_by_xpath("//button[contains(text(),'Да, верно')]").click()
        self.assertEqual("МОСКВА", driver.find_element_by_css_selector("#choose-city>span").text)
        driver.get(self.baseURL)
        driver.find_element_by_css_selector("#nav-item-1>a").click()
        driver.find_element_by_xpath("(//img[@alt='Кольцо обручальное с алмазной гранью из красного золота 585 пробы'])[1]").click()
        driver.find_element_by_xpath("(//a[contains(text(),'Добавить в корзину')])[2]").click()
        driver.find_element_by_xpath("(//a[contains(text(),'Перейти в корзину')])[3]").click()
        driver.find_element_by_css_selector("button.b-button").click()
        driver.find_element_by_name("userName").send_keys("autotest")
        driver.find_element_by_name("userEmail").send_keys("autotest@zoloto585.ru")
        driver.find_element_by_name("smsPhone").send_keys(Keys.HOME + self.testphone)
        driver.find_element_by_xpath("(//button[@type='submit'])[3]").click()
        driver.find_element_by_name("smsCode").send_keys(Keys.HOME + "6543")
        driver.find_element_by_css_selector("#order-submit").click()
        self.assertEqual("БЛАГОДАРИМ ВАС ЗА ЗАКАЗ", driver.find_element_by_css_selector("div.section.basket__title.basket__title--step3>div>h4").text)


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()