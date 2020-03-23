*** Settings ***
Library  SeleniumLibrary
Library  RequestsLibrary
Library  Collections
Library  JSONLibrary
Library  requests
Library  ../MethodFiles/PayloadAttack.py


*** Variables ***


*** Keywords ***
Execute GET Method API
    [Arguments]  ${API_Excel_Location}  ${API_Excel_Sheet_Name}  ${API_Module_Name}  ${Payload_Excel_Location}  ${Payload_Sheet_Name}  ${Expected_Status_Code}
    log to console  "Executing GET Method API"
    ${result}=  perform_get_payload_attack  ${API_Excel_Location}  ${API_Excel_Sheet_Name}  ${API_Module_Name}  ${Payload_Excel_Location}  ${Payload_Sheet_Name}
    log to console  "Executed Sucessfully"
    log to console  ${Expected_Status_Code}
    [return]  ${result}
    log to console  ${result}
    LIST SHOULD NOT CONTAIN VALUE  ${result}  ${Expected_Status_Code}  Vulnerability Observed


Execute POST Method API
    [Arguments]  ${API_Excel_Location}  ${API_Excel_Sheet_Name}  ${API_Module_Name}  ${Payload_Excel_Location}  ${Payload_Sheet_Name}  ${Expected_Status_Code}
    log to console  "Executing POST Method API"
    ${result}=  perform_post_payload_attack  ${API_Excel_Location}  ${API_Excel_Sheet_Name}  ${API_Module_Name}  ${Payload_Excel_Location}  ${Payload_Sheet_Name}
    log to console  "Executed Sucessfully"
    log to console  ${Expected_Status_Code}
    [return]  ${result}
    log to console  ${result}
    LIST SHOULD NOT CONTAIN VALUE  ${result}  ${Expected_Status_Code}  Vulnerability Observed

Execute PUT Method API
    [Arguments]  ${API_Excel_Location}  ${API_Excel_Sheet_Name}  ${API_Module_Name}  ${Payload_Excel_Location}  ${Payload_Sheet_Name}  ${Expected_Status_Code}
    log to console  "Executing PUT Method API"
    ${result}=  perform_put_payload_attack  ${API_Excel_Location}  ${API_Excel_Sheet_Name}  ${API_Module_Name}  ${Payload_Excel_Location}  ${Payload_Sheet_Name}
    log to console  "Executed Sucessfully"
    log to console  ${Expected_Status_Code}
    [return]  ${result}
    log to console  ${result}
    LIST SHOULD NOT CONTAIN VALUE  ${result}  ${Expected_Status_Code}  Vulnerability Observed

Execute ALL Method API
    [Arguments]  ${API_Excel_Location}  ${API_Excel_Sheet_Name}  ${API_Module_Name}  ${Payload_Excel_Location}  ${Payload_Sheet_Name}  ${Expected_Status_Code}
    log to console  "Executing ALL Method API"
    ${result}=  perform_allmethod_payload_attack  ${API_Excel_Location}  ${API_Excel_Sheet_Name}  ${API_Module_Name}  ${Payload_Excel_Location}  ${Payload_Sheet_Name}
    log to console  "Executed Sucessfully"
    log to console  ${Expected_Status_Code}
    [return]  ${result}
    log to console  ${result}
    LIST SHOULD NOT CONTAIN VALUE  ${result}  ${Expected_Status_Code}  Vulnerability Observed