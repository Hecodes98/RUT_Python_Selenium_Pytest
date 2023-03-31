from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
        self.error_message = (By.ID, "mat-error-1")
        self.search_ticket_number = (By.XPATH, "//span[contains(text(),'Buscar comparendo')]")
        self.record_violation = (By.XPATH, "//span[contains(text(),'Registrar Infracción')]")

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
            EC.presence_of_element_located(self.search_ticket_number)
        )
        search_ticket_element.click()

    def click_record_violation_button(self):
        record_violation_element = WebDriverWait(self.driver, TIME_SECONDS_UNIT).until(
            EC.element_to_be_clickable(self.record_violation)
        )
        record_violation_element.click()

    def fill_ticket_number_textbox(self,ticket_number):
        ticket_number_element = WebDriverWait(self.driver, TIME_SECONDS_UNIT).until(
            EC.presence_of_element_located(self.ticket_number_textbox)
        )
        ticket_number_element.send_keys(ticket_number)

    def verify_error_message(self):
        error_message_element = WebDriverWait(self.driver, TIME_SECONDS_UNIT).until(
            EC.presence_of_element_located(self.error_message)
        )
        return error_message_element.text