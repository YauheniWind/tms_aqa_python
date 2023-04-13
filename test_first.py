from selenium import webdriver
from selenium.webdriver.common.by import By


def test_basket():
    driver = webdriver.Chrome("/Users/evgenijgravdin/Desktop/tms_aqa_python/chromedriver")
    driver.get("https://www.istores.sk")

    driver.fullscreen_window()
    logo_xpath = '//*[@id="basketcont"]'
    logo_locator = driver.find_element(By.XPATH, logo_xpath)

    logo_locator.click()

    current_url = driver.current_url

    assert current_url == "https://www.istores.sk/nakupni-kosik.html#step_1"
