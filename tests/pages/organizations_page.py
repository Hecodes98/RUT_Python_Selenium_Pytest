from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from config import TIME_SECONDS_UNIT

class OrganizationsPage:
    def __init__(self, driver):
        self.driver = driver
        self.organization_type_input = (By.ID,"mat-select-0")
        self.organization_CEA_type = (By.ID, "mat-option-2")
        self.document_type_input = (By.ID, "mat-select-2")
        self.document_type_cc = (By.ID, "mat-option-4")
        self.document_number_textbox = (By.ID, "mat-input-1")
        self.commercial_registration_number_textbox = (By.ID, "mat-input-2")
        self.search_button = (By.XPATH, "//span[contains(text(),'Buscar')]")


    def click_organization_type_input(self):
        # Esperar a que el botón de cierre de sesión esté presente y sea visible en la página
        element = WebDriverWait(self.driver, TIME_SECONDS_UNIT).until(
            EC.presence_of_element_located(self.organization_type_input)
        )
        # Esperar hasta que el elemento sea visible en la página
        element = WebDriverWait(self.driver, TIME_SECONDS_UNIT).until(
            EC.visibility_of_element_located(self.organization_type_input)
        )
        element.click()

        organization_CEA_type_element = WebDriverWait(self.driver, TIME_SECONDS_UNIT).until(
            EC.element_to_be_clickable(self.organization_CEA_type)
        )

        organization_CEA_type_element.click()
        print("pase")

    def click_document_type_and_select_cc(self):
        # Esperar a que el botón de cierre de sesión esté presente y sea visible en la página
        element = WebDriverWait(self.driver, TIME_SECONDS_UNIT).until(
            EC.presence_of_element_located(self.document_type_input)
        )
        # Esperar hasta que el elemento sea visible en la página
        element.click()

        cc_element = WebDriverWait(self.driver, TIME_SECONDS_UNIT).until(
            EC.element_to_be_clickable(self.document_type_cc)
        )

        cc_element.click()
        print("pase")

    def send_document_number(self, document_number):
        document_number_element = WebDriverWait(self.driver, TIME_SECONDS_UNIT).until(
            EC.presence_of_element_located(self.document_number_textbox)
        )
        document_number_element.send_keys(document_number)

    def send_commercial_registration_number(self, commercial_registration_number):
        commercial_registration_number_element = WebDriverWait(self.driver, TIME_SECONDS_UNIT).until(
            EC.presence_of_element_located(self.commercial_registration_number_textbox)
        )
        commercial_registration_number_element.send_keys(commercial_registration_number)
    
    def click_search_button(self):
        search_button_element = WebDriverWait(self.driver, TIME_SECONDS_UNIT).until(
            EC.element_to_be_clickable(self.search_button)
        )
        self.driver.execute_script("arguments[0].scrollIntoView();", search_button_element)
        search_button_element.click()