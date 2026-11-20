from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class LoginPage:
    LOGIN_LINK = (By.LINK_TEXT, "Log in")
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[name='username']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[name='password']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Log out']")
    LOGIN_SUCCESS_MESSAGE = (
        By.XPATH,
        "//h3[normalize-space()='You are logged in success']"
    )

    OK_BUTTON = (
        By.CSS_SELECTOR,
        "[role='dialog'] .modal-content a[href='/search']"
    )

    def __init__(self, driver):
        self.driver = driver

    def open_login_page(self):
        self.driver.find_element(*self.LOGIN_LINK).click()

    def fill_email_field(self, email):
        field = self.driver.find_element(*self.EMAIL_INPUT)
        field.clear()
        field.send_keys(email)

    def fill_password_field(self, password):
        field = self.driver.find_element(*self.PASSWORD_INPUT)
        field.clear()
        field.send_keys(password)

    def click_on_login_button(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def is_email_invalid(self):
        invalid_email = (By.CSS_SELECTOR, "input[name='username']:invalid")
        return bool(self.driver.find_elements(*invalid_email))

    def is_logout_present(self):
        return bool(self.driver.find_elements(*self.LOGOUT_BUTTON))

    def confirm_successful_login(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                self.LOGIN_SUCCESS_MESSAGE
            )
        )

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                self.OK_BUTTON
            )
        ).click()

        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located(
                (By.CSS_SELECTOR, "[role='dialog']")
            )
        )

        WebDriverWait(self.driver, 10).until(
            EC.url_contains("/search")
        )