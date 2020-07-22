@regression
Feature: Navigation bars in the home page

@before_scenario @after_scenario @smoke @TCID-1
    Scenario: Verify the navigation bars on home page are visible with smoke
      Given I go to the page "https://www.python.org/"
      Then the "main navigation" bar should be visible
      And the "top navigation" bar should be visible
      And the "options" bar should be visible

  @before_scenario @after_scenario @TCID-2
    Scenario: Verify the navigation bars on home page are visible without smoke
      Given I go to the page "https://www.python.org/"
      Then the "main navigation" bar should be visible
      And the "top navigation" bar should be visible
      And the "options" bar should be visible