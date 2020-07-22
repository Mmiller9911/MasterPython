@regression @frontend
Feature: Frontend tests for mystore


  @TCID-1
  Scenario: Adding 50% off coupon should discount the whole cart by 50%
    Given I go to the "home" page
    And I add 3 random item to cart from the homepage
    And I click on cart in the top nav bar and verify cart page opens
    And I select 'Free Shipping' option
    And I get the total dollar amount of the cart
    And I get a valid 50% off coupon
    And I apply coupon to the cart
    Then the total should be reduced by 50%


   @TCID-2
  Scenario Outline: Create coupon with minimum parameters should create a coupon
    Given I create a "<discount_type>" coupon
    Then the coupon should exist in the database

    Examples:
        | discount_type |
        | None          |
        | percent       |
        | fixed_cart    |
        | fixed_product |

  @TCID-3
  Scenario: Verify the given coupon metadata is recorded correctly
    Given I create a coupon with given parameters
     """
     {
     "discount_type": "fixed_cart",
     "amount": "50",
     "individual_use": "false",
     "usage_count": 10,
     "usage_limit": 5,
     "exclude_sale_items": "True"
     }
     """

    Then I verify the given data in the database
     """
     {
     "discount_type": "fixed_cart",
     "coupon_amount": "50",
     "individual_use": "no",
     "usage_limit": "5",
     "usage_count": "0",
     "usage_limit_per_user": "0",
     "date_expires": "None",
     "exclude_sale_items": "yes"
     }
     """

#    @before_scenario @after_scenario @smoke @TCID-4
#    Scenario: Verify the navigation bars on home page are visible with smoke
#      Given I go to the page "https://www.python.org/"
#      Then the "main navigation" bar should be visible
#      And the "top navigation" bar should be visible
#      And the "options" bar should be visible
#
#  @before_scenario @after_scenario @TCID-5
#    Scenario: Verify the navigation bars on home page are visible without smoke
#      Given I go to the page "https://www.python.org/"
#      Then the "main navigation" bar should be visible
#      And the "top navigation" bar should be visible
#      And the "options" bar should be visible

  @TCID-6
  Scenario: Valid user should be able to login with valid details
    Given I go to the "my account" page
    And I type 'matt.miller@mqmsolutions.com' into the username field of login form
    And I type 'hunky123!' into the password field of login form
    When I click on the 'login' button
    Then the user should be logged in


  @TCID-7
  Scenario: Valid user should not be able to login with invalid details
    Given I go to the "my account" page
    And I type 'matt.miller@mqmsolutions.com' into the username field of login form
    And I type '123456' into the password field of login form
    When I click on the 'login' button
    Then error message with email 'matt.miller@mqmsolutions.com' should be displayed


  @TCID-8
  Scenario: Unknown user gets correct error displayed
    Given I go to the "my account" page
    And I type 'unknown@mqmsolutions.com' into the username field of login form
    And I type '123456' into the password field of login form
    When I click on the 'login' button
    Then error message with 'Unknown email' should be displayed

  @TCID-9
  Scenario: New user places an order for 1 item without creating an account
    Given I go to the "home" page
    And I add 4 random item to cart from the homepage
    And I click on cart in the top nav bar and verify cart page opens
    And I select 'Free Shipping' option
    And I click on 'Proceed to checkout' button on the cart page
    And I verify 'Checkout' page is loaded
    And I fill in the billing details form
    When I click on 'Place Order' button in the checkout page
    Then the 'order received page' should load with correct data
    And I verify order is created in the database


