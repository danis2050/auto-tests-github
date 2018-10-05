import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class ChooseCityTests(unittest.TestCase):

    baseURL = "https://zoloto585.ru/"

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def test_choose_city_moscow(self):
        driver = self.driver
        driver.get(self.baseURL)
        driver.find_element_by_css_selector("#choose-city>span").click()
        driver.find_element_by_xpath("(//a[contains(text(),'Москва')])[2]").click()
        self.assertEqual("МОСКВА", driver.find_element_by_css_selector("#choose-city>span").text)
        driver.find_element_by_xpath("//button[contains(text(),'Да, верно')]").click()
        self.assertEqual("МОСКВА", driver.find_element_by_css_selector("#choose-city>span").text)

    def test_choose_city_saintpetersburg(self):
        driver = self.driver
        driver.get(self.baseURL)
        driver.find_element_by_css_selector("#choose-city>span").click()
        driver.find_element_by_xpath("(//a[contains(text(),'Санкт-Петербург')])[2]").click()
        self.assertEqual("САНКТ-ПЕТЕРБУРГ", driver.find_element_by_css_selector("#choose-city>span").text)
        driver.find_element_by_xpath("//button[contains(text(),'Да, верно')]").click()
        self.assertEqual("САНКТ-ПЕТЕРБУРГ", driver.find_element_by_css_selector("#choose-city>span").text)

    def test_choose_city_ufa(self):
        driver = self.driver
        driver.get(self.baseURL)
        driver.find_element_by_css_selector("#choose-city>span").click()
        driver.find_element_by_xpath("//a[contains(text(),'Уфа')]").click()
        self.assertEqual("УФА", driver.find_element_by_css_selector("#choose-city>span").text)
        driver.find_element_by_xpath("//button[contains(text(),'Да, верно')]").click()
        self.assertEqual("УФА", driver.find_element_by_css_selector("#choose-city>span").text)

    def test_choose_city_samara(self):
        driver = self.driver
        driver.get(self.baseURL)
        driver.find_element_by_css_selector("#choose-city>span").click()
        driver.find_element_by_xpath("//a[contains(text(),'Самара')]").click()
        self.assertEqual("САМАРА", driver.find_element_by_css_selector("#choose-city>span").text)

    def test_choose_city(self):
        driver = self.driver
        driver.get(self.baseURL)
        driver.find_element_by_css_selector("#choose-city>span").click()
        driver.find_element_by_xpath("(//a[contains(text(),'Москва')])[2]").click()
        self.assertEqual("МОСКВА", driver.find_element_by_css_selector("#choose-city>span").text)
        driver.find_element_by_css_selector("#choose-city>span").click()
        driver.find_element_by_xpath("//a[contains(text(),'Самара')]").click()
        self.assertEqual("САМАРА", driver.find_element_by_css_selector("#choose-city>span").text)
        driver.find_element_by_css_selector("#choose-city>span").click()
        driver.find_element_by_xpath("//a[contains(text(),'Уфа')]").click()
        self.assertEqual("УФА", driver.find_element_by_css_selector("#choose-city>span").text)
        driver.find_element_by_xpath("//button[contains(text(),'Да, верно')]").click()
        self.assertEqual("УФА", driver.find_element_by_css_selector("#choose-city>span").text)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()