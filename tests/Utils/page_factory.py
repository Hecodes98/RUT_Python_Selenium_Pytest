from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.search_information_page import SearchInformationPage
from pages.organizations_page import OrganizationsPage
from pages.facility_manager import FacilityManagerPage

class PageFactory:
    @staticmethod
    def create_page(driver, page_name):
        if page_name == "login":
            return LoginPage(driver)
        elif page_name == "home":
            return HomePage(driver)
        elif page_name == "search_info":
            return SearchInformationPage(driver)
        elif page_name == "organizations":
            return OrganizationsPage(driver)
        elif page_name == "facility_manager":
            return FacilityManagerPage(driver)
        else:
            raise ValueError("Page not found: " + page_name)
