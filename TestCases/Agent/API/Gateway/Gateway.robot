*** Settings ***
Library  SeleniumLibrary
Resource  ../../../Resources/API.robot

*** Variables ***
${Excel_Location}  D:/Programming/Application Security/coe-application-security/DataFiles/API.xlsx
${Payload_Excel_Location}  D:/Programming/Application Security/coe-application-security/DataFiles/Payloads.xlsx


*** Test Cases ***
TC_001 HTTP Strict Transport Security Check on GATEWAY GET API
    log to console  "HTTP Strict Transport Security Check on GATEWAY GET API"
    HTTP Strict Transport Security  ${Excel_Location}  Agent  TEST

TC_002 Verb Parameter Tampering on GATEWAY GET API
    log to console  "Performing Verb Tampering attack on GATEWAY GET API"
    Dangerous Method  ${Excel_Location}  Agent  TEST


TC_003 SQL Injection Attack on GATEWAY GET API
    log to console  "Performing SQL Injection Attack on GATEWAY GET API"
    input_validation  ${Excel_Location}  Agent  TEST  ${Payload_Excel_Location}  TEST

*** Keywords ***