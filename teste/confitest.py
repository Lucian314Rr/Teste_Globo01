import pytest

from LoginPag.LoginPage import LoginPage


def pytest_addoption(parser):
    parser.addoption('--browser', default='chrome', help='Browser test')


@pytest.fixture()
def browser(request):
    select_browser = request.config.getoption('browser').lower()
    if select_browser not in ['chrome', 'firefox', 'safari']:
        select_browser = 'chrome'
    return select_browser


@pytest.fixture()
def setup_login_page(browser):
    login_page = LoginPage(browser=browser)
    yield login_page
    login_page.close()


@pytest.fixture()
def login_site_firefox():
    login_page = LoginPage(browser='firefox')
    login_page.efetuar_login()
    yield login_page
    login_page.close()


@pytest.fixture()
def login_site(browser):
    login_page = LoginPage(browser=browser)
    login_page.efetuar_login()
    yield login_page
    login_page.close()
