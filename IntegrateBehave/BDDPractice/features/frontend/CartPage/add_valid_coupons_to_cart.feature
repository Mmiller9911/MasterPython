
@cart @coupon @coupon_feature @fe
Feature: Add valid coupons to cart

  @TCID-44
  Scenario: Adding 50% off coupon should discount the whole cart by 50%
    Given I go to the "home" page
    And I add 3 random item to cart from the homepage
    And I click on cart in the top nav bar and verify cart page opens
    And I select 'Free Shipping' option
    And I get the total dollar amount of the cart
    And I get a valid 50% off coupon
    And I apply coupon to the cart
    Then the total should be reduced by 50%