*** Settings ***
Library  SeleniumLibrary
Resource  ../../../../Resources/API.robot
Resource  ../../../../Resources/DatabaseConnect.robot

*** Variables ***
${Excel_Location}  D:/Programming/Application Security/coe-application-security/DataFiles/API.xlsx
${Payload_Excel_Location}  D:/Programming/Application Security/coe-application-security/DataFiles/Payloads.xlsx

*** Test Cases ***
TC_001 
    log to console  "Verifying Batch Profile API is functionally working"
    Execute API  ${Excel_Location}  Agent  ACMS_Batch_Profiles_API
