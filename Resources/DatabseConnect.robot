Execute Query
    [Arguments]    ${queryString}
    log    ${queryString}
    Comment    ${status}    ${result}    Run Keyword And Ignore Error    Execute Sql String    ${queryString}
    ${status}    @{queryResults}    Run Keyword And Ignore Error    Query    ${queryString}
    ${query}    Set Variable    ${queryResults[0][0]}
    Comment     Remove extra characters
    ${query}    Convert To String    ${query}
    ${query}    Replace String    ${query}    ('    ${EMPTY}
    ${result}    Replace String    ${query}    ',)    ${EMPTY}
    [Return]    ${result}