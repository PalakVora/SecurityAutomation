import requests, openpyxl,json, re, traceback, logging, time

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
                            data['API'] = str((SheetName["A" + str(RowContents.row)]).value)
                            print(data['API'] + "\n")
                        except Exception as error:
                            print("Error in getting API Name")
                            traceback.print_stack()
                            Excel_WorkBook.close()
                            break

                        try:
                            data['HTTPMethod'] = str((SheetName["B" + str(RowContents.row)]).value)
                            print(data['HTTPMethod'] + "\n")
                        except Exception as error:
                            print(error)
                            traceback.print_stack()
                            Excel_WorkBook.close()
                            break

                        try:
                            data['Protocol'] = str((SheetName["C" + str(RowContents.row)]).value)
                            print(data['Protocol'] + "\n")
                        except Exception as error:
                            print("Error in getting Protocol")
                            traceback.print_stack()
                            Excel_WorkBook.close()
                            break

                        try:
                            data['BaseURL'] = str((SheetName["D" + str(RowContents.row)]).value)
                            print(data['BaseURL'] + "\n")
                        except Exception as error:
                            print("Error in Getting Base URL")
                            traceback.print_stack()
                            Excel_WorkBook.close()
                            break

                        try:
                            data['RelativeURL'] = str((SheetName["E" + str(RowContents.row)]).value)
                            print(data['RelativeURL'] + "\n")
                        except Exception as error:
                            print("Error in getting Relative URL")
                            traceback.print_stack()
                            Excel_WorkBook.close()
                            break

                        try:
                            data['URL'] = str(data['Protocol']) + "://" + str(data['BaseURL']) + str(data['RelativeURL'])
                            print(data['URL'])
                        except Exception as error:
                            print(error)
                            traceback.print_stack()
                            Excel_WorkBook.close()
                            break

                        try:
                            data['Body'] = json.loads(str((SheetName["F" + str(RowContents.row)]).value))
                            print(data['Body'])
                        except Exception as error:
                            print(error)
                            traceback.print_stack()
                            Excel_WorkBook.close()
                            break

                        try:
                            data['Header'] = json.loads(str((SheetName["G" + str(RowContents.row)]).value))
                            print(data['Header'])
                        except Exception as error:
                            print(error)
                            traceback.print_stack()
                            Excel_WorkBook.close()
                            break

                        try:
                            data['Cookie'] = json.loads(str((SheetName["H" + str(RowContents.row)]).value))
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


def HHI(Excel_Location, Excel_Sheet_Name, Module_Name):
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
        BaseURL = returnvalue['BaseURL']
    except Exception as error:
        print(error)
        traceback.print_stack()

    try:
        RelativeURL = returnvalue['RelativeURL']
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
        Check_BaseURL = re.findall(r'\$(.*?)\$', str(BaseURL))
        if (Check_BaseURL != ""):
            for key in Check_BaseURL:
                BaseURL = BaseURL.replace("$", "")
            print(URL)
        else:
            print("No Change in Base URL")
    except Exception as error:
        print(error)
        traceback.print_stack()

    try:
        Check_RelativeURL = re.findall(r'\$(.*?)\$', str(RelativeURL))
        if (Check_RelativeURL != ""):
            for key in Check_RelativeURL:
                RelativeURL = RelativeURL.replace("$", "")
            print(RelativeURL)
        else:
            print("No Change in Relative URL")
    except Exception as error:
        print("Error in reading Relative URL")
        traceback.print_stack()

    try:
        Check_Method = re.findall(r'\$(.*?)\$', str(Method))
        if (Check_Method != ""):
            for key in Check_Method:
                Method = Method.replace("$", "")
            print(Method)
        else:
            print("No Change in Method")
    except Exception as error:
        print("Error in finding Method")
        traceback.print_stack()

    try:
        Check_Protocol = re.findall(r'\$(.*?)\$', str(Protocol))
        if (Check_Protocol != ""):
            for key in Check_Protocol:
                Protocol = Protocol.replace("$", "")
            print(Protocol)
        else:
            print("No Change in Protocol")
    except Exception as error:
        print("Error in finding Protocol")
        traceback.print_stack()

    try:
        Check_URL = re.findall(r'\$(.*?)\$', str(URL))
        if(Check_URL != ""):
            for key in Check_URL:
                URL = URL.replace("$","")
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
                Header = Header.replace("$", "")
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
        StatusCode = {}
        XForwardedHost_Headers = {'X-Forwarded-Host':'www.geeksforgeeks.org'}
        print(XForwardedHost_Headers)
        XForwardedFor_Headers = {'X-Forwarded-For': '127.0.0.1'}
        print(XForwardedFor_Headers)
        XForwardedFor_Headers = {'X-Forwarded-For': '127.0.0.1'}
        print(XForwardedFor_Headers)
        XForwardedProto_Headers = {'X-Forwarded-Proto': 'http'}
        print(XForwardedProto_Headers)
        Attack_Host = BaseURL.replace(BaseURL, "www.geeksforgeeks.org")
        print(Attack_Host)
        try:
            URL = str(Protocol) + "://" + str(BaseURL) + str(RelativeURL)
            print("URL: " + str(URL))
            HOST_Attack_URL = str(Protocol) + "://" + str(Attack_Host) + str(RelativeURL)
            print("Host Header Injection URL: " + str(HOST_Attack_URL))
        except Exception as error:
            print("Error in concatenating URL with Vulnerable host")
            traceback.print_stack()

        if(Method == 'GET'):
            HOST_GET = requests.get(HOST_Attack_URL, data=Body, headers=Header)
            result['HOST StatusCode'] = str(HOST_GET.status_code)

            XForwardedHost_GET = requests.get(HOST_Attack_URL, data=Body, headers=XForwardedHost_Headers)
            result['X-Forwarded-Host StatusCode'] = str(XForwardedHost_GET.status_code)

            XForwardedFor_GET = requests.get(HOST_Attack_URL, data=Body, headers=XForwardedFor_Headers)
            result['X-Forwarded-Header StatusCode'] = str(XForwardedFor_GET.status_code)

            XForwardedProto_GET = requests.get(HOST_Attack_URL, data=Body, headers=XForwardedProto_Headers)
            result['X-Forwarded-Proto StatusCode'] = str(XForwardedProto_GET.status_code)

        elif(Method == 'POST'):
            HOST_POST = requests.post(HOST_Attack_URL, data=Body, headers=Header)
            result['HOST StatusCode'] = str(HOST_POST.status_code)

            XForwardedHost_POST = requests.post(HOST_Attack_URL, data=Body, headers=XForwardedHost_Headers)
            result['X-Forwarded-Host StatusCode'] = str(XForwardedHost_POST.status_code)

            XForwardedFor_POST = requests.post(HOST_Attack_URL, data=Body, headers=XForwardedFor_Headers)
            result['X-Forwarded-Header StatusCode'] = str(XForwardedFor_POST.status_code)

            XForwardedProto_POST = requests.post(HOST_Attack_URL, data=Body, headers=XForwardedProto_Headers)
            result['X-Forwarded-Proto StatusCode'] = str(XForwardedProto_POST.status_code)

        elif (Method == 'PUT'):
            HOST_PUT = requests.put(HOST_Attack_URL, data=Body, headers=Header)
            result['HOST StatusCode'] = str(HOST_PUT.status_code)

            XForwardedHost_PUT = requests.put(HOST_Attack_URL, data=Body, headers=XForwardedHost_Headers)
            result['X-Forwarded-Host StatusCode'] = str(XForwardedHost_PUT.status_code)

            XForwardedFor_PUT = requests.put(HOST_Attack_URL, data=Body, headers=XForwardedFor_Headers)
            result['X-Forwarded-Header StatusCode'] = str(XForwardedFor_PUT.status_code)

            XForwardedProto_PUT = requests.put(HOST_Attack_URL, data=Body, headers=XForwardedProto_Headers)
            result['X-Forwarded-Proto StatusCode'] = str(XForwardedProto_PUT.status_code)

        elif (Method == 'DELETE'):
            HOST_DELETE = requests.delete(HOST_Attack_URL, data=Body, headers=Header)
            result['HOST StatusCode'] = str(HOST_DELETE.status_code)

            XForwardedHost_DELETE = requests.delete(HOST_Attack_URL, data=Body, headers=XForwardedHost_Headers)
            result['X-Forwarded-Host StatusCode'] = str(XForwardedHost_DELETE.status_code)

            XForwardedFor_DELETE = requests.delete(HOST_Attack_URL, data=Body, headers=XForwardedFor_Headers)
            result['X-Forwarded-Header StatusCode'] = str(XForwardedFor_DELETE.status_code)

            XForwardedProto_DELETE = requests.delete(HOST_Attack_URL, data=Body, headers=XForwardedProto_Headers)
            result['X-Forwarded-Proto StatusCode'] = str(XForwardedProto_DELETE.status_code)

    except Exception as error:
        print("Error in executing HOST Injection")
        traceback.print_stack()

    return result