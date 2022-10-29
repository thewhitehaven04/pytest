from ui.pages.base import BasePage
from selenium.webdriver.common.by import By


class DynamicIDPage(BasePage):

    DYNAMIC_ID_BUTTON = (By.XPATH, '//button[text()="Button with Dynamic ID"]')

    def __init__(self, driver):
        super().__init__(driver=driver)