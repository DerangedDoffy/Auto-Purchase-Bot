from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome("insert")     # file location

driver.get('https://www.bestbuy.com/site/nvidia-geforce-rtx-3060-ti-8gb-gddr6-pci-express-4-0-graphics-card-steel-and-black/6439402.p?skuId=6439402')

def time1():
    return time.sleep(1)

def time2():
    return time.sleep(2)

def time3():
    return time.sleep(3)

buyButton = False

while not buyButton: 
    try:
        
        addToCartBtn = driver.find_element_by_class_name("btn-disabled")     # element "btn-disabled" is when it's out of stock
        time.sleep(60)      # sleeps for 60 seconds 
        driver.refresh()   #refreshes page
    
    except:  

        addToCartBtn = driver.find_element_by_class_name('btn-primary')   # element "btn-primary" is when it's in stock
        addToCartBtn.click()    # clicks the add to cart button 
        print('In stock!')
        print("Attempting to add to cart")
        newBtn = driver.find_element_by_class_name('btn-primary')
        newBtn.click
        buyButton = True       # ends the loop
        
driver.get("https://www.bestbuy.com/cart")  # cart button 

time1()

shipping = driver.find_element_by_xpath("//*[starts-with(@id,'fulfillment-shipping-')]")
shipping.click()

print('Shipping clicked')

time2()

checkoutBtn = driver.find_element_by_class_name('btn-primary')
checkoutBtn.click()

print('Entering checkout')

time2()

email_enter = 'insert'
email_input = driver.find_element_by_id('fld-e')

email_input.send_keys(email_enter)

passwd_enter = 'insert'
passwd_input = driver.find_element_by_id('fld-p1')

passwd_input.send_keys(passwd_enter)

sign_in = driver.find_element_by_xpath('/html/body/div[1]/div/section/main/div[2]/div[1]/div/div/div/div/form/div[3]/button')
sign_in.click()

time2()

print('Entering information')

fname_enter = 'insert' 
fname_input = driver.find_element_by_xpath('//*[@id="consolidatedAddresses.ui_address_2.firstName"]')

fname_input.send_keys(fname_enter)      # enters fname_enter into fname_input

lname_enter = 'insert'
lname_input = driver.find_element_by_xpath('//*[@id="consolidatedAddresses.ui_address_2.lastName"]')

lname_input.send_keys(lname_enter)

address_enter = 'insert'
address_input = driver.find_element_by_xpath('//*[@id="consolidatedAddresses.ui_address_2.street"]')

address_input.send_keys(address_enter)

hide = driver.find_element_by_class_name('autocomplete__toggle')
hide.click()        # clicks hide suggestions 

city_enter = 'insert'
city_input = driver.find_element_by_xpath('//*[@id="consolidatedAddresses.ui_address_2.city"]')

city_input.send_keys(city_enter)

select_state = Select(driver.find_element_by_xpath('//*[@id="consolidatedAddresses.ui_address_2.state"]'))
select_state.select_by_index('insert')  # selects state by numbered index order ex: (12,13,14)

zipCode = 'insert'
zip_input = driver.find_element_by_xpath('//*[@id="consolidatedAddresses.ui_address_2.zipcode"]')
  
zip_input.send_keys(zipCode)

Continue = driver.find_element_by_xpath('//*[@id="checkoutApp"]/div[2]/div[1]/div[1]/main/div[2]/div[2]/form/section/div/div[2]/div/div/button')
Continue.click()

time3()

security = 'insert'
security_input = driver.find_element_by_xpath('//*[@id="credit-card-cvv"]')

security_input.send_keys(security)

final_order = driver.find_element_by_xpath('//*[@id="checkoutApp"]/div[2]/div[1]/div[1]/main/div[2]/div[3]/div/section/div[4]/button')
final_order.click()

print('Order placed')
