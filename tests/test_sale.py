import pytest


@pytest.mark.regression
def test_to_open_women_deals_page(sale_page):
    # Go to https://magento.softwaretestingboard.com/sale.html
    sale_page.open_page()

    # Open the women's deal page
    sale_page.open_women_deals()

    # Assert the success text
    sale_page.check_women_deals_success_text_is('Women Sale')


@pytest.mark.regression
def test_to_open_men_deals_page(sale_page):
    # Go to https://magento.softwaretestingboard.com/sale.html
    sale_page.open_page()

    # Open the men's deal page
    sale_page.open_men_deals()

    # Assert the success text
    sale_page.check_men_deals_success_text_is('Men Sale')


@pytest.mark.regression
def test_to_open_luma_deals_page(sale_page):
    # Go to https://magento.softwaretestingboard.com/sale.html
    sale_page.open_page()

    # Open the luma's deal page
    sale_page.open_luma_deals()

    # Assert the success text
    sale_page.check_luma_deals_success_text_is('Gear')
