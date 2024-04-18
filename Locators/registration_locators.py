from selenium.webdriver.common.by import By
from conftest import DriverSetUp

driver = DriverSetUp.driver


# Per Page Locators - can be placed under one class
# Locators can also be placed under function


def firstname_error():
    firstname_error_text = driver.find_element(By.XPATH, "//*[@id='firstname-error']")
    return firstname_error_text


def lastname_error():
    lastname_error_text = driver.find_element(By.XPATH, "//*[@id='lastname-error']")
    return lastname_error_text


def email_error():
    email_error_text = driver.find_element(By.XPATH, "//*[@id='email_address-error']")
    return email_error_text


def password_error():
    password_error_text = driver.find_element(By.XPATH, "//*[@id='password-error']")
    return password_error_text


def confirm_password_error():
    confirm_password_error_text = driver.find_element(By.XPATH, "//*[@id='password-confirmation-error']")
    return confirm_password_error_text


def password_validation_error():
    password_validation_error_text = driver.find_element(By.XPATH, "//*[@id='password-error']")
    return password_validation_error_text


def account_button():
    create_account_button = driver.find_element(By.XPATH, "//*[@id='form-validate']/div/div[1]/button")
    return create_account_button


# class RegistrationErrorLocators:
#     firstname_error_text = driver.find_element(By.XPATH, "//*[@id='firstname-error']")
#     lastname_error_text = driver.find_element(By.XPATH, "//*[@id='lastname-error']")
#     email_error_text = driver.find_element(By.XPATH, "//*[@id='email_address-error']")
#     password_error_text = driver.find_element(By.XPATH, "//*[@id='password-error']")
#     confirm_password_error_text = driver.find_element(By.XPATH, "//*[@id='password-confirmation-error']")


class RegistrationLocators:
    firstname_text = driver.find_element(By.XPATH, "//*[@id='firstname']")
    lastname_text = driver.find_element(By.ID, "lastname")
    email_text = driver.find_element(By.XPATH, "//*[@id='email_address']")
    password_text = driver.find_element(By.XPATH, "//*[@id='password']")
    confirm_password_text = driver.find_element(By.XPATH, "//*[@id='password-confirmation']")
