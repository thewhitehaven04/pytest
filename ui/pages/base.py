from typing import Tuple
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import BROWSER_CONFIG
from selenium.common.exceptions import (
    StaleElementReferenceException,
    ElementNotVisibleException,
    ElementNotInteractableException,
)


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.ignored_exceptions = [
            StaleElementReferenceException,
            ElementNotInteractableException,
            ElementNotVisibleException,
        ]

    def click(self, locator) -> None:
        element = WebDriverWait(
            driver=self.driver,
            timeout=BROWSER_CONFIG["DEFAULT_TIMEOUT"],
            poll_frequency=BROWSER_CONFIG["DEFAULT_POLL_FREQUENCY"],
            ignored_exceptions=self.ignored_exceptions,
        ).until(EC.element_to_be_clickable(locator))
        element.click()

    def get_element(self, locator: Tuple[str, str]) -> WebElement:
        return WebDriverWait(
            driver=self.driver,
            timeout=BROWSER_CONFIG["DEFAULT_TIMEOUT"],
            poll_frequency=BROWSER_CONFIG["DEFAULT_POLL_FREQUENCY"],
            ignored_exceptions=self.ignored_exceptions
        ).until(EC.presence_of_element_located(locator=locator))

    def is_element_displayed(self, locator: Tuple[str, str]) -> bool:
        try:
            WebDriverWait(
                driver=self.driver,
                timeout=BROWSER_CONFIG["DEFAULT_TIMEOUT"],
                poll_frequency=BROWSER_CONFIG["DEFAULT_POLL_FREQUENCY"],
            ).until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False
