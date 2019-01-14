import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class TestHomepage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()

