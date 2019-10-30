from selenium import webdriver
from WP_499.pages.home.login_page import LoginPage
import unittest
import pytest
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("oneTimeSetUp")
class LoginTest(unittest.TestCase):
    # baseURL = 'http://499.wordpress.imunify.local/wp-login.php'
    # driver = webdriver.Firefox(executable_path='D:\\QA\\Drivers\geckodriver.exe')
    # driver.maximize_window()
    # driver.implicitly_wait(3)
    # lp = LoginPage(driver)

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)

    @pytest.mark.run(order=2)
    def test_validLogIn(self):
        # self.driver.get(self.baseURL)
        self.lp.login('admin', 'password1')

        homepageContent = self.driver.find_element(By.ID, 'wpbody-content')
        assert homepageContent is not None
        # self.driver.quit()

    @pytest.mark.run(order=1)
    def test_invalidLogIn(self):
        # self.driver.get(self.baseURL)
        self.lp.login('admin', 'password')
        homepageContent = self.driver.find_element(By.ID, 'login_error')
        assert homepageContent is not None

