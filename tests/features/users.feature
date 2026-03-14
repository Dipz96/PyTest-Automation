Feature: Users API

  Scenario: Get list of users
    Given the API client is available
    When I request the list of users on page 2
    Then the response status should be 200
    And the response should contain user data