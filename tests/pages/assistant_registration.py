from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.common.exceptions import TimeoutException

from config import TIME_SECONDS_UNIT

class AssistantRegistrationPage:
    def __init__(self, driver):
        self.driver = driver
        self.accept_modal_button = (By.XPATH, "//button[contains(text(),'Aceptar')]")
        self.document_type_select_input = (By.ID, "mat-select-0")
        self.cc_option = (By.ID, "mat-option-0")
        self.document_number_textbox = (By.ID, "mat-input-0")
        self.consult_button = (By.XPATH, "//span[contains(text(),'Consultar')]")
        self.ticket_number_textbox = (By.ID, "mat-input-19")
        self.error_message = (By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[1]/mat-dialog-container[1]/ciasmr-app-registro-infraccion[1]/div[1]/form[1]/div[1]/div[1]/mat-form-field[1]/div[1]/div[2]/div[1]/mat-error[1]")
        self.search_ticket_number = (By.XPATH, "//span[contains(text(),'Buscar comparendo')]")
        self.record_violation = (By.XPATH, "//span[contains(text(),'Registrar Infracción')]")
        self.infraction_error_message = (By.XPATH, "//body[1]/div[1]/div[2]/div[1]/mat-dialog-container[1]/ciasmr-app-registro-infraccion[1]/div[1]/form[1]/div[2]/div[1]/mat-form-field[1]/div[1]/div[2]/div[1]/mat-error[1]")
        self.modal_error_message = (By.XPATH, "//body[1]/div[3]/div[1]/div[2]")
        self.accept_modal_button_ticket_already_exist = (By.XPATH, "//body[1]/div[3]/div[1]/div[6]/button[1]")


    def click_accept_modal_button(self):
        # Esperar a que el campo de usuario esté presente en la página
        modal_button_element = WebDriverWait(self.driver, TIME_SECONDS_UNIT).until(
            EC.presence_of_element_located(self.accept_modal_button)
        )
        modal_button_element = WebDriverWait(self.driver, TIME_SECONDS_UNIT).until(
            EC.element_to_be_clickable(self.accept_modal_button)
        )
        modal_button_element.click()

    def click_document_type_select_input(self):
        WebDriverWait(self.driver, TIME_SECONDS_UNIT).until(
            EC.invisibility_of_element(self.accept_modal_button)
        )
        document_type_select_element = WebDriverWait(self.driver, TIME_SECONDS_UNIT).until(
            EC.presence_of_element_located(self.document_type_select_input)
        )
        document_type_select_element.click()
    
    def click_cc_option(self):
        cc_element = WebDriverWait(self.driver, TIME_SECONDS_UNIT).until(
            EC.presence_of_element_located(self.cc_option)
        )
        cc_element.click()

    def fill_document_number_textbox(self,document_number):
        document_number_element = WebDriverWait(self.driver, TIME_SECONDS_UNIT).until(
            EC.presence_of_element_located(self.document_number_textbox)
        )
        document_number_element.send_keys(document_number)

    def click_consult_button(self):
        consult_button_element = WebDriverWait(self.driver, TIME_SECONDS_UNIT).until(
            EC.presence_of_element_located(self.consult_button)
        )
        consult_button_element.click()


    def click_search_ticket_number_button(self):
        search_ticket_element = WebDriverWait(self.driver, TIME_SECONDS_UNIT).until(
            EC.element_to_be_clickable(self.search_ticket_number)
        )
        search_ticket_element.click()


    def click_record_violation_button(self):
        record_violation_element = WebDriverWait(self.driver, TIME_SECONDS_UNIT).until(
            EC.element_to_be_clickable(self.record_violation)
        )
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", record_violation_element)
        record_violation_element.click()

    def fill_ticket_number_textbox(self,ticket_number):
        ticket_number_element = WebDriverWait(self.driver, TIME_SECONDS_UNIT).until(
            EC.presence_of_element_located(self.ticket_number_textbox)
        )
        ticket_number_element.send_keys(ticket_number)

    def verify_error_message(self):
        try:
            error_message_element = WebDriverWait(self.driver, TIME_SECONDS_UNIT).until(
                EC.presence_of_element_located(self.error_message)
            )
            return error_message_element.text
        except TimeoutException:
            return "There's no error message"
        
    def verify_infraction_error_message(self):
        try:
            infraction_error_message_element = WebDriverWait(self.driver, TIME_SECONDS_UNIT).until(
                EC.presence_of_element_located(self.infraction_error_message)
            )
            return infraction_error_message_element.text
        except TimeoutException:
            return "There's no error message"
        
    def verify_modal_error_message(self):
        try:
            modal_error_message_element = WebDriverWait(self.driver, TIME_SECONDS_UNIT).until(
                EC.presence_of_element_located(self.modal_error_message)
            )
            return modal_error_message_element.text
        except TimeoutException:
            return "There's no error message"
    
    def click_accept_modal_button_ticket_already_exist(self):
        accept_modal_element = WebDriverWait(self.driver, TIME_SECONDS_UNIT).until(
            EC.element_to_be_clickable(self.accept_modal_button_ticket_already_exist)
        )
        accept_modal_element.click()

