from config import EMAIL, PASSWORD
from pages.login_page import LoginPage


class TestLoginNegative:

    def test_login_with_wrong_password(self, driver):
        login_page = LoginPage(driver)
        login_page.open_login_page()
        login_page.fill_email_field(EMAIL)
        login_page.fill_password_field(PASSWORD + "9")
        login_page.click_on_login_button()

        assert not login_page.is_logout_present(), (
            "sign in with incorrect password"
        )

    def test_login_with_empty_password(self, driver):
        login_page = LoginPage(driver)
        login_page.open_login_page()
        login_page.fill_email_field(EMAIL)
        login_page.fill_password_field("")
        login_page.click_on_login_button()

        assert not login_page.is_logout_present(), (
            "sign in with empty password"
        )

    def test_login_with_invalid_email_format(self, driver):
        login_page = LoginPage(driver)
        login_page.open_login_page()
        login_page.fill_email_field("student.example.com")
        login_page.fill_password_field(PASSWORD)
        login_page.click_on_login_button()

        assert login_page.is_email_invalid(), (
            "brouser not declined incorrect email"
        )