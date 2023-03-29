from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import TIME_SECONDS_UNIT


class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.logout_button = (By.CSS_SELECTOR, "div.container-buttons-home div[routerlink='auth/login'] button")
        self.menu_button = (By.XPATH, "//app-header/mat-toolbar[1]/div[1]/div[1]/div[1]/button[1]")
        self.search_information = (By.XPATH, "(//span[@class='mat-list-item-content'])[2]")
        self.violations = (By.CSS_SELECTOR, "a[href='#/ciascursos/infraccion/consulta-establecimiento']")
        self.organizations = (By.CSS_SELECTOR, "a[href='#/ciasconsultas/organismos/sin-cursos-comparendos']")

    def click_logout(self):
        # Esperar a que el botón de cierre de sesión esté presente y sea visible en la página
        logout_button_element = WebDriverWait(self.driver, TIME_SECONDS_UNIT).until(
            EC.presence_of_element_located(self.logout_button)
        )
        logout_button_element.click()

    def click_menu_button(self):
        # Esperar a que el botón de cierre de sesión esté presente y sea visible en la página
        menu_button_element = WebDriverWait(self.driver, TIME_SECONDS_UNIT).until(
            EC.presence_of_element_located(self.menu_button)
        )
        menu_button_element.click()
    
    def click_search_information_option(self):
        search_information_element = WebDriverWait(self.driver, TIME_SECONDS_UNIT).until(
            EC.presence_of_element_located(self.search_information)
        )
        search_information_element.click()
    
    def click_violations_option(self):
        violation_element = WebDriverWait(self.driver, TIME_SECONDS_UNIT).until(
            EC.element_to_be_clickable(self.violations)
        )
        violation_element.click()

    def click_organizations_option(self):
        organization_element = WebDriverWait(self.driver, TIME_SECONDS_UNIT).until(
            EC.element_to_be_clickable(self.organizations)
        )
        organization_element.click()