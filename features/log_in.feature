Feature: Test Sign Up

  Scenario: Observe Log in form
    Given Log in form opened
    Then I see expected elements


  Scenario: Log in as a valid user (using email in the log in field)
    Given Log in form opened
    When I enter valid email in the "Email or Username" field
    And I enter valid password in the "Password" field
    And I press the submit button
    Given I wait for the "My Profile" to load
    Then "My Profile" menu appears


  Scenario: Log in as a valid user (using username in the log in field)
    Given Log in form opened
    When I enter valid username in the "Email or Username" field
    And I enter valid password in the "Password" field
    And I press the submit button
    Given I wait for the "My Profile" to load
    Then "My Profile" menu appears


  Scenario: Log out
    Given Log in form opened
    When I enter valid email in the "Email or Username" field
    And I enter valid password in the "Password" field
    And I press the submit button
    Given I wait for the "My Profile" to load
    When I click "Log out" button
    Then "My Profile" menu disappears


  Scenario: Log in with blank username and password
    Given Log in form opened
    Then Log in button is disabled


  Scenario: Log in without username
    Given Log in form opened
    When I enter valid password in the "Password" field
    Then Log in button is disabled


  Scenario: Log in with invalid username and invalid password
    Given Log in form opened
    When I enter invalid username in the "Email or Username" field
    And I enter invalid password in the "Password" field
    And I press the submit button
    Then Wrong notification appears

  Scenario: Log in without password
    Given Log in form opened
    When I enter valid email in the "Email or Username" field
    And I press the submit button
    Then Log in button is disabled


  Scenario: Log in with valid username and invalid password
    Given Log in form opened
    When I enter valid email in the "Email or Username" field
    And I enter invalid password in the "Password" field
    And I press the submit button
    Then Wrong notification appears

  Scenario: Log in with valid username and password, which is 8 symbols long
    Given Log in form opened
    When I enter valid username
    And I enter valid password, which is 8 symbols long
    And I press the submit button
    Given I wait for the "My Profile" to load
    Then "My Profile" menu appears


  Scenario: Log in with invalid username and valid password
    Given Log in form opened
    When I enter invalid username in the "Email or Username" field
    And I enter valid password in the "Password" field
    And I press the submit button
    Then Wrong notification appears


  Scenario: Log in with valid password in the log in field, and valid login in the password field
    Given Log in form opened
    When I enter valid email in the "Password" field
    And I enter valid password in the "Email or Username" field
    And I press the submit button
    Then Wrong notification appears


  Scenario: Log in with script in the log in field and valid password
    Given Log in form opened
    When I enter script in the "Email or Username" field
    And I enter valid password in the "Password" field
    And I press the submit button
    Then Wrong notification appears

  Scenario: Log in with SQL query in the log in field and valid password
    Given Log in form opened
    When I enter SQL query in the "Email or Username" field
    And I enter valid password in the "Password" field
    And I press the submit button
    Then Wrong notification appears