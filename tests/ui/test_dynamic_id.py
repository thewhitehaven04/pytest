from config import TEST_SITE_ROOT_URL
from fixtures.browser import get_chrome as browser
from ui.pages.main import MainPage


class TestsDynamicId:

    def test_click_on_dynamic_id(self, browser) -> None:
        browser.get(TEST_SITE_ROOT_URL)

        dynamic_page = MainPage(driver=browser).go_to_dynamic_id_page()
        dynamic_page.click(dynamic_page.DYNAMIC_ID_BUTTON)
