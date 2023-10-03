import yaml
import requests
import logging


S = requests.Session()
with open("testdata.yaml", encoding='utf-8') as f:
    data = yaml.safe_load(f)



def test_newpost(user_login):
    n = S.post(url=data['address2'], headers={'X-Auth-Token': user_login},
           data={'title': data['title'], 'description': data['description'], 'content': data['content']})
    logging.debug(f"Response is {str(n)}")
    assert str(n) == '<Response [200]>', 'post_create FAIL'
