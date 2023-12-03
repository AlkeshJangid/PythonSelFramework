# All the commonly used or repeated used programs are placed on a single page
# which called the conftest file

import pytest
from selenium import webdriver

# Adding Command Liner in conftest.py to use Desired Browser...
def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        print('Opening Chrome')
        driver = webdriver.Chrome()
    elif browser == "firefox":
        print('Opening Firefox')
        driver = webdriver.Firefox()
    elif browser == "edge":
        print('Opening Edge')
        driver = webdriver.Edge()
    else:
        print('Headless Mode Open')
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("headless")
        driver = webdriver.Chrome(options=chrome_options)
    return driver
# --------------------------------------------------------------------------------------

# Used for test_Params
@pytest.fixture(params =[
    ("Admin", "admin123", "Pass"),
    ("Admin1", "admin123", "Fail"),
    ("Admin", "admin1234", "Fail"),
    ("Admin1", "admin1234", "Fail")
])
def getDataForLogin(request):
    return request.param
