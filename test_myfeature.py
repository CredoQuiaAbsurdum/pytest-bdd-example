# coding=utf-8
"""Proof of concept that my framework works feature tests."""

import pytest
from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)

@scenario('myfeature.feature', 'My first test')
def test_my_first_test():
    """My first test."""



@given('I navigate to the zoo website')
def i_navigate_to_the_zoo_website():
    """I navigate to the zoo website."""
    print "Executed the navigate to zoo"


@when('I click on the check button')
def i_click_on_the_check_button():
    """I click on the check button."""
    print "Executed the click on adoption link method"


@then('I check to see that no animals are available')
def i_check_to_see_that_no_animals_are_available():
    """I check to see that no animals are available."""
    print "Checked that the no animals string was visible or not"
