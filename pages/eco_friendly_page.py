from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage
from pages.locators import eco_friendly_locators as loc
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class EcoFriendly(BasePage):
    page_url = '/collections/eco-friendly.html'

    def add_to_cart(self):
        element_product_field = self.find(loc.element_product_locator)
        button_add_to_cart = self.find(loc.button_add_to_cart_locator)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(loc.element_product_locator))
        ActionChains(self.driver).move_to_element(element_product_field).perform()
        button_add_to_cart.click()

    def add_to_wishlist(self):
        element_product_field = self.find(loc.element_product_locator)
        button_add_to_wishlist = self.find(loc.button_add_to_wish_list_locator)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(loc.element_product_locator))
        ActionChains(self.driver).move_to_element(element_product_field).perform()
        button_add_to_wishlist.click()

    def add_to_compare(self):
        element_product_field = self.find(loc.element_product_locator)
        button_add_to_compare = self.find(loc.button_add_to_compare_locator)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(loc.element_product_locator))
        ActionChains(self.driver).move_to_element(element_product_field).perform()
        button_add_to_compare.click()

    def check_cart_success_text_is(self, text):
        # Locate, wait and save the outputted element in the variable
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(loc.details_locator))
        cart_success_text = self.driver.find_element(*loc.details_locator)
        assert cart_success_text.text == text

    def check_wishlist_success_text_is(self, text):
        # Locate, wait and save the outputted element in the variable
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(loc.customer_login_locator))
        cart_success_text = self.driver.find_element(*loc.customer_login_locator)
        assert cart_success_text.text == text

    def check_compare_text_displayed(self):
        # Locate, wait and save the outputted element in the variable
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc.compare_link_locator))
        compare_link = self.driver.find_element(*loc.compare_link_locator)
        assert compare_link.is_displayed(), "Link is not present on the page."
