from WP_499.base.selenium_driver import SeleniumDriver
import pytest

class LoginPage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def login(self, username, password):
        self.sendKeys('user_login', username)
        self.sendKeys('user_pass', password)
        self.elementClick('wp-submit')

    def loginSuccess(self):
        result = self.isElementPresent('wpbody-content')
        return result

    def loginFailed(self):
        result = self.isElementPresent('login_error')
        return result