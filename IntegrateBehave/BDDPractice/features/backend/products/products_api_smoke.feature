@my_products_smoke @after_all
  Feature: Products API smoke

    @TCID-24 @after_scenario
    Scenario: Verify correct number of products is returned from GET products
      Given I get the number of Available products from the database
      When I get the number of Available products from the API
      Then the number of products should match

    @TCID-7 @after_scenario
    Scenario: Verify correct number of products is returned from GET products with ONE step
      Given I get the number of Available products from the API and the DATABASE
      Then the number of products should match

    @TCID-8 @after_scenario
    Scenario: Passing data from the command line
      Given I create a new user

    @TCID-9 @after_scenario
    Scenario: Passing string from the step
      Given I access string in a step
      """
      This is a string of text to pass to the step. More stringy goodness
      """

      @TCID-30 @after_scenario
    Scenario: Passing string from the step in JSON
      Given I add string of a different type
      """
      {"first_name": "Admas", "last_name": "Kinfu", "phone": "4895735934"}
      """

      @TCID-31 @after_scenario
    Scenario: Give me a failure
      Given I have a failing test

#    @TCID-25 @after_scenario
#    Scenario: Verify correct product id is returned for a product
#      Given I get 1 random product from the database
#      Then I verify the product API returns the correct product by id

