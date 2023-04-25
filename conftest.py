import pytest

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture
def browser():
    driver = webdriver.Chrome(
        ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()
    )
    driver.implicitly_wait(1)

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
