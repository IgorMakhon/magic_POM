from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def test_successful_registration(driver, random_string_10_chars):
    # Go to https://magento.softwaretestingboard.com/customer/account/create/
    driver.get('https://magento.softwaretestingboard.com/customer/account/create/')

    # Locate and complete the first name(fn) field with the positive(Stepan) name
    driver.find_element(By.ID, 'firstname').send_keys(f'{random_string_10_chars}')

    # Locate and complete the last name(ln) field with the positive(Ivanov) name
    driver.find_element(By.ID, 'lastname').send_keys(f'{random_string_10_chars}')

    # Locate and complete the email address field with the positive(test@test.com) value
    driver.find_element(By.ID, 'email_address').send_keys(f'{random_string_10_chars}@test.com')

    # Locate and complete the password field with the positive(Password1!) value
    driver.find_element(By.ID, 'password').send_keys('Password1!')

    # Locate and complete the confirm_password field with the positive(Password1!) value
    driver.find_element(By.ID, 'password-confirmation').send_keys('Password1!')

    # Locate and click the button 'Create an Account'
    driver.find_element(By.XPATH, '//button[@title="Create an Account"]/span').click()

    # Locate, wait and save the outputted element in the variable
    success_txt = (
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
            (By.XPATH, "//*/div[.='Thank you for registering with Main Website Store.']")
            )
        )
    )

    assert success_txt.text == 'Thank you for registering with Main Website Store.'


def test_sign_in_fields_are_mandatory(driver, random_string_10_chars):
    # Go to https://magento.softwaretestingboard.com/customer/account/create/
    driver.get('https://magento.softwaretestingboard.com/customer/account/create/')

    # Locate and complete the first name field with the positive name
    driver.find_element(By.ID, 'firstname').send_keys(f'{random_string_10_chars}')

    # Locate and complete the last name(ln) field with the positive(Ivanov) name
    driver.find_element(By.ID, 'lastname').send_keys(f'{random_string_10_chars}')

    # Locate and click the button 'Create an Account'
    driver.find_element(By.XPATH, '//button[@title="Create an Account"]/span').click()

    # Locate, wait and save the outputted validation message for 'email' field in the variable
    validation_email = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "email_address-error")))

    # Locate, wait and save the outputted validation message for 'Password' field in the variable
    validation_password = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "password-error")))

    assert (
            validation_email.text == 'This is a required field.' and
            validation_password.text == 'This is a required field.'
    )


def test_personal_information_fields_are_mandatory(driver, random_string_10_chars):
    # Go to https://magento.softwaretestingboard.com/customer/account/create/
    driver.get('https://magento.softwaretestingboard.com/customer/account/create/')

    # Locate and complete the email address field with the positive(test@test.com) value
    driver.find_element(By.ID, 'email_address').send_keys(f'{random_string_10_chars}@test.com')

    # Locate and complete the password field with the positive(Password1!) value
    driver.find_element(By.ID, 'password').send_keys('Password1!')

    # Locate and complete the confirm_password field with the positive(Password1!) value
    driver.find_element(By.ID, 'password-confirmation').send_keys('Password1!')

    # Locate and click the button 'Create an Account'
    driver.find_element(By.XPATH, '//button[@title="Create an Account"]/span').click()

    # Locate, wait and save the outputted validation message for 'email' field in the variable
    validation_firstname = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "firstname-error")))

    # Locate, wait and save the outputted validation message for 'Password' field in the variable
    validation_lastname = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "lastname-error")))

    assert (
            validation_firstname.text == 'This is a required field.' and
            validation_lastname.text == 'This is a required field.'
    )
