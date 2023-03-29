import time
from selenium.webdriver.common.by import By
from Utils.page_factory import PageFactory
from config import BASE_URL


#from registration_page import RegistrationPage


class TestLoginAndRegistration:
    def test_login(self, driver):
        login_page = PageFactory.create_page(driver, "login")
        driver.get(BASE_URL)
        login_page.fill_inputs_and_click_login("404477901", "1qazxsw2.")
        time.sleep(15)
        assert driver.current_url == "https://azspkdevstcus004.z19.web.core.windows.net/#/"

    def test_fill_violations_textboxes_and_click_search_button(self, driver):
        login_page = PageFactory.create_page(driver, "login")
        driver.get(BASE_URL)
        login_page.fill_inputs_and_click_login("404477901", "1qazxsw2.")
        home_page = PageFactory.create_page(driver, "home")
        home_page.click_menu_button()
        home_page.click_search_information_option()
        home_page.click_violations_option()
        search_information_page = PageFactory.create_page(driver, "search_info")
        time.sleep(10)
        search_information_page.click_select_input_type_document_cc()
        search_information_page.send_document_number("123456")
        search_information_page.send_ticket_initial_date("6/4/2001")
        search_information_page.send_ticket_final_date("10/4/2001")
        search_information_page.send_ticket_number("87654")
        search_information_page.click_search_button()
        time.sleep(10)
    
    def test_fill_organizations_textboxes_and_click_search(self, driver):
        login_page = PageFactory.create_page(driver, "login")
        driver.get(BASE_URL)
        login_page.fill_inputs_and_click_login("404477901", "1qazxsw2.")
        home_page = PageFactory.create_page(driver, "home")
        home_page.click_menu_button()
        home_page.click_search_information_option()
        home_page.click_organizations_option()
        organizations_page = PageFactory.create_page(driver,"organizations")
        time.sleep(10)
        organizations_page.click_organization_type_input()
        organizations_page.click_document_type_and_select_cc()
        organizations_page.send_document_number('1088035775')
        organizations_page.send_commercial_registration_number('99887766')
        time.sleep(10)
    

