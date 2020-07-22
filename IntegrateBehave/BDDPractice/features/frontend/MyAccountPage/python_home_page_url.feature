@regression
Feature: Verifying the home page url goes to the right place

    @TCID-3
    Scenario: The Python home page should have correct title
        Given I go to the page "https://www.python.org/"
        Then the page title should be "Welcome to Python.org"

     @TCID-4
    Scenario: The Python home page should have correct url
        Given I go to the page "https://www.python.org/"
        Then current url should be "www.python.org"