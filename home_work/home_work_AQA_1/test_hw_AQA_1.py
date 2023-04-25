from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions

from Helper import Helper
from ElementsObject import ElementsObject
class TestsPage:
    def test_drag_and_drop(self, browser):
        helper = Helper(browser)
        helper.driver.get("https://demoqa.com/droppable")

        helper.driver.fullscreen_window()

        drag_el_loc = helper.get_locator_by_xpath(ElementsObject.drag_el_loc)
        drop_el_loc = helper.get_locator_by_xpath(ElementsObject.drop_el_loc)

        action = ActionChains(browser)

        action.drag_and_drop(drag_el_loc, drop_el_loc).perform()
        browser.save_screenshot("test_1.png")
        assert expected_conditions.text_to_be_present_in_element(
            (By.XPATH, drop_el_loc), "Dropped!"
        )  # Проверка переместился ли элемент


# Пререход на сайте через submit
def test_log_in(browser, credentials):
    helper = Helper(browser)
    helper.driver.get("https://www.saucedemo.com")

    login_loc = helper.get_locator_by_xpath(ElementsObject.login_loc)
    password_loc = helper.get_locator_by_xpath(ElementsObject.password_loc)
    login_button = helper.get_locator_by_xpath(ElementsObject.submit_loc)

    login_loc.send_keys(credentials["login"])  # Логин
    password_loc.send_keys(credentials["password"])  # Пароль
    login_button.click()  # Нажимаем кнопку "Login"

    current_url = browser.current_url  # получем актуальный url

    assert current_url == "https://www.saucedemo.com/inventory.html"  # Проверяем что  переход совершился


# Добавление элемента в корзину
def test_add_in_basket(browser, credentials):
    helper = Helper(browser)
    helper.driver.get("https://www.saucedemo.com")

    login_loc = helper.get_locator_by_xpath(ElementsObject.login_loc)
    password_loc = helper.get_locator_by_xpath(ElementsObject.password_loc)
    login_button = helper.get_locator_by_xpath(ElementsObject.submit_loc)

    login_loc.send_keys(credentials["login"])  # Логин
    password_loc.send_keys(credentials["password"])  # Пароль
    login_button.click()  # Нажимаем кнопку "Login"

    name_of_product_loc = helper.get_locator_by_xpath(ElementsObject.name_of_product).text

    add_to_card_loc = helper.get_locator_by_xpath(ElementsObject.add_to_cart_product)
    add_to_card_loc.click()

    basket_loc = helper.get_locator_by_xpath(ElementsObject.basket_first_page)
    basket_loc.click()

    name_of_product_in_basket_loc = helper.get_locator_by_xpath(
        ElementsObject.name_of_product_in_basket
    ).text

    assert name_of_product_loc == name_of_product_in_basket_loc  # Проверяем что в корзине тот элемент


# Отображение формы регистрации после нажатия submit
def test_registration_form(browser):
    helper = Helper(browser)
    helper.driver.get("https://demoqa.com/text-box")
    helper.driver.fullscreen_window()

    full_name_loc = helper.get_locator_by_xpath(ElementsObject.full_name)
    email_loc = helper.get_locator_by_xpath(ElementsObject.email)
    current_address = helper.get_locator_by_xpath(ElementsObject.current_address)
    permanent_address = helper.get_locator_by_xpath(ElementsObject.permanent_address)
    submit_button_loc = helper.get_locator_by_xpath(ElementsObject.submit_button_registration)

    full_name_loc.send_keys("Ev Gev")
    email_loc.send_keys("ev.gev@gmail.com")
    current_address.send_keys("logMoc 12")
    permanent_address.send_keys("MocLog 21")
    submit_button_loc.click()

    modal_win_loc = helper.get_locator_by_xpath(ElementsObject.modal_window_)

    if modal_win_loc.is_displayed():
        name_in_modal_loc = helper.get_locator_by_xpath(ElementsObject.name_in_modal_window)
        assert "Ev Gev" == name_in_modal_loc.text.split(":")[1]  # Проверяем правильность имени


# Поиск книги
def test_searching_book(browser):
    helper = Helper(browser)
    helper.driver.get("https://demoqa.com/books")

    search_box_loc = helper.get_locator_by_xpath(ElementsObject.search_box)
    search_box_loc.send_keys("Git")

    name_of_book_loc = helper.get_locator_by_xpath(ElementsObject.name_of_book)

    assert name_of_book_loc.text == "Git Pocket Guide"  # Проверка та ли книга нашлась


# Перемещение объекта
def test_drag_and_drop_2(browser):
    helper = Helper(browser)
    helper.driver.get("https://demoqa.com/droppable")

    helper.driver.fullscreen_window()

    drag_el_loc = helper.get_locator_by_xpath(ElementsObject.drag_el_loc)
    drop_el_loc = helper.get_locator_by_xpath(ElementsObject.drop_el_loc)

    action = ActionChains(browser)

    action.drag_and_drop(drag_el_loc, drop_el_loc).perform()
    browser.save_screenshot("test_1.png")
    assert expected_conditions.text_to_be_present_in_element(
        (By.XPATH, drop_el_loc), "Dropped!"
    )  # Проверка переместился ли элемент
