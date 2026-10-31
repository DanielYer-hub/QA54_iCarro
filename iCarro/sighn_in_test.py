import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from config import EMAIL, PASSWORD

URL = "https://icarro-v1.netlify.app/search?page=0&size=10"

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get(URL)
    yield driver
    driver.quit()

class TestLogin:
    def test_login_success(self, driver):
        driver.find_element(By.LINK_TEXT, "Log in").click()
        driver.find_element(By.CSS_SELECTOR, "[name='username']").send_keys(EMAIL)
        driver.find_element(By.CSS_SELECTOR, "[name='password']").send_keys(PASSWORD)
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        logout_button = driver.find_element(By.XPATH, "//button[text()='Log out']")
        assert logout_button.is_displayed()