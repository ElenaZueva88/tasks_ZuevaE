import yaml
import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from module import Site


with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)

name = testdata.get("username")
passw = testdata.get("password")
post_title = testdata.get("post_title")
post_description = testdata.get("post_description")
post_content = testdata.get("post_content")

@pytest.fixture(scope="module")
def site():
    site_instance = Site(testdata["address"], testdata["browser"])
    yield site_instance
    site_instance.quit()

def test_step1(site, x_selector1, x_selector2, x_selector3, btn_selector, er1):
    input1 = site.find_element("xpath", x_selector1)
    input1.send_keys("test")

    input2 = site.find_element("xpath", x_selector2)
    input2.send_keys("passw")

    btn = site.find_element("css", btn_selector)
    btn.click()

    err_label = site.find_element("xpath", x_selector3)
    text = err_label.text
    assert text == er1

def test_step2(site, x_selector1, x_selector2, x_selector4, btn_selector, er2):
    input1 = site.find_element("xpath", x_selector1)
    input1.clear()
    input1.send_keys(name)

    input2 = site.find_element("xpath", x_selector2)
    input2.clear()
    input2.send_keys(passw)

    btn = site.find_element("css", btn_selector)
    btn.click()

    user_label = site.find_element("xpath", x_selector4)
    text = user_label.text
    assert text == er2

def test_add_post(site, x_selector1, x_selector2, btn_selector, create_btn, post_title_input, post_description_input, post_content_input, post_save_btn, post_title_selector):
    # Нажимаем на кнопку создания поста
    create_post_btn = site.find_element("css", create_btn)
    create_post_btn.click()
    time.sleep(testdata["wait"])

    # Вводим данные поста
    title_input = site.find_element("xpath", post_title_input)
    title_input.send_keys(post_title)

    description_input = site.find_element("xpath", post_description_input)
    description_input.send_keys(post_description)

    content_input = site.find_element("xpath", post_content_input)
    content_input.send_keys(post_content)
    time.sleep(testdata["wait"])

    # Сохраняем пост
    wait = WebDriverWait(site.driver, 10)
    save_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, post_save_btn)))
    save_button.click()

    # Ждем, пока заголовок нового поста не станет видимым, чтобы проверить, что пост сохранился
    saved_post_title = wait.until(
        EC.presence_of_element_located((By.XPATH, f"//h1[text()='{post_title}']"))
    )

    # Проверяем, что новый пост появился с заданным названием
    post_title_element = site.find_element("xpath", post_title_selector)
    assert post_title_element.text == post_title
