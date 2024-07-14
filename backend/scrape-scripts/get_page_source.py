import time
from selenium import webdriver


driver = webdriver.Chrome()

url = 'https://www.ycombinator.com/companies/elayne'
driver.get(url)
time.sleep(5) 

page_source = driver.page_source

with open('page_source.html', 'w', encoding='utf-8') as file:
    file.write(page_source)

driver.quit()
