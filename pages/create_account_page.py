from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage
from pages.locators import create_account_locators as loc
from utils import project_ec


class CreateAccount(BasePage):
    page_url = '/customer/account/create/'

    def fill_all_account_form(self, *args):
        firstname_field = self.find(loc.firstname_locator)
        lastname_field = self.find(loc.lastname_locator)
        email = self.find(loc.email_locator)
        passw = self.find(loc.password_locator)
        passw_conf = self.find(loc.password_confirmation_locator)
        button = self.find(loc.button_create_account_locator)
        firstname_field.send_keys(args)
        lastname_field.send_keys(args)
        email.send_keys(args, '@test.com')
        passw.send_keys('Password1!')
        passw_conf.send_keys('Password1!')
        button.click()

    def fill_personal_info_form(self, *args):
        firstname_field = self.find(loc.firstname_locator)
        lastname_field = self.find(loc.lastname_locator)
        button = self.find(loc.button_create_account_locator)
        firstname_field.send_keys(args)
        lastname_field.send_keys(args)
        button.click()

    def fill_signin_info_form(self, *args):
        email = self.find(loc.email_locator)
        passw = self.find(loc.password_locator)
        passw_conf = self.find(loc.password_confirmation_locator)
        button = self.find(loc.button_create_account_locator)
        email.send_keys(args, '@test.com')
        passw.send_keys('Password1!')
        passw_conf.send_keys('Password1!')
        button.click()

    def check_success_text_is(self, text):
        WebDriverWait(self.driver, 5).until(project_ec.text_is_not_empty_in_element(loc.success_text_locator))
        #  the * is used for unpacking the contents of the loc.error_locator tuple. The find_element method of the
        #  Selenium WebDriver expects two arguments: the locator strategy and the locator value.
        #  By using *loc.error_locator, you are effectively unpacking the tuple so that its elements are passed
        #  as separate arguments to the find_element method.
        error_alert = self.driver.find_element(*loc.success_text_locator)
        assert error_alert.text == text

    def check_personal_validation_text_is(self, text):
        # Locate, wait and save the outputted validation message for 'firstname' field in the variable
        WebDriverWait(self.driver, 10).until(project_ec.text_is_not_empty_in_element(loc.error_firstname_locator))
        validation_firstname = self.driver.find_element(*loc.error_firstname_locator)
        assert validation_firstname.text == text

    def check_sign_in_validation_text_is(self, text):
        # Locate, wait and save the outputted validation message for 'email' field in the variable
        WebDriverWait(self.driver, 10).until(project_ec.text_is_not_empty_in_element(loc.error_email_locator))
        validation_email = self.driver.find_element(*loc.error_email_locator)
        assert validation_email.text == text
