from playwright.sync_api import expect
from pages.locators import login_locators as loc
from pages.base_page import BasePage

ERROR_MESSAGE = '[data-test="error"]'

class LoginPage(BasePage):

    page_url = '/v1/'

    def fill_login_form(self, login, password):
        email_field = self.find(loc.email_field_loc)
        password_field = self.find(loc.password_field_loc)
        button = self.find(loc.button_loc)
        email_field.fill(login)
        password_field.fill(password)
        button.click()

    def check_error_alert(self, text):
        expect(self.find(ERROR_MESSAGE)).to_have_text(text)
