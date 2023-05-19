from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from config import TIME_SECONDS_UNIT


class Actions:
    def element_to_be_clickable(self, driver, element):
        try:
            return WebDriverWait(driver, TIME_SECONDS_UNIT).until(
                EC.element_to_be_clickable(element)
            )
        except TimeoutException:
            raise Exception(f"El elemento: {element}, no es clickeable después de {TIME_SECONDS_UNIT}")
    
<<<<<<< HEAD
<<<<<<< HEAD
    def presence_of_all_elements_located(self, driver, element):
        try:
            return WebDriverWait(driver, TIME_SECONDS_UNIT).until(
                EC.presence_of_all_elements_located(element)
            )
        except TimeoutException:
            raise Exception(f"Los elementos: {element}, no son localizables en la página luego de {TIME_SECONDS_UNIT}")
    
=======
=======
>>>>>>> 1e06bb2d134eaf1f772cfea721b9555c7534f202
    def get_random_element_from_a_list_of_elemenets (self, driver, element):
        try:
            elements = WebDriverWait(driver, TIME_SECONDS_UNIT).until(
                EC.presence_of_all_elements_located(element)
            )
            return elements[0]
        except TimeoutException:
            raise Exception(f"No hay elemenetos: {element}, después de {TIME_SECONDS_UNIT}")
    
    def get_a_list_of_elemenets (self, driver, element):
        try:
            elements = WebDriverWait(driver, TIME_SECONDS_UNIT).until(
                EC.presence_of_all_elements_located(element)
            )
            return elements
        except TimeoutException:
            raise Exception(f"No hay elemenetos: {element}, después de {TIME_SECONDS_UNIT}")
    
<<<<<<< HEAD
>>>>>>> 1e06bb2d134eaf1f772cfea721b9555c7534f202
=======
>>>>>>> 1e06bb2d134eaf1f772cfea721b9555c7534f202
