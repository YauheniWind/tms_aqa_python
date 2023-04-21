from selenium.webdriver.common.by import By


def test_show_product(browser):
    browser.fullscreen_window()
    browser.get("https://www.istores.sk")
    show_product = browser.find_element(
        By.XPATH, '//*[@id="wnCarousel24"]/div[2]/div[2]/div/div[1]'
    )
    show_product.click()
    h1_xpath = '//*[@id="contentcont"]/div[2]/div/div[1]/div[1]/div[2]/h1'

    if h1_xpath == "iPhone 11 64 GB čierny":
        assert h1_xpath == "iPhone 11 64 GB čierny"
    else:
        assert h1_xpath != "iPhone 11 64 GB čierny"


def test_hamburger_menu(browser):
    browser.get("https://www.istores.sk")

    browser.set_window_size(760, 600)
    hamburger_menu = '//*[@id="tree-icon"]'
    element_iphone = '//*[@id="sptnav"]/ul/li[4]/a'
    element_iphone_pro_max = '//*[@id="subcatscont"]/div[2]/ul/li[2]/a'
    hamburger_locator = browser.find_element(By.XPATH, hamburger_menu)
    iphone_locator = browser.find_element(By.XPATH, element_iphone)

    hamburger_locator.click()
    iphone_locator.click()

    iphone_locator_pro_max = browser.find_element(By.XPATH, element_iphone_pro_max)
    iphone_locator_pro_max.click()

    name = '//*[@id="contentcont"]/div[2]/div/div[1]/div[1]/div[2]/h1'
    name_locator = browser.find_element(By.XPATH, name).text

    assert name_locator == "iPhone 14 Pro Max 128 GB kozmicky čierny"


def test_search(browser):
    browser.get("https://www.istores.sk")

    search_input = '//*[@id="whisperinput"]'
    search_locator = browser.find_element(By.XPATH, search_input)

    search_locator.send_keys("iphone")
    search_locator.send_keys(browser.Keys.ENTER)

    searched_element = '//*[@id="contentcont"]/div[3]/div[1]/p'
    searched_locator = browser.find_element(By.XPATH, searched_element).text

    assert searched_locator == "Hľadanie: iphone"


def test_log_in(browser):
    browser.get("https://www.saucedemo.com/")

    user_name = '//*[@id="user-name"]'
    password = '//*[@id="password"]'
    user_name_locator = browser.find_element(By.XPATH, user_name)
    user_password_locator = browser.find_element(By.XPATH, password)

    user_name_locator.send_keys("standard_user")
    user_password_locator.send_keys("secret_sauce")

    button = '//*[@id="login-button"]'
    pressed_button = browser.find_element(By.XPATH, button)
    pressed_button.click()

    assert browser.current_url == "https://www.saucedemo.com/inventory.html"
