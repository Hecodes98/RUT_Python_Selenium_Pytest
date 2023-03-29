from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from config import TIME_SECONDS_UNIT

class SearchInformationPage:
    def __init__(self, driver):
        self.driver = driver
        self.document_select_input = (By.CSS_SELECTOR, "#mat-select-0[formcontrolname='tipoDocumentoId']")
        self.cc_option = (By.ID, "mat-option-3")
        self.document_number_textbox = (By.CSS_SELECTOR, "input[formcontrolname='numeroDocumento']")
        self.ticket_initial_date = (By.CSS_SELECTOR, "input[formcontrolname='fechaInicio']")
        self.ticket_final_date = (By.CSS_SELECTOR, "input[formcontrolname='fechaTerminacion']")
        self.ticket_number_textbox = (By.CSS_SELECTOR, "input[formcontrolname='numeroComparendo']")
        self.search_button = (By.XPATH, "//span[contains(text(),'Buscar')]")


    def click_select_input_type_document_cc(self):
        # Esperar a que el botón de cierre de sesión esté presente y sea visible en la página
        element = WebDriverWait(self.driver, TIME_SECONDS_UNIT).until(
            EC.presence_of_element_located(self.document_select_input)
        )
        # Esperar hasta que el elemento sea visible en la página
        element = WebDriverWait(self.driver, TIME_SECONDS_UNIT).until(
            EC.visibility_of_element_located(self.document_select_input)
        )
        element.click()

        cc_option_element = WebDriverWait(self.driver, TIME_SECONDS_UNIT).until(
            EC.element_to_be_clickable(self.cc_option)
        )

        cc_option_element.click()
        print("pase")

    def send_document_number(self, document_number):
        input_document_number_element = WebDriverWait(self.driver, TIME_SECONDS_UNIT).until(
            EC.presence_of_element_located(self.document_number_textbox)
        )
        input_document_number_element.send_keys(document_number)

    def send_ticket_initial_date(self, ticket_initial_date):
        initial_date_element = WebDriverWait(self.driver, TIME_SECONDS_UNIT).until(
            EC.presence_of_element_located(self.ticket_initial_date)
        )
        initial_date_element.send_keys(ticket_initial_date)

    def send_ticket_final_date(self, ticket_final_date):
        final_date_element = WebDriverWait(self.driver, TIME_SECONDS_UNIT).until(
            EC.presence_of_element_located(self.ticket_final_date)
        )
        final_date_element.send_keys(ticket_final_date)
    
    def send_ticket_number(self, ticket_number):
        ticket_number_textbox_element = WebDriverWait(self.driver, TIME_SECONDS_UNIT).until(
            EC.presence_of_element_located(self.ticket_number_textbox)
        )
        ticket_number_textbox_element.send_keys(ticket_number)
    
    def click_search_button(self):
        search_button_element = WebDriverWait(self.driver, TIME_SECONDS_UNIT).until(
            EC.element_to_be_clickable(self.search_button)
        )
        self.driver.execute_script("arguments[0].scrollIntoView();", search_button_element)
        search_button_element.click()