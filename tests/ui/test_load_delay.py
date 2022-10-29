from fixtures.browser import get_chrome as browser
from config import TEST_SITE_ROOT_URL
from steps.web_element_checks import is_element_displayed
from ui.pages.main import MainPage


class TestPageDelay:

    def test_page_delay(self, browser):
        browser.get(TEST_SITE_ROOT_URL)
        load_delay_page = MainPage(driver=browser).go_to_delay_page()
        is_element_displayed(load_delay_page,
                             load_delay_page.BUTTON_AFTER_DELAY)
