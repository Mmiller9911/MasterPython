"""
Module containing common function used in several tests.
Functions that are not test or feature specific.
"""
from BDDCommon.CommonConfigs import urlconfig
from selenium import webdriver
import time
import logging as logger


def go_to(context, location):
    if not location.startswith('http'):
        base_url = urlconfig.URLCONFIG.get('base_url')
        partial_url = urlconfig.URLCONFIG.get(location)
        url = base_url + partial_url
    else:
        url = location
    logger.info("111111")
    logger.info(f"navigating to url {url}")
    context.driver.get(url)
    return context.driver


def assert_page_title(context, expected_title):
    actual_title = context.driver.title

    print("The actual title is: {}".format(actual_title))
    print("The expected title is: {}".format(expected_title))

    assert expected_title == actual_title, "The title is not as expected." \
                                           " Expected: {}, Actual: {}".format(expected_title, actual_title)
    print("The page title is as expected.")


def assert_current_url(context, expected_url):
    current_url = context.driver.current_url

    if not expected_url.startswith('http') or not expected_url.startswith('https'):
        expected_url = 'https://' + expected_url + '/'

    assert current_url == expected_url, "The current url is not as expected." \
                                        " Actual: {}, Expected: {}".format(current_url, expected_url)

    print("The page url is as expected.")


def url_contains(context, text):
    current_url = context.driver.current_url
    if text in current_url:
        return True
    else:
        return False


def assert_url_contains(context, text):
    contains = url_contains(context, text)
    assert contains, f"Current url '{context.driver.current_url}' does not contain text '{text}'."


def find_element(context, locator_attribute, locator_text):
    possible_locators = ["id", "xpath", "link text", "partial link text", "name", "tag name", "class name", "css selector"]

    if locator_attribute not in possible_locators:
        raise Exception('The locator attribute provided is not in the approved attributes. Or the spelling and format does not match.\
                            The approved attributes are : %s ' % possible_locators)
    try:
        element = context.driver.find_element(locator_attribute, locator_text)
        return element
    except Exception as e:
        raise Exception(e)


def find_elements(context, locator_attribute, locator_text):
    possible_locators = ["id", "xpath", "link text", "partial link text", "name", "tag name", "class name", "css selector"]

    if locator_attribute not in possible_locators:
        raise Exception('The locator attribute provided is not in the approved attributes. Or the spelling and format does not match.\
                            The approved attributes are : %s ' % possible_locators)
    try:
        element = context.driver.find_elements(locator_attribute, locator_text)
        return element
    except Exception as e:
        raise Exception(e)


def is_element_visible(element):
    if element.is_displayed():
        return True
    else:
        return False


def assert_element_visible(context_or_element, locator_att=None, locator_text=None):

    if isinstance(context_or_element, webdriver.remote.webelement.WebElement):
        element = context_or_element
    else:
        element = context_or_element.driver.find_element(locator_att, locator_text)

    if not element.is_displayed():
        raise AssertionError('The element is not displayed')


def type_into_element(context_or_element, input_value, locator_att, locator_text):

    if isinstance(context_or_element, webdriver.remote.webelement.WebElement):
        input_field = context_or_element
    else:
        input_field = context_or_element.driver.find_element(locator_att, locator_text)

    input_field.send_keys(input_value)


def click(context_or_element, locator_att=None, locator_text=None):

    if isinstance(context_or_element, webdriver.remote.webelement.WebElement):
        element = context_or_element
    else:
        element = context_or_element.driver.find_element(locator_att, locator_text)

    element.click()


def element_contains_text(context_or_element, expected_text, locator_att, locator_text, case_sensitive=False):
    if isinstance(context_or_element, webdriver.remote.webelement.WebElement):
        element = context_or_element
    else:
        element = context_or_element.driver.find_element(locator_att, locator_text)

    element_text = element.text
    if not case_sensitive:
        if expected_text.lower() in element_text.lower():
            return True
        else:
            return False
    else:
            return True if expected_text in element_text else False


def assert_element_contains_text(context_or_element, expected_text, locator_att, locator_text, case_sensitive=False):
    max_try = 5
    sleep_bn_try = 2
    for i in range(max_try):
        try:
            contains = element_contains_text(context_or_element, expected_text, locator_att, locator_text, case_sensitive=False)
            assert contains, "Element does not contain text"
            break
        except AssertionError:
            time.sleep(sleep_bn_try)
    else:
        # this will only be executed if the entire for has completed and no break has happened
        raise Exception(f"Element with type '{locator_att}' text '{locator_text}', does not contain text {expected_text}"
                        f"Retried '{max_try}' times with a wait of '{sleep_bn_try}' seconds.")


def assert_radio_is_selected(context_or_element, locator_att=None, locator_text=None, case_sensitive=False):
    if isinstance(context_or_element, webdriver.remote.webelement.WebElement):
        element = context_or_element
    else:
        element = context_or_element.driver.find_element(locator_att, locator_text)

    ischecked = element.get_attribute('checked')
    assert ischecked, f"The radio is not selected {element.get_attribute('name')}"


def get_element_text(context_or_element, locator_att=None, locator_text=None):
    if isinstance(context_or_element, webdriver.remote.webelement.WebElement):
        element_text = context_or_element.text
    else:
        element = context_or_element.driver.find_element(locator_att, locator_text)
        element_text = element.text

    return element_text
