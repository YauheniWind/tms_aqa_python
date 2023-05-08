import pytest

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def browser():
    driver = webdriver.Chrome(
        ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()
    )
    driver.implicitly_wait(1)

    yield driver

    driver.close()
    driver.quit()

def browser_make(request):
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    browser = request.config.getoption("--browser")
    if browser == 'chrome':
        driver = webdriver.Chrome(options=options)
        driver.implicitly_wait(5)
    else:
        driver = webdriver.Firefox()
        driver.implicitly_wait(5)

    yield driver

    driver.close()
    driver.quit()

@pytest.fixture()
def browser_firefox():
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    driver.implicitly_wait(1)

    yield driver

    driver.close()
    driver.quit()


@pytest.fixture()
def credentials():
    return {"login": "standard_user", "password": "secret_sauce"}

def pytest_addoption(parser):
    parser.addoption("--address", action="store", default="http://192.168.122.244/", help="HuntBox web address")
    parser.addoption("--browser", action="store", default="firefox", help="Browser name")

@pytest.fixture
def open_page(browser):
    browser.get("http://the-internet.herokuapp.com/dynamic_controls")