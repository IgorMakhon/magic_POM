import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


@pytest.mark.regression
def test_to_open_women_deals_page(driver):
    # Define the locators
    women_deals_locator = (By.XPATH, "//*/main/div[4]/div[1]/div[2]/div[1]/a")
    women_sale_locator = (By.XPATH, "//*/main/div[1]/h1/span")

    # Go to https://magento.softwaretestingboard.com/sale.html
    driver.get('https://magento.softwaretestingboard.com/sale.html')

    # Wait fot the women deals
    element = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(women_deals_locator))

    # Click the women deals
    element.click()

    # Locate, wait and save the outputted element in the variable
    woman_sale_text = (WebDriverWait(driver, 10).until(EC.presence_of_element_located(women_sale_locator)))

    assert woman_sale_text.text == 'Women Sale'


@pytest.mark.regression
def test_to_open_men_deals_page(driver):
    # Define the locators
    men_deals_locator = (By.CLASS_NAME, "sale-mens")
    men_sale_locator = (By.XPATH, "//main/div[1]/h1/span")

    # Go to https://magento.softwaretestingboard.com/sale.html
    driver.get('https://magento.softwaretestingboard.com/sale.html')

    # Wait fot the women deals
    element = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(men_deals_locator))

    # Click the women deals
    element.click()

    # Locate, wait and save the outputted element in the variable
    man_sale_text = (WebDriverWait(driver, 10).until(EC.presence_of_element_located(men_sale_locator)))

    assert man_sale_text.text == 'Men Sale'


@pytest.mark.regression
def test_to_open_luma_deals_page(driver):
    # Define the locators
    luma_deals_locator = (By.CLASS_NAME, "sale-women")
    luma_sale_locator = (By.XPATH, "//main/div[1]/h1/span")

    # Go to https://magento.softwaretestingboard.com/sale.html
    driver.get('https://magento.softwaretestingboard.com/sale.html')

    # Wait fot the women deals
    element = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(luma_deals_locator))

    # Click the women deals
    element.click()

    # Locate, wait and save the outputted element in the variable
    man_sale_text = (WebDriverWait(driver, 10).until(EC.presence_of_element_located(luma_sale_locator)))

    assert man_sale_text.text == 'Gear'
