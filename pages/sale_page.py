from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage
from pages.locators import sale_page_locators as loc
from utils import project_ec


class SalePage(BasePage):
    page_url = '/sale.html'

    def open_women_deals(self):
        women_deals_element = self.find(loc.women_deals_locator)
        women_deals_element.click()

    def open_men_deals(self):
        men_deals_element = self.find(loc.men_deals_locator)
        men_deals_element.click()

    def open_luma_deals(self):
        men_deals_element = self.find(loc.luma_deals_locator)
        men_deals_element.click()

    def check_women_deals_success_text_is(self, text):
        # Locate, wait and save the outputted validation message for 'firstname' field in the variable
        WebDriverWait(self.driver, 10).until(project_ec.text_is_not_empty_in_element(loc.women_sale_locator))
        women_deals_success_text = self.driver.find_element(*loc.women_sale_locator)
        assert women_deals_success_text.text == text

    def check_men_deals_success_text_is(self, text):
        # Locate, wait and save the outputted validation message for 'firstname' field in the variable
        WebDriverWait(self.driver, 10).until(project_ec.text_is_not_empty_in_element(loc.men_sale_locator))
        men_deals_success_text = self.driver.find_element(*loc.men_sale_locator)
        assert men_deals_success_text.text == text

    def check_luma_deals_success_text_is(self, text):
        # Locate, wait and save the outputted validation message for 'firstname' field in the variable
        WebDriverWait(self.driver, 10).until(project_ec.text_is_not_empty_in_element(loc.luma_sale_locator))
        luma_deals_success_text = self.driver.find_element(*loc.luma_sale_locator)
        assert luma_deals_success_text.text == text
