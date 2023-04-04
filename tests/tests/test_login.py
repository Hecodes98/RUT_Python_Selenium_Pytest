from selenium.webdriver.common.by import By
from Utils.page_factory import PageFactory
from Utils.signature_process import SignatureProcess
from pywinauto.application import Application
from config import BASE_URL
from pytest_check import check
from assertpy import assert_that
import pytest
import time


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
        time.sleep(5)
        signaturate_process = SignatureProcess()
        signaturate_process.signature_process()
        facility_manager.click_save_modal_button()

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

    def prueba(self, driver, username, password, document_number, ticket_number ,assistant_registration_page):
        login_page = PageFactory.create_page(driver, "login")
        driver.get(BASE_URL)
        login_page.fill_inputs_and_click_login(username, password)
        home_page = PageFactory.create_page(driver, "home")
        home_page.click_menu_button()
        home_page.click_courses_menu_option()
        home_page.click_attendee_registration_menu_option()
        assistant_registration_page.click_accept_modal_button()
        assistant_registration_page.click_document_type_select_input()
        assistant_registration_page.click_cc_option()
        assistant_registration_page.fill_document_number_textbox(document_number)
        assistant_registration_page.click_consult_button()
        assistant_registration_page.click_record_violation_button()
        assistant_registration_page.fill_ticket_number_textbox(ticket_number)
        time.sleep(5) #Botón buscar numero de comparendo, cuenta con un retraso propio de la página web, 
        #por eso se usa time.sleep(5) para este caso en especial, al quitar este time.sleep retorna error, que sería el comportamiento esperado
        assistant_registration_page.click_search_ticket_number_button()
        

    @pytest.mark.parametrize("username, password, document_number, ticket_number", [("404477901", "1qazxsw2.","12345678", "")])
    def test_attendee_registration_page_no_data_input(self,driver, username, password, document_number, ticket_number):
        """
        Verifica que se puede hacer login exitosamente con credenciales válidas.
        """
        assistant_registration_page = PageFactory.create_page(driver, "assistant_registration")
        self.prueba(driver, username, password, document_number, ticket_number ,assistant_registration_page)
        with check:
            assert_that(assistant_registration_page.verify_error_message()).described_as("Validar que el mensaje de error se muestre sin agregar datos").is_equal_to("- Número Comparendo es obligatorio") 
    
        time.sleep(5)  

    @pytest.mark.parametrize("username, password, document_number, ticket_number", [("404477901", "1qazxsw2.","12345678", "12345")])
    def test_attendee_registration_page_wrong_data_input(self,driver, username, password, ticket_number, document_number):
        """
        Verifica que se puede hacer login exitosamente con credenciales válidas.
        """
        assistant_registration_page = PageFactory.create_page(driver, "assistant_registration")
        self.prueba(driver, username, password, document_number, ticket_number, assistant_registration_page)
        with check:
            assert_that(assistant_registration_page.verify_error_message()).described_as("Validar que el mensaje de error se muestre sin agregar datos").is_equal_to("- 'Número Comparendo' no cumple con el formato requerido") 
    
        time.sleep(5)  
    
    @pytest.mark.parametrize("username, password, document_number, ticket_number", [("404477901", "1qazxsw2.","12345678", "12345678901234567890")])
    def test_attendee_registration_page_right_data_input(self,driver, username, password, ticket_number, document_number):
        """
        Verifica que se puede hacer login exitosamente con credenciales válidas.
        """
        assistant_registration_page = PageFactory.create_page(driver, "assistant_registration")
        self.prueba(driver, username, password, document_number, ticket_number, assistant_registration_page)
        with check:
            assert_that(assistant_registration_page.verify_error_message()).described_as("Validar que el mensaje de error se muestre sin agregar datos").is_equal_to("There's no error message") 

        with check:
            assert_that(assistant_registration_page.verify_infraction_error_message()).described_as("Validar que el mensaje de error se muestre sin agregar datos").is_equal_to("There's no error message") 

        time.sleep(5)  
    
    @pytest.mark.parametrize("username, password, document_number, ticket_number", [("404477901", "1qazxsw2.","12345678", "17345678901254267690")])
    def test_attendee_registration_page_inexistent_data_input(self,driver, username, password, ticket_number, document_number):
        """
        Verifica que se puede hacer login exitosamente con credenciales válidas.
        """
        assistant_registration_page = PageFactory.create_page(driver, "assistant_registration")
        self.prueba(driver, username, password, document_number, ticket_number, assistant_registration_page)
        with check:
            assert_that(assistant_registration_page.verify_error_message()).described_as("Validar que el mensaje de error se muestre sin agregar datos").is_equal_to("There's no error message") 

        with check:
            assert_that(assistant_registration_page.verify_infraction_error_message()).described_as("Validar que el mensaje de error se muestre sin agregar datos").is_equal_to("- Infracción es obligatorio") 

        time.sleep(5) 

    @pytest.mark.parametrize("username, password, document_number, ticket_number", [("404477901", "1qazxsw2.","12345678", "76364000000021299635")])
    def test_attendee_registration_page_ticket_already_register(self,driver, username, password, ticket_number, document_number):
        """
        Verifica que se puede hacer login exitosamente con credenciales válidas.
        """
        assistant_registration_page = PageFactory.create_page(driver, "assistant_registration")
        self.prueba(driver, username, password, document_number, ticket_number, assistant_registration_page)
        with check:
            assert_that(assistant_registration_page.verify_modal_error_message()).described_as("Validar que el mensaje de error se muestre sin agregar datos").is_equal_to("El comparendo tiene asociado un curso") 

        assistant_registration_page.click_accept_modal_button()

        time.sleep(5) 
        

#El comparendo tiene asociado un curso


