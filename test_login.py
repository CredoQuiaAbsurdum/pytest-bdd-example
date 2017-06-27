# coding=utf-8
"""login feature tests."""

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



@scenario('login.feature', 'Successful login')
def test_successful_login():
    """Successful login."""


@given('I am on the login screen')
def i_am_on_the_login_screen():
    """I am on the login screen."""
    driver.get("http://301-docker-host.sol38.com/login?session_id=123456789#anchor")


@when('I provide a valid username')
def i_provide_a_valid_username():
    """I provide a valid username."""
    driver.find_element_by_xpath("form-control ng-pristine ng-valid ng-touched").send_keys("qazaxine1@smartsti.com")


@when('I provide the corresponding password')
def i_provide_the_corresponding_password():
    """I provide the corresponding password."""
    driver.find_element_by_css_selector("form-control ng-pristine ng-valid ng-touched").send_keys("qazaxine1@smartsti.com")


@when('I press Submit')
def i_press_submit():
    """I press Submit."""
    driver.find_element_by_class("btn btn-primary btn-fill").click()



@then('I am logged in')
def i_am_logged_in():
    """I am logged in."""

