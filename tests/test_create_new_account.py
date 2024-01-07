import pytest
import logging


#  It is used to create a logger object in Python using the logging module
#  The LOGGER object is used  to log messages at various severity levels, such as debug, info, warning, error.
LOGGER = logging.getLogger(__name__)


@pytest.mark.regression
def test_successful_registration(create_account_page, random_string_10_chars):
    # Open https://magento.softwaretestingboard.com/customer/account/create/
    create_account_page.open_page()

    # Complete all required fields and click the button to submit the form
    create_account_page.fill_all_account_form(random_string_10_chars)

    # Assert the success text
    create_account_page.check_success_text_is('Thank you for registering with Main Website Store.')
    LOGGER.critical('Test result is Ok')


@pytest.mark.regression
def test_sign_in_fields_are_mandatory(create_account_page, random_string_10_chars):
    # Open https://magento.softwaretestingboard.com/customer/account/create/
    create_account_page.open_page()

    # Complete sign-in fields and click the button to submit the form
    create_account_page.fill_signin_info_form(random_string_10_chars)

    # Assert the validation text for personal field 'email'
    create_account_page.check_personal_validation_text_is('This is a required field.')
    LOGGER.critical('Test result is Ok')


@pytest.mark.regression
def test_personal_information_fields_are_mandatory(create_account_page, random_string_10_chars):
    # Open https://magento.softwaretestingboard.com/customer/account/create/
    create_account_page.open_page()

    # Complete personal fields and click the button to submit the form
    create_account_page.fill_personal_info_form(random_string_10_chars)

    # Assert the required validation text for sign in field 'first name'
    create_account_page.check_sign_in_validation_text_is('This is a required field.')
    LOGGER.critical('Test result is Ok')
