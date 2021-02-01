import openpyxl,traceback
def readexcel(Excel_Location, Excel_Sheet_Name, Module_Name):
    data = {}
    print("Opening Excel")
    try:
        Excel_WorkBook = openpyxl.load_workbook(Excel_Location)
        print("Opened Excel")
    except Exception as error:
        print("Error in opening API Excel File")
        traceback.print_stack()
    return Excel_WorkBook

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