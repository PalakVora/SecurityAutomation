*** Settings ***
Library  SeleniumLibrary
Resource  ../../../../Resources/API.robot

*** Variables ***
${Excel_Location}  D:/Programming/Application Security/coe-application-security/DataFiles/API.xlsx
${Payload_Excel_Location}  D:/Programming/Application Security/coe-application-security/DataFiles/Payloads.xlsx

*** Test Cases ***
TC_001 Verify Configuration Profile API is functionally working
    log to console  "Verifying Configuration Profile API is functionally working"
    Execute API  ${Excel_Location}  Agent  ACMS_AGENT-Configuration_Profiles

TC_002 HTTP Strict Transport Security Check on Configuration Profile API
    log to console  "Performing HTTP Strict Transport Security Check on Configuration Profile API"
    HTTP Strict Transport Security  ${Excel_Location}  Agent  ACMS_AGENT-Configuration_Profiles

TC_003 SQL Injection on Configuration Profile API
    log to console  "Performing SQL Injection Attack on Configuration Profile API"
    Injection Attack  ${Excel_Location}  Agent  ACMS_AGENT-Configuration_Profiles  ${Payload_Excel_Location}  SQL

TC_004 Cross Site Scripting on Configuration Profile API
    log to console  "Performing Cross Site Scripting Attack on Configuration Profile API"
    Injection Attack  ${Excel_Location}  Agent  ACMS_AGENT-Configuration_Profiles  ${Payload_Excel_Location}  XSS

TC_005 Local File Inclusion Attack on Configuration Profile API
    log to console  "Performing Local File Inclusion Attack on Configuration Profile API"
    Injection Attack  ${Excel_Location}  Agent  ACMS_AGENT-Configuration_Profiles  ${Payload_Excel_Location}  LFI

TC_006 Lightweight Directory Access Protocol Attack on Configuration Profile API
    log to console  "Performing Lightweight Directory Access Protocol Attack on Configuration Profile API"
    Injection Attack  ${Excel_Location}  Agent  ACMS_AGENT-Configuration_Profiles  ${Payload_Excel_Location}  LDAP

TC_007 Server Side Injection Attack on Configuration Profile API
    log to console  "Performing Server Side Injection Attack on Configuration Profile API"
    Injection Attack  ${Excel_Location}  Agent  ACMS_AGENT-Configuration_Profiles  ${Payload_Excel_Location}  SSI

TC_008 XPath Injection on Configuration Profile API
    log to console  "Performing XPath Injection Attack on Configuration Profile API"
    Injection Attack  ${Excel_Location}  Agent  ACMS_AGENT-Configuration_Profiles  ${Payload_Excel_Location}  XPATH

TC_009 Basic Bash Command Injection on Configuration Profile API
    log to console  "Performing Basic Bash Command Injection Attack on Configuration Profile API"
    Injection Attack  ${Excel_Location}  Agent  ACMS_AGENT-Configuration_Profiles  ${Payload_Excel_Location}  BASH

TC_010 Verb Parameter Tampering on Configuration Profile API
    log to console  "Performing Verb Tampering attack on Configuration Profile API"
    Dangerous Method  ${Excel_Location}  Agent  ACMS_AGENT-Configuration_Profiles

TC_011 Host Header Injection Attack on Configuration Profile API
    log to console  "Performing Host Header Injection Attack on Configuration Profile API"
    Host Header Injection Attack  ${Excel_Location}  Agent  ACMS_AGENT-Configuration_Profiles

TC_012 Cross Origin Resource Sharing on Configuration Profile API
    log to console  "Performing Cross Origin Resource Sharing on Configuration Profile API"
    Cross Origin Resource Sharing  ${Excel_Location}  Agent  ACMS_AGENT-Configuration_Profiles

