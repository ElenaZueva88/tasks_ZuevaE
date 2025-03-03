import logging

from api_helper import api_get_posts, api_create_post, api_get_user_posts


def test_get_posts(login, testtext1):
    logging.info("Test API 1 Starting")
    res = api_get_posts(login)
    assert res is not None
    assert res.status_code == 200
    titles = [post["title"] for post in res.json()["data"]]
    assert testtext1 in titles

def test_create_post(login, post_data):
    logging.info("Test API 2 Starting")
    res = api_create_post(login, post_data)
    assert res is not None
    assert res.status_code == 200

def test_get_user_posts(login, created_post):
    logging.info("Test API 3 Starting")
    res = api_get_user_posts(login)
    assert res is not None
    assert res.status_code == 200
    descriptions = [post["description"] for post in res.json()["data"]]
    assert created_post["description"] in descriptions
