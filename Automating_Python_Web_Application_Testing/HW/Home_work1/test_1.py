import requests
import yaml


# Загрузка конфигурации из YAML файла
with open("config.yaml") as f:
    data = yaml.safe_load(f)

#Проверка поста с определенным заголовком
def test_step1(login, testtext1):
    header = {"X-Auth-Token": login}
    res = requests.get(data["address"] + "api/posts", params={"owner": "notMe"}, headers=header)
    listres = [i["title"] for i in res.json()["data"]]
    assert testtext1 in listres

#Проверка создание нового поста
def test_step2(login, post_data):
    header = {"X-Auth-Token": login}
    res = requests.post(data["address"] + "api/posts", headers=header, data=post_data)
    assert res.status_code == 200

#Проверка наличия поста по его описанию
def test_step3(login, created_post):
    header = {"X-Auth-Token": login}
    res = requests.get(data["address"] + "api/posts", params={"owner": "me"}, headers=header)
    descriptions = [i["description"] for i in res.json()["data"]]
    assert created_post["description"] in descriptions
