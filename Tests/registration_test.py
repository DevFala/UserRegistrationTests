from Actions.registration_actions import click_create_account_button
from Locators.registration_locators import (RegistrationLocators, password_validation_error, password_error,
                                            firstname_error, lastname_error, email_error, confirm_password_error)

registration_locator = RegistrationLocators()
expected_error_value = "This is a required field."
expected_password_validation_error_value = ("Minimum of different classes of characters in password is 3. Classes of "
                                            "characters: Lower Case, Upper Case, Digits, Special Characters.")


# Function to run the test case
def register_without_firstname_lastname():
    registration_locator.password_text.send_keys("Test password")
    registration_locator.confirm_password_text.send_keys("Test password")
    registration_locator.email_text.send_keys("someemail@gmai.com")
    click_create_account_button()

    firstname_error_value = firstname_error()
    lastname_error_value = lastname_error()

    assert expected_error_value in firstname_error_value and expected_error_value not in lastname_error_value


# Function to run the test case
def register_without_confirm_password():
    registration_locator.firstname_text.send_keys("test")
    registration_locator.lastname_text.send_keys("last name value")
    registration_locator.password_text.send_keys("Test password")
    registration_locator.email_text.send_keys("someemail@gmai.com")
    click_create_account_button()

    confirm_password_value = confirm_password_error()

    assert expected_error_value in confirm_password_value


# Function to run the test case
def register_without_email():
    registration_locator.firstname_text.send_keys("test")
    registration_locator.lastname_text.send_keys("last name value")
    registration_locator.password_text.send_keys("Test password")
    registration_locator.confirm_password_text.send_keys("Test password")
    click_create_account_button()

    email_value = email_error()

    assert expected_error_value in email_value


# Function to run the test case
def input_invalid_password():
    registration_locator.password_text.send_keys("test")

    actual_error_value = password_validation_error()
    assert expected_error_value in actual_error_value
