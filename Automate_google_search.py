from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Launch the Chrome browser and open Google
driver = webdriver.Chrome()
driver.get("https://www.google.com/")

try:
    # Wait for the search box to be present
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "q"))
    )

    # Enter a search query
    search_query = "Automating Google Search with Selenium Python"
    search_box.send_keys(search_query)
    search_box.send_keys(Keys.RETURN)

    # Wait for the search results page to load
    WebDriverWait(driver, 10).until(
        EC.title_contains(search_query)
    )

    # Wait for a few seconds to see the search results (you can adjust this based on your needs)
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//h3[@class='t']"))
    )

finally:
    # Close the browser
    driver.quit()