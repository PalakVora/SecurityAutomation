*** Settings ***
Library  MethodFiles/Mathematics.py
Library  MethodFiles/OS.py
Library  SeleniumLibrary
Library  OperatingSystem
Library  robot.api.logger
Resource  Methods.robot
Library  RequestsLibrary
Library  Collections

#Test Setup  Start Browser and Maximize
#Test Teardown  Close Browser Window

*** Variables ***
${student_id}  28
${base_url}  http://thetestingworldapi.com
${relative_url}  api/studentsDetails
${relative_url1}  api/studentsDetails/${student_id}



*** Test Cases ***
TC_001 Browser Start and Open URL
    Start Browser and Maximize
    #[Setup]  Start Browser and Maximize

TC_002 Insert Data In Text Feild
    Enter Username Password Email  Testing  testingworld@gmail.com  Abc@1234

TC_003 Clear Data From Text Feild
    Clear Element Text  name:fld_username

TC_004 Select Radio Button
    Select Radio Button  add_type  office  #Radio Button is located via Groupname and locator

TC_005 Select CheckBox
    Select Checkbox  name:terms

TC_006 Click On Button
    Click Button  xpath://input[@type='submit']

TC_007 Click On Link
    Click Link  xpath://a[text()='Read Detail']
    [Teardown]  Close Browser Window


TC_009 Create Folder
    Create folder at Runtime  Hacking  Subhacking

TC_010 Concatenation of Values
    Concatenation of two values  Testing  World

*** Keywords ***
