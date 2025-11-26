import pytest
from pages.sale_page import SalePage
from pages.login_page import LoginPage
from playwright.sync_api import BrowserContext
from selenium import webdriver
from time import sleep


# @pytest.fixture()
# def page(context: BrowserContext, playwright):
#     playwright.selectors.set_test_id_attribute("id")
#     page = context.new_page()
#     page.set_viewport_size({'width': 1920, 'height': 1080})
#     return page

@pytest.fixture()
def sale_page(page):
    return SalePage(page)

@pytest.fixture()
def login_page(page):
    return LoginPage(page)







