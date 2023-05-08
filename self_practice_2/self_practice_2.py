from Helper import Helper
from self_practice_2.PageObject import PageObject


class TestPracticeLesson(Helper):
    def __init__(self, driver):
        super().__init__(driver)

        self.elements = PageObject()

    def waiting_element_checkbox(self):
        self.waiting_element(self.elements.DM_CHECKBOX)

    def click_element_(self):
        self.click_radio_button(self.elements.DM_REMOVE_BUTTON)

    def waiting_element_message(self):
        self.waiting_element(self.elements.DM_MESSAGE)

    def present_text(self):
        self.ec_text_to_be_present_in_element(self.elements.DM_MESSAGE, "It's gone!")

    def waiting_(self):
        assert self.waiting_disappearance_element(self.elements.DM_CHECKBOX)
