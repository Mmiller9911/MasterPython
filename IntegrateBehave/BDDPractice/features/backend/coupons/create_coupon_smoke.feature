
Feature: Create Coupon Smoke

  @TCID-36
  Scenario Outline: Create coupon with minimum parameters should create a coupon
    Given I create a "<discount_type>" coupon
    Then the coupon should exist in the database

    Examples:
        | discount_type |
        | None          |
        | percent       |
        | fixed_cart    |
        | fixed_product |