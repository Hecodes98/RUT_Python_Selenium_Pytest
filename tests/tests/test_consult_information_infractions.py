from selenium.webdriver.common.by import By
from Utils.page_factory import PageFactory
from config import BASE_URL
from pytest_check import check
from assertpy import assert_that
import pytest
import time

class TestConsultInformationInfraction:
    
    def base(self, driver, username, password):
        login_page = PageFactory.create_page(driver, "login")
        driver.get(BASE_URL)
        login_page.fill_inputs_and_click_login(username=username, password=password)
        home_page = PageFactory.create_page(driver, "home")
        home_page.click_menu_button()
        home_page.click_search_information_option()
        home_page.click_violations_option()
        

    @pytest.mark.EP1_CUR01535
    @pytest.mark.parametrize("username, password", [("404477902", "1qazxsw2.")])
    def test_EP1_CUR01535(self, driver, username, password):
        self.UI_elements_text = set(["Carnet Diplomático","Cédula Ciudadanía","Cédula de Extranjería",
                                     "NIT", "Pasaporte", "Permiso por Protección Temporal",
                                     "Registro Civil","TI2","Tarjeta de Identidad"])
        self.base(driver,username,password)
        search_information_page = PageFactory.create_page(driver, "search_info")
        time.sleep(10)
        search_information_page.click_select_input()
        with check:
            assert_that(search_information_page.get_all_dropdown_options(UI_elements=self.UI_elements_text)).is_true()
        time.sleep(10)

    @pytest.mark.EP2_CUR01535
    @pytest.mark.parametrize("username, password", [("404477902", "1qazxsw2.")])
    def test_EP2_CUR01535(self, driver, username, password):
        self.base(driver,username,password)
        search_information_page = PageFactory.create_page(driver, "search_info")
        time.sleep(10)
        search_information_page.click_search_button()
        error_text = search_information_page.get_ticket_number_error()
        with check:
            assert_that(error_text).described_as("Error Obligatory Mesage").is_equal_to("- Número de Comparendo es obligatorio")
        time.sleep(10)

    @pytest.mark.EP3_CUR01535
    @pytest.mark.parametrize("username, password", [("404477902", "1qazxsw2.")])
    def test_EP3_CUR01535(self, driver, username, password):
        """
        Consultar Infracciones registradas por el establecimiento 
        - Validar campos "Fecha Inicio" y "Fecha Fin".
        """
        self.base(driver,username,password)
        search_information_page = PageFactory.create_page(driver, "search_info")
        time.sleep(10)
        search_information_page.send_ticket_initial_date("6/4/2001")
        search_information_page.send_ticket_final_date("10/4/2001")
        time.sleep(5)
    
    @pytest.mark.EP6_CUR01535
    @pytest.mark.parametrize("username, password", [("404477902", "1qazxsw2.")])
    def test_EP6_CUR01535(self, driver, username, password):
        """
        Validar que el sistema recupere todos los comparendos (Manuales y recuperados del SIMIT),
        registrados por el establecimiento CIA y muestre la información en una tabla.
        """
        self.base(driver,username,password)
        search_information_page = PageFactory.create_page(driver, "search_info")
        time.sleep(10)
        search_information_page.click_search_button()
        error_text = search_information_page.get_ticket_number_error()
        with check:
            assert_that(error_text).described_as("Error Obligatory Mesage").is_equal_to("- Número de Comparendo es obligatorio")
        time.sleep(10)
    
    @pytest.mark.EP9_CUR01535
    @pytest.mark.parametrize("username, password", [("404477902", "1qazxsw2.")])
    def test_EP9_CUR01535(self, driver, username, password):
        """
        Consulta de Infracción - Validar la recuperación de todos los  comparendos - Opción "Buscar" - Actor CEA/OT.
        """
        self.base(driver,username,password)
        search_information_page = PageFactory.create_page(driver, "search_info")
        time.sleep(10)
        search_information_page.click_select_input_type_document_cc()
        search_information_page.send_document_number("12345678")
        search_information_page.send_ticket_initial_date("6/4/2001")
        search_information_page.send_ticket_final_date("10/4/2001")
        search_information_page.send_ticket_number("87654")
        search_information_page.click_search_button()
        time.sleep(10)

    @pytest.mark.EP11_CUR01535
    @pytest.mark.parametrize("username, password", [("404477902", "1qazxsw2.")])
    def test_EP11_CUR01535(self, driver, username, password):
        """
        Consulta de Infracción - Validar la recuperación de todos los  comparendos - Opción "Buscar" - Actor CEA/OT.
        """
        self.base(driver,username,password)
        search_information_page = PageFactory.create_page(driver, "search_info")
        time.sleep(10)
        search_information_page.click_select_input_type_document_cc()
        search_information_page.send_document_number("123456")
        search_information_page.send_ticket_initial_date("6/4/2001")
        search_information_page.send_ticket_final_date("10/4/2001")
        search_information_page.send_ticket_number("87654")
        search_information_page.click_search_button()
        error_text = search_information_page.get_modal_message_error()
        with check:
            assert_that(error_text).described_as("Error Obligatory Mesage").is_equal_to("No se encontraron registros")
        time.sleep(10)

    @pytest.mark.EP13_CUR01535
    @pytest.mark.parametrize("username, password", [("404477902", "1qazxsw2.")])
    def test_EP13_CUR01535(self, driver, username, password):
        """
        Consulta de Infracción - Validar la recuperación de todos los  comparendos - Opción "Buscar" - Actor CEA/OT.
        """
        self.base(driver,username,password)
        search_information_page = PageFactory.create_page(driver, "search_info")
        time.sleep(10)
        search_information_page.click_select_input_type_document_cc()
        search_information_page.send_document_number("123456")
        search_information_page.send_ticket_initial_date("6/4/2001")
        search_information_page.send_ticket_final_date("10/4/2001")
        search_information_page.send_ticket_number("87654")
        search_information_page.click_clean_button()
        time.sleep(10)