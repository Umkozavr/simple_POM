from playwright.sync_api import expect
from pages.base_page import BasePage

head_loc = 'product_label'


class SalePage(BasePage):
    page_url = '/v1/inventory.html'

    def check_header_title(self, text):
        expect(self.find(head_loc)).to_have_text(text)