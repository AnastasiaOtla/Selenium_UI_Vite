import time

from pages.login_page import LoginPage


def test_go_to_login(browser):
    link = 'http://34.141.58.52:8080/#/login'
    page = LoginPage(browser, link)
    page.open()
    page.go_to_login()
    page.go_to_pass()
    page.click_to_login_btn()
    time.sleep(2)
    browser.save_screenshot('login_screen.png')
