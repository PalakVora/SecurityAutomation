import json, requests, openpyxl, traceback, re

def readexcel(Excel_Location, Excel_Sheet_Name, Module_Name):
    data = {}
    print("Opening Excel")
    try:
        Excel_WorkBook = openpyxl.load_workbook(Excel_Location)
        print("Opened Excel")
    except Exception as error:
        print("Error in opening API Excel File")
        traceback.print_stack()

    try:
        for SheetName in Excel_WorkBook.worksheets:
            if SheetName.title == Excel_Sheet_Name:
                ActiveWorkSheet = Excel_WorkBook[SheetName.title]
                print("Title of Sheet = " + ActiveWorkSheet.title)
                RowLength = SheetName.max_row
                ColumnLength = SheetName.max_column
                for i in range(1, RowLength + 1):
                    RowContents = SheetName.cell(row=i, column=1)
                    print("Row " + str(RowContents.row) + " = " + str(RowContents.value))
                    if ((RowContents.value) == Module_Name):
                        print("Module Found : " + str(RowContents.value) + " in Row - " + str(
                            RowContents.row) + " of Worksheet - " + ActiveWorkSheet.title)
                    else:
                        continue

                    for j in range(1, ColumnLength + 1):
                        Response = dict()
                        ColumnContents = SheetName.cell(row=RowContents.row, column=j)
                        print(ColumnContents.value, end="" + "\n")

                        try:
                            API_Name = (SheetName["A" + str(RowContents.row)])
                            print(API_Name.value)
                            data['API'] = str(API_Name.value)
                            print(data['API'])
                        except Exception as error:
                            print(error)
                            traceback.print_stack()
                            Excel_WorkBook.close()
                            break

                        try:
                            HTTP_Method = (SheetName["B" + str(RowContents.row)])
                            print(HTTP_Method.value)
                            data['HTTPMethod'] = str(HTTP_Method.value)
                            print(data['HTTPMethod'])
                        except Exception as error:
                            print(error)
                            traceback.print_stack()
                            Excel_WorkBook.close()
                            break

                        try:
                            Request_Protocol = (SheetName["C" + str(RowContents.row)])
                            print(Request_Protocol.value)
                            data['Protocol'] = str(Request_Protocol.value)
                            print(data['Protocol'] + "\n")
                        except Exception as error:
                            print(error)
                            traceback.print_stack()
                            Excel_WorkBook.close()
                            break

                        try:
                            Request_BaseURL = (SheetName["D" + str(RowContents.row)])
                            print("BaseURL = " + str(Request_BaseURL.value) + "\n")
                        except Exception as error:
                            print(error)
                            traceback.print_stack()
                            Excel_WorkBook.close()
                            break

                        try:
                            Request_RelativeURL = (SheetName["E" + str(RowContents.row)])
                            print("RelativeURL = " + str(Request_RelativeURL.value) + "\n")
                        except Exception as error:
                            print(error)
                            traceback.print_stack()
                            Excel_WorkBook.close()
                            break

                        try:
                            data['URL'] = str(data['Protocol']) + "://" + str(Request_BaseURL.value) + str(Request_RelativeURL.value)
                            print(data['URL'])
                        except Exception as error:
                            print(error)
                            traceback.print_stack()
                            Excel_WorkBook.close()
                            break

                        try:
                            Body_Row = (SheetName["F" + str(RowContents.row)])
                            Body_Content = str(Body_Row.value)
                            print("Body = " + Body_Content + "\n")
                            data['Body'] = json.loads(Body_Content)
                            print(data['Body'])
                        except Exception as error:
                            print(error)
                            traceback.print_stack()
                            Excel_WorkBook.close()
                            break

                        try:
                            Header_Row = (SheetName["G" + str(RowContents.row)])
                            Header_Content = str(Header_Row.value)
                            print("Header = " + Header_Content + "\n")
                            data['Header'] = json.loads(Header_Content)
                            print(data['Header'])
                        except Exception as error:
                            print(error)
                            traceback.print_stack()
                            Excel_WorkBook.close()
                            break

                        try:
                            Cookie_Row = (SheetName["H" + str(RowContents.row)])
                            Cookie_Content = str(Cookie_Row.value)
                            print("Cookie = " + Cookie_Content + "\n")
                            data['Cookie'] = json.loads(Cookie_Content)
                            print(data['Cookie'])
                        except Exception as error:
                            print(error)
                            traceback.print_stack()
                            Excel_WorkBook.close()
                            break
                        break
                    break
                    print(data)
                    Excel_WorkBook.close()

    except:
        print("Error in reading contents")
    return data



def Dangerous_Methods(Excel_Location, Excel_Sheet_Name, Module_Name):
    result = []
    try:
        returnvalue = readexcel(Excel_Location, Excel_Sheet_Name, Module_Name)
        print("Data from find_vulnerable_parameters ")
        print(result)
    except Exception as error:
        print(error)
        traceback.print_stack()

    try:
        API = returnvalue['API']
    except Exception as error:
        print(error)
        traceback.print_stack()

    try:
        Method = returnvalue['HTTPMethod']
    except Exception as error:
        print(error)
        traceback.print_stack()

    try:
        Protocol = returnvalue['Protocol']
    except Exception as error:
        print(error)
        traceback.print_stack()

    try:
        URL = returnvalue['URL']
    except Exception as error:
        print(error)
        traceback.print_stack()

    try:
        Body = returnvalue['Body']
    except Exception as error:
        print(error)
        traceback.print_stack()

    try:
        Header = returnvalue['Header']
    except Exception as error:
        print(error)
        traceback.print_stack()

    try:
        Cookie = returnvalue['Cookie']
    except Exception as error:
        print(error)
        traceback.print_stack()

    try:
        Check_URL = re.findall(r'\$(.*?)\$', str(URL))
        if (Check_URL != ""):
            for key in Check_URL:
                URL = URL.replace("$", "")
            print(URL)
        else:
            print("No Change in URL")
    except Exception as error:
        print(error)
        traceback.print_stack()

    try:
        Check_Body = re.findall(r'\$(.*?)\$', str(Body))
        if (Check_Body != ""):
            for key in Check_Body:
                Body = Body.replace("$", "")
            print(Body)
        else:
            print("No Change in Body")
            print(Body)
    except Exception as error:
        print(error)
        traceback.print_stack()

    try:
        Check_Header = re.findall(r'\$(.*?)\$', str(Header))
        if (Check_Header != ""):
            for key in Check_Header:
                URL = URL.replace("$", "")
            print(Header)
        else:
            print("No Change in Header")
            print(Header)
    except Exception as error:
        print(error)
        traceback.print_stack()

    try:
        Check_Cookie = re.findall(r'\$(.*?)\$', str(Cookie))
        if (Check_Cookie != ""):
            for key in Check_Cookie:
                Cookie = Cookie.replace("$", "")
            print(Cookie)
        else:
            print("No Change in Cookie")
            print(Cookie)
    except Exception as error:
        print(error)
        traceback.print_stack()

    if(Method == 'GET'):
        print("Its a GET Method")
        StatusCode = {}
        try:
            POST = requests.post(str(URL), data=Body, headers=Header)
            StatusCode['POST'] = str(POST.status_code)
            Response_Body = str(POST.text)
            Response_Header = str(POST.headers)
            Response_Cookie = str(POST.cookies)

            print("POST Status Code = " + StatusCode['POST'])
            print("POST Response Body: " + Response_Body)
            print("POST Response Header: " + Response_Header)
            print("POST Response Cookie: " + Response_Cookie)

        except Exception as error:
            print("Error in executing POST Method")
            traceback.print_stack()

        try:
            PUT = requests.put(URL, data=Body, headers=Header)
            StatusCode['PUT'] = str(PUT.status_code)
            Response_Body = str(PUT.text)
            Response_Header = str(PUT.headers)
            Response_Cookie = str(PUT.cookies)

            print("PUT Status Code = " + StatusCode['PUT'])
            print("PUT Response Body: " + Response_Body)
            print("PUT Response Header: " + Response_Header)
            print("PUT Response Cookie: " + Response_Cookie)

        except Exception as error:
            print("Error in executing PUT Method")
            traceback.print_stack()

        try:
            PATCH = requests.patch(URL, data=Body, headers=Header)
            StatusCode['PATCH'] = str(PATCH.status_code)
            Response_Body = str(PATCH.text)
            Response_Header = str(PATCH.headers)
            Response_Cookie = str(PATCH.cookies)

            print("PATCH Status Code = " + StatusCode['PATCH'])
            print("PATCH Response Body: " + Response_Body)
            print("PATCH Response Header: " + Response_Header)
            print("PATCH Response Cookie: " + Response_Cookie)

        except Exception as error:
            print("Error in executing PATCH Method")
            traceback.print_stack()

        try:
            HEAD = requests.head(URL, data=Body, headers=Header)
            StatusCode['HEAD'] = str(HEAD.status_code)
            Response_Body = str(HEAD.text)
            Response_Header = str(HEAD.headers)
            Response_Cookie = str(HEAD.cookies)

            print("HEAD Status Code = " + StatusCode['HEAD'])
            print("HEAD Response Body: " + Response_Body)
            print("HEAD Response Header: " + Response_Header)
            print("HEAD Response Cookie: " + Response_Cookie)

        except Exception as error:
            print("Error in executing HEAD Method")
            traceback.print_stack()

        try:
            DELETE = requests.delete(str(URL), data=Body, headers=Header)
            StatusCode['DELETE'] = str(DELETE.status_code)
            Response_Body = str(DELETE.text)
            Response_Header = str(DELETE.headers)
            Response_Cookie = str(DELETE.cookies)

            print("DELETE Status Code = " + StatusCode['DELETE'])
            print("DELETE Response Body: " + Response_Body)
            print("DELETE Response Header: " + Response_Header)
            print("DELETE Response Cookie: " + Response_Cookie)

        except Exception as error:
            print("Error in executing DELETE Method")
            traceback.print_stack()

        result.append(str(StatusCode))

    elif(Method == 'POST'):
        StatusCode = {}
        try:
            GET = requests.get(str(URL), data=Body, headers=Header)
            StatusCode['GET'] = str(GET.status_code)
            Response_Body = str(GET.text)
            Response_Header = str(GET.headers)
            Response_Cookie = str(GET.cookies)

            print("GET Status Code = " + StatusCode['GET'])
            print("GET Response Body: " + Response_Body)
            print("GET Response Header: " + Response_Header)
            print("GET Response Cookie: " + Response_Cookie)

        except Exception as error:
            print("Error in executing GET Method")
            traceback.print_stack()

        try:
            PUT = requests.put(URL, data=Body, headers=Header)
            StatusCode['PUT'] = str(PUT.status_code)
            Response_Body = str(PUT.text)
            Response_Header = str(PUT.headers)
            Response_Cookie = str(PUT.cookies)

            print("PUT Status Code = " + StatusCode['PUT'])
            print("PUT Response Body: " + Response_Body)
            print("PUT Response Header: " + Response_Header)
            print("PUT Response Cookie: " + Response_Cookie)
        except Exception as error:
            print("Error in executing PUT Method")
            traceback.print_stack()

        try:
            PATCH = requests.patch(URL, data=Body, headers=Header)
            StatusCode['PATCH'] = str(PATCH.status_code)
            Response_Body = str(PATCH.text)
            Response_Header = str(PATCH.headers)
            Response_Cookie = str(PATCH.cookies)

            print("PATCH Status Code = " + StatusCode['PATCH'])
            print("PATCH Response Body: " + Response_Body)
            print("PATCH Response Header: " + Response_Header)
            print("PATCH Response Cookie: " + Response_Cookie)
        except Exception as error:
            print("Error in executing PATCH Method")
            traceback.print_stack()

        try:
            HEAD = requests.head(URL, data=Body, headers=Header)
            StatusCode['HEAD'] = str(HEAD.status_code)
            Response_Body = str(HEAD.text)
            Response_Header = str(HEAD.headers)
            Response_Cookie = str(HEAD.cookies)

            print("HEAD Status Code = " + StatusCode['HEAD'])
            print("HEAD Response Body: " + Response_Body)
            print("HEAD Response Header: " + Response_Header)
            print("HEAD Response Cookie: " + Response_Cookie)
        except Exception as error:
            print("Error in executing HEAD Method")
            traceback.print_stack()


        try:
            DELETE = requests.delete(str(URL), data=Body, headers=Header)
            StatusCode['DELETE'] = str(DELETE.status_code)
            Response_Body = str(DELETE.text)
            Response_Header = str(DELETE.headers)
            Response_Cookie = str(DELETE.cookies)

            print("DELETE Status Code = " + StatusCode['DELETE'])
            print("DELETE Response Body: " + Response_Body)
            print("DELETE Response Header: " + Response_Header)
            print("DELETE Response Cookie: " + Response_Cookie)

        except Exception as error:
            print("Error in executing DELETE Method")
            traceback.print_stack()

        result.append(str(StatusCode))

    elif(Method == 'PUT'):
        StatusCode = {}
        try:
            GET = requests.get(str(URL), data=Body, headers=Header)
            StatusCode['GET'] = str(GET.status_code)
            Response_Body = str(GET.text)
            Response_Header = str(GET.headers)
            Response_Cookie = str(GET.cookies)

            print("GET Status Code = " + StatusCode['GET'])
            print("GET Response Body: " + Response_Body)
            print("GET Response Header: " + Response_Header)
            print("GET Response Cookie: " + Response_Cookie)
        except Exception as error:
            print("Error in executing GET Method")
            traceback.print_stack()

        try:
            POST = requests.post(str(URL), data=Body, headers=Header)
            StatusCode['POST'] = str(POST.status_code)
            Response_Body = str(POST.text)
            Response_Header = str(POST.headers)
            Response_Cookie = str(POST.cookies)

            print("POST Status Code = " + StatusCode['POST'])
            print("POST Response Body: " + Response_Body)
            print("POST Response Header: " + Response_Header)
            print("POST Response Cookie: " + Response_Cookie)
        except Exception as error:
            print("Error in executing POST Method")
            traceback.print_stack()

        try:
            PATCH = requests.patch(URL, data=Body, headers=Header)
            StatusCode['PATCH'] = str(PATCH.status_code)
            Response_Body = str(PATCH.text)
            Response_Header = str(PATCH.headers)
            Response_Cookie = str(PATCH.cookies)

            print("PATCH Status Code = " + StatusCode['PATCH'])
            print("PATCH Response Body: " + Response_Body)
            print("PATCH Response Header: " + Response_Header)
            print("PATCH Response Cookie: " + Response_Cookie)
        except Exception as error:
            print("Error in executing PATCH Method")
            traceback.print_stack()

        try:
            HEAD = requests.head(URL, data=Body, headers=Header)
            StatusCode['HEAD'] = str(HEAD.status_code)
            Response_Body = str(HEAD.text)
            Response_Header = str(HEAD.headers)
            Response_Cookie = str(HEAD.cookies)

            print("HEAD Status Code = " + StatusCode['HEAD'])
            print("HEAD Response Body: " + Response_Body)
            print("HEAD Response Header: " + Response_Header)
            print("HEAD Response Cookie: " + Response_Cookie)
        except Exception as error:
            print("Error in executing HEAD Method")
            traceback.print_stack()


        try:
            DELETE = requests.delete(str(URL), data=Body, headers=Header)
            StatusCode['DELETE'] = str(DELETE.status_code)
            Response_Body = str(DELETE.text)
            Response_Header = str(DELETE.headers)
            Response_Cookie = str(DELETE.cookies)

            print("DELETE Status Code = " + StatusCode['DELETE'])
            print("DELETE Response Body: " + Response_Body)
            print("DELETE Response Header: " + Response_Header)
            print("DELETE Response Cookie: " + Response_Cookie)

        except Exception as error:
            print("Error in executing DELETE Method")
            traceback.print_stack()

        result.append(str(StatusCode))

    elif (Method == 'DELETE'):
        StatusCode = {}
        try:
            GET = requests.get(str(URL), data=Body, headers=Header)
            StatusCode['GET'] = str(GET.status_code)
            Response_Body = str(GET.text)
            Response_Header = str(GET.headers)
            Response_Cookie = str(GET.cookies)

            print("GET Status Code = " + StatusCode['GET'])
            print("GET Response Body: " + Response_Body)
            print("GET Response Header: " + Response_Header)
            print("GET Response Cookie: " + Response_Cookie)
        except Exception as error:
            print("Error in executing GET Method")
            traceback.print_stack()

        try:
            POST = requests.post(str(URL), data=Body, headers=Header)
            StatusCode['POST'] = str(POST.status_code)
            Response_Body = str(POST.text)
            Response_Header = str(POST.headers)
            Response_Cookie = str(POST.cookies)

            print("POST Status Code = " + StatusCode['POST'])
            print("POST Response Body: " + Response_Body)
            print("POST Response Header: " + Response_Header)
            print("POST Response Cookie: " + Response_Cookie)
        except Exception as error:
            print("Error in executing POST Method")
            traceback.print_stack()


        try:
            PUT = requests.put(URL, data=Body, headers=Header)
            StatusCode['PUT'] = str(PUT.status_code)
            Response_Body = str(PUT.text)
            Response_Header = str(PUT.headers)
            Response_Cookie = str(PUT.cookies)

            print("PUT Status Code = " + StatusCode['PUT'])
            print("PUT Response Body: " + Response_Body)
            print("PUT Response Header: " + Response_Header)
            print("PUT Response Cookie: " + Response_Cookie)
        except Exception as error:
            print("Error in executing PUT Method")
            traceback.print_stack()

        try:
            PATCH = requests.patch(URL, data=Body, headers=Header)
            StatusCode['PATCH'] = str(PATCH.status_code)
            Response_Body = str(PATCH.text)
            Response_Header = str(PATCH.headers)
            Response_Cookie = str(PATCH.cookies)

            print("PATCH Status Code = " + StatusCode['PATCH'])
            print("PATCH Response Body: " + Response_Body)
            print("PATCH Response Header: " + Response_Header)
            print("PATCH Response Cookie: " + Response_Cookie)
        except Exception as error:
            print("Error in executing PATCH Method")
            traceback.print_stack()

        try:
            HEAD = requests.head(URL, data=Body, headers=Header)
            StatusCode['HEAD'] = str(HEAD.status_code)
            Response_Body = str(HEAD.text)
            Response_Header = str(HEAD.headers)
            Response_Cookie = str(HEAD.cookies)

            print("HEAD Status Code = " + StatusCode['HEAD'])
            print("HEAD Response Body: " + Response_Body)
            print("HEAD Response Header: " + Response_Header)
            print("HEAD Response Cookie: " + Response_Cookie)
        except Exception as error:
            print("Error in executing HEAD Method")
            traceback.print_stack()

        result.append(str(StatusCode))

    return result

