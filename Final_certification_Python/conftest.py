import pytest
import requests
import yaml
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

with open('./testdata.yaml') as f:
    testdata = yaml.safe_load(f)


@pytest.fixture(scope="function")
def browser():
    service = Service(executable_path=ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()

@pytest.fixture()
def login():
    response = requests.post(testdata['website1'],
                             data={'username': testdata['username'], 'password': testdata['password']})
    if response.status_code == 200:
        return response.json()['token']

@pytest.fixture()
def user_id():
    response = requests.post(testdata['website1'],
                             data={'username': testdata['username'], 'password': testdata['password']})
    if response.status_code == 200:
        return response.json()['id']