# coding=utf-8
"""Check the page title feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)
import pytest
from selenium import webdriver

@pytest.fixture(autouse=True, scope='function')
def setup(request):
    global driver
    driver = webdriver.Chrome("/Users/yuxuan.zhao/chromedriver")
    def fin():
        driver.quit()
        request.addfinalizer(fin)

@scenario('PageTitle.feature', 'Check page title for XX page',
          example_converters=dict(xx_link=str, xx=str))
def test_check_page_title_for_adoption_page():
    """Check page title for Adoption page."""


@given('I am on the zoo website')
@given('I am on the homepage of zoo website')
def i_am_on_the_zoo_website():
    """I am on the zoo website."""
    driver.get("http://www.thetestroom.com/webapp/")

@when('I navigate to <xx_link>')
def i_navigate_to_xx_link(xx_link):
    """I navigate to <xx_link>."""
    driver.find_element_by_id(xx_link).click()

@then('I check page title is "<xx>"')
def i_check_page_title_is_xx(xx):
    """I check page title is "<xx>"."""
    assert xx in driver.title

@then('I close the browser')
def i_close_the_browser():
    """I close the browser."""
    driver.close()
