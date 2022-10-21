from selenium import webdriver
import unittest
from selenium.webdriver.common.by import By

class Google_open(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver= webdriver.Chrome("E:\\Driver\\chromedriver.exe")
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(3)
        cls.driver.get("https://www.google.com/")
        cls.driver.implicitly_wait(3)

    def test_search(self):
        self.driver.get("https://www.google.com/")
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.XPATH, '//input[@name="q"]').send_keys("Iphone 14")
        self.driver.find_element(By.XPATH, '//input[@name="q"]').submit()

