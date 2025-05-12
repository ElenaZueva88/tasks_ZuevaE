import time
from base_page import OperationsHelper
import yaml
from main_page import MainPage
from about_page import AboutPage
from test_api import TestApi

with open('./testdata.yaml') as f:
    testdata = yaml.safe_load(f)


def test_successful_login(browser):
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login(testdata['username'])
    testpage.enter_pass(testdata['password'])
    testpage.click_login_button()
    hello_text = testpage.find_element(testdata['LOCATOR_HELLO_TEXT']).text
    assert f"Hello, {testdata['username']}" == hello_text


def test_about_header_size(browser):
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.login()
    mainpage = MainPage(browser, browser.current_url)
    mainpage.go_to_about_page()
    time.sleep(2)
    aboutpage = AboutPage(browser, browser.current_url)
    font_size = aboutpage.get_header_size()
    assert font_size == '32px'


def test_api_user_name(login, user_id):
    response = TestApi.get_username_from_profile(login, user_id)
    assert response.status_code == 200 and response.json()['username'] == testdata['username']