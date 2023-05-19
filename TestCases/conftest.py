import pytest
import self
from selenium import webdriver

from Utilities.ReadProperties import readconfig


@pytest.fixture
def setup(browser):
    driver = webdriver.Chrome()
    driver.implicitly_wait(20)
    baseURL = readconfig.getApplicationURL()
    if browser == 'Chrome':
        # global driver
        print("launching chrome browser")
        driver.get(baseURL)
        driver.maximize_window()
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print("launching firefox browser")
        driver.get(baseURL)
        driver.maximize_window()
    else:
        driver = webdriver.Edge()
        driver.get(self.baseURL)
        driver.maximize_window()
    return driver


def pytest_addoption(parser):  # This will get the value from CLI/hooks
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):  # This will return the browser value to setup method
    return request.config.getoption("--browser")


#####PyTest HTML Report #####
def pytest_configure(config):
    config._metadata['Project Name'] = 'orangeHRM-2'
    config._metadata['Module Name'] = 'Forgetpassword'
    config._metadata['Testers'] = 'Brinda'


# It is hook for delete/modify environment into HTML Report
@pytest.hookimpl(tryfirst=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
