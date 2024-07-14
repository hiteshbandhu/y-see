import json
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm
from time import sleep

def scrape_company(company):
    try:
        url = f"https://r.jina.ai/{company['href']}"
        response = requests.get(url)
        sleep(2)
        response.raise_for_status()  # Raises a HTTPError if the status is 4xx, 5xx

        return {
            'name': company['company_name'],
            'link': company['href'],
            'short_description': company['description'],
            'long_description': response.text  # This will be the full Markdown content
        }
    except requests.RequestException as e:
        print(f"Error scraping {company['href']}: {str(e)}")
        return None

# Load the existing JSON file
with open('links.json', 'r') as file:
    companies = json.load(file)

detailed_companies = []

# Use ThreadPoolExecutor for parallel scraping
with ThreadPoolExecutor(max_workers=3) as executor:
    future_to_company = {executor.submit(scrape_company, company): company for company in companies}
    
    for future in tqdm(as_completed(future_to_company), total=len(companies), desc="Scraping company descriptions"):
        result = future.result()
        if result:
            detailed_companies.append(result)

# Save the detailed data to a new JSON file
with open('y_comb_company_detail.json', 'w', encoding='utf-8') as file:
    json.dump(detailed_companies, file, indent=4, ensure_ascii=False)

print(f"Scraping completed. Details saved for {len(detailed_companies)} companies.")