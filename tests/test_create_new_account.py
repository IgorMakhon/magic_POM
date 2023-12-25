from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def test_with_positive_values(driver, random_string_10_chars):
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

    # Locate, wait and save the outputted element in the # Locate, wait and save the outputted element in the variable

    success_txt = (
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
            (By.XPATH, "//*/div[.='Thank you for registering with Main Website Store.']")
            )
        )
    )

    assert success_txt.text == 'Thank you for registering with Main Website Store.'
