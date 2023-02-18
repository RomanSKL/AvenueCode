Feature: Sign In


  Scenario: User is able to log in with valid credentials
    Given Open Sign in page
    When Enter Email
    When Enter Password
    Then Sign In
