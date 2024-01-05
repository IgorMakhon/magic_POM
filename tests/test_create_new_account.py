import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


@pytest.mark.current
def test_successful_registration(driver, random_string_10_chars):
    # Define the locators
    firstname_locator = (By.ID, 'firstname')
    lastname_locator = (By.ID, 'lastname')
    email_locator = (By.ID, 'email_address')
    password_locator = (By.ID, 'password')
    password_confirmation_locator = (By.ID, 'password-confirmation')
    button_create_account_locator = (By.XPATH, '//button[@title="Create an Account"]/span')
    success_text_locator = (By.XPATH, "//*/div[.='Thank you for registering with Main Website Store.']")

    # Go to https://magento.softwaretestingboard.com/customer/account/create/
    driver.get('https://magento.softwaretestingboard.com/customer/account/create/')

    # Locate and complete the first name(fn) field with the positive(Stepan) name
    driver.find_element(firstname_locator).send_keys(f'{random_string_10_chars}')

    # Locate and complete the last name(ln) field with the positive(Ivanov) name
    driver.find_element(lastname_locator).send_keys(f'{random_string_10_chars}')

    # Locate and complete the email address field with the positive(test@test.com) value
    driver.find_element(email_locator).send_keys(f'{random_string_10_chars}@test.com')

    # Locate and complete the password field with the positive(Password1!) value
    driver.find_element(password_locator).send_keys('Password1!')

    # Locate and complete the confirm_password field with the positive(Password1!) value
    driver.find_element(password_confirmation_locator).send_keys('Password1!')

    # Locate and click the button 'Create an Account'
    driver.find_element(button_create_account_locator).click()

    # Locate, wait and save the outputted element in the variable
    success_txt = (WebDriverWait(driver, 10).until(EC.visibility_of_element_located(success_text_locator)))

    assert success_txt.text == 'Thank you for registering with Main Website Store.'


@pytest.mark.regression
def test_sign_in_fields_are_mandatory(driver, random_string_10_chars):
    # Define the locators
    firstname_locator = (By.ID, 'firstname')
    lastname_locator = (By.ID, 'lastname')
    button_create_account_locator = (By.XPATH, '//button[@title="Create an Account"]/span')
    error_email_locator = (By.ID, "email_address-error")
    error_password_locator = (By.ID, "password-error")

    # Go to https://magento.softwaretestingboard.com/customer/account/create/
    driver.get('https://magento.softwaretestingboard.com/customer/account/create/')

    # Locate and complete the first name field with the positive name
    driver.find_element(firstname_locator).send_keys(f'{random_string_10_chars}')

    # Locate and complete the last name(ln) field with the positive(Ivanov) name
    driver.find_element(lastname_locator).send_keys(f'{random_string_10_chars}')

    # Locate and click the button 'Create an Account'
    driver.find_element(button_create_account_locator).click()

    # Locate, wait and save the outputted validation message for 'email' field in the variable
    validation_email = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(error_email_locator))

    # Locate, wait and save the outputted validation message for 'Password' field in the variable
    validation_password = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(error_password_locator))

    assert (
            validation_email.text == 'This is a required field.' and
            validation_password.text == 'This is a required field.'
    )


@pytest.mark.regression
def test_personal_information_fields_are_mandatory(driver, random_string_10_chars):
    # Define the locators
    email_locator = (By.ID, 'email_address')
    password_locator = (By.ID, 'password')
    password_confirmation_locator = (By.ID, 'password-confirmation')
    button_create_account_locator = (By.XPATH, '//button[@title="Create an Account"]/span')
    error_firstname_locator = (By.ID, "firstname-error")
    error_lastname_locator = (By.ID, "lastname-error")

    # Go to https://magento.softwaretestingboard.com/customer/account/create/
    driver.get('https://magento.softwaretestingboard.com/customer/account/create/')

    # Locate and complete the email address field with the positive(test@test.com) value
    driver.find_element(email_locator).send_keys(f'{random_string_10_chars}@test.com')

    # Locate and complete the password field with the positive(Password1!) value
    driver.find_element(password_locator).send_keys('Password1!')

    # Locate and complete the confirm_password field with the positive(Password1!) value
    driver.find_element(password_confirmation_locator).send_keys('Password1!')

    # Locate and click the button 'Create an Account'
    driver.find_element(button_create_account_locator).click()

    # Locate, wait and save the outputted validation message for 'email' field in the variable
    validation_firstname = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(error_firstname_locator))

    # Locate, wait and save the outputted validation message for 'Password' field in the variable
    validation_lastname = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(error_lastname_locator))

    assert (
            validation_firstname.text == 'This is a required field.' and
            validation_lastname.text == 'This is a required field.'
    )
