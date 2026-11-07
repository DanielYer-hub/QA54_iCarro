from selenium.webdriver.common.by import By


class LoginPage:
    LOGIN_LINK = (By.LINK_TEXT, "Log in")
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[name='username']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[name='password']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Log out']")

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