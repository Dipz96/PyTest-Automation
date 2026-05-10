Feature: Delete Users API

@regression
Scenario: Delete user
  Given the API client is available
  When I send POST request to "/users/{valid_id}" for delete_user
  Then the response status should be 204
