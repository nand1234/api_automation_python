from typing import List
import pytest
from src.client import Request

base_url = "https://api.github.com/search"

@pytest.fixture
def client():
    headers={'Accept': 'application/vnd.github.v3.text-match+json'}
    return Request(base_url,headers,"", "")

def test1(client):  
    response = client.GET('/repositories',{'q': 'requests+language:python'})
    json_response = response.json()
    repository = json_response['items'][0]
    assert repository != None




