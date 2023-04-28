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

        helper.click_radio_button(ElementsObject.radio_button)
        radio_button_text = helper.get_text(ElementsObject.radio_button)

        span_text = helper.get_text(ElementsObject.span_text)
        browser.save_screenshot("test_1.png")
        assert radio_button_text == span_text

    def test_checkbox(self, browser):
        helper = Helper(browser)
        helper.driver.get("https://demoqa.com/checkbox")

        helper.select_checkbox(ElementsObject.home_checkbox, True) # open manu
        helper.select_checkbox(ElementsObject.arrow_button, True) # click on arrow
        helper.select_checkbox(ElementsObject.desktop_checkbox, True) #uncheck desktop
        hidden_text_locator = helper.get_locator_by_xpath(ElementsObject.result_text)
        browser.save_screenshot("test_2.png")
        assert hidden_text_locator.is_displayed()

    def test_scroll(self, browser):
        helper = Helper(browser)
        helper.driver.get("https://demoqa.com/elements")
        helper.driver.fullscreen_window()

        footer = helper.get_locator_by_xpath(ElementsObject.scroll_footer)
        helper.remove_element_from_DOM(footer)

        scroll_to_interactions = helper.get_locator_by_xpath(ElementsObject.scroll)
        helper.scroll_to_element(scroll_to_interactions)

        browser.save_screenshot("test_3.png")
        assert scroll_to_interactions.is_displayed()

    def test_select_value_from_dropdown(self, browser):
        helper = Helper(browser)
        helper.driver.get("https://demoqa.com/select-menu")
        helper.driver.fullscreen_window()

        helper.select_value_from_dropdown(ElementsObject.select_one)
        helper.select_value_from_dropdown(ElementsObject.dr_select)

        select_one_text = helper.get_text(ElementsObject.select_one_text)

        browser.save_screenshot("test_4.png")
        assert select_one_text == "Dr."

    def test_input_text(self, browser):
        helper = Helper(browser)
        helper.driver.get("https://demoqa.com/text-box")
        helper.driver.fullscreen_window()

        input_text = helper.enter_text_and_get_attribute_value(ElementsObject.input_full_name, "Hello")

        helper.get_attribute_(ElementsObject.input_full_name, "value")
        helper.get_attribute_(ElementsObject.input_full_name, "class")

        browser.save_screenshot("test_5.png")
        assert input_text == "Hello"
