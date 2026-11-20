import pytest
from selenium import webdriver
from config import EMAIL, PASSWORD
from pages.login_page import LoginPage
from selenium.webdriver.support.ui import WebDriverWait

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

@pytest.fixture
def authenticated(driver):
    login_page = LoginPage(driver)

    login_page.open_login_page()
    login_page.fill_email_field(EMAIL)
    login_page.fill_password_field(PASSWORD)
    login_page.click_on_login_button()

    login_page.confirm_successful_login()

    return driver