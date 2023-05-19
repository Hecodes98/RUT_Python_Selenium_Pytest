from Utils.page_factory import PageFactory
from Utils.save_screenshots import SaveScreenshots
from config import BASE_URL, ORGANIZATIONS_BASE
from pytest_check import check
from assertpy import assert_that
import pytest
import time

class TestScheduling:

    def base(self, driver, username, password):
        login_page = PageFactory.create_page(driver, "login")
        driver.get(BASE_URL)
        login_page.fill_inputs_and_click_login(username, password)
        home_page = PageFactory.create_page(driver, "home")
        home_page.click_menu_button()
        home_page.click_courses_menu_option()
        home_page.click_courses_scheduling_option()
        time.sleep(20)

    @pytest.mark.base
    @pytest.mark.parametrize("username, password", [("404477902", "1qazxsw2.")])
    def test_base(self, driver, username, password):
        self.base(driver,username,password)
        scheduling_page = PageFactory.create_page(driver, "scheduling")
        scheduling_page.click_room_select_input()
        scheduling_page.click_room_one_option()
        scheduling_page.click_day_option()
        time.sleep(2)
        scheduling_page.click_next_option()
        time.sleep(2)
        scheduling_page.scroll_top()
        time.sleep(2)
        scheduling_page.click_record_violation_button()
        time.sleep(2)
        scheduling_page.click_instruction_input_option()
        time.sleep(2)
        scheduling_page.click_first_instructor_option()
        time.sleep(2)
        scheduling_page.click_accept_button()
        time.sleep(3)

    @pytest.mark.EP4_CUR01525
    @pytest.mark.parametrize("username, password", [("404477902", "1qazxsw2.")])
    def test_EP4_CUR01525(self, driver, username, password):
        """
        IMPORTANT: Los test del EP1 a EP4, EP11, EP15 estan contemplados en este test

        Validar que se muestren los campos que trae por defecto la "Hora inicio" y la "Hora fin" 
        de la franja horaria seleccionada en el calendario, son campos no editables.
        
        """
        self.base(driver,username,password)
        scheduling_page = PageFactory.create_page(driver, "scheduling")
        scheduling_page.click_room_select_input()
        scheduling_page.click_room_one_option()
        scheduling_page.click_day_option()
        time.sleep(2)
        scheduling_page.click_next_option()
        time.sleep(2)
        scheduling_page.scroll_top()
        time.sleep(2)
        scheduling_page.click_record_violation_button()
        time.sleep(2)
        text_element = scheduling_page.validate_inputs_appears()
        with check:
            assert_that(text_element).described_as("Hora Inicio").is_true() 
    
    @pytest.mark.EP5_CUR01525
    @pytest.mark.parametrize("username, password", [("404477902", "1qazxsw2.")])
    def test_EP5_CUR01525(self, driver, username, password):
        """
        IMPORTANT: Los test del EP7 estan contemplados en este test
        Validar que la lista desplegable de selección única, muestres los instructores 
        activos asociados a la ciudad y sede, deben estar organizados alfabéticamente 
        de forma ascendente. El tamaño corresponde al almacenado en el sistema.
        """
        self.base(driver,username,password)
        scheduling_page = PageFactory.create_page(driver, "scheduling")
        scheduling_page.click_room_select_input()
        scheduling_page.click_room_one_option()
        scheduling_page.click_day_option()
        time.sleep(2)
        scheduling_page.click_next_option()
        time.sleep(2)
        scheduling_page.scroll_top()
        time.sleep(2)
        scheduling_page.click_record_violation_button()
        time.sleep(2)
        scheduling_page.click_instruction_input_option()
        time.sleep(2)

    @pytest.mark.EP6_CUR01525
    @pytest.mark.parametrize("username, password", [("404477902", "1qazxsw2.")])
    def test_EP5_CUR01525(self, driver, username, password):
        """
        Validar que el sistema muestre los Filtros de Búsqueda Campo del "Establecimiento", 
        la lista desplegable "Sala" y las opciones "Día", "Mes", "Año" o "Agenda" (agendas ya registradas). 
        Si no hay agendamientos el calendario se debe mostrar vacío. Prototipo A.
        """
        self.base(driver,username,password)
        scheduling_page = PageFactory.create_page(driver, "scheduling")
        scheduling_page.click_room_select_input()
        scheduling_page.click_room_one_option()
        scheduling_page.click_agenda()
        scheduling_page.click_day_option()
        time.sleep(2)
        scheduling_page.click_next_option()
        time.sleep(2)
        scheduling_page.scroll_top()
        time.sleep(2)
        scheduling_page.click_record_violation_button()
        time.sleep(2)
        scheduling_page.click_instruction_input_option()
        time.sleep(2)

    @pytest.mark.EP8_CUR01525
    @pytest.mark.parametrize("username, password", [("404477902", "1qazxsw2.")])
    def test_EP5_CUR01525(self, driver, username, password):
        """
        Validar que al presionar la opción "Aceptar" el sistema valide obligatoriedad 
        y especificaciones en los campos de la ventana "Nueva Agenda".
        """
        self.base(driver,username,password)
        scheduling_page = PageFactory.create_page(driver, "scheduling")
        scheduling_page.click_room_select_input()
        scheduling_page.click_room_one_option()
        scheduling_page.click_day_option()
        time.sleep(2)
        scheduling_page.click_next_option()
        time.sleep(2)
        scheduling_page.scroll_top()
        time.sleep(2)
        scheduling_page.click_record_violation_button()
        time.sleep(2)
        scheduling_page.click_accept_button()
        time.sleep(2)
        text_element=scheduling_page.get_error_message()
        time.sleep(2)
        with check:
            assert_that(text_element).described_as("- Instructor es obligatorio").is_true() 
       