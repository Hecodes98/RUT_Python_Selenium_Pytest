from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import TIME_SECONDS_UNIT

import time

class FacilityManagerPage:
    def __init__(self, driver):
        self.driver = driver
        self.close_error_button = (By.XPATH, "//button[contains(text(),'Aceptar')]")
        self.new_room_button = (By.XPATH, "//span[contains(text(),'Nueva Sala')]")
        self.name_textbox = (By.CSS_SELECTOR, "input#mat-input-1")
        self.capacity_textbox = (By.CSS_SELECTOR, "input#mat-input-2")
        self.save_button = (By.XPATH, "//span[contains(text(),'Guardar')]")
        self.accept_modal_button = (By.XPATH, "//button[contains(text(),'Aceptar')]")



    def click_accept_button_for_close_error_modal(self):
        close_modal = WebDriverWait(self.driver, TIME_SECONDS_UNIT).until(
            EC.element_to_be_clickable(self.close_error_button)
        )
        close_modal.click()
    
    def click_new_room_button(self):
        new_room_element = WebDriverWait(self.driver, TIME_SECONDS_UNIT).until(
            EC.presence_of_element_located(self.new_room_button)
        )
        new_room_element.click()
    
    def fill_name_textbox(self, name):
        name_textbox_element = WebDriverWait(self.driver, TIME_SECONDS_UNIT).until(
            EC.presence_of_element_located(self.name_textbox)
        )
        name_textbox_element.send_keys(name)

    def fill_capacity_textbox(self, capacity):
        capacity_textbox_element = WebDriverWait(self.driver, TIME_SECONDS_UNIT).until(
            EC.presence_of_element_located(self.capacity_textbox)
        )
        capacity_textbox_element.send_keys(capacity)

    def click_save_button(self):
        save_button_element = WebDriverWait(self.driver, TIME_SECONDS_UNIT).until(
            EC.element_to_be_clickable(self.save_button)
        )
        save_button_element.click()
    
    def click_accept_modal_button_twice(self):
        accept_modal_button_element = WebDriverWait(self.driver, TIME_SECONDS_UNIT).until(
            EC.element_to_be_clickable(self.accept_modal_button)
        )
        accept_modal_button_element.click()
        accept_modal_button_element = WebDriverWait(self.driver, TIME_SECONDS_UNIT).until(
            EC.element_to_be_clickable(self.accept_modal_button)
        )
        accept_modal_button_element.click()
