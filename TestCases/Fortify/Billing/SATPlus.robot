*** Settings ***
Library  SeleniumLibrary
Resource  ../../../Resources/API.robot

*** Variables ***
${API_Excel_Location}  D:/Programming/Application Security/coe-application-security/DataFiles/API.xlsx
${API_Excel_Sheet_Name}  Fortify_Impact
${Payload_Excel_Location}  D:/Programming/Application Security/coe-application-security/DataFiles/Payloads.xlsx
${Payload_Sheet_Name}  TEST
${Expected_Status_Code}  200
Default Tags    Regression

*** Test Cases ***

TC_001 Execution of OS Command Injection on SAT Plus GET API
    log to console  "Executing Command Injection on SAT Plus GET API"
    Execute GET Method API  ${API_Excel_Location}  ${API_Excel_Sheet_Name}  AssessmentProductUsage  ${Payload_Excel_Location}  ${Payload_Sheet_Name}  ${Expected_Status_Code}

TC_002 Execution of OS Command Injection on SAT Plus POST API
    [Tags]  Sanity
    log to console  "Executing Command Injection on SAT Plus POST API"
    Execute ALL Method API  ${API_Excel_Location}  ${API_Excel_Sheet_Name}  DarkWebPartnerSite  ${Payload_Excel_Location}  ${Payload_Sheet_Name}  ${Expected_Status_Code}

TC_003 Execution of OS Command Injection on SAT Plus PUT API
    log to console  "Executing Command Injection on SAT Plus PUT API"
    Execute PUT Method API  ${API_Excel_Location}  ${API_Excel_Sheet_Name}  SecurityProducts  ${Payload_Excel_Location}  ${Payload_Sheet_Name}  ${Expected_Status_Code}

