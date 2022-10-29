import pytest
from config import TEST_SITE_ROOT_URL
from steps.web_element_checks import (
    is_element_displayed,
    is_web_element_text_equal_to,
)
from ui.pages.main import MainPage
from fixtures.browser import get_chrome as browser


class TestClientSide:

    def test_data_calculation(self, browser):
        """Вычисление данных на клиенте"""
        browser.get(TEST_SITE_ROOT_URL)
        client_side_page = MainPage(
            driver=browser).go_to_client_side_delay_page()

        client_side_page.click(client_side_page.BUTTON_CLIENT_LOGIC)
        client_side_page.is_element_displayed(client_side_page.I_SPINNER)
        is_web_element_text_equal_to(
            client_side_page.get_element(client_side_page.BUTTON_CLIENT_LOGIC),
            "Button Triggering Client Side Logic",
        )
        is_element_displayed(client_side_page,
                             client_side_page.P_SUCCESSFULLY_CALCULATED)
