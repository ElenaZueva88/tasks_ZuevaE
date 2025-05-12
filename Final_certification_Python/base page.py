from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import yaml

with open('./testdata.yaml') as f:
    testdata = yaml.safe_load(f)


class BasePage:
    def __init__(self, driver, url="http://test-stand.gb.ru"):
        self.driver = driver
        self.url = url

    def find_element(self, locator, time=10):
        try:
            element = WebDriverWait(self.driver, time).until(EC.presence_of_element_located((By.XPATH, locator)),
                                                             message=f"Can't find element by locator {locator}")
        except:
            element = None
        return element

    def get_element_property(self, locator, property):
        element = self.find_element(locator)
        return element.value_of_css_property(property)

    def go_to_site(self):
        return self.driver.get(self.url)


class OperationsHelper(BasePage):
    def enter_login(self, word=testdata['username']):
        login_field = self.find_element(testdata['LOCATOR_LOGIN_FIELD'])
        login_field.clear()
        login_field.send_keys(word)

    def enter_pass(self, word=testdata['password']):
        pass_field = self.find_element(testdata['LOCATOR_PASS_FIELD'])
        pass_field.clear()
        pass_field.send_keys(word)

    def click_login_button(self):
        self.find_element(testdata['LOCATOR_LOGIN_BTN']).click()

    def login(self):
        self.enter_login()
        self.enter_pass()
        self.click_login_button()