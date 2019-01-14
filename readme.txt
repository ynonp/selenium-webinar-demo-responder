python + selenium

## Agenda

1. Homepage
  * HTTPS is required
  * Tab functionality works
  * Refresh captcha changes the image
  * Trial signup link appears and works

2. Account
  * Login works
  * Logout works
  * Change email requires password
  * Change password requires password
  * Can change email
  * Can change password

3. Email Editor
  * Can change message type
  * Can open page editor
  * Can set values in fields and save
  * Warning is shown if exiting before all fields are set




## Cheat Sheet

### Test File Starter

```
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

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


