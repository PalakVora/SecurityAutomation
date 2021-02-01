*** Settings ***
Library  SeleniumLibrary
Resource  ../../../../Resources/API.robot
Resource  ../../../../Resources/DatabaseConnect.robot

*** Variables ***
${Excel_Location}  D:/Programming/Application Security/coe-application-security/DataFiles/API.xlsx
${Payload_Excel_Location}  D:/Programming/Application Security/coe-application-security/DataFiles/Payloads.xlsx

*** Test Cases ***

TC_002 HTTP Strict Transport Security Check on Batch Profile API
    log to console  "Performing HTTP Strict Transport Security Check on Batch Profile API"
    HTTP Strict Transport Security  ${Excel_Location}  Agent  ACMS_Batch_Profiles_API


TC_010 Verb Parameter Tampering on Batch Profile API
    log to console  "Performing Verb Tampering attack on Batch Profile API"
    Dangerous Method  ${Excel_Location}  Agent  ACMS_Batch_Profiles_API

TC_011 Host Header Injection Attack on Batch Profile
    log to console  "Performing Host Header Injection Attack on Batch Profile"
    Host Header Injection Attack  ${Excel_Location}  Agent  ACMS_Batch_Profiles_API

TC_012 Cross Origin Resource Sharing on Batch Profile
    log to console  "Performing Cross Origin Resource Sharing on Batch Profile"
    Cross Origin Resource Sharing  ${Excel_Location}  Agent  ACMS_Batch_Profiles_API
    

