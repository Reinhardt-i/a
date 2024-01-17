from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()

# Maximize the browser window
driver.maximize_window()

# Navigate to the website
driver.get("https://book.spicejet.com/search.aspx")

try:
    # Wait for the "Departure City" dropdown to be clickable
    departure_city_dropdown = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'select[name="ControlGroupSearchView$AvailabilitySearchInputSearchVieworiginStation1"]'))
    )

    # Click on "Departure City" dropdown
    departure_city_dropdown.click()

    # Select "Chennai (MMA)" from the dropdown
    chennai_option = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, '//option[text()="Chennai (MMA)"]'))
    )
    chennai_option.click()

    # Wait for the "Arrival City" dropdown to be clickable
    arrival_city_dropdown = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'select[name="ControlGroupSearchView$AvailabilitySearchInputSearchViewdestinationStation1"]'))
    )

    # Click on "Arrival City" dropdown
    arrival_city_dropdown.click()

    # Select "Delhi (DEL)" from the dropdown
    delhi_option = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, '//option[text()="Delhi (DEL)"]'))
    )
    delhi_option.click()

    # Select "20" as the depart date
    depart_date_dropdown = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//option[@value="20"]'))
    )
    depart_date_dropdown.click()

    # Select "BDT" as currency
    currency_dropdown = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'select[name="ControlGroupSearchView$AvailabilitySearchInputSearchView_DropDownListCurrency"]'))
    )
    currency_dropdown.send_keys("BDT")

    # Click on the flight icon to search for the flight
    search_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[value="Search Flights"]'))
    )
    search_button.click()

finally:
    # Close the WebDriver
    driver.quit()
