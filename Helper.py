from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

class Helper:

    def __init__(self, driver):
        self.driver = driver

    def get_locator_by_xpath(self, selector):
        # '//*[@id="userName"]'
        xpath = (By.XPATH, selector)
        return self.driver.find_element(*xpath)

    def get_locator_by_css(self, selector):
        # .class_name
        css = (By.CSS_SELECTOR, selector)
        return self.driver.find_element(*css)

    def get_locator_by_id(self, selector):
        id = (By.ID, selector)
        return self.driver.find_element(*id)

    def get_locator_by_class_name(self, selector):
        # class_name
        class_name = (By.CLASS_NAME, selector)
        return self.driver.find_element(*class_name)

    def get_locator_by_contains(self, selector):
        xpath = (By.XPATH, f'//div[contains(@class,"{selector}")]')
        return self.driver.find_element(*xpath)

    def get_locator_by_contains_text(self, text):
        xpath = (By.XPATH, f'//*[contains(text(),"{text}")]')
        return self.driver.find_element(*xpath)

    def click_element(self, locator):
        selector = self.wait_for_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView", selector)
        selector.click()

    def wait_for_element(self, selector):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, selector)))

    def assert_that_element_is_selected(self, selector):
        return self.get_locator_by_css(selector).is_selected()

    def scroll_to_element(self,locator):
        return ActionChains(self.driver).scroll_to_element(locator).perform()

    def remove_element_from_DOM(self, locator):
        return self.driver.execute_script("arguments[0].remove();", locator)

    def select_value_from_dropdown(self, value):
        element = self.get_locator_by_xpath(value)
        element.click()

    def select_checkbox(self, locator, value=True):
        element = self.get_locator_by_xpath(locator)
        current_check = element.is_selected()
        if current_check != value:
            element.click()

    def click_radio_button(self, locator):
        element = self.get_locator_by_xpath(locator)
        element.click()

    def switch_to_iframe(self, locator):
        return self.driver.switch_to.frame(self.driver.find_element(By.XPATH, locator))

    def get_text(self, locator):
        return self.get_locator_by_xpath(locator).text

    def enter_text_and_get_attribute_value(self, locator, text):
        element = self.get_locator_by_xpath(locator)
        element.send_keys(text)
        entered_text = element.get_attribute("value")

        return entered_text

    def get_attribute_(self, locator, value):
        element = self.get_locator_by_xpath(locator)
        if value == "class":
            return element.get_attribute("class")
        else:
            return element.get_attribute("value")

    def waiting_element(self, locator):
        return WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, locator))
            )

    def waiting_disappearance_element(self, locator):
        return WebDriverWait(self.driver, 10).until_not(
            EC.presence_of_element_located((By.XPATH, locator))
        )

    def element_is_enabled(self, locator):
        element = self.get_locator_by_xpath(locator)
        if element.is_enabled():
            return True
        return False

    def ec_text_to_be_present_in_element(self, element, text):
        return EC.text_to_be_present_in_element(element, text)