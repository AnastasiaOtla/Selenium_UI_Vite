from .base_page import BasePage
from .locators import LoginPageLocators
from .input_data import AuthorizationInput


class LoginPage(BasePage):
    def go_to_login(self):
        login_email = self.browser.find_element(*LoginPageLocators.LOGIN_EMAIL)
        login_email.send_keys(AuthorizationInput.email_valid)

    def go_to_pass(self):
        login_pass = self.browser.find_element(*LoginPageLocators.LOGIN_PASS)
        login_pass.send_keys(AuthorizationInput.pass_valid)

    def click_pass_title(self):  # action to make possible to call def click_to_login_btn
        pass_title = self.browser.find_element(*LoginPageLocators.PASS_TITLE)
        pass_title.click()

    def click_to_login_btn(self):
        login_btn = self.browser.find_element(*LoginPageLocators.LOGIN_BTN)
        login_btn.submit()
