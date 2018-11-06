Feature: Test Header

  Scenario: Observe header menu
    Given I am on the homepage
    Then I see all expected elements

  Scenario: Click the "WOT" logo
    Given I am on the homepage
    When I click on the "WOT" logo
    Then I am on the homepage


  Scenario: Click the "Activity" tab
    Given I am on the homepage
    When I click the "Activity" tab
    Then I am on the "Activity" page


  Scenario: Click the "Blog" tab
    Given I am on the homepage
    When I click the "Blog" tab
    Then I am on the "Blog" page


  Scenario: Click the "FAQ" tab
    Given I am on the homepage
    When I click the "Help" tab
    And I click the "FAQ" tab
    Then I am on the "FAQ" page


  Scenario: Click the "Forum" tab
    Given I am on the homepage
    When I click the "Help" tab
    And I click the "Forum" tab
    Then I am on the "Forum" page


  Scenario: Click the "Guidelines" tab
    Given I am on the homepage
    When I click the "Help" tab
    And I click the "Guidelines" tab
    Then I am on the "Guidelines" page


  Scenario: Click the "Contact" tab
    Given I am on the homepage
    When I click the "Help" tab
    And I click the "Contact" tab
    Then I am on the "Contact" page


  Scenario: Click the "Sign Up" button
    Given I am on the homepage
    When I click the "Sign Up" button
    Then Sign up popup appears

  Scenario: Close the "Sign Up" form by clicking outside
    Given I am on the homepage
    When I click the "Sign Up" button
    And I click outside the "Sign Up" form
    Then I am on the homepage


  Scenario: Click the "Log in" button
    Given I am on the homepage
    When I click the "Log in" button
    Then Log in popup appears


  Scenario: Close the "Log in" form by clicking outside
    Given I am on the homepage
    When I click the "Log in" button
    And I click outside the "Log in" form
    Then I am on the homepage