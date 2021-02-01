*** Settings ***
Library  SeleniumLibrary
Resource  ../Resources/API.robot

*** Variables ***
${Excel_Location}  D:/Programming/Application Security/coe-application-security/DataFiles/API.xlsx
${Payload_Excel_Location}  D:/Programming/Application Security/coe-application-security/DataFiles/Payloads.xlsx

*** Test Cases ***
TC_001 
    log to console  "Performing SQL Injection Attack on Batch Profile API"
    Injection Attack  ${Excel_Location}  ${team}  ${aPI}  ${Payload_Excel_Location}  SQL

TC_002 Cross Site Scripting on Batch Profile API
    log to console  "Performing Cross Site Scripting Attack on Batch Profile API"
    Injection Attack  ${Excel_Location}  Agent  ACMS_Batch_Profiles_API  ${Payload_Excel_Location}  XSS

TC_003 Local File Inclusion Attack on Batch Profile API
    log to console  "Performing Local File Inclusion Attack on Batch Profile API"
    Injection Attack  ${Excel_Location}  Agent  ACMS_Batch_Profiles_API  ${Payload_Excel_Location}  LFI

TC_004 Lightweight Directory Access Protocol Attack on Batch Profile API
    log to console  "Performing Lightweight Directory Access Protocol Attack on Batch Profile API"
    Injection Attack  ${Excel_Location}  Agent  ACMS_Batch_Profiles_API  ${Payload_Excel_Location}  LDAP

TC_005 Server Side Injection Attack on Batch Profile API
    log to console  "Performing Server Side Injection Attack on Batch Profile API"
    Injection Attack  ${Excel_Location}  Agent  ACMS_Batch_Profiles_API  ${Payload_Excel_Location}  SSI

TC_006 XPath Injection on Batch Profile API
    log to console  "Performing XPath Injection Attack on Batch Profile API"
    Injection Attack  ${Excel_Location}  Agent  ACMS_Batch_Profiles_API  ${Payload_Excel_Location}  XPATH

TC_007 Basic Bash Command Injection on Batch Profile API
    log to console  "Performing Basic Bash Command Injection Attack on Batch Profile API"
    Injection Attack  ${Excel_Location}  Agent  ACMS_Batch_Profiles_API  ${Payload_Excel_Location}  BASH
