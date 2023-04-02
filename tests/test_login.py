import pytest
from pages.login import LoginPage
from utils.helpers import get_config_value
from logger import Logger

logger = Logger('test.log')


@pytest.fixture(scope="module")
def login_page(request):
    login_page = LoginPage()
    yield login_page
    if request.node.rep_call.failed:
        login_page.capture_screenshot("login_failure")

def test_login_with_valid_credentials(login_page):
    logger.info('Starting test_login_with_valid_credentials...')
    username = get_config_value("valid_username")
    password = get_config_value("valid_password")
    login_page.login(username, password)
    assert login_page.is_logged_in() == True

def test_login_with_invalid_credentials(login_page):
    logger.info('Starting test_login_with_invalid_credentials...')
    username = get_config_value("invalid_username")
    password = get_config_value("invalid_password")
    login_page.login(username, password)
    assert login_page.is_logged_in() == False



