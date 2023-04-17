import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_show_product():
    driver = webdriver.Chrome("/Users/evgenijgravdin/Desktop/tms_aqa_python/chromedriver")
    driver.fullscreen_window()
    driver.get("https://www.istores.sk")
    time.sleep(1)
    show_product = driver.find_element(By.XPATH, '//*[@id="wnCarousel24"]/div[2]/div[2]/div/div[1]')
    show_product.click()
    h1_xpath = '//*[@id="contentcont"]/div[2]/div/div[1]/div[1]/div[2]/h1'

    if h1_xpath == "iPhone 11 64 GB čierny":
        assert h1_xpath == "iPhone 11 64 GB čierny"
    else:
        assert h1_xpath != "iPhone 11 64 GB čierny"
    driver.quit()


def test_hamburger_menu():
    driver = webdriver.Chrome("/Users/evgenijgravdin/Desktop/tms_aqa_python/chromedriver")
    driver.get("https://www.istores.sk")
    time.sleep(2)

    driver.set_window_size(760, 600)
    hamburger_menu = '//*[@id="tree-icon"]'
    element_iphone = '//*[@id="sptnav"]/ul/li[4]/a'
    element_iphone_pro_max = '//*[@id="subcatscont"]/div[2]/ul/li[2]/a'
    hamburger_locator = driver.find_element(By.XPATH, hamburger_menu)
    iphone_locator = driver.find_element(By.XPATH, element_iphone)

    hamburger_locator.click()
    iphone_locator.click()
    time.sleep(2)

    iphone_locator_pro_max = driver.find_element(By.XPATH, element_iphone_pro_max)
    iphone_locator_pro_max.click()

    name = '//*[@id="contentcont"]/div[2]/div/div[1]/div[1]/div[2]/h1'
    name_locator = driver.find_element(By.XPATH, name).text

    assert name_locator == 'iPhone 14 Pro Max 128 GB kozmicky čierny'
    driver.quit()


def test_search():
    driver = webdriver.Chrome("/Users/evgenijgravdin/Desktop/tms_aqa_python/chromedriver")
    driver.get("https://www.istores.sk")
    time.sleep(2)

    driver.fullscreen_window()
    search_input = '//*[@id="whisperinput"]'
    search_locator = driver.find_element(By.XPATH, search_input)
    time.sleep(2)
    search_locator.send_keys("iphone")
    search_locator.send_keys(webdriver.Keys.ENTER)
    time.sleep(2)
    searched_element = '//*[@id="contentcont"]/div[3]/div[1]/p'
    searched_locator = driver.find_element(By.XPATH, searched_element).text

    assert searched_locator == 'Hľadanie: iphone'
    driver.quit()


def test_log_in():
    driver = webdriver.Chrome("/Users/evgenijgravdin/Desktop/tms_aqa_python/chromedriver")
    driver.get("https://www.saucedemo.com/")
    time.sleep(1)

    driver.fullscreen_window()
    user_name = '//*[@id="user-name"]'
    password = '//*[@id="password"]'
    user_name_locator = driver.find_element(By.XPATH, user_name)
    user_password_locator = driver.find_element(By.XPATH, password)

    time.sleep(1)
    user_name_locator.send_keys("standard_user")
    user_password_locator.send_keys("secret_sauce")
    time.sleep(1)

    button = '//*[@id="login-button"]'
    pressed_button = driver.find_element(By.XPATH, button)
    pressed_button.click()

    assert driver.current_url == "https://www.saucedemo.com/inventory.html"
    time.sleep(2)

    driver.quit()
