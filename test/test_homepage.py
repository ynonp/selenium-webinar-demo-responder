import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import pdb


class TestHomepage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def tearDown(self):
        self.driver.close()

    def test_homepage_title(self):
        self.driver.get('https://cp.responder.co.il/')
        self.assertEqual('רב מסר - שיווק חכם בדואר אלקטרוני', self.driver.title)

    def test_homepage_forces_https(self):
        self.driver.get('https://cp.responder.co.il/')
        self.assertTrue(self.driver.current_url.startswith('https://'))

    def test_tabs_work(self):
        self.driver.implicitly_wait(5)
        self.driver.get('https://cp.responder.co.il')
        self.driver.find_element_by_css_selector('a[href="#forgot"]').click()
        self.driver.find_element_by_css_selector('#forgot.active')
        self.assertTrue(self.driver.find_element_by_css_selector('#forgot').is_displayed())
        self.assertFalse(self.driver.find_element_by_css_selector('#login').is_displayed())

        self.driver.find_element_by_css_selector('a[href="#login"]').click()
        self.driver.find_element_by_css_selector('#login.active')

        self.assertFalse(self.driver.find_element_by_css_selector('#forgot').is_displayed())
        self.assertTrue(self.driver.find_element_by_css_selector('#login').is_displayed())

if __name__ == '__main__':
    unittest.main()

