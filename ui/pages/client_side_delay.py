from selenium.webdriver.support.wait import WebDriverWait
from config import BROWSER_CONFIG
from ui.pages.base import BasePage
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.common.by import By


class ClientSideDelayPage(BasePage):

    BUTTON_CLIENT_LOGIC = (By.XPATH, '//button[@id="ajaxButton"]')
    I_SPINNER = (By.XPATH, '//i[@id="spinner"]')
    P_SUCCESSFULLY_CALCULATED = (By.XPATH, '//p[@class="bg-success"]')

    def __init__(self, driver) -> None:
        super().__init__(driver=driver)
        self.is_loaded()

    def is_loaded(self) -> None:
        WebDriverWait(
            driver=self.driver,
            timeout=BROWSER_CONFIG["DEFAULT_TIMEOUT"],
            poll_frequency=BROWSER_CONFIG["DEFAULT_POLL_FREQUENCY"],
        ).until(
            presence_of_element_located(
                locator=(By.XPATH, '//h3[text()="Client Side Delay"]')
            )
        )