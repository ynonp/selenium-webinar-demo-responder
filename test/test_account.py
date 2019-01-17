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


class TestAccount(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.implicitly_wait(5)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

    def setUp(self):
        self.driver.delete_all_cookies()

    def test_login(self):
        self.login()
        body = self.driver.find_element_by_css_selector('body')
        self.assertEqual('ab_controlpanel', body.get_attribute('class'))

    def test_logout(self):
        self.login()
        menu = self.driver.find_element_by_css_selector('#menu1 a[href="account_editsettings.php"]')
        item = self.driver.find_element_by_css_selector('#menu1 a[href="logout.php"]')

        ActionChains(self.driver).move_to_element(menu).click(item).perform()

        # wait until #username is visible
        self.driver.find_element_by_css_selector('#username')

        body = self.driver.find_element_by_css_selector('body')
        self.assertEqual('', body.get_attribute('class'))

    def test_change_email_requires_password(self):
        self.login()
        menu = self.driver.find_element_by_css_selector('#menu1 a[href="account_editsettings.php"]')
        menu.click()
        email = self.driver.find_element_by_css_selector('input[name="users_email"]')
        email.clear()
        email.send_keys('ynon@tocode.co.il')
        email.submit()

        wait = WebDriverWait(self.driver, 10)
        alert = wait.until(EC.alert_is_present())
        alert.accept()

        el = self.driver.find_element_by_css_selector(':focus')
        self.assertEqual('users_password', el.get_attribute('name'))

    def login(self):
        self.driver.get('https://cp.responder.co.il/')
        us = self.driver.find_element_by_css_selector('#username')
        ps = self.driver.find_element_by_css_selector('#password')
        us.send_keys('ynonp3')
        ps.send_keys('1020304050')
        us.submit()



if __name__ == '__main__':
    unittest.main()
