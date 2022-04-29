import json
import random

import pytest
import requests
from requests.auth import HTTPBasicAuth

from API_testing.github_credentials import username, password

base_url = 'https://api.github.com'
base_auth=HTTPBasicAuth(username,password)
repo_name='demo_testing'+ str(random.randrange(1,50))

def test_get_repository_list():
    get_repo_url = base_url + '/users/gowthaml07/repos'
    get_repo_responce= requests.request('GET',get_repo_url,auth=base_auth)
    repo_list= json.loads(get_repo_responce.text)
    print(repo_list)
    repository=[]
    for repos in repo_list:
        repository.append(repos.get('name'))
    print(repository)
    assert 'Selenium_Framework' in repository

def test_creat_repository():
    get_repo_url = base_url + '/user/repos'
    payload={'name':repo_name}
    repo_responce=requests.request('POST',get_repo_url,auth=base_auth,data=json.dumps(payload))
    assert repo_responce.status_code==201

def test_update_repository():
    get_repo_url = base_url + '/repos/gowthaml07/demo_testing9'
    print(get_repo_url)
    payload={'name':'demo_testing1'}
    repo_responce=requests.request('PATCH',get_repo_url,auth=base_auth,data=json.dumps(payload))
    assert repo_responce.status_code==200

def test_delete_repository():
    get_repo_url = base_url + '/repos/gowthaml07/demo_testing1'
    print(get_repo_url)
    # payload={'name':'demo_testing1'}
    repo_responce=requests.request('DELETE',get_repo_url,auth=base_auth)
    assert repo_responce.status_code==204
