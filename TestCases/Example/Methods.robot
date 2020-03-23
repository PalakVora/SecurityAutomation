*** Settings ***
Library  SeleniumLibrary
Library  RequestsLibrary
Library  Collections
Library  requests
Library  MethodFiles/Mathematics.py
Library  MethodFiles/OS.py

*** Variables ***
${Browser}  Firefox
${URL}  http://thetestingworld.com/testings
${URL1}  http://robotframework.org/

*** Keywords ***
Start Browser and Maximize
    Open Browser  ${URL}  ${Browser}
    Maximize Browser Window
    ${Title}=  Get Title
    Log  ${Title}
    [Return]  ${Title}

Close Browser Window
    ${ClosingWindowTitle}=  Get Title
    Log  ${ClosingWindowTitle}
    Close Browser

Enter Username Password Email
    [arguments]  ${username}  ${email}  ${password}
    Input Text  name:fld_username  ${username}
    Input Text  xpath://input[@name='fld_email']  ${email}
    Input Text  name:fld_password  ${password}

Create folder at Runtime
    [arguments]  ${foldername}  ${subfoldername}
    create_folder  ${foldername}
    create_sub_folder  ${subfoldername}
    Log  "Task Done Successfully"

Concatenation of two values
    [arguments]  ${username}  ${password}
    log to console  "Executing Concatenation of two values"
    ${resultvalue}=  concatenate_two_values  ${username}  ${password}
    log  ${resultvalue}
    Should Be Equal  ${resultvalue}  Hello  Concatenated values are different






