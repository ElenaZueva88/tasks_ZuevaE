from base_page import BasePage, OperationsHelper
import yaml

with open('./testdata.yaml') as f:
    testdata = yaml.safe_load(f)


class AboutPage(BasePage):
    def get_header_size(self):
        return self.get_element_property(testdata['LOCATOR_ABOUT_HEADER'], 'font-size')