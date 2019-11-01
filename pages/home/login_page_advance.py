from base.selenium_driver import SeleniumDriver
from selenium.webdriver.common.by import By
from base.basepage import BasePage
import time


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def login(self, username, password):
        # self.waitForElement('user_login')
        # time.sleep(1)
        # inputLogin = self.driver.find_element_by_id('user_login')
        # inputLogin.clear()
        # inputLogin.send_keys(username)
        # self.sendDelayedKeys('user_login', username)
        self.sendKeys(username, 'user_login')

        # self.waitForElement('user_pass')
        time.sleep(1)
        # self.sendDelayedKeys('user_pass', password)
        # inputPass = self.driver.find_element_by_id('user_pass')
        # inputPass.clear()
        # inputPass.send_keys(password)
        self.sendKeys(password, 'user_pass')
        time.sleep(1)
        # self.waitForElement('wp-submit')
        self.elementClick('wp-submit')
        # loginButton = self.driver.find_element_by_id('wp-submit')
        # loginButton.click()
        # time.sleep(3)

    def loginSuccess(self):
        result = self.isElementPresent('wpbody-content')
        return result

    def loginFailed(self):
        result = self.isElementPresent('login_error')
        return result

    def verifyLoginTitle(self):
        return self.verifyPageTitle("Google")
