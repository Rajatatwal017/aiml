import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.driver_cache import DriverCacheManager

# Cache driver locally
cache_root = os.path.join(os.getcwd(), "drivers")
os.makedirs(os.path.join(cache_root, ".wdm"), exist_ok=True)
cache_manager = DriverCacheManager(root_dir=cache_root)

driver = webdriver.Chrome(
    service=Service(
        ChromeDriverManager(cache_manager=cache_manager).install()
    )
)

company = {
    'company_name': [],
    'rating': [],
    'reviews': [],
    'locations': [],
    'salaries': [],
    'interviews': [],
    'benefits': []
}

driver.get("https://www.ambitionbox.com/list-of-companies?page=1")

companies_names = driver.find_elements(By.CSS_SELECTOR, 'h2.companyCardWrapper__companyName')
companies_rating = driver.find_elements(By.CSS_SELECTOR, '.rating_text.rating_text--md div')
companies_reviews = driver.find_elements(By.CSS_SELECTOR, 'span.companyCardWrapper__ActionCount')
companies_locations = driver.find_elements(By.CSS_SELECTOR, 'span.companyCardWrapper__interLinking')
companies_salaries = driver.find_elements(By.CSS_SELECTOR, 'span.companyCardWrapper__ActionTitle')
companies_interviews = driver.find_elements(By.CSS_SELECTOR, 'span.companyCardWrapper__ActionTitle')
companies_benefits = driver.find_elements(By.CSS_SELECTOR, 'span.companyCardWrapper__ActionTitle')

for company_name, company_rating, company_review, company_location, company_salary, company_interview, company_benefit in zip(
    companies_names, companies_rating, companies_reviews, companies_locations, companies_salaries, companies_interviews, companies_benefits
):
    company['company_name'].append(company_name.text.strip())
    company['rating'].append(company_rating.text.strip())
    company['reviews'].append(company_review.text.strip())
    company['locations'].append(company_location.text.strip())
    company['salaries'].append(company_salary.text.strip())
    company['interviews'].append(company_interview.text.strip())
    company['benefits'].append(company_benefit.text.strip())

for i in range(len(company['company_name'])):
    print(
        company['company_name'][i],
        company['rating'][i],
        company['reviews'][i],
        company['locations'][i],
        company['salaries'][i],
        company['interviews'][i],
        company['benefits'][i]
    )


driver.quit()