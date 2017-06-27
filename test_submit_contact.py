# coding=utf-8
"""Submit a valid contact form feature tests."""

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


@scenario('SubmitContact.feature', 'Submit form using valid data')
def test_submit_form_using_valid_data():
    """Submit form using valid data."""


@given('I am on the zoo website')
def i_am_on_the_zoo_website():
    """I am on the zoo website."""
    driver.get("http://www.thetestroom.com/webapp/")

@when('I navigate to "contact_link"')
def i_navigate_to_contact_link():
    """I navigate to "contact_link"."""
    driver.find_element_by_id("contact_link").click()

@when('I submit the form with valid data')
def i_submit_the_form_with_valid_data():
    """I submit the form with valid data."""
    #driver.find_element_by_name("name_field").sendKeys(data.get(1).get(1))
    #driver.find_element_by_name("address_field").sendKeys(data.get(2).get(1))
    #driver.find_element_by_name("postcode_field").sendKeys(data.get(3).get(1))
    #driver.find_element_by_name("email_field").sendKeys(data.get(4).get(1))

    driver.find_element_by_name("name_field").send_keys("Chris")
    driver.find_element_by_name("address_field").send_keys("Galaxy")
    driver.find_element_by_name("postcode_field").send_keys("P2D F3F")
    driver.find_element_by_name("email_field").send_keys("light@star.com")


@then('I check that the form has been subimtted')
def i_check_that_the_form_has_been_subimtted():
    """I check that the form has been subimtted."""
    driver.find_element_by_id("submit_message").click()
    assert "Contact Confirmation" in driver.title

@then('I close the browser')
def i_close_the_browser():
    """I close the browser."""
    driver.close()
    driver.quit()