*** Settings ***
Library  SeleniumLibrary
Resource  ../Resources/API.robot


*** Variables ***
${Excel_Location}  D:/Programming/Application Security/coe-application-security/DataFiles/API.xlsx

*** Test Cases ***
TC_001 
    log to console  "Verifying Batch Profile API is functionally working"
    Execute API  ${Excel_Location}  Agent  ACMS_Batch_Profiles_API