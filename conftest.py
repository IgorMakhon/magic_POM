import random
import string
import pytest
from selenium import webdriver
from pages.create_account_page import CreateAccount
from pages.eco_friendly_page import EcoFriendly
from pages.sale_page import SalePage


@pytest.fixture()
def driver():
    # Initialize the Chrome WebDriver
    chrome_driver = webdriver.Chrome()
    # Maximize the window
    chrome_driver.maximize_window()
    return chrome_driver


@pytest.fixture()
def random_string_10_chars():
    # Generate random title or body
    return "".join(random.choice(string.ascii_lowercase) for _ in range(10))


@pytest.fixture()
def create_account_page(driver):
    return CreateAccount(driver)


@pytest.fixture()
def eco_friendly_page(driver):
    return EcoFriendly(driver)


@pytest.fixture()
def sale_page(driver):
    return SalePage(driver)
