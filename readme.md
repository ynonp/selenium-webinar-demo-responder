python + selenium

## Agenda

1. Homepage
  * HTTPS is required
  * Tab functionality works

2. Account
  * Login works
  * Logout works
  * Change email requires password
  * Can change email

## Cheat Sheet

### Test File Starter

```
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

class TestHomepage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.close()

    def test_something(self):
        pass

if __name__ == '__main__':
    unittest.main()
```

### Driver Commands

Visit a page:

```
self.driver.get('https://www.tocode.co.il')
```

Find element and click it

```
el = self.driver.find_element_by_css_selector('#forgot')
el.click()
```

Get current url

```
self.driver.current_url
```

Get current page title

```
self.driver.title
```

Set implicit wait

```
driver.implicitly_wait(10)
```

### Other Python Tips

Put a breakpoint

```
import pdb
pdb.set_trace()
```

### Useful links

Unit test reference:

https://docs.python.org/3/library/unittest.html

Python Selenium Docs
https://selenium-python.readthedocs.io/index.html
