from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.wait import WebDriverWait
from config import BROWSER_CONFIG
from ui.pages.base import BasePage


class LoadDelayPage(BasePage):

    BUTTON_AFTER_DELAY = (By.XPATH,
                          '//button[text()="Button Appearing After Delay"]')

    def __init__(self, driver):
        super().__init__(driver=driver)
        self.is_loaded()

    def is_loaded(self):
        WebDriverWait(
            driver=self.driver,
            timeout=BROWSER_CONFIG['DEFAULT_TIMEOUT'],
            poll_frequency=BROWSER_CONFIG['DEFAULT_POLL_FREQUENCY']).until(
                presence_of_element_located(
                    locator=(By.XPATH,
                             '//div[@class="container"]/h3[.="Load Delays"]')))
