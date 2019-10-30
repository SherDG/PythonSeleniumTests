import pytest
from selenium import webdriver

@pytest.yield_fixture(scope="class")
def oneTimeSetUp(request, browser='firefox'):
    print("Running one time setUp")
    baseURL = 'http://499.wordpress.imunify.local/wp-login.php'
    if browser == 'firefox':
        driver = webdriver.Firefox(executable_path='D:\\QA\\Drivers\geckodriver.exe')
        driver.maximize_window()
        driver.implicitly_wait(3)
        # driver.get(baseURL)
        print("Running tests on FF")
    else:
        print("Running tests on chrome")
        driver = webdriver.Chrome(executable_path='D:\\QA\\Drivers\chromedriver.exe')
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