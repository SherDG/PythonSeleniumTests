from selenium import webdriver
from WP_499.pages.home.login_page import LoginPage
# from WP_499.utilities.softAssertions import TestStatus
import unittest
import pytest
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("oneTimeSetUp")
class LoginTest(unittest.TestCase):
    baseURL = 'http://499.wordpress.imunify.local/wp-login.php'

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        # self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=2)
    def test_validLogIn(self):
        self.driver.get(self.baseURL)
        self.lp.login('admin', 'password1')
        homepageContent = self.driver.find_element(By.ID, 'wpbody-content')
        # self.ts.mark(homepageContent, "Login was successful")
        # self.ts.markFinal("test_validLogin", homepageContent, "Login was successful")
        assert homepageContent is not None

    @pytest.mark.run(order=1)
    def test_invalidLogIn(self):
        self.driver.get(self.baseURL)
        self.lp.login('admin', 'password')
        homepageContent = self.driver.find_element(By.ID, 'login_error')
        assert homepageContent is not None
        # homepageContent = self.driver.find_element(By.ID, 'wpbody-content')
        # self.ts.mark(homepageContent, "Login was successful")

