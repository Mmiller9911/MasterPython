Feature:
  Order Placement

  @TCID-33
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
