import pytest
import requests
import yaml

with open('config.yaml') as f:
    data = yaml.safe_load(f)
    username, password, adress = data["username"], data["password"], data["address"]

S = requests.Session()


@pytest.fixture()
def user_login():
    rest1 = S.post(url=adress, data={'username': username, 'password': password})
    return rest1.json()['token']
