import requests
import yaml

with open('./testdata.yaml') as f:
    testdata = yaml.safe_load(f)

class TestApi:
    @staticmethod
    def get_username_from_profile(login, user_id):
        return requests.get(testdata['website_get_user_profile'] + str(user_id), headers={'X-Auth-Token': login})