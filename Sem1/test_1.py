import yaml
import requests


S = requests.Session()
with open("config.yaml", encoding='utf-8') as f:
    data = yaml.safe_load(f)
    username, password, address, address2 = data["username"], data["password"], data["address"], data["address2"]


def test_rest(user_login):
    return (S.get(url=address, headers={'X-Auth-Token': user_login}))


def test_newpost(user_login):
    n = S.post(address2, headers={'X-Auth-Token': user_login},
               data={'title': 'Новый пост',
                     'description': 'Post запрос',
                     'content': 'текст нового поста'})
    return n.json()
