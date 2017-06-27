from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)

import pytest
from selenium import webdriver


@pytest.fixture(autouse=True, scope='module')
def setup(request):
    global driver
    driver = webdriver.Chrome("/Users/yuxuan.zhao/chromedriver")
    def fin():
        driver.quit()
        request.addfinalizer(fin)


@scenario('ContactConfirm.feature', 'Check form is validated when there are no errors')
def test_check_form_is_validated_when_there_are_no_errors():
    """Check form is validated when there are no errors."""


@given('I am on the zoo website')
def i_am_on_the_zoo_website():
    """I am on the zoowebsite."""
    driver.get("http://www.thetestroom.com/webapp/")

@when('I click the button of contact link')
def i_click_the_button_of_contact_link():
    """I click the button of contact link."""
    driver.find_element_by_id("contact_link").click()


@when('populate the contact form')
def populate_the_contact_form():
    """populate the contact form."""
    driver.find_element_by_name("name_field").send_keys("Chris")
    driver.find_element_by_name("address_field").send_keys("Galaxy")
    driver.find_element_by_name("postcode_field").send_keys("P2D F3F")
    driver.find_element_by_name("email_field").send_keys("light@star.com")
    driver.find_element_by_id("submit_message").click()


@then('I close the browser')
def i_close_the_browser():
    """I close the browser."""
    driver.close()


@then('I should be on the contact confirmation page')
def i_should_be_on_the_contact_confirmation_page():
    """I should be on the contact confirmation page."""
    assert driver.title == "Contact Confirmation"
