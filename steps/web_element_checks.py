from typing import Tuple
from selenium.webdriver.remote.webelement import WebElement

from ui.pages.base import BasePage


def is_web_element_attribute_value_equal_to(element: WebElement,
                                            attribute: str, value) -> None:
    """
    Element's attribute value is equal to the expected value

    Arguments:
        element -- web element;
        attribute -- name of the attribute
    """
    actual_value = element.get_attribute(attribute)
    assert (
        actual_value == value
    ), f"The expected attribute value does not match the actual value.\nExpected value: '{value}'\nActual value: '{actual_value}'"


def is_web_element_text_equal_to(element: WebElement,
                                 expected_text: str) -> None:
    """
    Test whether element's text matches expected text.

    Arguments:
        element -- web element;
        expected text -- text to be compared against
    """
    assert (
        element.text == expected_text
    ), f"Element's actual text ('{element.text}') does not match the expected text ('{expected_text}')"

def is_element_displayed(page: BasePage, locator: Tuple[str, str]) -> None:
    assert page.is_element_displayed(
        locator=locator), f"The element {locator[1]} is not displayed"
