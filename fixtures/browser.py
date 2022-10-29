import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture(scope="function", params=["chrome", "firefox"])
def browser_factory(request):
    if request.param == "chrome":
        browser = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()))

    elif request.param == "firefox":
        browser = webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install()))
    else:
        raise ValueError(f"This browser {browser_name} is not supported")

    yield browser
    browser.quit()


@pytest.fixture(scope="function")
def get_chrome():
    browser = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()))
    yield browser
    browser.quit()