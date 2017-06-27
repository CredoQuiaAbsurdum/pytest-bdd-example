# pytest-bdd Cheat Sheet

### Recommendations
Before using this cheat sheet:
+ Learn the following about [Gherkin](https://cucumber.io/docs/reference#gherkin):
  - Feature, Scenario
  - Given, When, Then
  - Scenario Outline, Examples
  - Tags
  - Comments
+ For people without any Python experience, learn basic syntax of Python such as:
  - indentation 
  - commenting 
  - declarition of variables and functions
+ Read through the official document: [pytest-bdd.pdf](https://media.readthedocs.org/pdf/pytest-bdd/latest/pytest-bdd.pdf) .

### Setup

##### 1. Install [python](https://www.python.org/downloads/) environment
	
##### 2. Install [pip](https://media.readthedocs.org/pdf/pip/latest/pip.pdf)
1. Download **[get-pip.py](https://bootstrap.pypa.io/get-pip.py)**
2. Run following command:
```
python get-pip.py
```
3. Upgrade pip
```
pip install -U pip
```

##### 3. Instal [pytest](https://media.readthedocs.org/pdf/pytest/latest/pytest.pdf)
```
pip install -U pytest
```

##### 4. Install [pytest-bdd](https://media.readthedocs.org/pdf/pytest-bdd/latest/pytest-bdd.pdf)
```
pip install pytest-bdd
```

##### 5. Install [selenium](https://media.readthedocs.org/pdf/selenium-python/latest/selenium-python.pdf)

```
pip install selenium
```
##### 6. Download a webdriver
* [chromedriver](https://sites.google.com/a/chromium.org/chromedriver/downloads)
* fireboxdriver
* etc.


### Write feature files
##### • Template
```
# This is a comment
@aTag @anotherTag @etc...
Feature: some description ...
	Scenario: some description ...
		Given ...
		When ...
		Then ...
    And ...
```

##### • Scenario Outline

```
#pageTitle.feature
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
```  
  
* **Vertical** example table
```
Scenario Outline: Outlined given, when, thens 
Given there are <start> cucumbers
When I eat <eat> cucumbers
Then I should have <left> cucumbers
Examples: Vertical
| start | 12 | 2  | 
| eat   | 5  | 1  |  
| left  | 7  | 1  |
```

### Generate test files
**NOTICE:** 
* A test file and its corresponding feature file MUST stay in the same dirctory
* The name of a test file MUST be in the form of <i>test_\*.py</i> or <i>\*_test.py</i>
* After the generation by pytest-bdd, *And* will be autometically modified to *given*, *when*, or *then* in the test file according to its previous sentence.

• Create fully functional but of course empty tests and step definitions for given a feature file.
```
pytest-bdd generate someFeature.feature
```
• Redirect the generated code to a test file.
```
pytest-bdd generate pageTitle.feature > test_some_feature.py
```
• Advanced code generation
```
py.test --generate-missing --feature features tests/functional
```

### Modify test files

##### • import 
```python
from pytest_bdd import (given, scenario, then, when)
import pytest
from selenium import webdriver
```


##### • Fixture for driver setup
Allow the browser automaticlly run before executing tests and quit after all the tests finished.
```
@pytest.fixture(autouse=True, scope='function')
def setup(request):
    global driver
    driver = webdriver.Chrome("/Users/yuxuan.zhao/chromedriver")
    def fin():
        driver.quit()
        request.addfinalizer(fin)
```

##### • Step definition
* Step aliases
```python
@given('I am on the zoo website')
@given('I am on the homepage of zoo website')
def i_am_on_the_zoo_website():
    """I am on the zoo website."""
    driver.get("http://www.thetestroom.com/webapp/")
```

* Step arguments
```python
@when('I navigate to <xx_link>')
def i_navigate_to_xx_link(xx_link):
    """I navigate to <xx_link>."""
    driver.find_element_by_id(xx_link).click()
```

* Driver usage  
  - Navigate to a page given by the URL
```
driver.get("http://www.python.org")  
```
  - An assertion to confirm that title has “Python” word in it
```
assert "Python" in driver.title
```  
  - Find an element
```
elem = driver.find_element_by_name("q")
# find_element_by_id
# find_element_by_name
# find_element_by_link_text
# find_element_by_partial_link_text
# etc..
```
  - Clear filds
```
elem.clear()
```  
  - Sending keys
```
from selenium.webdriver.common.keys import Keys
elem.send_keys("pycon")
```
See more information in the official document: [selenium-python.pdf](https://media.readthedocs.org/pdf/selenium-python/latest/selenium-python.pdf)


### Run the tests

* Running all the tests
```
pytest
```
* Running a specified file
```
pytest test_something.py
```
* Running tests with sepcific tags
```
pytest -k "Tag1 and Tag2 and Tag3"
```
* Running tests without a certain tag
```
pytest -k "not Tag1"
```

### Reporting
To have an output in json format:
```
py.test --cucumberjson=<path to json report>
```


### Example

https://github.com/VirtaKuivapuu/pytest-bdd-example



