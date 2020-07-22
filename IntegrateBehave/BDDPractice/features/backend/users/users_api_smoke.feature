@user_api_smoke @smoke
  Feature: User API smoke

    @TCID-29
    Scenario: Verify 'POST/customers' create user
      Given I generate random email and password
      When I call 'create customer' API
      Then customer should be created