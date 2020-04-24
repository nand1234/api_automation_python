import requests
from requests.auth import HTTPBasicAuth

class Request:
    def __init__(self,base_url, auth_username, auth_password):
        self.base_url = base_url
        self.auth_username= auth_username
        self.auth_password= auth_password

        
    def set_headers(self, headers):
        add_headers = {}
        add_headers.update(headers)
        add_headers.update( {'Accept': 'application/vnd.github.v3.text-match+json'})
        return add_headers

    def GET(self,endpoint,param, headers):
        if param != None:
            return requests.get(url=self.base_url + endpoint,headers=self.set_headers(headers),params=param, auth=HTTPBasicAuth(self.auth_username, self.auth_password))
        return requests.get(url=self.base_url + endpoint,headers=self.headers,auth=HTTPBasicAuth(self.auth_username, self.auth_password))  

    def POST(self,endpoint,body,headers):
        return requests.post(url=self.base_url + endpoint,headers=self.set_headers(headers), data=body, auth=HTTPBasicAuth(self.auth_username, self.auth_password))

    def PUT(self,endpoint,body,headers):
        return requests.put(url=self.base_url + endpoint,headers=self.set_headers(headers),data=body,auth=HTTPBasicAuth(self.auth_username, self.auth_password))
    
    def PATCH(self,endpoint,body,headers):
        return requests.patch(url=self.base_url + endpoint,headers=self.set_headers(headers),data=body, auth=HTTPBasicAuth(self.auth_username, self.auth_password))

    def DELETE(self,endpoint,body,headers):
        return requests.delete(url=self.base_url + endpoint,headers=self.set_headers(headers), auth=HTTPBasicAuth(self.auth_username, self.auth_password))

    def HEAD(self,endpoint,body,headers):
        return requests.head(url=self.base_url + endpoint,headers=self.set_headers(headers), auth=HTTPBasicAuth(self.auth_username, self.auth_password))

    def OPTIONS(self,endpoint,body,headers):
        return requests.options(url=self.base_url + endpoint,headers=self.set_headers(headers), auth=HTTPBasicAuth(self.auth_username, self.auth_password))
