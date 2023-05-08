from self_practice_2.self_practice_2 import TestPracticeLesson


def test_checkbox(browser, open_page):
    tpl = TestPracticeLesson(browser)

    tpl.waiting_element_checkbox()
    tpl.click_element_()
    tpl.waiting_element_message()
    tpl.present_text()
    tpl.waiting_()
