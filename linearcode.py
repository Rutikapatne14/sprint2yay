# linear code of demowebshop

from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
path=r"C:\Users\ASUS\Desktop\driver_\chromedriver.exe"
driver = webdriver.Chrome(path)
driver.get("https://demowebshop.tricentis.com/")
time.sleep(2)
driver.maximize_window()


# to click on Apparel&shoes module
driver.find_element("xpath",'//a[@href="/apparel-shoes"]').click()   #apparel&shoes

# to click on Sort By dropdown
sortbyvar= driver.find_element("id","products-orderby")
selobj=Select(sortbyvar)
selobj.select_by_visible_text('Position')
time.sleep(5)

selobj.select_by_visible_text('Name: A to Z')
time.sleep(5)
driver.back()

selobj.select_by_visible_text('Name: Z to A')
time.sleep(5)
driver.back()

selobj.select_by_visible_text('Price: Low to High')
time.sleep(5)
driver.back()

selobj.select_by_visible_text('Price: High to Low')
time.sleep(5)
driver.back()

selobj.select_by_visible_text('Created on')
time.sleep(5)
driver.back()


# click on DisplayBy dropdown
displayvar= driver.find_element("xpath","//select[@id='products-pagesize']")
selobj1=Select(displayvar)
selobj1.select_by_value("https://demowebshop.tricentis.com/apparel-shoes?pagesize=4")
time.sleep(5)
driver.back()

selobj1.select_by_value("https://demowebshop.tricentis.com/apparel-shoes?pagesize=8")
time.sleep(5)
driver.back()

selobj1.select_by_index(2)
time.sleep(5)
driver.back()


# click on View As dropdown
viewas=driver.find_element("xpath","//select[@id='products-viewmode']")
selobj2=Select(viewas)
selobj2.select_by_visible_text('List')
time.sleep(5)
driver.back()

selobj2.select_by_visible_text('Grid')
time.sleep(5)
driver.back()



# click on each product to open it and see details
list1=["50's Rockabilly Polka Dot Top JR Plus Size","Blue and green Sneaker","Blue Jeans","Casual Golf Belt","Custom T-Shirt","Denim Short with Rhinestones","Genuine Leather Handbag with Cell Phone Holder & Many Pockets","Men's Wrinkle Free Long Sleeve","Sunglasses ","Women's Running Shoe","Wool Hat"]
for item in list1:
    driver.find_element("xpath",f'''//a[text()="{item}"]''').click()
    time.sleep(3)
    driver.back()
    time.sleep(3)


# to click on each product's add to cart button and check it is clickable or not
click_each_addtocart = driver.find_elements("xpath",f"//input[@value='Add to cart']")
for x in range(2,12):
    time.sleep(2)
    click_each_addtocart[x].click()
    time.sleep(2)





