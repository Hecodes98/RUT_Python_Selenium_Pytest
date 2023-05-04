from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Utils.actions import Actions
from selenium.common.exceptions import TimeoutException

from config import TIME_SECONDS_UNIT

class SchedulingPage:
    def __init__(self, driver):
        self.actions = Actions()
        self.driver = driver
        self.room_select_input = (By.XPATH, "//mat-select[@id='mat-select-0']")
        self.room_one_option = (By.XPATH, "//span[contains(text(),'Aula 1')]")
        self.day_option_button = (By.XPATH, "//button[contains(text(),'Día')]")
        self.agenda = (By.XPATH, "//button[contains(text(),'Agenda')]")
        self.next_option_button = (By.XPATH, "//button[contains(text(),'>')]")
        self.back_option_button = (By.XPATH, "//button[contains(text(),'<')]")
        self.time_selection_option = (By.XPATH, "//tbody/tr[7]/td[2]")
        self.instructor_select_input = (By.XPATH, "//mat-select[@id='mat-select-2']")
        self.first_instructor_option = (By.XPATH, "//span[contains(text(),'CYDEQ LQCELYS')]")
        self.accept_button = (By.XPATH, "//span[contains(text(),'Aceptar')]")
        self.init_time = (By.XPATH, "//mat-label[contains(text(),'Hora Inicio')]")
        self.error_message = (By.ID, "mat-error-1")


    def click_room_select_input(self):
        select_element = self.actions.element_to_be_clickable(driver=self.driver, element=self.room_select_input)
        select_element.click()
    
    def click_room_one_option(self):
        room_one_element = self.actions.element_to_be_clickable(driver=self.driver, element=self.room_one_option)
        room_one_element.click()
    
    def click_day_option(self):
        day_button_element = self.actions.element_to_be_clickable(driver=self.driver, element=self.day_option_button)
        day_button_element.click()

    def click_next_option(self):
        next_element = self.actions.element_to_be_clickable(driver=self.driver, element=self.next_option_button)
        next_element.click()

    def click_back_option(self):
        back_element = self.actions.element_to_be_clickable(driver=self.driver, element=self.back_option_button)
        back_element.click()

    def scroll_top(self):
        reference_element_to_scroll = self.actions.element_to_be_clickable(driver=self.driver, element=self.room_select_input)
        self.driver.execute_script("arguments[0].scrollIntoView();", reference_element_to_scroll)

    def click_record_violation_button(self):
        time_selection_element = self.actions.element_to_be_clickable(driver=self.driver, element=self.time_selection_option)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", time_selection_element)
        time_selection_element.click()

    def click_instruction_input_option(self):
        instructor_element = self.actions.element_to_be_clickable(driver=self.driver, element=self.instructor_select_input)
        instructor_element.click()
    
    def click_first_instructor_option(self):
        first_instructor_element = self.actions.element_to_be_clickable(driver=self.driver, element=self.first_instructor_option)
        first_instructor_element.click()
    
    def click_accept_button(self):
        accept_button_element = self.actions.element_to_be_clickable(driver=self.driver, element=self.accept_button)
        accept_button_element.click()

    def click_agenda(self):
        agenda_element = self.actions.element_to_be_clickable(driver=self.driver, element=self.agenda)
        agenda_element.click()

    def validate_inputs_appears(self):
        time_element = self.actions.element_to_be_clickable(driver=self.driver, element=self.init_time)
        return time_element.text
    
    def get_error_message(self):
        error_element = self.actions.element_to_be_clickable(driver=self.driver, element=self.error_message)
        return error_element.text