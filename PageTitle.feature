#JUnit Cucumber Tutorial 04 - Parameter Handling

#Scenario: Check page title for Adoption page
  #	Given I am on the zoo website
  # When I navigate to "adoption_link"
  #	Then I check page title is "Adoption"
  #	And I close the browser

  #Scenario: Check page title for About page
  #	Given I am on the zoo website
  #	When I navigate to "about_link"
  #	Then I check page title is "About"
  #	And I close the browser

  #Scenario: Check page title for Contact page
  #	Given I am on the zoo website
  #	When I navigate to "contact_link"
  #	Then I check page title is "Contact"
  #	And I close the browser


@pa @ge @title

Feature: Check the page title

  Scenario Outline: Check page title for XX page
  	Given I am on the zoo website
  	When I navigate to <xx_link>
  	Then I check page title is "<xx>"
  	And I close the browser

    Examples:
    |xx_link        |xx       |
    |adoption_link  |Adoption |
    |about_link     |About    |
    |contact_link   |Contact  |

