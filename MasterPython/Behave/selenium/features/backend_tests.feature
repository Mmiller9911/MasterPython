@regression @backend
Feature: Backend tests for the woocommerce API


    @TCID-10
    Scenario: Verify correct number of products is returned from GET products
      Given I get the number of Available products from the database
      When I get the number of Available products from the API
      Then the number of products should match

    @TCID-11
    Scenario: Verify correct number of products is returned from GET products with ONE step
      Given I get the number of Available products from the API and the DATABASE
      Then the number of products should match

    @TCID-12
    Scenario: Passing data from the command line
      Given I create a new user

    @TCID-13
    Scenario: Passing string from the step
      Given I access string in a step
      """
      This is a string of text to pass to the step. More stringy goodness
      """

    @TCID-14
  Scenario: Passing string from the step in JSON
    Given I add string of a different type
    """
    {"first_name": "Admas", "last_name": "Kinfu", "phone": "4895735934"}
    """

  @TCID-18
  Scenario: Verify 'POST/customers' create user
    Given I generate random email and password
    When I call 'create customer' API
    Then customer should be created

  @TCID-19 @after_scenario
  Scenario: Generate new test data set and use it to register x number of users and check they can log in to the system
    Given I create "5" new users using a test data creator
    And I go to the "my account" page
    When I register the users on mystore
    Then the users can log in to mystore

  @TCID-20 @after_scenario
  Scenario: Generate new test data set and use export it into a CSV file
    Given I create "5" new users using a test data creator
    When I output the data into a CSV file
    Then all the data is output correctly

    #      @TCID-15 @after_scenario
#    Scenario: Give me a failure
#      Given I have a failing test

#    @TCID-25 @after_scenario
#    Scenario: Verify correct product id is returned for a product
#      Given I get 1 random product from the database
#      Then I verify the product API returns the correct product by id