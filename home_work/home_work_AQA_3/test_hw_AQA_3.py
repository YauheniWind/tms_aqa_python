import requests
import filecmp

from Helper import Helper
from ElementsObject import ElementsObject


class TestDynamicControls:
    def test_checkbox(self, browser):
        helper = Helper(browser)
        helper.driver.get("http://the-internet.herokuapp.com/dynamic_controls")

        helper.waiting_element(ElementsObject.dm_checkbox)

        dm_remove_button = helper.get_locator_by_xpath(ElementsObject.dm_remove_button)
        dm_remove_button.click()
        dm_message = helper.waiting_element(ElementsObject.dm_message)

        helper.ec_text_to_be_present_in_element(dm_message, "It's gone!")
        assert helper.waiting_disappearance_element(ElementsObject.dm_checkbox)

    def test_input(self, browser):
        helper = Helper(browser)
        helper.driver.get("http://the-internet.herokuapp.com/dynamic_controls")

        helper.waiting_element(ElementsObject.dm_input)
        helper.get_locator_by_xpath(ElementsObject.dm_input)

        if helper.element_is_enabled(ElementsObject.dm_input):
            print("element is enabled")
            browser.quit()

        dm_enable_button = helper.get_locator_by_xpath(ElementsObject.dm_enable_button)
        dm_enable_button.click()

        dm_message = helper.waiting_element(ElementsObject.dm_message)
        helper.ec_text_to_be_present_in_element(dm_message, "It's disabled!")

        assert helper.element_is_enabled(ElementsObject.dm_input)


class TestDownloadUpload:
    def test_download(self, browser):
        helper = Helper(browser)
        helper.driver.get("http://the-internet.herokuapp.com/download")

        download_link = helper.get_locator_by_xpath(ElementsObject.download_link)
        download_url = download_link.get_attribute("href")

        response = requests.get(download_url)

        downloaded_file = "/Users/evgenijgravdin/Desktop/tms_aqa_python/home_work/home_work_AQA_3/file_pdf.pdf"
        with open(downloaded_file, "wb") as file:
            file.write(response.content)

        main_file_path = "/Users/evgenijgravdin/Desktop/tms_aqa_python/home_work/home_work_AQA_3/file_pdf.pdf"
        file_eq = filecmp.cmp(downloaded_file, main_file_path)

        if file_eq:
            print("Files equal")
        else:
            print("not")

    def test_upload(self, browser):
        helper = Helper(browser)
        helper.driver.get("http://the-internet.herokuapp.com/upload")

        input_file = helper.get_locator_by_xpath(ElementsObject.input_file)
        photo_path = "/Users/evgenijgravdin/Desktop/tms_aqa_python/home_work/home_work_AQA_3/sys_photo.jpeg"

        input_file.send_keys(photo_path)

        upload_button = helper.get_locator_by_xpath(ElementsObject.file_upload)
        upload_button.click()

        uploaded_file = helper.get_text(ElementsObject.uploaded_file)

        assert uploaded_file == "sys_photo.jpeg"
