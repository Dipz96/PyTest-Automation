Feature: Create User API

@regression
Scenario: Get list of users
  Given the API client is available
  And I have the following request payload
      """
      {
        "name": "morpheus",
        "job": "leader"
      }
      """
  When I send POST request to "/users"
  Then the response status should be 200
  And the response should contain created user details