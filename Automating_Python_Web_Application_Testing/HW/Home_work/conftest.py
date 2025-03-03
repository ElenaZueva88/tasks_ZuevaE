import pytest, yaml
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)
    browser = testdata["browser"]

@pytest.fixture(scope="session")
def browser():
    if browser == "firefox":
        service = Service(executable_path=GeckoDriverManager().install())
        option = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(service=service, options=option)
    else:
        service = Service(executable_path=ChromeDriverManager().install())
        option = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=service, options=option)
    yield driver
    driver.quit()
