from Locators import registration_locators

registration_locator = registration_locators.account_button()


def click_create_account_button():
    registration_locator.submit_button.click()
