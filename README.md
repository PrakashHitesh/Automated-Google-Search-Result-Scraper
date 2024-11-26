# Google Search Results Scraper

## Description

This project is a Python-based web scraper that uses Selenium to automate Google searches and extract search results (titles, links, and descriptions). The scraped data is saved into a CSV file for easy access and analysis.

## Features

  - Automates Google search for a user-provided query.
  - Scrapes search results including:
     + Title
     + Link
     + Description
  - Saves the scraped results in a CSV file (google_results.csv).

## Technologies Used

  - Python: Programming language used for the script.
  - Selenium: Used for web automation and scraping.
  - CSV: For storing search results in a structured format.

## Prerequisites

  - Python 3.x installed on your system.
  - Google Chrome installed.
  - ChromeDriver compatible with your Chrome version.


## Installation and Setup

  1. Clone this repository or download the script.
  2. Install the required Python packages:
            
            
         pip install selenium

 3. Update the chromedriver_path variable in the script with the path to your ChromeDriver.
    
        chromedriver_path = "C:\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe"  


## Usage

  1. Run the script:
     
         python scraper.py

 2. Enter a search query when prompted.
 3. The script will scrape Google search results and save them in a file named google_results.csv in the same directory as the script.
 4. Open the google_results.csv file to view the results.


## Notes

  - The script automatically handles Google's cookie consent banner (if present).
  - If Google blocks automation, consider using proxies or rotating user-agents to avoid detection.

## License

This project is licensed under the MIT License.
