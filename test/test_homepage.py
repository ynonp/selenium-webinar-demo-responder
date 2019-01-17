import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select

import pdb
import time


class TestHomepage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.implicitly_wait(5)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

    def setUp(self):
        self.driver.delete_all_cookies()

    def test_title(self):
        self.driver.get('https://cp.responder.co.il/')
        self.assertEqual('רב מסר - שיווק חכם בדואר אלקטרוני', self.driver.title)

    def test_refresh_photo_when_cant_connect(self):
        self.driver.get('https://cp.responder.co.il/')
        el = self.driver.find_element_by_css_selector('#loginTabs a[href="#forgot"]')
        el.click()
        img = self.driver.find_element_by_css_selector('#captcha')
        src1 = img.get_attribute('src')
        refresh = self.driver.find_element_by_css_selector('#captcha + a')
        refresh.click()

        img = self.driver.find_element_by_css_selector('#captcha')
        src2 = img.get_attribute('src')

        self.assertTrue(src1 != src2)


if __name__ == '__main__':
    unittest.main()
