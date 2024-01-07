# The main purpose of this function is to create and return a predicate function
# (a function that returns either True or False) that checks whether the text content of a web element located by the
# specified locator is not empty.

def text_is_not_empty_in_element(locator):
    # It defines an inner function named _predicate, which takes a Selenium WebDriver instance driver as an argument.
    def _predicate(driver):
        #  It locates a web element on the web page using the find_element method of the Selenium WebDriver.
        #  The *locator syntax is used to unpack the elements of the locator tuple and pass them
        #  as arguments to the find_element method.
        element = driver.find_element(*locator)
        if len(element.text) > 0:
            return True
        else:
            return False

    return _predicate
