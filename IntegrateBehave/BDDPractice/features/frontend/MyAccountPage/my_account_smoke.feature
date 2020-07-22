@my_account_smoke @after_all
Feature: My Account Smoke Tests

  @TCID-10 @after_scenario
  Scenario: Valid user should be able to login with valid details
    Given I go to the "my account" page
    And I type 'matt.miller@mqmsolutions.com' into the username field of login form
    And I type 'hunky123!' into the password field of login form
    When I click on the 'login' button
    Then the user should be logged in

  @TCID-11 @after_scenario
  Scenario: Valid user should not be able to login with invalid details
    Given I go to the "my account" page
    And I type 'matt.miller@mqmsolutions.com' into the username field of login form
    And I type '123456' into the password field of login form
    When I click on the 'login' button
    Then error message with email 'matt.miller@mqmsolutions.com' should be displayed

  @TCID-12 @after_scenario
  Scenario: Unknown user gets correct error displayed
    Given I go to the "my account" page
    And I type 'unknown@mqmsolutions.com' into the username field of login form
    And I type '123456' into the password field of login form
    When I click on the 'login' button
    Then error message with 'Unknown email' should be displayed