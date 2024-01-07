import pytest


@pytest.mark.regression
def test_add_to_card(eco_friendly_page):
    # Open https://magento.softwaretestingboard.com/collections/eco-friendly.html
    eco_friendly_page.open_page()

    # Add the product to the cart
    eco_friendly_page.add_to_cart()

    # Assert the success text
    eco_friendly_page.check_cart_success_text_is('Details')


@pytest.mark.regression
def test_add_to_wishlist(eco_friendly_page):
    # Open https://magento.softwaretestingboard.com/collections/eco-friendly.html
    eco_friendly_page.open_page()

    # Add the product to the wishlist
    eco_friendly_page.add_to_wishlist()

    # Assert the success text
    eco_friendly_page.check_wishlist_success_text_is("Customer Login")


@pytest.mark.regression
def test_add_to_compare(eco_friendly_page):
    # Open https://magento.softwaretestingboard.com/collections/eco-friendly.html
    eco_friendly_page.open_page()

    # Add the product to the compare list
    eco_friendly_page.add_to_compare()

    # Assert the success link is displayed
    eco_friendly_page.check_compare_text_displayed()
