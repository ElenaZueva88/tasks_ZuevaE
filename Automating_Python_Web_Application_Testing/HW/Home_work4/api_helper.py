import logging
import requests
import yaml

with open("./testdata.yaml") as f:
    data = yaml.safe_load(f)


def api_get_posts(login, owner="notMe"):
    header = {"X-Auth-Token": login}
    url = data["address"] + "api/posts"
    params = {"owner": "notMe"}

    try:
        res = requests.get(url, params=params, headers=header)
        logging.debug(
            f"GET request to {url} with params: {params} and headers: {header}. Response code: {res.status_code}")
        return res
    except Exception as e:
        logging.error(f"Exception occurred during GET request to {url}: {e}")
        return None


def api_create_post(login, post_data):
    header = {"X-Auth-Token": login}
    url = data["address"] + "api/posts"

    try:
        res = requests.post(url, headers=header, data=post_data)
        logging.debug(
            f"POST request to {url} with headers: {header} and data: {post_data}. Response code: {res.status_code}")
        return res
    except Exception as e:
        logging.error(f"Exception occurred during POST request to {url}: {e}")
        return None


def api_get_user_posts(login):
    header = {"X-Auth-Token": login}
    url = data["address"] + "api/posts"
    params = {"owner": "me"}

    try:
        res = requests.get(url, params=params, headers=header)
        logging.debug(
            f"GET request to {url} with params: {params} and headers: {header}. Response code: {res.status_code}")
        return res
    except Exception as e:
        logging.error(f"Exception occurred during GET request to {url}: {e}")
        return None
