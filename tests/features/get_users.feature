Feature: Get Users API

@regression
Scenario: Get list of users
  Given the API client is available
  When I send GET request to "/users?page=2"
  Then the response status should be 200
  And the response should match test data "users_list"

@smoke
Scenario: Get single user
  Given the API client is available
  When I send GET request to "/users/{valid_id}"
  Then the response status should be 200
  And the response should match test data "single_user"

@regression
Scenario: Get delayed response
  Given the API client is available
  When I send GET request to "/users?delay=3"
  Then the response status should be 200
  And the response should match test data "users_list"
  And the response time should match test data "delay"

@regression
Scenario: Get invalid user
  Given the API client is available
  When I send GET request to "/users/{invalid_id}"
  Then the response status should be 404