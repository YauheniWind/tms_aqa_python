from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions


# Пререход на сайте через submit
def test_log_in(browser, credentials, locators):
    browser.get("https://www.saucedemo.com")

    login_loc = browser.find_element(By.XPATH, locators["login_loc"])
    password_loc = browser.find_element(By.XPATH, locators["password_loc"])
    login_button = browser.find_element(By.XPATH, locators["submit_loc"])

    login_loc.send_keys(credentials["login"])  # Логин
    password_loc.send_keys(credentials["password"])  # Пароль
    login_button.click()  # Нажимаем кнопку "Login"

    current_url = browser.current_url  # получем актуальный url

    assert (
        current_url == "https://www.saucedemo.com/inventory.html"
    )  # Проверяем что  переход совершился


# Добавление элемента в корзину
def test_add_in_basket(browser, credentials, locators):
    browser.get("https://www.saucedemo.com")

    login_loc = browser.find_element(By.XPATH, locators["login_loc"])
    password_loc = browser.find_element(By.XPATH, locators["password_loc"])
    login_button = browser.find_element(By.XPATH, locators["submit_loc"])

    login_loc.send_keys(credentials["login"])  # Логин
    password_loc.send_keys(credentials["password"])  # Пароль
    login_button.click()  # Нажимаем кнопку "Login"

    name_of_product_loc = browser.find_element(
        By.XPATH, '//*[@id="item_4_title_link"]/div'
    ).text

    add_to_card_loc = browser.find_element(
        By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]'
    )
    add_to_card_loc.click()

    basket_loc = browser.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a')
    basket_loc.click()

    name_of_product_in_basket_loc = browser.find_element(
        By.XPATH, '//*[@id="item_4_title_link"]/div'
    ).text

    assert name_of_product_loc == name_of_product_in_basket_loc


# Отображение формы регистрации после нажатия submit
def test_registration_form(browser):
    browser.get("https://demoqa.com/text-box")
    browser.fullscreen_window()

    full_name_loc = browser.find_element(By.XPATH, '//*[@id="userName"]')
    email_loc = browser.find_element(By.XPATH, '//*[@id="userEmail"]')
    current_address = browser.find_element(By.XPATH, '//*[@id="currentAddress"]')
    permanent_address = browser.find_element(By.XPATH, '//*[@id="permanentAddress"]')
    submit_button_loc = browser.find_element(By.XPATH, '//*[@id="submit"]')

    full_name_loc.send_keys("Ev Gev")
    email_loc.send_keys("ev.gev@gmail.com")
    current_address.send_keys("logMoc 12")
    permanent_address.send_keys("MocLog 21")
    submit_button_loc.click()

    modal_win_loc = browser.find_element(By.XPATH, '//*[@id="output"]/div')

    if modal_win_loc.is_displayed():
        name_in_modal_loc = browser.find_element(By.XPATH, '//*[@id="name"]')
        assert "Ev Gev" == name_in_modal_loc.text.split(":")[1]

# Поиск книги
def test_searching_book(browser):
    browser.get("https://demoqa.com/books")

    search_box_loc = browser.find_element(By.XPATH, '//*[@id="searchBox"]')
    search_box_loc.send_keys("Git")

    name_of_book_loc = browser.find_element(
        By.XPATH, '//*[@id="see-book-Git Pocket Guide"]/a'
    )

    assert name_of_book_loc.text == "Git Pocket Guide"

# Перемещение объекта
def test_drag_and_drop(browser):
    browser.get("https://demoqa.com/droppable")
    browser.fullscreen_window()

    browser.fullscreen_window()
    drag_el_loc = browser.find_element(By.XPATH, '//*[@id="draggable"]')
    drop_el_loc = browser.find_element(By.XPATH, '//*[@id="droppable"]')

    action = ActionChains(browser)

    action.drag_and_drop(drag_el_loc, drop_el_loc).perform()

    assert expected_conditions.text_to_be_present_in_element(
        (By.XPATH, drop_el_loc), "Dropped!"
    )
