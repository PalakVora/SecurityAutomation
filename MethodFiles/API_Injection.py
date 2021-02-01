import re, requests, json, openpyxl, time, traceback


def readexcel(Excel_Location, Excel_Sheet_Name, Module_Name):
    data = {}
    print("Opening Excel")
    try:
        Excel_WorkBook = openpyxl.load_workbook(Excel_Location)
        print("Opened Excel")
    except:
        print("Error in opening API Excel File")

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
                            HTTP_Method = (SheetName["B" + str(RowContents.row)])
                            print(HTTP_Method.value)
                            data['HTTPMethod'] = str(HTTP_Method.value)
                            print(data['HTTPMethod'])
                        except:
                            print("Error in reading HTTP Method from Excel File")
                            Excel_WorkBook.close()
                            break

                        try:
                            Request_Protocol = (SheetName["C" + str(RowContents.row)])
                            print(Request_Protocol.value)
                            data['Protocol'] = str(Request_Protocol.value)
                            print(data['Protocol'] + "\n")
                        except:
                            print("Error in reading Request Protocol from Excel File")
                            Excel_WorkBook.close()
                            break

                        try:
                            Request_BaseURL = (SheetName["D" + str(RowContents.row)])
                            print("BaseURL = " + str(Request_BaseURL.value) + "\n")
                        except:
                            print("Error in reading Request Base URL from Excel File")
                            Excel_WorkBook.close()
                            break

                        try:
                            Request_RelativeURL = (SheetName["E" + str(RowContents.row)])
                            print("RelativeURL = " + str(Request_RelativeURL.value) + "\n")
                        except:
                            print("Error in reading Request Relative URL from Excel File")
                            Excel_WorkBook.close()
                            break

                        try:
                            data['URL'] = str(data['Protocol']) + "://" + str(Request_BaseURL.value) + str(Request_RelativeURL.value)
                            print(data['URL'])
                        except:
                            print("Error in concatenating URL")
                            Excel_WorkBook.close()
                            break

                        try:
                            Body_Row = (SheetName["F" + str(RowContents.row)])
                            Body_Content = str(Body_Row.value)
                            print("Body = " + Body_Content + "\n")
                            data['Body'] = json.loads(Body_Content)
                            print(data['Body'])
                        except:
                            print("Error in reading Request Body from Excel File")
                            Excel_WorkBook.close()
                            break

                        try:
                            Header_Row = (SheetName["G" + str(RowContents.row)])
                            Header_Content = str(Header_Row.value)
                            print("Header = " + Header_Content + "\n")
                            data['Header'] = json.loads(Header_Content)
                            print(data['Header'])
                        except:
                            print("Error in reading Request Header from Excel File")
                            Excel_WorkBook.close()
                            break

                        try:
                            Cookie_Row = (SheetName["H" + str(RowContents.row)])
                            Cookie_Content = str(Cookie_Row.value)
                            print("Cookie = " + Cookie_Content + "\n")
                            data['Cookie'] = json.loads(Cookie_Content)
                            print(data['Cookie'])
                        except:
                            print("Error in reading Request Cookie from Excel File")
                            Excel_WorkBook.close()
                            break

                        print(data)

                        break
    except:
        print("Error in reading contents")

    return data

def find_vulnerable_parameters(Excel_Location, Excel_Sheet_Name, Module_Name):
    parameter = {}
    try:
        result = readexcel(Excel_Location, Excel_Sheet_Name, Module_Name)
        print("Data from find_vulnerable_parameters ")
        print(result)
    except:
        print('Error in executing Read Excel Method')

    try:
        Method = str(result['HTTPMethod'])
        parameter['HTTPMethod'] = Method
        print("HTTP Method: " + parameter['HTTPMethod'])

        Protocol = str(result['Protocol'])
        parameter['Protocol'] = Protocol
        print("Protocol: " + parameter['Protocol'])

        parameter['URL'] = str(result['URL'])
        print("URL: " + str(parameter['URL']))

        parameter['Body']=result['Body']
        print("Body: " + str(parameter['Body']))

        parameter['Header']=result['Header']
        print("Header: " + str(parameter['Header']))

        parameter['Cookie']=result['Cookie']
        print("Cookie: " + str(parameter['Cookie']))

    except:

        print("Error in Reading API Contents")

    try:
        parameter['URL_Parameter'] = re.findall(r'\$(.*?)\$', parameter['URL'])
        if(parameter['URL_Parameter'] != ""):
            print("Parameter found in URL")
            print(parameter['URL_Parameter'])
        else:
            print("No Parameter found in URL")
            parameter['URL_Parameter'] = parameter['URL']

        parameter['Body_Parameter'] = re.findall(r'\$(.*?)\$', str(parameter['Body']))
        if(parameter['Body_Parameter'] != ""):
            print("Parameter found in Body")
            print(parameter['Body_Parameter'])
        else:
            print("No Parameter found in Body")
            parameter['Body_Parameter'] = parameter['Body']

        parameter['Header_Parameter'] = re.findall(r'\$(.*?)\$', str(parameter['Header']))
        if (parameter['Header_Parameter'] != ""):
            print("Parameter found in Header")
            print(parameter['Header_Parameter'])
        else:
            print("No Parameter found in Header")
            parameter['Header_Parameter'] = parameter['Header']

        parameter['Cookie_Parameter'] = re.findall(r'\$(.*?)\$', str(parameter['Cookie']))
        if (parameter['Cookie_Parameter'] != ""):
            print("Parameter found in Cookie")
            print(parameter['Cookie_Parameter'])
        else:
            print("No Parameter found in Cookie")
            parameter['Cookie_Parameter'] = parameter['Cookie']
    except:
        print("Error in fetching Parameters")

    return parameter


def input_validation(Excel_Location, Excel_Sheet_Name, Module_Name, Payload_Excel_Location, Payload_Sheet_Name):
    result = []
    print("Executing Input Validation")
    Attack = find_vulnerable_parameters(Excel_Location, Excel_Sheet_Name, Module_Name)
    print("Data from input_validation")
    print(Attack)

    Method = Attack['HTTPMethod']
    print(Method)

    URL = Attack['URL']
    print("URL: " + URL)
    URL_Parameter = Attack['URL_Parameter']
    print("Parameters in URL: ")
    print(URL_Parameter)

    Body = Attack['Body']
    print("Body: ")
    print(Body)
    Body_Parameter = Attack['Body_Parameter']
    print("Parameters in Body: ")
    print(Body_Parameter)

    Header = Attack['Header']
    print("Header: ")
    print(Header)
    Header_Parameter = Attack['Header_Parameter']
    print("Parameters in Header: ")
    print(Header_Parameter)

    Cookie = Attack['Cookie']
    print("Cookie: ")
    print(Cookie)
    Cookie_Parameter = Attack['Cookie_Parameter']
    print("Parameters in Cookie: ")
    print(Cookie_Parameter)
    try:
        if(Method == 'GET'):
            print('Executing GET Method')

            if(URL_Parameter != ""):
                print("Parameter found in URL")
                Payload_Excel_WorkBook_Location = openpyxl.load_workbook(Payload_Excel_Location)
                for Payload_SheetName in Payload_Excel_WorkBook_Location.worksheets:
                    if Payload_SheetName.title == Payload_Sheet_Name:
                        print("Worksheet Found = " + Payload_SheetName.title)
                        Payload_ActiveWorkSheet = Payload_Excel_WorkBook_Location[Payload_SheetName.title]
                        print("Title of Sheet = " + Payload_ActiveWorkSheet.title)
                        Payload_RowLength = Payload_SheetName.max_row
                        Payload_ColumnLength = Payload_SheetName.max_column
                        print("Number of Payloads for " + str(Payload_SheetName.title) + " = " + str(Payload_RowLength - 1))
                        for i in range(2, Payload_RowLength + 1):
                            Payload_RowContents = Payload_SheetName.cell(row=i, column=1)
                            print("Row " + str(Payload_RowContents.row - 1) + " = " + str(Payload_RowContents.value), end="" + "\n")
                            for key in URL_Parameter:
                                AttackURL = URL.replace(key, str(Payload_RowContents.value))
                                AttackURL = AttackURL.replace("$", "")
                                print(AttackURL)
                                AttackBody = str(Body).replace("$", "")
                                print(AttackBody)
                                AttackHeader = str(Header).replace("$", "")
                                print(AttackHeader)
                                AttackCookie = str(Cookie).replace("$", "")
                                print(AttackCookie)
                                try:
                                    response = requests.get(AttackURL, data=AttackBody, headers=Header)
                                    StatusCode = str(response.status_code)
                                    print(StatusCode + "\n")
                                    result.append(StatusCode)
                                    print(result)
                                    time.sleep(10)
                                except:
                                    print(traceback)
                                    print("Error in executing: " + str(AttackURL))
                                    StatusCode = '500'
                                    result.append(StatusCode)
                                    print(result)
                                    time.sleep(10)
                                print(result)
            else:
                print("No Parameter choosen in the API")

        elif(Method == 'POST'):
            print('Executing POST Method')

            if(URL_Parameter != ""):
                print("Parameter found in POST URL")
                Payload_Excel_WorkBook_Location = openpyxl.load_workbook(Payload_Excel_Location)
                for Payload_SheetName in Payload_Excel_WorkBook_Location.worksheets:
                    if Payload_SheetName.title == Payload_Sheet_Name:
                        print("Worksheet Found = " + Payload_SheetName.title)
                        Payload_ActiveWorkSheet = Payload_Excel_WorkBook_Location[Payload_SheetName.title]
                        print("Title of Sheet = " + Payload_ActiveWorkSheet.title)
                        Payload_RowLength = Payload_SheetName.max_row
                        Payload_ColumnLength = Payload_SheetName.max_column
                        print("Number of Payloads for " + str(Payload_SheetName.title) + " = " + str(Payload_RowLength - 1))
                        for i in range(2, Payload_RowLength + 1):
                            Payload_RowContents = Payload_SheetName.cell(row=i, column=1)
                            print("Row " + str(Payload_RowContents.row - 1) + " = " + str(Payload_RowContents.value), end="" + "\n")
                            for key in URL_Parameter:
                                AttackURL = URL.replace(key, str(Payload_RowContents.value))
                                AttackURL = AttackURL.replace("$", "")
                                print(AttackURL)
                                AttackBody = str(Body).replace("$", "")
                                print(AttackBody)
                                AttackHeader = str(Header).replace("$", "")
                                print(AttackHeader)
                                AttackCookie = str(Cookie).replace("$", "")
                                print(AttackCookie)
                                try:
                                    response = requests.post(AttackURL, data=AttackBody, headers=Header)
                                    StatusCode = str(response.status_code)
                                    print(StatusCode + "\n")
                                    result.append(StatusCode)
                                    print(result)
                                    time.sleep(10)
                                except:
                                    print("Error in executing: " + str(AttackURL))
                                    StatusCode = '500'
                                    result.append(StatusCode)
                                    print(result)
                                    time.sleep(10)
                                print(result)

            elif(Body_Parameter != ""):
                print("Parameter found in POST Body")
                Payload_Excel_WorkBook_Location = openpyxl.load_workbook(Payload_Excel_Location)
                for Payload_SheetName in Payload_Excel_WorkBook_Location.worksheets:
                    if Payload_SheetName.title == Payload_Sheet_Name:
                        print("Worksheet Found = " + Payload_SheetName.title)
                        Payload_ActiveWorkSheet = Payload_Excel_WorkBook_Location[Payload_SheetName.title]
                        print("Title of Sheet = " + Payload_ActiveWorkSheet.title)
                        Payload_RowLength = Payload_SheetName.max_row
                        Payload_ColumnLength = Payload_SheetName.max_column
                        print("Number of Payloads for " + str(Payload_SheetName.title) + " = " + str(
                            Payload_RowLength - 1))
                        for i in range(2, Payload_RowLength + 1):
                            Payload_RowContents = Payload_SheetName.cell(row=i, column=1)
                            print("Row " + str(Payload_RowContents.row - 1) + " = " + str(Payload_RowContents.value),
                                  end="" + "\n")
                            for key in Body_Parameter:
                                AttackBody = Body.replace(key, str(Payload_RowContents.value))
                                AttackURL = AttackURL.replace("$", "")
                                print(AttackURL)
                                AttackBody = str(Body).replace("$", "")
                                print(AttackBody)
                                AttackHeader = str(Header).replace("$", "")
                                print(AttackHeader)
                                AttackCookie = str(Cookie).replace("$", "")
                                print(AttackCookie)
                                try:
                                    response = requests.post(AttackURL, data=AttackBody, headers=Header)
                                    StatusCode = str(response.status_code)
                                    print(StatusCode + "\n")
                                    result.append(StatusCode)
                                    print(result)
                                    time.sleep(10)
                                except:
                                    print("Error in executing: " + str(AttackURL))
                                    StatusCode = '500'
                                    result.append(StatusCode)
                                    print(result)
                                    time.sleep(10)
                                print(result)

            elif(Header_Parameter != ""):
                print("Parameter found in POST Header")
                Payload_Excel_WorkBook_Location = openpyxl.load_workbook(Payload_Excel_Location)
                for Payload_SheetName in Payload_Excel_WorkBook_Location.worksheets:
                    if Payload_SheetName.title == Payload_Sheet_Name:
                        print("Worksheet Found = " + Payload_SheetName.title)
                        Payload_ActiveWorkSheet = Payload_Excel_WorkBook_Location[Payload_SheetName.title]
                        print("Title of Sheet = " + Payload_ActiveWorkSheet.title)
                        Payload_RowLength = Payload_SheetName.max_row
                        Payload_ColumnLength = Payload_SheetName.max_column
                        print("Number of Payloads for " + str(Payload_SheetName.title) + " = " + str(
                            Payload_RowLength - 1))
                        for i in range(2, Payload_RowLength + 1):
                            Payload_RowContents = Payload_SheetName.cell(row=i, column=1)
                            print("Row " + str(Payload_RowContents.row - 1) + " = " + str(Payload_RowContents.value),
                                  end="" + "\n")
                            for key in Header_Parameter:
                                AttackHeader = Header.replace(key, str(Payload_RowContents.value))
                                AttackURL = AttackURL.replace("$", "")
                                print(AttackURL)
                                AttackBody = str(Body).replace("$", "")
                                print(AttackBody)
                                AttackHeader = str(Header).replace("$", "")
                                print(AttackHeader)
                                AttackCookie = str(Cookie).replace("$", "")
                                print(AttackCookie)
                                try:
                                    response = requests.post(AttackURL, data=AttackBody, headers=Header)
                                    StatusCode = str(response.status_code)
                                    print(StatusCode + "\n")
                                    result.append(StatusCode)
                                    print(result)
                                    time.sleep(10)
                                except:
                                    print("Error in executing: " + str(AttackURL))
                                    StatusCode = '500'
                                    result.append(StatusCode)
                                    print(result)
                                    time.sleep(10)
                                print(result)

            elif(Cookie_Parameter != ""):
                print("Parameter found in POST Cookie")
                Payload_Excel_WorkBook_Location = openpyxl.load_workbook(Payload_Excel_Location)
                for Payload_SheetName in Payload_Excel_WorkBook_Location.worksheets:
                    if Payload_SheetName.title == Payload_Sheet_Name:
                        print("Worksheet Found = " + Payload_SheetName.title)
                        Payload_ActiveWorkSheet = Payload_Excel_WorkBook_Location[Payload_SheetName.title]
                        print("Title of Sheet = " + Payload_ActiveWorkSheet.title)
                        Payload_RowLength = Payload_SheetName.max_row
                        Payload_ColumnLength = Payload_SheetName.max_column
                        print("Number of Payloads for " + str(Payload_SheetName.title) + " = " + str(
                            Payload_RowLength - 1))
                        for i in range(2, Payload_RowLength + 1):
                            Payload_RowContents = Payload_SheetName.cell(row=i, column=1)
                            print("Row " + str(Payload_RowContents.row - 1) + " = " + str(Payload_RowContents.value),
                                  end="" + "\n")
                            for key in Cookie_Parameter:
                                AttackCookie = Cookie.replace(key, str(Payload_RowContents.value))
                                AttackURL = AttackURL.replace("$", "")
                                print(AttackURL)
                                AttackBody = str(Body).replace("$", "")
                                print(AttackBody)
                                AttackHeader = str(Header).replace("$", "")
                                print(AttackHeader)
                                AttackCookie = str(Cookie).replace("$", "")
                                print(AttackCookie)
                                try:
                                    response = requests.post(AttackURL, data=AttackBody, headers=Header)
                                    StatusCode = str(response.status_code)
                                    print(StatusCode + "\n")
                                    result.append(StatusCode)
                                    print(result)
                                    time.sleep(10)
                                except:
                                    print("Error in executing: " + str(AttackURL))
                                    StatusCode = '500'
                                    result.append(StatusCode)
                                    print(result)
                                    time.sleep(10)
                                print(result)
            else:
                print("No Parameter choosen in the API")

        elif(Method == 'PUT'):
            print('Executing PUT Method')

            if(URL_Parameter != ""):
                print("Parameter found in PUT URL")
                Payload_Excel_WorkBook_Location = openpyxl.load_workbook(Payload_Excel_Location)
                for Payload_SheetName in Payload_Excel_WorkBook_Location.worksheets:
                    if Payload_SheetName.title == Payload_Sheet_Name:
                        print("Worksheet Found = " + Payload_SheetName.title)
                        Payload_ActiveWorkSheet = Payload_Excel_WorkBook_Location[Payload_SheetName.title]
                        print("Title of Sheet = " + Payload_ActiveWorkSheet.title)
                        Payload_RowLength = Payload_SheetName.max_row
                        Payload_ColumnLength = Payload_SheetName.max_column
                        print("Number of Payloads for " + str(Payload_SheetName.title) + " = " + str(Payload_RowLength - 1))
                        for i in range(2, Payload_RowLength + 1):
                            Payload_RowContents = Payload_SheetName.cell(row=i, column=1)
                            print("Row " + str(Payload_RowContents.row - 1) + " = " + str(Payload_RowContents.value), end="" + "\n")
                            for key in URL_Parameter:
                                AttackURL = URL.replace(key, str(Payload_RowContents.value))
                                AttackURL = AttackURL.replace("$", "")
                                print(AttackURL)
                                AttackBody = str(Body).replace("$", "")
                                print(AttackBody)
                                AttackHeader = str(Header).replace("$", "")
                                print(AttackHeader)
                                AttackCookie = str(Cookie).replace("$", "")
                                print(AttackCookie)
                                try:
                                    response = requests.put(AttackURL, data=AttackBody, headers=Header)
                                    StatusCode = str(response.status_code)
                                    print(StatusCode + "\n")
                                    result.append(StatusCode)
                                    print(result)
                                    time.sleep(10)
                                except:
                                    print("Error in executing: " + str(AttackURL))
                                    StatusCode = '500'
                                    result.append(StatusCode)
                                    print(result)
                                    time.sleep(10)
                                print(result)

            elif(Body_Parameter != ""):
                print("Parameter found in PUT Body")
                Payload_Excel_WorkBook_Location = openpyxl.load_workbook(Payload_Excel_Location)
                for Payload_SheetName in Payload_Excel_WorkBook_Location.worksheets:
                    if Payload_SheetName.title == Payload_Sheet_Name:
                        print("Worksheet Found = " + Payload_SheetName.title)
                        Payload_ActiveWorkSheet = Payload_Excel_WorkBook_Location[Payload_SheetName.title]
                        print("Title of Sheet = " + Payload_ActiveWorkSheet.title)
                        Payload_RowLength = Payload_SheetName.max_row
                        Payload_ColumnLength = Payload_SheetName.max_column
                        print("Number of Payloads for " + str(Payload_SheetName.title) + " = " + str(
                            Payload_RowLength - 1))
                        for i in range(2, Payload_RowLength + 1):
                            Payload_RowContents = Payload_SheetName.cell(row=i, column=1)
                            print("Row " + str(Payload_RowContents.row - 1) + " = " + str(Payload_RowContents.value),
                                  end="" + "\n")
                            for key in Body_Parameter:
                                AttackBody = Body.replace(key, str(Payload_RowContents.value))
                                AttackURL = AttackURL.replace("$", "")
                                print(AttackURL)
                                AttackBody = str(Body).replace("$", "")
                                print(AttackBody)
                                AttackHeader = str(Header).replace("$", "")
                                print(AttackHeader)
                                AttackCookie = str(Cookie).replace("$", "")
                                print(AttackCookie)
                                try:
                                    response = requests.put(AttackURL, data=AttackBody, headers=Header)
                                    StatusCode = str(response.status_code)
                                    print(StatusCode + "\n")
                                    result.append(StatusCode)
                                    print(result)
                                    time.sleep(10)
                                except:
                                    print("Error in executing: " + str(AttackURL))
                                    StatusCode = '500'
                                    result.append(StatusCode)
                                    print(result)
                                    time.sleep(10)
                                print(result)

            elif(Header_Parameter != ""):
                print("Parameter found in PUT Header")
                Payload_Excel_WorkBook_Location = openpyxl.load_workbook(Payload_Excel_Location)
                for Payload_SheetName in Payload_Excel_WorkBook_Location.worksheets:
                    if Payload_SheetName.title == Payload_Sheet_Name:
                        print("Worksheet Found = " + Payload_SheetName.title)
                        Payload_ActiveWorkSheet = Payload_Excel_WorkBook_Location[Payload_SheetName.title]
                        print("Title of Sheet = " + Payload_ActiveWorkSheet.title)
                        Payload_RowLength = Payload_SheetName.max_row
                        Payload_ColumnLength = Payload_SheetName.max_column
                        print("Number of Payloads for " + str(Payload_SheetName.title) + " = " + str(
                            Payload_RowLength - 1))
                        for i in range(2, Payload_RowLength + 1):
                            Payload_RowContents = Payload_SheetName.cell(row=i, column=1)
                            print("Row " + str(Payload_RowContents.row - 1) + " = " + str(Payload_RowContents.value),
                                  end="" + "\n")
                            for key in Header_Parameter:
                                AttackHeader = Header.replace(key, str(Payload_RowContents.value))
                                AttackURL = AttackURL.replace("$", "")
                                print(AttackURL)
                                AttackBody = str(Body).replace("$", "")
                                print(AttackBody)
                                AttackHeader = str(Header).replace("$", "")
                                print(AttackHeader)
                                AttackCookie = str(Cookie).replace("$", "")
                                print(AttackCookie)
                                try:
                                    response = requests.get(AttackURL, data=AttackBody, headers=Header)
                                    StatusCode = str(response.status_code)
                                    print(StatusCode + "\n")
                                    result.append(StatusCode)
                                    print(result)
                                    time.sleep(10)
                                except:
                                    print("Error in executing: " + str(AttackURL))
                                    StatusCode = '500'
                                    result.append(StatusCode)
                                    print(result)
                                    time.sleep(10)
                                print(result)

            elif(Cookie_Parameter != ""):
                print("Parameter found in PUT Cookie")
                Payload_Excel_WorkBook_Location = openpyxl.load_workbook(Payload_Excel_Location)
                for Payload_SheetName in Payload_Excel_WorkBook_Location.worksheets:
                    if Payload_SheetName.title == Payload_Sheet_Name:
                        print("Worksheet Found = " + Payload_SheetName.title)
                        Payload_ActiveWorkSheet = Payload_Excel_WorkBook_Location[Payload_SheetName.title]
                        print("Title of Sheet = " + Payload_ActiveWorkSheet.title)
                        Payload_RowLength = Payload_SheetName.max_row
                        Payload_ColumnLength = Payload_SheetName.max_column
                        print("Number of Payloads for " + str(Payload_SheetName.title) + " = " + str(
                            Payload_RowLength - 1))
                        for i in range(2, Payload_RowLength + 1):
                            Payload_RowContents = Payload_SheetName.cell(row=i, column=1)
                            print("Row " + str(Payload_RowContents.row - 1) + " = " + str(Payload_RowContents.value),
                                  end="" + "\n")
                            for key in Cookie_Parameter:
                                AttackCookie = Cookie.replace(key, str(Payload_RowContents.value))
                                AttackURL = AttackURL.replace("$", "")
                                print(AttackURL)
                                AttackBody = str(Body).replace("$", "")
                                print(AttackBody)
                                AttackHeader = str(Header).replace("$", "")
                                print(AttackHeader)
                                AttackCookie = str(Cookie).replace("$", "")
                                print(AttackCookie)
                                try:
                                    response = requests.put(AttackURL, data=AttackBody, headers=Header)
                                    StatusCode = str(response.status_code)
                                    print(StatusCode + "\n")
                                    result.append(StatusCode)
                                    print(result)
                                    time.sleep(10)
                                except:
                                    print("Error in executing: " + str(AttackURL))
                                    StatusCode = '500'
                                    result.append(StatusCode)
                                    print(result)
                                    time.sleep(10)
                                print(result)
            else:
                print("No Parameter choosen in the API")

        if(Method == 'DELETE'):
            print('Executing DELETE Method')

            if(URL_Parameter != ""):
                print("Parameter found in DELETE URL")
                Payload_Excel_WorkBook_Location = openpyxl.load_workbook(Payload_Excel_Location)
                for Payload_SheetName in Payload_Excel_WorkBook_Location.worksheets:
                    if Payload_SheetName.title == Payload_Sheet_Name:
                        print("Worksheet Found = " + Payload_SheetName.title)
                        Payload_ActiveWorkSheet = Payload_Excel_WorkBook_Location[Payload_SheetName.title]
                        print("Title of Sheet = " + Payload_ActiveWorkSheet.title)
                        Payload_RowLength = Payload_SheetName.max_row
                        Payload_ColumnLength = Payload_SheetName.max_column
                        print("Number of Payloads for " + str(Payload_SheetName.title) + " = " + str(Payload_RowLength - 1))
                        for i in range(2, Payload_RowLength + 1):
                            Payload_RowContents = Payload_SheetName.cell(row=i, column=1)
                            print("Row " + str(Payload_RowContents.row - 1) + " = " + str(Payload_RowContents.value), end="" + "\n")
                            for key in URL_Parameter:
                                AttackURL = URL.replace(key, str(Payload_RowContents.value))
                                AttackURL = AttackURL.replace("$", "")
                                print(AttackURL)
                                AttackBody = str(Body).replace("$", "")
                                print(AttackBody)
                                AttackHeader = str(Header).replace("$", "")
                                print(AttackHeader)
                                AttackCookie = str(Cookie).replace("$", "")
                                print(AttackCookie)
                                try:
                                    response = requests.delete(AttackURL, data=AttackBody, headers=Header)
                                    StatusCode = str(response.status_code)
                                    print(StatusCode + "\n")
                                    result.append(StatusCode)
                                    print(result)
                                    time.sleep(10)
                                except:
                                    print("Error in executing: " + str(AttackURL))
                                    StatusCode = '500'
                                    result.append(StatusCode)
                                    print(result)
                                    time.sleep(10)
                                print(result)

            elif(Body_Parameter != ""):
                print("Parameter found in DELETE Body")
                Payload_Excel_WorkBook_Location = openpyxl.load_workbook(Payload_Excel_Location)
                for Payload_SheetName in Payload_Excel_WorkBook_Location.worksheets:
                    if Payload_SheetName.title == Payload_Sheet_Name:
                        print("Worksheet Found = " + Payload_SheetName.title)
                        Payload_ActiveWorkSheet = Payload_Excel_WorkBook_Location[Payload_SheetName.title]
                        print("Title of Sheet = " + Payload_ActiveWorkSheet.title)
                        Payload_RowLength = Payload_SheetName.max_row
                        Payload_ColumnLength = Payload_SheetName.max_column
                        print("Number of Payloads for " + str(Payload_SheetName.title) + " = " + str(
                            Payload_RowLength - 1))
                        for i in range(2, Payload_RowLength + 1):
                            Payload_RowContents = Payload_SheetName.cell(row=i, column=1)
                            print("Row " + str(Payload_RowContents.row - 1) + " = " + str(Payload_RowContents.value),
                                  end="" + "\n")
                            for key in Body_Parameter:
                                AttackBody = Body.replace(key, str(Payload_RowContents.value))
                                AttackURL = AttackURL.replace("$", "")
                                print(AttackURL)
                                AttackBody = str(Body).replace("$", "")
                                print(AttackBody)
                                AttackHeader = str(Header).replace("$", "")
                                print(AttackHeader)
                                AttackCookie = str(Cookie).replace("$", "")
                                print(AttackCookie)
                                try:
                                    response = requests.delete(AttackURL, data=AttackBody, headers=Header)
                                    StatusCode = str(response.status_code)
                                    print(StatusCode + "\n")
                                    result.append(StatusCode)
                                    print(result)
                                    time.sleep(10)
                                except:
                                    print("Error in executing: " + str(AttackURL))
                                    StatusCode = '500'
                                    result.append(StatusCode)
                                    print(result)
                                    time.sleep(10)
                                print(result)

            elif(Header_Parameter != ""):
                print("Parameter found in DELETE Header")
                Payload_Excel_WorkBook_Location = openpyxl.load_workbook(Payload_Excel_Location)
                for Payload_SheetName in Payload_Excel_WorkBook_Location.worksheets:
                    if Payload_SheetName.title == Payload_Sheet_Name:
                        print("Worksheet Found = " + Payload_SheetName.title)
                        Payload_ActiveWorkSheet = Payload_Excel_WorkBook_Location[Payload_SheetName.title]
                        print("Title of Sheet = " + Payload_ActiveWorkSheet.title)
                        Payload_RowLength = Payload_SheetName.max_row
                        Payload_ColumnLength = Payload_SheetName.max_column
                        print("Number of Payloads for " + str(Payload_SheetName.title) + " = " + str(
                            Payload_RowLength - 1))
                        for i in range(2, Payload_RowLength + 1):
                            Payload_RowContents = Payload_SheetName.cell(row=i, column=1)
                            print("Row " + str(Payload_RowContents.row - 1) + " = " + str(Payload_RowContents.value),
                                  end="" + "\n")
                            for key in Header_Parameter:
                                AttackHeader = Header.replace(key, str(Payload_RowContents.value))
                                AttackURL = AttackURL.replace("$", "")
                                print(AttackURL)
                                AttackBody = str(Body).replace("$", "")
                                print(AttackBody)
                                AttackHeader = str(Header).replace("$", "")
                                print(AttackHeader)
                                AttackCookie = str(Cookie).replace("$", "")
                                print(AttackCookie)
                                try:
                                    response = requests.delete(AttackURL, data=AttackBody, headers=Header)
                                    StatusCode = str(response.status_code)
                                    print(StatusCode + "\n")
                                    result.append(StatusCode)
                                    print(result)
                                    time.sleep(10)
                                except:
                                    print("Error in executing: " + str(AttackURL))
                                    StatusCode = '500'
                                    result.append(StatusCode)
                                    print(result)
                                    time.sleep(10)
                                print(result)

            elif(Cookie_Parameter != ""):
                print("Parameter found in DELETE Cookie")
                Payload_Excel_WorkBook_Location = openpyxl.load_workbook(Payload_Excel_Location)
                for Payload_SheetName in Payload_Excel_WorkBook_Location.worksheets:
                    if Payload_SheetName.title == Payload_Sheet_Name:
                        print("Worksheet Found = " + Payload_SheetName.title)
                        Payload_ActiveWorkSheet = Payload_Excel_WorkBook_Location[Payload_SheetName.title]
                        print("Title of Sheet = " + Payload_ActiveWorkSheet.title)
                        Payload_RowLength = Payload_SheetName.max_row
                        Payload_ColumnLength = Payload_SheetName.max_column
                        print("Number of Payloads for " + str(Payload_SheetName.title) + " = " + str(
                            Payload_RowLength - 1))
                        for i in range(2, Payload_RowLength + 1):
                            Payload_RowContents = Payload_SheetName.cell(row=i, column=1)
                            print("Row " + str(Payload_RowContents.row - 1) + " = " + str(Payload_RowContents.value),
                                  end="" + "\n")
                            for key in Cookie_Parameter:
                                AttackCookie = Cookie.replace(key, str(Payload_RowContents.value))
                                AttackURL = AttackURL.replace("$", "")
                                print(AttackURL)
                                AttackBody = str(Body).replace("$", "")
                                print(AttackBody)
                                AttackHeader = str(Header).replace("$", "")
                                print(AttackHeader)
                                AttackCookie = str(Cookie).replace("$", "")
                                print(AttackCookie)
                                try:
                                    response = requests.delete(AttackURL, data=AttackBody, headers=Header)
                                    StatusCode = str(response.status_code)
                                    print(StatusCode + "\n")
                                    result.append(StatusCode)
                                    print(result)
                                    time.sleep(10)
                                except:
                                    print("Error in executing: " + str(AttackURL))
                                    StatusCode = '500'
                                    result.append(StatusCode)
                                    print(result)
                                    time.sleep(10)
                                print(result)
            else:
                print("No Parameter choosen in the API")

    except:
        print("Error in identifying the method")
    return result

"""
    for key in URL_Parameter:
        AttackURL = URL.replace(key, '<script>alert(1)</script>')
        print(AttackURL)
        AttackURL = AttackURL.replace("$", "")
        AttackBody = str(Body).replace("$", "")
        AttackHeader = str(Header).replace("$", "")
        AttackCookie = str(Cookie).replace("$", "")
        print("Vulnerable URL = " + AttackURL)
        try:
            response = requests.post(str(AttackURL), data=AttackBody, headers=AttackHeader, cookies=AttackCookie, timeout=100)
            print(response)
            StatusCode = str(response.status_code)
            result['StatusCode'] = str(StatusCode)
        except:
            print("Error in executing: " + str(AttackURL))
            result['StatusCode'] = '500'


    print(result)
    return result



        for key in Parametrized_URL:
            newURL = URL.replace(key, '<script>alert(1)</script>')
            newURL = newURL.replace("$", "")
            print("Vulnerable URL = " + newURL)
            break
"""