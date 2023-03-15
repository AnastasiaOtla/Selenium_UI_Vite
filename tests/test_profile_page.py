import time
import pytest
from pages.profile_page import ProfilePage
from tests.test_login_page import test_go_to_login


@pytest.mark.smoke
@pytest.mark.regression
def test_go_to_quit_button(browser):
    test_go_to_login(browser)
    link = 'http://34.141.58.52:8080/#/profile'
    page = ProfilePage(browser, link)
    page.open()
    page.go_to_quit_button()
    browser.save_screenshot('quit_btn_screen.png')


@pytest.mark.regression
def test_go_to_edit_pet_profile(browser):
    test_go_to_login(browser)
    link = 'http://34.141.58.52:8080/#/profile'
    page = ProfilePage(browser, link)
    page.open()
    page.go_to_edit_pet_profile()
    browser.save_screenshot('edit_profile_screen.png')


@pytest.mark.smoke
@pytest.mark.regression
def test_go_to_add_pet(browser):
    test_go_to_login(browser)
    link = 'http://34.141.58.52:8080/#/profile'
    page = ProfilePage(browser, link)
    page.open()
    page.go_to_add_pet_btn()
    page.go_to_add_new_name()
    page.go_to_add_new_age()
    page.choose_new_pet_type()
    page.choose_new_pet_type_dog()
    page.choose_new_pet_gender()
    page.choose_new_pet_gender_male()
    page.go_to_submit_add_pet_btn()
    page.open()
    time.sleep(2)
    browser.save_screenshot('add_pet_screen.png')
