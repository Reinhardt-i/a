from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


class BookScript:
    def __init__(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get("https://book.spicejet.com/search.aspx")

        # Locate the departure dropdown and click
        departure = self.driver.find_element(By.NAME,
                                             "ControlGroupSearchView_AvailabilitySearchInputSearchVieworiginStation1_CTXT")
        departure.click()

        # Wait for the dropdown container element
        wait = WebDriverWait(self.driver, 5)
        dropdown_container = wait.until(EC.presence_of_element_located((By.ID, "dropdownGroup1")))

        # Find all country elements in the dropdown
        country_elements = dropdown_container.find_elements(By.CSS_SELECTOR, "ul li a")

        # Select Chennai (MAA) as departure city
        self.get_departure(country_elements, "Chennai (MAA)")

        # Select Delhi (DEL) as arrival city
        self.get_arrival(country_elements, "Delhi (DEL)")

        # Select date 20
        self.select_date(20)

        # Select currency BDT
        self.select_currency("BDT")

        # Click on the search button
        search_button = self.driver.find_element(By.XPATH,
                                                 "/html/body/div[19]/form/div[2]/div/div[2]/div[3]/div/div[11]/div/span/input")
        search_button.click()

    def get_departure(self, country_elements, departure_city):
        for country_element in country_elements:
            country_text = country_element.text
            print(country_text)

            if country_text == departure_city:
                country_element.click()

    def get_arrival(self, country_elements, arrival_city):
        for country_element in country_elements:
            country_text = country_element.text
            print(country_text)

            if country_text == arrival_city:
                country_element.click()

    def select_date(self, day):
        date_element = self.driver.find_element(By.XPATH, f'//a[@data-date="{day}"]')
        date_element.click()

    def select_currency(self, currency_name):
        currency = self.driver.find_element(By.XPATH,
                                            "/html/body/div[19]/form/div[2]/div/div[2]/div[3]/div/div[4]/p/select")
        dropdown_select = Select(currency)
        dropdown_select.select_by_visible_text(currency_name)


if __name__ == "__main__":
    book_script = BookScript()
