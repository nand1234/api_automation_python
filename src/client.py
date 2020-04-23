import requests
from requests.auth import HTTPBasicAuth

class Request:
    def __init__(self,base_url,headers, auth_username, auth_password):
        self.base_url = base_url
        self.headers = headers
        self.auth_username= auth_username
        self.auth_password= auth_password

    def GET(self,endpoint,param):
        if param != None:
            return requests.get(url=self.base_url + endpoint,headers=self.headers,params=param, auth=HTTPBasicAuth(self.auth_username, self.auth_password))
        return requests.get(url=self.base_url + endpoint,headers=self.headers,auth=HTTPBasicAuth(self.auth_username, self.auth_password))  

    def POST(self,endpoint,body):
        return requests.post(url=self.base_url + endpoint,headers=self.headers, data=body, auth=HTTPBasicAuth(self.auth_username, self.auth_password))

    def PUT(self,endpoint,body):
        return requests.put(url=self.base_url + endpoint,headers=self.headers,data=body,auth=HTTPBasicAuth(self.auth_username, self.auth_password))
    
    def PATCH(self,endpoint,body):
        return requests.patch(url=self.base_url + endpoint,headers=self.headers,data=body, auth=HTTPBasicAuth(self.auth_username, self.auth_password))

    def DELETE(self,endpoint,body):
        return requests.delete(url=self.base_url + endpoint,headers=self.headers, auth=HTTPBasicAuth(self.auth_username, self.auth_password))

    def HEAD(self,endpoint,body):
        return requests.head(url=self.base_url + endpoint,headers=self.headers, auth=HTTPBasicAuth(self.auth_username, self.auth_password))

    def OPTIONS(self,endpoint,body):
        return requests.options(url=self.base_url + endpoint,headers=self.headers, auth=HTTPBasicAuth(self.auth_username, self.auth_password))
        