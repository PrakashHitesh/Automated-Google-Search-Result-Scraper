import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Path to chromedriver (update this to your actual path)
chromedriver_path = "C:\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe"
service = Service(chromedriver_path)
driver = webdriver.Chrome(service=service)

driver.get("https://www.google.com")

# Accept cookies if prompted
try:
    accept_cookies_button = driver.find_element(By.XPATH, "//button[text()='I agree']")
    accept_cookies_button.click()
    time.sleep(2)
except:
    pass  

# Search for a query
query = input("Enter your search query: ")
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys(query)
search_box.send_keys(Keys.RETURN)

time.sleep(2)

# Scrape search results
results = driver.find_elements(By.CSS_SELECTOR, "div.tF2Cxc")
search_results = []

for idx, result in enumerate(results, start=1):  # Enumerate to show result numbers
    try:
        title = result.find_element(By.CSS_SELECTOR, "h3").text
    except:
        title = "No Title"
    try:
        link = result.find_element(By.CSS_SELECTOR, "a").get_attribute("href")
    except:
        link = "No Link"
    try:
        description = result.find_element(By.CSS_SELECTOR, "span.aCOpRe").text
    except:
        description = "No Description"

    # Add result to the list
    search_results.append({"Title": title, "Link": link, "Description": description})

    # Display results in a well-mannered way
    print(f"\nResult {idx}:")
    print(f"Title       : {title}")
    print(f"Link        : {link}")
    print(f"Description : {description}")
    print("-" * 50)

# Write results to CSV
csv_file = "google_results.csv"
with open(csv_file, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["Title", "Link", "Description"])
    writer.writeheader()
    writer.writerows(search_results)

print(f"\nResults saved to '{csv_file}'")

# Close the browser
driver.quit()
