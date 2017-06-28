#Parameter Handling

@page @title

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

