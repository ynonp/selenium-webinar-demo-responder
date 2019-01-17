import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

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
        self.driver.get('https://cp.responder.co.il/login/account_editsettings.php')
        inp = self.driver.find_element_by_css_selector('input[name="users_username"]')
        username = inp.get_attribute('value')
        self.assertEqual('ynonp3', username)

    def test_logout(self):
        self.login()
        menu = self.driver.find_element_by_css_selector('#menu1 a[href="account_editsettings.php"]')
        item = self.driver.find_element_by_css_selector('.submenu a[href="logout.php"]')
        ActionChains(self.driver).move_to_element(menu).click(item).perform()
        self.driver.find_element_by_css_selector('#login')
        self.assertEqual('https://cp.responder.co.il/', self.driver.current_url)

    def test_change_email_requires_password(self):
        self.login()
        self.driver.get('https://cp.responder.co.il/login/account_editsettings.php')
        menu = self.driver.find_element_by_css_selector('#menu1 a[href="account_editsettings.php"]')
        menu.click()

        e = self.driver.find_element_by_css_selector('input[name="users_email"]')
        e.clear()
        e.send_keys('ynon@tocode.co.il')
        btn = self.driver.find_element_by_css_selector('form[action="do_change_name.php"] input[type="submit"]')
        btn.click()

        wait = WebDriverWait(self.driver, 10)
        alert = wait.until(EC.alert_is_present())
        alert.accept()

    def login(self):
        self.driver.get('https://cp.responder.co.il')
        self.driver.find_element_by_css_selector('#username').send_keys('ynonp3')
        self.driver.find_element_by_css_selector('#password').send_keys('1020304050')
        self.driver.find_element_by_css_selector('input[type="submit"]').click()
        self.driver.find_element_by_css_selector('#menu1')




if __name__ == '__main__':
    unittest.main()


