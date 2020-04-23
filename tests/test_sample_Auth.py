from typing import List
import pytest
from src.client import Request

base_url = "https://api.github.com/search"
auth_username = ""
auth_password= ""

@pytest.fixture
def client():
    headers={'Accept': 'application/vnd.github.v3.text-match+json'}
    return Request(base_url,headers,auth_username, auth_password)

def test1(client):  
    response = client.GET('/user', "")
    assert response != None




