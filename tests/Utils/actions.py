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