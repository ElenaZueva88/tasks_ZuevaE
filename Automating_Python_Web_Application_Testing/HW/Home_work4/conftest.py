import pytest, yaml, requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

with open("./testdata.yaml") as f:
    data = yaml.safe_load(f)

browser = data["browser"]

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

@pytest.fixture
def login():
    res = requests.post(data["address"] + "gateway/login", data={"username": data["username"], "password": data["password"]})
    return res.json()["token"]

@pytest.fixture
def testtext1():
    return "Приветствие"

@pytest.fixture
def post_data():
    return {
        "title": "Заголовок поста",
        "description": "Описание поста",
        "content": "Содержание поста"
    }

@pytest.fixture
def created_post(login, post_data):
    header = {"X-Auth-Token": login}
    res = requests.post(data["address"] + "api/posts", headers=header, data=post_data)
    assert res.status_code == 200
    return post_data
