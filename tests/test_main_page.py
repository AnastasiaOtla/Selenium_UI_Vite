import time
import pytest
from pages.main_page import MainPage
from tests.test_login_page import test_go_to_login


@pytest.mark.smoke
def test_go_to_login_page(browser):
    link = 'http://34.141.58.52:8080/#/'
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    browser.save_screenshot('login_screen.png')


@pytest.mark.regression
def test_go_to_filter_by_dog(browser):
    link = 'http://34.141.58.52:8080/#/'
    page = MainPage(browser, link)
    page.open()
    page.go_to_filter_by_type()
    page.go_to_filter_by_dog()
    time.sleep(2)
    browser.save_screenshot('filter_screen.png')


@pytest.mark.regression
def test_go_to_filter_by_pet_name(browser):
    link = 'http://34.141.58.52:8080/#/'
    page = MainPage(browser, link)
    page.open()
    page.go_to_filter_by_pet_name()
    time.sleep(2)
    browser.save_screenshot('filter_pet_name.png')


@pytest.mark.skip
def test_go_to_next_page(browser):
    link = 'http://34.141.58.52:8080/#/'
    page = MainPage(browser, link)
    page.open()
    page.go_to_next_page()
    time.sleep(2)
    browser.save_screenshot('next_page.png')


@pytest.mark.smoke()
def test_go_to_pet_details(browser):
    link = 'http://34.141.58.52:8080/#/'
    page = MainPage(browser, link)
    page.open()
    page.go_to_filter_by_pet_name()
    page.go_to_pet_details()
    time.sleep(3)
    browser.save_screenshot('pet_details.png')


@pytest.mark.skip()
def test_go_to_profile_page(browser):
    test_go_to_login(browser)
    link = 'http://34.141.58.52:8080/#/'
    page = MainPage(browser, link)
    page.open()
    page.go_to_profile_page()
    browser.save_screenshot('profile_page.png')
