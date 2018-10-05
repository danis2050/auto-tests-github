import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class AddToBasketTests(unittest.TestCase):

    baseURL = "https://zoloto585.ru/"

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def test_add_ring_to_basket(self):
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
        driver.find_element_by_css_selector("a.cart__clearLink").click()
        driver.find_element_by_css_selector("button.modal__button.modal__button--ok").click()
        self.assertEqual("Пустая", driver.find_element_by_css_selector("p").text)
        driver.back()





    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()