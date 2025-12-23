import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.driver_cache import DriverCacheManager

# Cache driver locally
# cache_root = os.path.join(os.getcwd(), "drivers")
os.makedirs(os.path.join(cache_root, ".wdm"), exist_ok=True)
cache_manager = DriverCacheManager(root_dir=cache_root)

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager(cache_manager=cache_manager).install())
)

iphone = {
    'model': [],
    'rating': [],
    'reviews': []
}

driver.get("https://www.amazon.in/s?k=iphone&i=electronics&rh=n%3A1389401031&ref=sr_pg_2")


#iphone_models = driver.find_elements(By.CSS_SELECTOR, "span.a-text-normal")
iphone_ratings = driver.find_elements(By.CSS_SELECTOR, "span.a-size-small.a-color-base")
iphone_reviews = driver.find_elements(By.CSS_SELECTOR, "span.a-size-mini.puis-normal-weight-text.s-underline-text")

for  rating, review in zip( iphone_ratings, iphone_reviews):
    #iphone['model'].append(model.text.strip())
    iphone['rating'].append(rating.text.strip())
    iphone['reviews'].append(review.text.strip())

#print(len(iphone['model']))
for i in range(len(iphone['rating'])):

    print( iphone['rating'][i], iphone['reviews'][i])

driver.quit()
