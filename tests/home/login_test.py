from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginTest():
    def test_validLogIn(self):
        baseURL = 'http://499.wordpress.imunify.local/wp-login.php'
        driver = webdriver.Firefox(executable_path='D:\QA\Drivers\geckodriver.exe')
        # driver = webdriver.Firefox('C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe')
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseURL)

        loginInput = driver.find_element(By.ID, "user_login")
        loginInput.send_keys('admin')

        passInput = driver.find_element(By.ID,'user_pass')
        passInput.send_keys('password1')

        loginButton = driver.find_element(By.ID,'wp-submit')
        loginButton.click()

        homepageContent = driver.find_element(By.ID,'wpbody-content')
        assert homepageContent is not None
        driver.quit()


ff = LoginTest()
ff.test_validLogIn()
