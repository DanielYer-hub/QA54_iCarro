import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    browser.maximize_window()

    browser.get(
        "https://icarro-v1.netlify.app/search?page=0&size=10"
    )

    yield browser

    browser.quit()