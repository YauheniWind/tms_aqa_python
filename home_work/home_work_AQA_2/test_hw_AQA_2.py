from selenium.webdriver.common.action_chains import ActionChains
from Helper import Helper
from ElementsObject import ElementsObject


class TestBBC:
    "#homepage-link > svg"
    '//*[@id="u8829042875479214"]//div[2]/div/div/img'

    '//*[@id="orb-header"]/div/nav[2]/ul/li[3]'  # locator
    '//*[@id="orb-header"]/div/nav[2]/ul/li[3]/a/span'  # text
    ".nw-o-news-wide-navigation > nav > ul > li:nth-of-type(odd)"


class TestElements:
    # check radio button
    def test_radio_button(self, browser):
        helper = Helper(browser)
        helper.driver.get("https://demoqa.com/radio-button")

        radio_button_locator = helper.get_locator_by_xpath(ElementsObject.radio_button)
        radio_button_text = radio_button_locator.text

        radio_button_locator.click()

        span_text_locator_text = helper.get_locator_by_css(
            ElementsObject.span_text
        ).text
        browser.save_screenshot(f"test_1.png")
        assert radio_button_text == span_text_locator_text

    def test_checkbox(self, browser):
        helper = Helper(browser)
        helper.driver.get("https://demoqa.com/checkbox")

        menu_locator = helper.get_locator_by_css(ElementsObject.menu)

        home_checkbox_locator = helper.get_locator_by_xpath(
            ElementsObject.home_checkbox
        )
        home_checkbox_locator.click()  # active checkbox
        menu_locator.click()  # open manu

        desktop_checkbox = helper.get_locator_by_css(ElementsObject.desktop_checkbox)
        desktop_checkbox.click()  # uncheck desktop

        hidden_text_locator = helper.get_locator_by_xpath(ElementsObject.result_text)

        browser.save_screenshot(f"test_2.png")
        assert hidden_text_locator.is_displayed()

    def test_scroll(self, browser):
        helper = Helper(browser)
        helper.driver.get("https://demoqa.com/elements")
        helper.driver.fullscreen_window()

        footer = helper.get_locator_by_xpath(ElementsObject.scroll_footer)
        helper.driver.execute_script("arguments[0].remove();", footer)

        scroll_to_interactions = helper.get_locator_by_xpath(ElementsObject.scroll)
        ActionChains(browser).scroll_to_element(scroll_to_interactions).perform()

        browser.save_screenshot(f"test_3.png")
        assert scroll_to_interactions.is_displayed()

    def test_select_value_from_dropdown(self, browser):
        helper = Helper(browser)
        helper.driver.get("https://demoqa.com/select-menu")
        helper.driver.fullscreen_window()

        select_one = helper.get_locator_by_xpath(ElementsObject.select_one)
        select_one.click()

        dr_select = helper.get_locator_by_xpath(ElementsObject.dr_select)
        dr_select.click()

        select_one_text = helper.get_locator_by_css(ElementsObject.select_one_text).text

        browser.save_screenshot(f"test_4.png")
        assert select_one_text == "Dr."

    def test_input_text(self, browser):
        helper = Helper(browser)
        helper.driver.get("https://demoqa.com/text-box")
        helper.driver.fullscreen_window()

        input_text = helper.get_locator_by_css(ElementsObject.input_full_name)
        input_text.send_keys("Hello")
        attr_type = input_text.get_attribute("value")
        attr_class = input_text.get_attribute("class")
        print(attr_class)

        browser.save_screenshot(f"test_5.png")
        assert attr_type == "Hello"
