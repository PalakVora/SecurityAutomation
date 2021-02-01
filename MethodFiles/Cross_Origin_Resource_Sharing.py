import requests, openpyxl,json, re, traceback, logging, time


#========================== OPEN EXCEL======================================

def readexcel(Excel_Location, Excel_Sheet_Name, Module_Name):
    data = {}
    print("Opening Excel")
    try:
        Excel_WorkBook = openpyxl.load_workbook(Excel_Location)
        print("Opened Excel")
    except Exception as error:
        print("Error in opening API Excel File")
        traceback.print_stack()

#========================== GET SHEET FROM EXCEL======================================

def find_sheet_name(Excel_Sheet_Name,Module_Name,Excel_WorkBook):
    print("inside sheet name")
    for sheetname in Excel_WorkBook.worksheets:
        if sheetname.title == Excel_Sheet_Name:
            ActiveWorkSheet = Excel_WorkBook[sheetname.title]
            print("Title of Sheet = " + ActiveWorkSheet.title)
            print("Sheetname =" + sheetname.title)
            return sheetname
        else:
            continue

#========================== FIND API NAME FROM EXCEL SHEET ======================================

def find_module_name(Sheetname,Module_Name):
    RowLength = Sheetname.max_row
    ColumnLength = Sheetname.max_column
    for i in range(1, RowLength + 2):
        RowContents = Sheetname.cell(row=i, column=1)
        print("Row " + str(RowContents.row) + " = " + str(RowContents.value))
        if ((RowContents.value) == Module_Name):
            print("Module Found : " + str(RowContents.value) + " in Row - " + str(RowContents.row) + " of Worksheet - " + Sheetname.title)
            return RowContents
        else:
            continue
        try:
            print(str((Sheetname["A" + str(RowContents.row)]).value) + "\n That API name section")
        except Exception as error:
            print("Error in getting API Name")
            traceback.print_stack()
        break
              

        #          for j in range(1, ColumnLength + 1):
        #             Response = dict()
        #            ColumnContents = SheetName.cell(row=RowContents.row, column=j)
        #           print(ColumnContents.value, end="" + "\n")

#========================== GET THE HTTP METHOD FROM THE API OF THE EXCEL SHEET ======================================
#      
def read_method(Sheetname,Rowcontents,Excel_WorkBook):
        try:
            HTTP_Method = (Sheetname["B" + str(Rowcontents.row)].value)
            print("ROw" + str(Rowcontents.row))
            print(HTTP_Method.value)
            return str(HTTP_Method.value)
        except Exception as error:
            print("Error in reading HTTP Method from Excel File")
            print(error)
            Excel_WorkBook.close()
            return 0
            
#========================== GET PROTOCOL FROM THE API OF THE EXCEL SHEET ======================================

def read_protocol(Sheetname,RowContents,Excel_WorkBook):
        try:
            Request_Protocol = (Sheetname["C" + str(RowContents.row)])
            print(Request_Protocol.value)
            return str(Request_Protocol.value)
        except Exception as error:
            print("Error in reading Request Protocol from Excel File")
            Excel_WorkBook.close()                        
                        


#========================== GET BASE URL FROM THE API OF THE EXCEL SHEET ======================================

def read_base_url(Sheetname,RowContents,Excel_WorkBook):
        try:
            Request_BaseURL = (Sheetname["D" + str(RowContents.row)])
            print("BaseURL = " + str(Request_BaseURL.value) + "\n")
            return str(Request_BaseURL.value)
           
        except:
            print("Error in reading Request Base URL from Excel File")
            Excel_WorkBook.close() 

#========================== GET RELATIVE URL FROM THE API OF THE EXCEL SHEET ======================================

def read_relative_url(Sheetname,RowContents,Excel_WorkBook):   
        try:
             Request_RelativeURL = (Sheetname["E" + str(RowContents.row)])
             print("RelativeURL = " + str(Request_RelativeURL.value) + "\n")
             return str(Request_RelativeURL.value)
        except:
            print("Error in reading Request Relative URL from Excel File")
            Excel_WorkBook.close()


   #                 SEt URL
  #                      try:
  #                          data['URL'] = str(data['Protocol']) + "://" + str(data['BaseURL']) + str(data['RelativeURL'])
  #                          print(data['URL'])
  #                      except Exception as error:
  #                          print(error)
  #                          traceback.print_stack()
 #                           Excel_WorkBook.close()
#                            break

 
#========================== GET BODY FROM THE API OF THE EXCEL SHEET ======================================

def read_body(Sheetname,RowContents,Excel_WorkBook):
    try:
        Body_Row = json.loads(str((Sheetname["F" + str(RowContents.row)]).value))
        print("Body ROW",Body_Row)
        return Body_Row
    except:
        print("Error in reading Request Body from Excel File")
        Excel_WorkBook.close()
#data['Body'] = json.loads(str((SheetName["F" + str(RowContents.row)]).value))
#Body_Row=(Sheetname["F" + str(RowContents.row)])                      

#========================== GET HEADER FROM THE API OF THE EXCEL SHEET ======================================

def read_header(Sheetname,RowContents,Excel_WorkBook):
    try:
        Header_Row = json.loads(str((Sheetname["G" + str(RowContents.row)]).value))
        return Header_Row
    except:
        print("Error in reading Request Header from Excel File")
        Excel_WorkBook.close()
#Header_Row = (Sheetname["G" + str(RowContents.row)])
#data['Header'] = json.loads(str((SheetName["G" + str(RowContents.row)]).value))                        try:

#========================== GET COOKIE FROM THE API OF THE EXCEL SHEET ======================================

def read_cookie(Sheetname,RowContents,Excel_WorkBook):
    try:
        Cookie_Row = json.loads(str((Sheetname["H" + str(RowContents.row)]).value))
        return Cookie_Row
    except:
        print("Error in reading Request Cookie from Excel File")
        Excel_WorkBook.close()
        
# Cookie_Row = (Sheetname["H" + str(RowContents.row)])
#  data['Cookie'] = json.loads(str((SheetName["H" + str(RowContents.row)]).value))

#========================== GET ALL API DETAILS TO SEND THE REQUEST ======================================
                      
def find_api(Excel_Location, Excel_Sheet_Name, Module_Name):
    try:
        data = {}
        Excel_WorkBook=readexcel(Excel_Location, Excel_Sheet_Name, Module_Name)
        print("Outside read excel")
        Sheetname=find_sheet_name(Excel_Sheet_Name,Module_Name,Excel_WorkBook)
        print("Out of sheet name" + Sheetname.title)
        Rowcontents=find_module_name(Sheetname,Module_Name)
        print("Outside row")
        if(read_method(Sheetname,Rowcontents,Excel_WorkBook)):
            method_name=read_method(Sheetname,Rowcontents,Excel_WorkBook)
            data['HTTPMethod'] = method_name
            print(data['HTTPMethod'])
        else:
             raise Error("HTTP Method not recognised")
        protocol_name=read_protocol(Sheetname,Rowcontents,Excel_WorkBook)
        data['Protocol'] = protocol_name
        print(data['Protocol'] + "\n")
        base_url=read_base_url(Sheetname,Rowcontents,Excel_WorkBook)
        relative_url=read_relative_url(Sheetname,Rowcontents,Excel_WorkBook)
        try:
            data['URL'] = str(data['Protocol']) + "://" + base_url + relative_url
            print(data['URL'])
        except:
            print("Error in concatenating URL")
            #Excel_WorkBook.close()
        body=read_body(Sheetname,Rowcontents,Excel_WorkBook)
        print("Body = " + body + "\n")
        data['Body'] = body
        print("Fdata Body")
        print(data['Body'])
        header=read_header(Sheetname,Rowcontents,Excel_WorkBook)
        print("Header = " + header + "\n")
        data['Header'] = json.loads(header)
        print(data['Header'])
        cookie=read_cookie(Sheetname,Rowcontents,Excel_WorkBook) 
        print("Cookie = " + cookie + "\n")
        data['Cookie'] = json.loads(cookie)
        print(data['Cookie'])
        print(data)
    except:
        print("Error in reading contents")

    return data


#========================== IDENTIFY THE $ PARAMETERS TO BE ATTACKED ======================================

def find_vulnerable_parameters(result):
    parameter = {}
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
        if(parameter['URL_Parameter']):
            print("Parameter found in URL")
            print(parameter['URL_Parameter'])
        else:
            print("No Parameter found in URL")
           # parameter['URL_Parameter'] = parameter['URL']

        parameter['Body_Parameter'] = re.findall(r'\$(.*?)\$', str(parameter['Body']))
        if(parameter['Body_Parameter']):
            print("Parameter found in Body")
            print(parameter['Body_Parameter'])
        else:
            print("No Parameter found in Body")
            parameter['Body_Parameter'] = parameter['Body']

        parameter['Header_Parameter'] = re.findall(r'\$(.*?)\$', str(parameter['Header']))
        if (parameter['Header_Parameter']):
            print("Parameter found in Header")
            print(parameter['Header_Parameter'])
        else:
            print("No Parameter found in Header")
            #parameter['Header_Parameter'] = parameter['Header']

        parameter['Cookie_Parameter'] = re.findall(r'\$(.*?)\$', str(parameter['Cookie']))
        if (parameter['Cookie_Parameter']):
            print("Parameter found in Cookie")
            print(parameter['Cookie_Parameter'])
        else:
            print("No Parameter found in Cookie")
            #parameter['Cookie_Parameter'] = parameter['Cookie']
    except:
        print("Error in fetching Parameters")

    return parameter


#========================== PERFORM ATTACK ON THE $ PARAMETERS AND GET RESPONSE ======================================

def perform_attack(Area,METhod,Any_Parameter,Payload_RowLength,Payload_SheetName,URL,Body,Header,Cookie):
    result = []
    if(Any_Parameter):
        print("Parameter found in = " + Area)
        for i in range(2, Payload_RowLength + 1):
            Payload_RowContents = Payload_SheetName.cell(row=i, column=1)
            print("Row " + str(Payload_RowContents.row - 1) + " = " + str(Payload_RowContents.value), end="" + "\n")
            for key in Any_Parameter:
                if(Area=='URL'):
                    print("Area is = " + Area)
                    AttackURL = URL.replace(key, str(Payload_RowContents.value))
                    AttackURL = AttackURL.replace("$", "")
                    print("Attack url : " + str(AttackURL))
                    AttackBody = str(Body).replace("$", "")
                    print("Body : " + str(AttackBody))
                    AttackHeader = str(Header).replace("$", "")
                    print("Header : " + str(AttackHeader))
                    AttackCookie = str(Cookie).replace("$", "")
                    print("Cookie : " + AttackCookie)
                elif(Area == 'Body'):
                    print("Area is = " + Area)
                    AttackBody = Body.replace(key, str(Payload_RowContents.value))
                    print("Original BOdy ===============" + AttackBody)
                    print("for2", i+1)
                    AttackURL = URL
                    print("URL : " + str(AttackURL))
                    AttackBody = str(AttackBody).replace("$", "")
                    print("AttackBody : " + str(AttackBody))
                    AttackHeader = str(Header)
                    print("Header : " + str(AttackHeader))
                    AttackCookie = str(Cookie)
                    print("Cookie : " +  AttackCookie)
                elif(Area == 'Header'):
                    print("Area is = " + Area)
                    AttackHeader = Header.replace(key, str(Payload_RowContents.value))
                    AttackURL = AttackURL.replace("$", "")
                    print(AttackURL)
                    AttackBody = str(Body).replace("$", "")
                    print(AttackBody)
                    AttackHeader = str(AttackHeader).replace("$", "")
                    print(AttackHeader)
                    AttackCookie = str(Cookie).replace("$", "")
                    print(AttackCookie)
                elif(Area == 'Cookie'):
                    print("Area is = " + Area)
                    AttackCookie = Cookie.replace(key, str(Payload_RowContents.value))
                    AttackURL = AttackURL.replace("$", "")
                    print(AttackURL)
                    AttackBody = str(Body).replace("$", "")
                    print(AttackBody)
                    AttackHeader = str(Header).replace("$", "")
                    print(AttackHeader)
                    AttackCookie = str(AttackCookie).replace("$", "")
                    print(AttackCookie)                
                try:
                    if (METhod == 'GET'):
                        print("Method found in attack = " + METhod)
                        response = requests.get(AttackURL, data=AttackBody, headers=AttackHeader)
                    elif(METhod == 'POST'):
                        print("Method found in attack = " + METhod)
                        response = requests.post(AttackURL, data=AttackBody, headers=AttackHeader)
                        print("Got ============ response")
                    elif(METhod == 'PUT'):
                        response = requests.put(AttackURL, data=AttackBody, headers=AttackHeader)
                    elif(METhod == 'DELETE'):
                        response = requests.delete(AttackURL, data=AttackBody, headers=AttackHeader)
                    StatusCode = str(response.status_code)
                    Response_Body = str(response.text)
                    print("Response Status Code : " + str(StatusCode) + "\n")
                    print("Response Body : " + str(Response_Body) + "\n")
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
    return result
                   

#========================== MAIN FUNCTION WHICH IS CALLED BY API.ROBOT ======================================

def CORS(Excel_Location, Excel_Sheet_Name, Module_Name):
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
        Origin = {'Origin':'www.geeksforgeeks.org'}
        print(Origin)

        if(Method == 'GET'):
            GET = requests.get(URL, data=Body, headers=Origin)
            result['GET StatusCode'] = str(GET.status_code)

        elif(Method == 'POST'):
            POST = requests.post(URL, data=Body, headers=Origin)
            result['GET StatusCode'] = str(POST.status_code)

        elif (Method == 'PUT'):
            PUT = requests.put(URL, data=Body, headers=Origin)
            result['HOST StatusCode'] = str(PUT.status_code)

        elif (Method == 'DELETE'):
            DELETE = requests.delete(URL, data=Body, headers=Origin)
            result['GET StatusCode'] = str(DELETE.status_code)

    except Exception as error:
        print("Error in executing HOST Injection")
        traceback.print_stack()

    return result