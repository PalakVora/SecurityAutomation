import requests, openpyxl, json, re, traceback

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
                            data['HTTPMethod'] = str(HTTP_Method.value)
                            print(data['HTTPMethod'])
                        except Exception as error:
                            print(error)
                            traceback.print_stack()
                            Excel_WorkBook.close()
                            break

                        try:
                            Protocol = str((SheetName["C" + str(RowContents.row)]).value)
                            print("Protocol : " + Protocol)
                            Check_Protocol = re.findall(r'\$(.*?)\$', str(Protocol))
                            print("Parameter Observed in Protocol : ")
                            print(Check_Protocol)
                            if(Check_Protocol != ''):
                                for key in Check_Protocol:
                                    if('https' in Check_Protocol):
                                        ReplaceProtocol = Protocol.replace("$", "")
                                        print("Protocol After Replaced with Dollars: ")
                                        print(ReplaceProtocol)
                                        print("Observed HTTPS")
                                        print("Changing to HTTP")
                                        data['Protocol'] = ReplaceProtocol.replace("https", "http")
                                        print("Changed to HTTP")
                                        print(data['Protocol'])
                                    elif('http' in Check_Protocol):
                                        data['Protocol'] = Protocol.replace("$", "")
                                        print("HTTP is used")
                                        print(data['Protocol'])
                            else:
                                print("Protocols are not marked as Parameters to test in Excel File")
                        except Exception as error:
                            print(error)
                            traceback.print_stack()


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
                            print("Complete URL: ")
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

def HSTS(Excel_Location, Excel_Sheet_Name, Module_Name):
    result = {}
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
        if(Check_URL != ""):
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


    try:
        if(Method == 'GET'):
            print("Found GET API, So Executing It.")
            try:
                GET = requests.get(URL, data=Body,headers=Header)
                print("Executed GET Method")
                result['StatusCode'] = str(GET.status_code)
                result['ResponseBody'] = str(GET.text)
                result['ResponseHeader'] = str(GET.headers)
                result['ResponseCookie'] = str(GET.cookies)
            except Exception as error:
                print(error)
                traceback.print_stack()

        elif (Method == 'POST'):
            print("Found POST API, So Executing It.")
            try:
                POST = requests.post(URL, data=Body, headers=Header)
                print("Executed POST Method")
                result['StatusCode'] = str(POST.status_code)
                result['ResponseBody'] = str(POST.text)
                result['ResponseHeader'] = str(POST.headers)
                result['ResponseCookie'] = str(POST.cookies)
            except Exception as error:
                print(error)
                traceback.print_stack()

        elif(Method == 'PUT'):
            print("Found PUT API, So Executing It.")
            try:
                PUT = requests.put(URL, data=Body, headers=Header)
                print("Executed POST Method")
                result['StatusCode'] = str(PUT.status_code)
                result['ResponseBody'] = str(PUT.text)
                result['ResponseHeader'] = str(PUT.headers)
                result['ResponseCookie'] = str(PUT.cookies)
            except Exception as error:
                print(error)
                traceback.print_stack()

        elif(Method == 'DELETE'):
            print("Found DELETE API, So Executing It.")
            try:
                DELETE = requests.put(URL, data=Body, headers=Header)
                print("Executed POST Method")
                result['StatusCode'] = str(DELETE.status_code)
                result['ResponseBody'] = str(DELETE.text)
                result['ResponseHeader'] = str(DELETE.headers)
                result['ResponseCookie'] = str(DELETE.cookies)
            except Exception as error:
                print(error)
                traceback.print_stack()
    except Exception as error:
        print(error)
        traceback.print_stack()

    return result

