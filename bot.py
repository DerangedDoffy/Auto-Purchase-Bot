# Log into the site with product 
# Find product under X amount 
# If product unavailable, wait until availability 
# Add product to cart 
# Add payment 
# Checkout 

import time
from selenium import webdriver 

# For using Chrome
browser = webdriver.Chrome('D:\\Downloads\\chromedriver_win32\\chromedriver.exe')

# BestBUy RTX 3080 page 
browser.get("https://www.bestbuy.com/site/nvidia-geforce-rtx-3070-8gb-gddr6-pci-express-4-0-graphics-card-dark-platinum-and-black/6429442.p?skuId=6429442")

buyButton = False

while not buybutton: 
    try:
        addToCartBtn = addButton = browser.find_element_by_class_name("btn-disabled")
        print("Button isn't ready yet.")
        time.sleep(1)
        browser.refresh()
    except:
        addToCartBtn = addButton = browser.find_element_by_class_name("btn-primary")
