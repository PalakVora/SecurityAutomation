import requests, openpyxl, re, time, json, traceback
from MethodFiles import Excel

class REST_Services:
    def __init__(self, HTTP_Method):
        TestData = Excel.Test_Data()
        URL = TestData.API_CompleteURL
        Body = TestData.API_Request_Body
        Header = TestData.API_Request_Header
        Cookie = TestData.API_Request_Cookie

        try:
            if(HTTP_Method == 'GET'):
                Response = requests.get(URL, data=Body, headers=Header,  cookies=Cookie)
            elif(HTTP_Method =='POST'):
                Response = requests.post(URL, data=Body, headers=Header,  cookies=Cookie)
            elif(HTTP_Method =='PUT'):
                Response=requests.put(URL, data=Body, headers=Header,  cookies=Cookie)
            elif(HTTP_Method == 'DELETE'):
                Response = requests.put(URL, data=Body, headers=Header, cookies=Cookie)
            elif(HTTP_Method == 'DELETE'):
                Response = requests.delete(URL, data=Body, headers=Header, cookies=Cookie)
            elif(HTTP_Method =='PATCH'):
                Response=requests.patch(URL, data=Body, headers=Header, cookies=Cookie)
            elif(HTTP_Method == 'HEAD'):
                Response = requests.head(URL, data=Body, headers=Header, cookies=Cookie)

            self.StatusCode = str(Response.status_code)
            self.ResponseBody = str(Response.text)
            self.ResponseHeader = str(Response.headers)
            self.ResponseCookie = str(Response.cookies)

            print("StatusCode = " + str(self.StatusCode))
            print("Response Body = " + str(self.ResponseBody))
            print("Response Header = " + str(self.ResponseHeader))
            print("Response Cookie = " + str(self.ResponseCookie))

        except:
            print("Method Not Found")

def Request_Method(HTTP_Method):
    return REST_Services



