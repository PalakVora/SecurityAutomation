*** Settings ***
Library  SeleniumLibrary
Library  OperatingSystem
Library  robot.api.logger
Resource  Methods.robot
Library  RequestsLibrary
Library  Collections
Library  JSONLibrary
Library  requests


#Test Setup  Start Browser and Maximize
#Test Teardown  Close Browser Window

*** Variables ***
${post_id}
${student_id_get}  27
${student_id_put}  1516
${base_url}  http://thetestingworldapi.com
${relative_url_get}  api/studentsDetails
${relative_url_get2}  api/studentsDetails/${post_id}
${relative_url_post}  api/studentsDetails
${relative_url_put}  api/studentsDetails/${post_id}
${relative_url_delete}  api/studentsDetails/${post_id}
${File_Path}  D:/Programming/Application Security/coe-application-security/Data Files/Data.xlsx

*** Test Cases ***

TC_001 Get Entire Student Details
    Create Session  Get_Session  ${base_url}
    ${response}=  Get Request  Get_Session  ${relative_url_get}
    should be equal as integers  200  ${response.status_code}  Concatenated values are different
    log to console  ${response.status_code}
    log to console  ${response.content}
    log to console  ${response.headers}

TC_002 Post Student Details
    Create Session  Post_Session  ${base_url}
    &{body}=  create dictionary  first_name=Testing  middle_name=A  last_name=World  date_of_birth=12/12/1990
    &{header}=  create dictionary  Content-Type=application/json
    ${response}=  post request  Post_Session  ${relative_url_post}  data=${body}  headers=${header}
    log to console  ${response.status_code}
    should be equal as integers  201  ${response.status_code}  Concatenated values are different
    log to console  ${response.headers}
    ${jsonresponse}=  to json  ${response.content}
    log to console  ${jsonresponse}
    @{json_response_list}=  get value from json  ${jsonresponse}  Testing
    log to console  @json_response_list
    #status is the key of the json response, we are looking for its key
    ${post_id}=  get from list  @{json_response_list}  0

    ${response_get}=  get request  Post_Session  ${relative_url_post}
    log to console  ${response_get}

TC_003 Get Any One Student Details
    Create Session  Get_Session  ${base_url}
    ${response}=  Get Request  Get_Session  ${relative_url_get2}
    #${actual_code}=  convert to string  ${response.status_code}      #Another way for comparison
    should be equal as integers  200  ${response.status_code}  Concatenated values are different
    log to console  ${response.status_code}
    log to console  ${response.content}
    log to console  ${response.headers}

TC_004 Put Student Details
    Create Session  Put_Session  ${base_url}
    &{body}=  create dictionary  id=${post_id}  first_name=Testing  middle_name=ABCDE  last_name=World  date_of_birth=12/12/1990
    &{header}=  create dictionary  Content-Type=application/json
    ${response}=  put request  Put_Session  ${relative_url_put}  data=${body}  headers=${header}
    log to console  ${response.status_code}
    should be equal as integers  201  ${response.status_code}  Concatenated values are different
    log to console  ${response.content}
    log to console  ${response.headers}

    ${response_get}=  get request  Put_Session  ${relative_url_put}
    log to console  ${response_get.content}

TC_005 Delete Student Details
    Create Session  Delete_Session  ${base_url}
    ${response}=  delete request  Delete_Session  ${relative_url_delete}
    log to console  ${response.status_code}
    should be equal as integers  200  ${response.status_code}  Concatenated values are different
    log to console  ${response.content}
    ${jsonresponse}=  to json  ${response.content}
    log to console  ${jsonresponse}
    @{json_response_list}=  get value from json  ${jsonresponse}  status
    #status is the key of the json response, we are looking for its key
    ${status}=  get from list  @{json_response_list}  0
    should be equal  ${status}  true


*** Keywords ***


