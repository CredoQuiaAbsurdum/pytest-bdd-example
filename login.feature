@login
Feature: login
	Scenario: Successful login
		Given I am on the login screen
		When I provide a valid username 
		And I provide the corresponding password
		And I press Submit
		Then I am logged in


#form-control ng-pristine ng-valid ng-touched
