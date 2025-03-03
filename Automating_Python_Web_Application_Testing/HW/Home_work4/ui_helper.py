from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging
import yaml

with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)
name = testdata.get("username")

class TestSearchLocators:
    ids = dict()
    with open("./locators.yaml") as f:
        locators = yaml.safe_load(f)
    for locator in locators["xpath"].keys():
        ids[locator] = (By.XPATH, locators["xpath"][locator])
    for locator in locators["css"].keys():
        ids[locator] = (By.CSS_SELECTOR, locators["css"][locator])

class OperationsHelper(BasePage):

# Вспомогательная функция для ввода текста поле

    def enter_text_intro_field(self, locator, word, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        logging.debug(f"Send {word} to element {element_name}")
        field = self.find_element(locator)
        if not field:
            logging.error(f"Element {locator} not found")
            return False
        try:
            field.clear()
            field.send_keys(word)
        except:
            logging.exception(f"Exception while operation with {locator}")
            return False
        return True

    def click_button(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        button = self.find_element(locator)
        if not button:
            return False
        try:
            button.click()
        except:
            logging.exception(f"Exception with click")
            return False
        logging.debug(f"Clicked {element_name} button")
        return True

    def get_text_fom_element(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator

        field = self.find_element(locator, time=3)
        if not field:
            return None
        try:
            text = field.text
        except:
            logging.exception(f"Exception while get tst from {element_name}")
            return None
        logging.debug(f"We finde text {text} in field {element_name}")
        return text


# методы ввода текста
    def enter_login(self, word):
        self.enter_text_intro_field(TestSearchLocators.ids["LOCATOR_LOGIN_FIELD"], word, description=f"Send {word} to element LOGIN_FIELD")
    def enter_pass(self, word):
        self.enter_text_intro_field(TestSearchLocators.ids["LOCATOR_PASS_FIELD"], word, description=f"Send {word} to element PASS_FIELD")
    def input_title_post(self, word):
        self.enter_text_intro_field(TestSearchLocators.ids["LOCATOR_POST_TITLE_FIELD"], word, description=f"Send {word} to element POST_TITLE_FIELD")
    def input_description_post(self, word):
        self.enter_text_intro_field(TestSearchLocators.ids["LOCATOR_POST_DESCRIPTION_FIELD"], word, description=f"Send {word} to element POST_DESCRIPTION_FIELD")
    def input_content_post(self, word):
        self.enter_text_intro_field(TestSearchLocators.ids["LOCATOR_POST_CONTENT_FIELD"], word, description=f"Send {word} to element POST_CONTENT_FIELD")
    def enter_your_name(self, word):
        self.enter_text_intro_field(TestSearchLocators.ids["LOCATOR_YOUR_NAME_CONTACT"], word, description=f"Send {word} to element NAME_CONTACT")
    def enter_your_email(self, word):
        self.enter_text_intro_field(TestSearchLocators.ids["LOCATOR_YOUR_EMAIL_CONTACT"],word, description=f"Send {word} to element EMAIL_CONTACT")
    def enter_your_content(self, word):
        self.enter_text_intro_field(TestSearchLocators.ids["LOCATOR_CONTENT_CONTACT"],word, description=f"Send {word} to element CONTENT_CONTACT")

# Методы, когда мы нажимаем на кнопки
    def click_login_button(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_LOGIN_BTN"], description="Click login button")
    def click_create_post_button(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_CREATE_BTN"], description="Click create post button")
    def click_save_post_button(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_SAVE_BTN"], description="Click save post button")
    def click_create_contact(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_CONTACT"], description="Click create contact")
    def click_submit_contact(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_CONTACT_BTN"], description="Click submit contact")

#Методы получения текста

    def get_user_text(self):
        return self.get_text_fom_element(TestSearchLocators.ids["LOCATOR_HELLO"])
    def get_error_text(self):
        return self.get_text_fom_element(TestSearchLocators.ids["LOCATOR_ERROR_FIELD"])
    def get_new_title_text(self):
        return self.get_text_fom_element(TestSearchLocators.ids["LOCATOR_SEARCH_TITLE_FIELD"])

    def get_alert_text(self):
            try:
                alert_field = self.driver.switch_to.alert
                text = alert_field.text
                logging.info(f"We find text {text} in alert")
                return text
            except:
                logging.exception("Exception with alert")
                return None
