from ui.pages.base import BasePage
from ui.pages.client_side_delay import ClientSideDelayPage
from ui.pages.dynamic_id import DynamicIDPage
from selenium.webdriver.common.by import By

from ui.pages.load_delay import LoadDelayPage


class MainPage(BasePage):

    def __init__(self, driver) -> None:
        super().__init__(driver=driver)

    def go_to_dynamic_id_page(self) -> DynamicIDPage:
        self.click(locator=(By.XPATH, '//a[@href="/dynamicid"]'))
        return DynamicIDPage(driver=self.driver)

    def go_to_client_side_delay_page(self) -> ClientSideDelayPage:
        self.click(locator=(By.XPATH, '//a[@href="/clientdelay"]'))
        return ClientSideDelayPage(driver=self.driver)

    def go_to_delay_page(self) -> LoadDelayPage:
        self.click(locator=(By.XPATH, '//a[@href="/loaddelay"]'))
        return LoadDelayPage(driver=self.driver)