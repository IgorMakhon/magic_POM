import random
import string
import pytest
from selenium import webdriver


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
