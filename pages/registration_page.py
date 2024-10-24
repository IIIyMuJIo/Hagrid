from selenium.webdriver.common.by import By
from base.base_page import BasePage


class RegistrationPage(BasePage):
    # Locators
    USERNAME_INPUT = (By.XPATH, "username")
    EMAIL_INPUT = (By.XPATH, "email")
    PASSWORD_INPUT = (By.XPATH, "password")
    CONFIRM_PASSWORD_INPUT = (By.XPATH, "confirm_password")
    SUBMIT_BUTTON = (By.XPATH, "button[type='submit']")
    SUCCESS_MESSAGE = (By.XPATH, ".success-message")
    EMAIL_CONFIRMATION_MESSAGE = (By.XPATH, ".email-confirmation")

    def fill_username(self, username):
        self.find_element(*self.USERNAME_INPUT).send_keys(username)

    def fill_email(self, email):
        self.find_element(*self.EMAIL_INPUT).send_keys(email)

    def fill_password(self, password):
        self.find_element(*self.PASSWORD_INPUT).send_keys(password)

    def fill_confirm_password(self, confirm_password):
        self.find_element(*self.CONFIRM_PASSWORD_INPUT).send_keys(confirm_password)

    def submit_registration(self):
        self.find_element(*self.SUBMIT_BUTTON).click()

    def get_success_message(self):
        return self.find_element(*self.SUCCESS_MESSAGE).text

    def get_email_confirmation_message(self):
        return self.find_element(*self.EMAIL_CONFIRMATION_MESSAGE).text
