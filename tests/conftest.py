import pytest
import time
from utilities import read_config
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture()
def test_setup_teardown(request):
    browser = read_config.get_config("basic info","browser")
    driver = None
    if browser.__eq__("chrome"):
        driver = webdriver.Chrome()
    elif browser.__eq__("firefox"):
        driver = webdriver.Firefox()
    elif browser.__eq__("edge"):
        driver = webdriver.Edge()
    else:
        print("Provide Correct browser name")
   # assert driver is not None, "WebDriver is not instantiated successfully"
    driver.maximize_window()
    driver.implicitly_wait(5)
    urls = read_config.get_config("basic info","url")
    driver.get(urls)
    request.cls.driver = driver
    yield
    driver.quit()