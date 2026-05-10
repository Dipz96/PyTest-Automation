Feature: Create User API

@regression
Scenario: Create user
  Given the API client is available
  And I have payload with name "morpheus" and job "leader"
  When I send POST request to "/users"
  Then the response status should be 201
  And the response should contain created user details