from selenium.webdriver.common.by import By
from pageObjects.AdminOpportunitiesPage import AdminOpportunities

class AdminDashboardPage:

    def __init__(self, driver):
        self.driver = driver

    searchField = (By.CSS_SELECTOR, "input[id='search']")
    searchButton = (By.CSS_SELECTOR, "button[type='submit']")
    searchResultsOpp = (By.PARTIAL_LINK_TEXT, "Opportunities")

    def search_field(self):
        return self.driver.find_element(*AdminDashboardPage.searchField)

    def search_button(self):
        return self.driver.find_element(*AdminDashboardPage.searchButton)

    def search_results_opportunities_button(self):
        self.driver.find_element(*AdminDashboardPage.searchResultsOpp).click()
        opportunitiesPage = AdminOpportunities(self.driver)
        return opportunitiesPage




