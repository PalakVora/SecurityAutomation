*** Settings ***
Library  SeleniumLibrary
Resource  ../../../Resources/API.robot

*** Variables ***
${Excel_Location}  D:/Programming/Application Security/coe-application-security/DataFiles/API.xlsx
${Payload_Excel_Location}  D:/Programming/Application Security/coe-application-security/DataFiles/Payloads.xlsx


*** Test Cases ***
TC_001 Arbitary HTTP Methods, XST Potentials and HEAD Access Control Bypass.
    log to console  "Executing Test Case 001"
    Dangerous Method  ${Excel_Location}  IAM  PUT

TC_002 Input Based Attack
    log to console  "Executing Test Case 002"
    input_validation  ${Excel_Location}  IAM  PUT  ${Payload_Excel_Location}  TEST

*** Keywords ***