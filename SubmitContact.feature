@submit @contact
Feature: Submit a valid contact form

  Scenario: Submit form using valid data
  	Given I am on the zoo website
  	When I navigate to "contact_link"
  	And I submit the form with valid data
    Then I check that the form has been subimtted
    And I close the browser
