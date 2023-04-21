from selenium.webdriver.common.by import By


def test_basket(browser):
    browser.get("https://www.istores.sk")

    logo_xpath = '//*[@id="basketcont"]'
    logo_locator = browser.find_element(By.XPATH, logo_xpath)

    logo_locator.click()

    current_url = browser.current_url

    assert current_url == "https://www.istores.sk/nakupni-kosik.html#step_1"


def test_basket_firefox(browser_firefox):
    browser_firefox.get("https://www.istores.sk")

    browser_firefox.fullscreen_window()
    logo_xpath = '//*[@id="basketcont"]'
    logo_locator = browser_firefox.find_element(By.XPATH, logo_xpath)

    logo_locator.click()

    current_url = browser_firefox.current_url

    assert current_url == "https://www.istores.sk/nakupni-kosik.html#step_1"

    browser_firefox.close()


def test_cookes(browser):
    browser.get("https://www.istores.sk")

    browser.fullscreen_window()

    browser.add_cookie({"name": "_fbp", "value": "fb.1.1680774700810.2092010717"})
    browser.delete_cookie("_fbp")
    browser.delete_all_cookies()


def test_js(browser):
    browser.get("https://www.istores.sk")

    browser.execute_script("document.getElementById('cookieUseAgreement').style.display = 'none'")

    # footer_xpath = (By.XPATH, '//*[@id="footercont"]/footer/div[6]')
    # footer_locator = driver.find_element(*footer_xpath)
    #
    # driver.execute_script("arguments[0].scrollIntoView();", footer_locator)
    # footer_locator.click()

    # current_url = driver.current_url


def test_checks_elements(browser):
    browser.get(
        "https://teachmeskills.by/kursy-programmirovaniya/qa-avtomatizirovannoe-testirovanie-na-python-online"
    )

    selector = browser.find_element(By.CLASS_NAME, 't517__innercol')
    selectors = browser.find_elements(By.CLASS_NAME, 't517__innercol')
    print(selectors)
    browser.execute_script("arguments[0].scrollIntoView();", selector)
    assert selector.is_displayed()
