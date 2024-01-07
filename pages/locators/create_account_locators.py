from selenium.webdriver.common.by import By


firstname_locator = (By.ID, 'firstname')
lastname_locator = (By.ID, 'lastname')
email_locator = (By.ID, 'email_address')
password_locator = (By.ID, 'password')
password_confirmation_locator = (By.ID, 'password-confirmation')
button_create_account_locator = (By.XPATH, '//button[@title="Create an Account"]/span')
success_text_locator = (By.XPATH, "//*/div[.='Thank you for registering with Main Website Store.']")
error_email_locator = (By.ID, "email_address-error")
error_password_locator = (By.ID, "password-error")
error_firstname_locator = (By.ID, "firstname-error")
error_lastname_locator = (By.ID, "lastname-error")
