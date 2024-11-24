*** Settings ***
Library           RequestsLibrary
Suite Setup       Create Session    nasa    https://ssd-api.jpl.nasa.gov

*** Variables ***
${BASE_URL}       https://ssd-api.jpl.nasa.gov
${CAD_ENDPOINT}   /cad.api

*** Test Cases ***

Verify API Returns 200 Status Code
    [Documentation]    Validate the API returns a successful response.
    ${response}=    Get On Session    nasa    ${CAD_ENDPOINT}
    Should Be Equal As Integers    ${response.status_code}    200

Verify API Returns Non-Empty Data
    [Documentation]    Confirm that the API response contains data.
    ${response}=    Get On Session    nasa    ${CAD_ENDPOINT}    params=dist-max=0.05
    Should Not Be Empty    ${response.json()}

*** Keywords ***
Log API Response
    [Arguments]    ${response}
    Log To Console    Status Code: ${response.status_code}
    Log To Console    Response Body: ${response.text}
