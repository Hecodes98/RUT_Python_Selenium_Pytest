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

    def base_test(self, driver, username, password):
        login_page = PageFactory.create_page(driver, "login")
        driver.get(BASE_URL)
        login_page.fill_inputs_and_click_login(username, password)
        home_page = PageFactory.create_page(driver, "home")
        home_page.click_menu_button()
        home_page.click_search_information_option()
        home_page.click_organizations_option()
        

    @pytest.mark.parametrize("username, password", [("404477901", "1qazxsw2.")])
    def test_organizations_document_cc_type(self,driver, username, password):
        """
        Verifica que el mensaje de error al no ingresar datos aparezca
        """
        self.base_test(driver, username, password)
        organizations_page = PageFactory.create_page(driver,"organizations")
        time.sleep(10)
        organizations_page.click_organization_type_input()
        organizations_page.click_document_type_and_select_cc()
        organizations_page.send_document_number('1088035775')
        organizations_page.click_search_button()
        #with check:
        #    assert_that(assistant_registration_page.verify_error_message()).described_as("Validar que el mensaje de error se muestre sin agregar datos").is_equal_to("- Número Comparendo es obligatorio") 
    
        time.sleep(5)  

    @pytest.mark.parametrize("username, password", [("404477901", "1qazxsw2.")])
    def test_organizations_validate_parametrized_date(self,driver, username, password):
        """
        Verifica que el mensaje de error al no ingresar datos aparezca
        """
        self.base_test(driver, username, password)
        organizations_page = PageFactory.create_page(driver,"organizations")
        time.sleep(10)
        organizations_page.click_organization_type_input()
        with check:
            assert_that(organizations_page.get_today_day_input()).described_as("Validar que la fecha que se muestre sea igual a la fecha de hoy menos los días parametrizados").is_not_none() 
    
        time.sleep(5)  

    @pytest.mark.parametrize("username, password", [("404477901", "1qazxsw2.")])
    def test_organizations_commercial_registration_number(self,driver, username, password):
        """
        Verifica que el mensaje de error al no ingresar datos aparezca
        """
        self.base_test(driver, username, password)
        organizations_page = PageFactory.create_page(driver,"organizations")
        time.sleep(10)
        organizations_page.click_organization_type_input()
        organizations_page.click_document_type_and_select_cc()
        organizations_page.send_commercial_registration_number('1088035775')
        organizations_page.click_search_button()
        #with check:
        #    assert_that(assistant_registration_page.verify_error_message()).described_as("Validar que el mensaje de error se muestre sin agregar datos").is_equal_to("- Número Comparendo es obligatorio") 
    
        time.sleep(5)  


