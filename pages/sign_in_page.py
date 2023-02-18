from selenium.webdriver.common.by import By
from pages.base_page import Page


class SignIn(Page):
    EMAIL_FIELD = (By.ID, 'user_email')
    PASSWORD_FIELD = (By.ID, 'user_password')
    SIGN_IN = (By.CSS_SELECTOR, "input[value='Sign in']")

    def open_sign_in_page(self):
        self.open_page('https://qa-test.avenuecode.io/users/sign_in')

    def enter_email(self):
        self.input_text('romanwork24@gmail.com', *self.EMAIL_FIELD)

    def enter_password(self):
        self.input_text('assessmentqa', *self.PASSWORD_FIELD)

    def sign_in(self):
        self.click(*self.SIGN_IN)