import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


@pytest.mark.regression
def test_add_to_card(driver):
    # Define the locators
    element_product_locator = (By.ID, "option-label-color-93-item-49")
    button_add_to_cart_locator = (
        By.XPATH, "//*[@id='maincontent']/div[3]/div[1]/div[4]/ol/li[1]/div/div/div[4]/div/div[1]/form/button/span"
    )
    details_locator = (By.XPATH, "//a[@id='tab-label-description-title']")

    # Go to https://magento.softwaretestingboard.com/collections/eco-friendly.html
    driver.get('https://magento.softwaretestingboard.com/collections/eco-friendly.html')

    # Wait for the element to be present
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located(element_product_locator))

    # Perform hover action
    ActionChains(driver).move_to_element(element).perform()

    # Wait for the button to be visible
    button = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(button_add_to_cart_locator))

    # Click the button
    button.click()

    # Locate, wait and save the outputted element in the variable
    cart_text = (WebDriverWait(driver, 10).until(EC.presence_of_element_located(details_locator)))

    assert cart_text.text == "Details"


@pytest.mark.regression
def test_add_to_wishlist(driver):
    # Define the locators
    element_product_locator = (By.ID, "option-label-color-93-item-49")
    button_add_to_wish_list_locator = (By.XPATH, "//*/a[@Title='Add to Wish List']")
    customer_login_locator = (By.XPATH, "//h1/span")

    # Go to https://magento.softwaretestingboard.com/collections/eco-friendly.html
    driver.get('https://magento.softwaretestingboard.com/collections/eco-friendly.html')

    # Wait for the element to be present
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located(element_product_locator))

    # Perform hover action
    ActionChains(driver).move_to_element(element).perform()

    # Wait for the button to be visible
    button = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(button_add_to_wish_list_locator))

    # Click the button
    button.click()

    # Locate, wait and save the outputted element in the variable
    customer_text = (WebDriverWait(driver, 10).until(EC.presence_of_element_located(customer_login_locator)))

    assert customer_text.text == "Customer Login"


@pytest.mark.regression
def test_add_to_compare(driver):
    # Define the locators
    element_product_locator = (By.ID, "option-label-color-93-item-49")
    button_add_to_compare_locator = (By.XPATH, "//*/a[@Title='Add to Compare']")
    compare_link_locator = (By.XPATH, "//*/a[@Title='Compare Products']")

    # Go to https://magento.softwaretestingboard.com/collections/eco-friendly.html
    driver.get('https://magento.softwaretestingboard.com/collections/eco-friendly.html')

    # Wait for the element to be present
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located(element_product_locator))

    # Perform hover action
    ActionChains(driver).move_to_element(element).perform()

    # Wait for the button to be visible
    button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(button_add_to_compare_locator))

    # Click the button
    button.click()

    # Locate, wait and save the outputted element in the variable
    compare_link = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(compare_link_locator))

    assert compare_link.is_displayed(), "Link is not present on the page."
