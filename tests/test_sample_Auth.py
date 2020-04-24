from typing import List
import pytest
from src.client import Request
from src.endpoints import endpoints

base_url = "https://api.github.com/search"
auth_username = ""
auth_password= ""

@pytest.fixture
def client():
    return Request(base_url,auth_username, auth_password)

def test1(client):  
    response = client.GET(endpoints.get_user, "","")
    assert response != None




