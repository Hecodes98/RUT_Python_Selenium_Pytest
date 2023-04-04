from Utils.page_factory import PageFactory
from config import BASE_URL
from pytest_check import check
from assertpy import assert_that
import pytest
import time


class TestAssistantRegistration:
    def test_login(self, driver):
        login_page = PageFactory.create_page(driver, "login")
        driver.get(BASE_URL)
        login_page.fill_inputs_and_click_login("404477901", "1qazxsw2.")
        time.sleep(15)
        assert driver.current_url == "https://azspkdevstcus004.z19.web.core.windows.net/#/"

    def base_test(self, driver, username, password, document_number, ticket_number ,assistant_registration_page):
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
        Verifica que el mensaje de error al no ingresar datos aparezca
        """
        assistant_registration_page = PageFactory.create_page(driver, "assistant_registration")
        self.base_test(driver, username, password, document_number, ticket_number ,assistant_registration_page)
        with check:
            assert_that(assistant_registration_page.verify_error_message()).described_as("Validar que el mensaje de error se muestre sin agregar datos").is_equal_to("- Número Comparendo es obligatorio") 
    
        time.sleep(5)  

    @pytest.mark.parametrize("username, password, document_number, ticket_number", [("404477901", "1qazxsw2.","12345678", "12345")])
    def test_attendee_registration_page_wrong_data_input(self,driver, username, password, ticket_number, document_number):
        """
        Verifica que el mensaje de error al ingresar menos de 20 caracteres en el campo de número de tiquet aparezca.
        """
        assistant_registration_page = PageFactory.create_page(driver, "assistant_registration")
        self.base_test(driver, username, password, document_number, ticket_number, assistant_registration_page)
        with check:
            assert_that(assistant_registration_page.verify_error_message()).described_as("Validar que el mensaje de error se muestre sin agregar datos").is_equal_to("- 'Número Comparendo' no cumple con el formato requerido") 
    
        time.sleep(5)  
    
    @pytest.mark.parametrize("username, password, document_number, ticket_number", [("404477901", "1qazxsw2.","12345678", "12345678901234567890")])
    def test_attendee_registration_page_right_data_input(self,driver, username, password, ticket_number, document_number):
        """
        Verifica que no aparezca ningún mensaje de error aparezca
        """
        assistant_registration_page = PageFactory.create_page(driver, "assistant_registration")
        self.base_test(driver, username, password, document_number, ticket_number, assistant_registration_page)
        with check:
            assert_that(assistant_registration_page.verify_error_message()).described_as("Validar que el mensaje de error se muestre sin agregar datos").is_equal_to("There's no error message") 

        with check:
            assert_that(assistant_registration_page.verify_infraction_error_message()).described_as("Validar que el mensaje de error se muestre sin agregar datos").is_equal_to("There's no error message") 

        time.sleep(5)  
    
    @pytest.mark.parametrize("username, password, document_number, ticket_number", [("404477901", "1qazxsw2.","12345678", "17345678901254267690")])
    def test_attendee_registration_page_inexistent_data_input(self,driver, username, password, ticket_number, document_number):
        """
        Verifica que se habiliten todos los campos y mensajes de solicitud de datos aparezcan
        """
        assistant_registration_page = PageFactory.create_page(driver, "assistant_registration")
        self.base_test(driver, username, password, document_number, ticket_number, assistant_registration_page)
        with check:
            assert_that(assistant_registration_page.verify_error_message()).described_as("Validar que el mensaje de error se muestre sin agregar datos").is_equal_to("There's no error message") 

        with check:
            assert_that(assistant_registration_page.verify_infraction_error_message()).described_as("Validar que el mensaje de error se muestre sin agregar datos").is_equal_to("- Infracción es obligatorio") 

        time.sleep(5) 

    @pytest.mark.parametrize("username, password, document_number, ticket_number", [("404477901", "1qazxsw2.","12345678", "76364000000021299635")])
    def test_attendee_registration_page_ticket_already_register(self,driver, username, password, ticket_number, document_number):
        """
        Verifica que modal de error aparezca
        """
        assistant_registration_page = PageFactory.create_page(driver, "assistant_registration")
        self.base_test(driver, username, password, document_number, ticket_number, assistant_registration_page)
        with check:
            assert_that(assistant_registration_page.verify_modal_error_message()).described_as("Validar que el mensaje de error se muestre sin agregar datos").is_equal_to("El comparendo tiene asociado un curso") 

        assistant_registration_page.click_accept_modal_button_ticket_already_exist()

        time.sleep(5) 


