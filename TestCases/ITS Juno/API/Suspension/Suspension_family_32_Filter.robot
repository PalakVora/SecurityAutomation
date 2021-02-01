*** Settings ***
Library  SeleniumLibrary
Resource  ../../../../Resources/API.robot

*** Variables ***
${Excel_Location}  D:/Programming/Application Security/coe-application-security/DataFiles/API.xlsx
${Payload_Excel_Location}  D:/Programming/Application Security/coe-application-security/DataFiles/Payloads.xlsx

*** Test Cases ***
TC_001 Verify Suspension API Family 32 Filter is functionally working
    log to console  "Verifying Suspension API Family 32 Filter is functionally working"
    Execute API  ${Excel_Location}  ITS_Juno  Suspension_family_32_Filter

TC_002 HTTP Strict Transport Security Check on Suspension API Family 32 Filter
    log to console  "Performing HTTP Strict Transport Security Check on Suspension API Family 32 Filter"
    HTTP Strict Transport Security  ${Excel_Location}  ITS_Juno  Suspension_family_32_Filter

TC_003 SQL Injection on Suspension API Family 32 Filter
    log to console  "Performing SQL Injection Attack on Suspension API Family 32 Filter"
    Injection Attack  ${Excel_Location}  ITS_Juno  Suspension_family_32_Filter  ${Payload_Excel_Location}  SQL

TC_004 Cross Site Scripting on Suspension API Family 32 Filter
    log to console  "Performing Cross Site Scripting Attack on Suspension API Family 32 Filter"
    Injection Attack  ${Excel_Location}  ITS_Juno  Suspension_family_32_Filter  ${Payload_Excel_Location}  XSS

TC_005 Local File Inclusion Attack on Suspension API Family 32 Filter
    log to console  "Performing Local File Inclusion Attack on Suspension API Family 32 Filter"
    Injection Attack  ${Excel_Location}  ITS_Juno  Suspension_family_32_Filter  ${Payload_Excel_Location}  LFI

TC_006 Lightweight Directory Access Protocol Attack on Suspension API Family 32 Filter
    log to console  "Performing Lightweight Directory Access Protocol Attack on Suspension API Family 32 Filter"
    Injection Attack  ${Excel_Location}  ITS_Juno  Suspension_family_32_Filter  ${Payload_Excel_Location}  LDAP

TC_007 Server Side Injection Attack on Suspension API Family 32 Filter
    log to console  "Performing Server Side Injection Attack on Suspension API Family 32 Filter"
    Injection Attack  ${Excel_Location}  ITS_Juno  Suspension_family_32_Filter  ${Payload_Excel_Location}  SSI

TC_008 XPath Injection on Suspension API Family 32 Filter
    log to console  "Performing XPath Injection Attack on Suspension API on Suspension API Family 32 Filter"
    Injection Attack  ${Excel_Location}  ITS_Juno  Suspension_family_32_Filter  ${Payload_Excel_Location}  XPATH

TC_009 Basic Bash Command Injection on Suspension API Family 32 Filter
    log to console  "Performing Basic Bash Command Injection Attack on Suspension API Family 32 Filter"
    Injection Attack  ${Excel_Location}  ITS_Juno  Suspension_family_32_Filter  ${Payload_Excel_Location}  BASH

TC_010 Verb Parameter Tampering on Suspension API Family 32 Filter
    log to console  "Performing Verb Tampering attack on Suspension API Family 32 Filter"
    Dangerous Method  ${Excel_Location}  ITS_Juno  Suspension_family_32_Filter

TC_011 Host Header Injection Attack on Suspension API Family 32 Filter
    log to console  "Performing Host Header Injection Attack on Suspension API Family 32 Filter"
    Host Header Injection Attack  ${Excel_Location}  ITS_Juno  Suspension_family_32_Filter

TC_012 Cross Origin Resource Sharing on Suspension API Family 32 Filter
    log to console  "Performing Cross Origin Resource Sharing on Suspension API Family 32 Filter"
    Cross Origin Resource Sharing  ${Excel_Location}  ITS_Juno  Suspension_family_32_Filter
