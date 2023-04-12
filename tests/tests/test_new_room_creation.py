from selenium.webdriver.common.by import By
from Utils.page_factory import PageFactory
from Utils.signature_process import SignatureProcess
from pywinauto.application import Application
from config import BASE_URL
from pytest_check import check
from assertpy import assert_that
import pytest
import time


class TestNewRoomCreation:

    def test_login(self, driver):
        login_page = PageFactory.create_page(driver, "login")
        driver.get(BASE_URL)
        login_page.fill_inputs_and_click_login("404477901", "1qazxsw2.")
        time.sleep(15)
        assert driver.current_url == "https://azspkdevstcus004.z19.web.core.windows.net/#/"

    def test_fill_textboxes_for_a_new_room_creation(self, driver):
        login_page = PageFactory.create_page(driver, "login")
        driver.get(BASE_URL)
        login_page.fill_inputs_and_click_login("404477901", "1qazxsw2.")
        home_page = PageFactory.create_page(driver, "home")
        home_page.click_menu_button()
        home_page.click_administration_menu_option()
        home_page.click_administration_organizations_button()
        facility_manager = PageFactory.create_page(driver, "facility_manager")
        facility_manager.click_accept_button_for_close_error_modal()
        facility_manager.click_new_room_button()
        facility_manager.fill_name_textbox("Hector Cardona")
        facility_manager.fill_capacity_textbox("2")
        facility_manager.click_save_button()
        facility_manager.click_accept_modal_button_twice()
        time.sleep(10)
        signaturate_process = SignatureProcess()
        signaturate_process.signature_process()
        facility_manager.click_save_modal_button()
    
    #@pytest.mark.parametrize("username, password", [("404477901", "1qazxsw2.")])
    #def test_organizations_validate_parametrized_date(self,driver, username, password):
        """
        Verifica que el mensaje de error al no ingresar datos aparezca
        """
    #    self.base_test(driver, username, password)
    #    organizations_page = PageFactory.create_page(driver,"organizations")
    #    time.sleep(10)
    #    organizations_page.click_organization_type_input()
    #    with check:
    #        assert_that(organizations_page.get_today_day_input()).described_as("Validar que la fecha que se muestre sea igual a la fecha de hoy menos los días parametrizados").is_not_none() 
    # 
    #    time.sleep(5)  

    """  
    @pytest.mark.parametrize("username, password", [("404477901", "1qazxsw2."), ("404477902", "1qazxsw2."), 
                                                      ("404477904", "1qazxsw2."), ("404477905", "1qazxsw2."),
                                                      ("404477903", "1qazxsw2.")])
    def test_fill_textboxes_for_instructor_page(self,driver,username,password):
        login_page = PageFactory.create_page(driver, "login")
        driver.get(BASE_URL)
        login_page.fill_inputs_and_click_login(username, password)
        home_page = PageFactory.create_page(driver, "home")
        home_page.click_menu_button()
        home_page.click_administration_menu_option()
        home_page.click_instructor_administration_option()
        time.sleep(10)
        instructor_page = PageFactory.create_page(driver, "instructor_page")
        instructor_page.click_document_type_select_input()
        instructor_page.click_cc_option()
        instructor_page.fill_document_type_textbox("99887766")
    """


