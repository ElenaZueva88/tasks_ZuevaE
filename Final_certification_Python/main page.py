from base_page import BasePage, OperationsHelper
import yaml

with open('./testdata.yaml') as f:
    testdata = yaml.safe_load(f)


class MainPage(BasePage):
    def go_to_about_page(self):
        self.find_element(testdata['LOCATOR_ABOUT_BUTTON']).click()