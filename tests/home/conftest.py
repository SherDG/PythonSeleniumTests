import pytest
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary


@pytest.yield_fixture(scope="class")
def oneTimeSetUp(request, browser='chrome'):
    print("Running one time setUp")
    baseURL = 'http://499.wordpress.imunify.local/wp-login.php'
    if browser == 'firefox':
        binary = FirefoxBinary('/usr/bin/firefox')
        driver = webdriver.Firefox(executable_path=r'/home/dima/QA/Drivers/firefox_linux64/geckodriver',firefox_binary=binary)
        driver.maximize_window()
        driver.implicitly_wait(1)
        # driver.get(baseURL)
        print("Running tests on FF")
    else:
        print("Running tests on chrome")
        driver = webdriver.Chrome(executable_path=r'/home/dima/QA/Drivers/chromedriver_linux64/chromedriver')
        # driver.get(baseURL)
    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    driver.quit()
    print("Running one time tearDown")

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operating system")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")