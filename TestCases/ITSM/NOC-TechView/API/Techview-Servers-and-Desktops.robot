*** Settings ***
Library  SeleniumLibrary
Resource  ../../../../Resources/API.robot

*** Variables ***
${Excel_Location}  D:/Programming/Application Security/coe-application-security/DataFiles/API.xlsx
${Payload_Excel_Location}  D:/Programming/Application Security/coe-application-security/DataFiles/Payloads.xlsx

*** Test Cases ***
TC_001 HTTP Strict Transport Security Check on ITS-ITGue
    log to console  "Performing HTTP Strict Transport Security Check on ITS-ITGue"
    HTTP Strict Transport Security  ${Excel_Location}  ITSM  ITS-ITGue

TC_002 SQL Injection on ITS-ITGue
    log to console  "Performing SQL Injection Attack on ITS-ITGue"
    Injection Attack  ${Excel_Location}  ITSM  ITS-ITGue  ${Payload_Excel_Location}  SQL

TC_003 Cross Site Scripting on ITS-ITGue
    log to console  "Performing Cross Site Scripting Attack on ITS-ITGue"
    Injection Attack  ${Excel_Location}  ITSM  ITS-ITGue  ${Payload_Excel_Location}  XSS

TC_005 Local File Inclusion Attack on ITS-ITGue
    log to console  "Performing Local File Inclusion Attack on ITS-ITGue"
    Injection Attack  ${Excel_Location}  ITSM  ITS-ITGue  ${Payload_Excel_Location}  LFI

TC_006 Lightweight Directory Access Protocol Attack on ITS-ITGue
    log to console  "Performing Lightweight Directory Access Protocol Attack on ITS-ITGue"
    Injection Attack  ${Excel_Location}  ITSM  ITS-ITGue ${Payload_Excel_Location}  LDAP

TC_007 Server Side Injection Attack on ITS-ITGue
    log to console  "Performing Server Side Injection Attack on ITS-ITGue"
    Injection Attack  ${Excel_Location}  ITSM  ITS-ITGue  ${Payload_Excel_Location}  SSI

TC_008 XPath Injection on ITS-ITGue
    log to console  "Performing XPath Injection Attack on ITS-ITGue"
    Injection Attack  ${Excel_Location}  ITSM  ITS-ITGue  ${Payload_Excel_Location}  XPATH

TC_009 Basic Bash Command Injection on ITS-ITGue
    log to console  "Performing Basic Bash Command Injection Attack on ITS-ITGue"
    Injection Attack  ${Excel_Location}  ITSM  ITS-ITGue  ${Payload_Excel_Location}  BASH

TC_010 Verb Parameter Tampering on ITS-ITGue
    log to console  "Performing Verb Tampering attack on ITS-ITGue"
    Dangerous Method  ${Excel_Location}  ITSM  ITS-ITGue

