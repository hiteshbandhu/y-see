import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tqdm import tqdm

Y_COMB_URL = "https://www.ycombinator.com/companies?batch=S24&batch=W24&batch=S23&batch=W23&tags=Artificial%20Intelligence&tags=SaaS&tags=AI&tags=Developer%20Tools&tags=Generative%20AI&tags=Open%20Source&tags=AI%20Assistant&tags=API&tags=Machine%20Learning&tags=Enterprise%20Software&tags=Health%20Tech&tags=Crypto%20%2F%20Web3&tags=Social%20Media&tags=NLP&tags=Fintech&tags=Analytics&tags=Payments&tags=Computer%20Vision&tags=AIOps&tags=AI-Enhanced%20Learning&tags=Conversational%20AI&tags=Warehouse%20Management%20Tech&tags=HR%20Tech&tags=Hard%20Tech&tags=Food%20Tech&tags=Restaurant%20Tech&tags=Sports%20Tech&tags=Mental%20Health%20Tech&tags=Alternative%20Battery%20Tech&tags=Civic%20Tech"


driver = webdriver.Chrome()

# scroll to the bottom of the page
def scroll_to_bottom(driver):
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)  # Wait to load the page
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height


url = Y_COMB_URL  
driver.get(url)
time.sleep(5)  
scroll_to_bottom(driver)

# scrape the data
companies = []
company_elements = driver.find_elements(By.CLASS_NAME, '_company_86jzd_338')

for company_element in tqdm(company_elements, desc="Scraping companies"):
    try:
        href = company_element.get_attribute('href')
        company_name = company_element.find_element(By.CLASS_NAME, '_coName_86jzd_453').text
        location = company_element.find_element(By.CLASS_NAME, '_coLocation_86jzd_469').text
        description = company_element.find_element(By.CLASS_NAME, '_coDescription_86jzd_478').text
        taglinks = company_element.find_elements(By.CLASS_NAME, '_tagLink_86jzd_1023')
        taglinks_text = [tag.text for tag in taglinks]

        company_data = {
            'href': href,
            'company_name': company_name,
            'location': location,
            'description': description,
            'taglinks': taglinks_text
        }
        companies.append(company_data)
    except Exception as e:
        print(f"Error scraping a company: {str(e)}")

# save to file
with open('y_comb_companies_links.json', 'w') as file:
    json.dump(companies, file, indent=4)

driver.quit()



