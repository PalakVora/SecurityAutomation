import PythonFiles.Utilities.Get_API as Getting_API
import PythonFiles.Utilities.Read_Excel as Getting_Sheet
import json
from py._error import Error

def find_api(excel_location, excel_sheet_name, module_name):
    try:
        data = {}
        excel_workbook=Getting_Sheet.readexcel(excel_location, excel_sheet_name, module_name)
        print("Outside read excel")
        sheetname=Getting_Sheet.find_sheet_name(excel_sheet_name,module_name,excel_workbook)
        print("Out of sheet name" + sheetname.title)
        rowcontents=Getting_API.find_module_name(sheetname,module_name)
        print("Outside row")
        if(Getting_API.read_method(sheetname,rowcontents,excel_workbook)):
            method_name=Getting_API.read_method(sheetname,rowcontents,excel_workbook)
            data['HTTPMethod'] = method_name
            print(data['HTTPMethod'])
        else:
             raise Error("HTTP Method not recognised")
        protocol_name=Getting_API.read_protocol(sheetname,rowcontents,excel_workbook)
        data['Protocol'] = protocol_name
        print(data['Protocol'] + "\n")
        base_url=Getting_API.read_base_url(sheetname,rowcontents,excel_workbook)
        relative_url=Getting_API.read_relative_url(sheetname,rowcontents,excel_workbook)
        try:
            data['URL'] = str(data['Protocol']) + "://" + base_url + relative_url
            print(data['URL'])
        except:
            print("Error in concatenating URL")
            #Excel_WorkBook.close()
        body=Getting_API.read_body(sheetname,rowcontents,excel_workbook)
        print("Body = " + body + "\n")
        data['Body'] = body
        print("Fdata Body")
        print(data['Body'])
        header=Getting_API.read_header(sheetname,rowcontents,excel_workbook)
        print("Header = " + header + "\n")
        data['Header'] = json.loads(header)
        print(data['Header'])
        get_cookie=Getting_API.read_cookie(sheetname,rowcontents,excel_workbook) 
        print("Cookie = " + get_cookie + "\n")
        data['Cookie'] = json.loads(get_cookie)
        print(data['Cookie'])
        print(data)
    except:
        print("Error in reading contents")

    return data
