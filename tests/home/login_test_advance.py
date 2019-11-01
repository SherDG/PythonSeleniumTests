from selenium import webdriver
from pages.home.login_page_advance import LoginPage
from utilities.softAssertions import TestStatus
import unittest
import pytest
from selenium.webdriver.common.by import By
import time

@pytest.mark.usefixtures("oneTimeSetUp")
class LoginTest(unittest.TestCase):
    baseURL = 'http://499.wordpress.imunify.local/wp-login.php'

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.order2
    def test_validLogIn(self):
        self.driver.get(self.baseURL)

        self.lp.login('admin', 'password1')
        result1 = self.lp.verifyLoginTitle()
        self.ts.mark(result1, "Title was successfully verified")

        result2 = self.lp.loginSuccess()

        self.ts.mark(result2, "Login was successful")

        self.ts.markFinal("test_validLogin", result2, "Login test")


    @pytest.mark.order1
    def test_invalidLogIn(self):
        self.driver.get(self.baseURL)

        self.lp.login('admin', 'password')
        result = self.lp.loginFailed()

        self.ts.mark(result, "Login was not successful")
        assert result == True

