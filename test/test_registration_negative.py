import uuid

from models.user import User
from pages.registration_page import RegistrationPage


def test_registration_with_empty_first_name(driver):
    registration_page = RegistrationPage(driver)

    user = User(
        first_name="",
        last_name="TestUser",
        email=f"test{uuid.uuid4().hex[:8]}@gmail.com",
        password="Aa_12345!"
    )

    registration_page.open_registration_page()
    registration_page.fill_registration_form(user)

    actual_error = registration_page.get_error_message(
        registration_page.FIRST_NAME_ERROR
    )

    assert actual_error == "Name is required", (
        f"Expected 'Name is required', got '{actual_error}'"
    )


def test_registration_with_empty_last_name(driver):
    registration_page = RegistrationPage(driver)

    user = User(
        first_name="TestUser",
        last_name="",
        email=f"test{uuid.uuid4().hex[:8]}@gmail.com",
        password="Aa_12345!"
    )

    registration_page.open_registration_page()
    registration_page.fill_registration_form(user)

    actual_error = registration_page.get_error_message(
        registration_page.LAST_NAME_ERROR
    )

    assert actual_error == "Last name is required", (
        f"Expected 'Last name is required', got '{actual_error}'"
    )


def test_registration_with_empty_email(driver):
    registration_page = RegistrationPage(driver)

    user = User(
        first_name="TestUser",
        last_name="TestUser",
        email="",
        password="Aa_12345!"
    )

    registration_page.open_registration_page()
    registration_page.fill_registration_form(user)

    actual_error = registration_page.get_error_message(
        registration_page.EMAIL_ERROR
    )

    assert actual_error == "Email is required", (
        f"Expected 'Email is required', got '{actual_error}'"
    )


def test_registration_with_empty_password(driver):
    registration_page = RegistrationPage(driver)

    user = User(
        first_name="TestUser",
        last_name="TestUser",
        email=f"test{uuid.uuid4().hex[:8]}@gmail.com",
        password=""
    )

    registration_page.open_registration_page()
    registration_page.fill_registration_form(user)

    actual_error = registration_page.get_error_message(
        registration_page.PASSWORD_ERROR
    )

    assert actual_error == "Password is required", (
        f"Expected 'Password is required', got '{actual_error}'"
    )
