from selenium.webdriver.common.by import By


element_product_locator = (By.ID, "option-label-color-93-item-49")
button_add_to_cart_locator = (
    By.XPATH, "//*[@id='maincontent']/div[3]/div[1]/div[4]/ol/li[1]/div/div/div[4]/div/div[1]/form/button/span"
)
details_locator = (By.XPATH, "//a[@id='tab-label-description-title']")
button_add_to_wish_list_locator = (By.XPATH, "//*/a[@Title='Add to Wish List']")
customer_login_locator = (By.XPATH, "//h1/span")
button_add_to_compare_locator = (By.XPATH, "//*/a[@Title='Add to Compare']")
compare_link_locator = (By.XPATH, "//*/a[@Title='Compare Products']")
