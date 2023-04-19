import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_text_box():
    browser = webdriver.Chrome()
    browser.get("https://demoqa.com/text-box")
    time.sleep(1)

    full_name_xpath = '//*[@id="userName"]'
    email_xpath = '//*[@id="userEmail"]'
    current_address_xpath = '//*[@id="currentAddress"]'
    permanent_address_xpath = '//*[@id="permanentAddress"]'
    submit_xpath = '//*[@id="submit"]'

    full_name_locator = browser.find_element(By.XPATH, full_name_xpath)
    email_locator = browser.find_element(By.XPATH, email_xpath)
    current_address_locator = browser.find_element(By.XPATH, current_address_xpath)
    permanent_address_locator = browser.find_element(By.XPATH, permanent_address_xpath)
    submit_locator = browser.find_element(By.XPATH, submit_xpath)

    full_name_locator.send_keys("Ev Grav")
    email_locator.send_keys("adamnor938@gmail.com")
    current_address_locator.send_keys("Lomnicka 124")
    permanent_address_locator.send_keys("Novozamocaka 22")
    time.sleep(2)
    submit_locator.click()
    browser.quit()


def test_checkbox():
    browser = webdriver.Chrome()
    browser.get("https://demoqa.com/checkbox")

    menu_xpath = '//*[@id="tree-node"]/ol/li/span/button'
    menu_locator = browser.find_element(By.XPATH, menu_xpath)

    home_checkbox_xpath = '//*[@id="tree-node"]/ol/li/span/label/span[1]'
    home_checkbox_locator = browser.find_element(By.XPATH, home_checkbox_xpath)
    time.sleep(2)
    home_checkbox_locator.click()  # active checkbox
    menu_locator.click()  # open manu
    time.sleep(2)

    hidden_text_xpath = '//*[@id="result"]'
    hidden_text_locator = browser.find_element(By.XPATH, hidden_text_xpath)

    if hidden_text_locator:
        print("Passed")
    time.sleep(2)


def test_radio_button():
    browser = webdriver.Chrome()
    browser.get("https://demoqa.com/radio-button")

    radio_button_xpath = '//label[@for="yesRadio"]'
    radio_button_locator = browser.find_element(By.XPATH, radio_button_xpath)
    radio_button_text = radio_button_locator.text
    radio_button_locator.click()
    time.sleep(2)
    span_text_xpath = '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/p/span'
    span_text_locator_text = browser.find_element(By.XPATH, span_text_xpath).text
    assert radio_button_text == span_text_locator_text


def test_buttons():
    browser = webdriver.Chrome()
    browser.get("https://demoqa.com/buttons")
    action = webdriver.ActionChains(browser)

    double_click_button_xpath = '//button[@id="doubleClickBtn"]'
    double_click_button_locator = browser.find_element(
        By.XPATH, double_click_button_xpath
    )
    action.double_click(double_click_button_locator).perform()
    time.sleep(5)

    right_click_button_xpath = '//button[@id="rightClickBtn"]'
    right_click_button_locator = browser.find_element(
        By.XPATH, right_click_button_xpath
    )
    action.context_click(right_click_button_locator).perform()
    time.sleep(2)
