#all functions
import time
import pytest
from Data import reading_objects
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

ASobj = reading_objects.read_locators_from_excel()

class Apparelshoes:
    def __init__(self, driver):
        self.driver = driver

# click on Apparel module
    def clickmodule(self):
        self.driver.find_element(*ASobj['beginbtn']).click()

# click on sortby dropdown AtoZ
    def clicksortbyatoz(self):
        ele = self.driver.find_element(*ASobj['sortbyvar'])
        selobj = Select(ele)
        selobj.select_by_visible_text('Name: A to Z')
        time.sleep(2)
        actionobj = ActionChains(self.driver)
        actionobj.send_keys(Keys.PAGE_DOWN).perform()
        time.sleep(2)
        actionobj.send_keys(Keys.PAGE_UP).perform()
        time.sleep(2)

# sort by ZtoA
    def clicksortbyztoa(self):
        ele = self.driver.find_element(*ASobj['sortbyvar'])
        selobj = Select(ele)
        selobj.select_by_visible_text('Name: Z to A')
        time.sleep(2)
        actionobj = ActionChains(self.driver)
        actionobj.send_keys(Keys.PAGE_DOWN).perform()
        time.sleep(2)
        actionobj.send_keys(Keys.PAGE_UP).perform()
        time.sleep(2)

# sort by Price:Low to High
    def clicksortbylowtohigh(self):
        ele = self.driver.find_element(*ASobj['sortbyvar'])
        selobj = Select(ele)
        selobj.select_by_visible_text('Price: Low to High')
        time.sleep(2)
        actionobj = ActionChains(self.driver)
        actionobj.send_keys(Keys.PAGE_DOWN).perform()
        time.sleep(2)
        actionobj.send_keys(Keys.PAGE_UP).perform()
        time.sleep(2)

# sort by Price:High to Low
    def clicksortbyhightolow(self):
        ele = self.driver.find_element(*ASobj['sortbyvar'])
        selobj = Select(ele)
        selobj.select_by_visible_text('Price: High to Low')
        time.sleep(2)
        actionobj = ActionChains(self.driver)
        actionobj.send_keys(Keys.PAGE_DOWN).perform()
        time.sleep(2)
        actionobj.send_keys(Keys.PAGE_UP).perform()
        time.sleep(2)

# sort by CreatedOn
    def clicksortbycreatedon(self):
        ele = self.driver.find_element(*ASobj['sortbyvar'])
        selobj = Select(ele)
        selobj.select_by_visible_text('Created on')
        time.sleep(2)
        actionobj = ActionChains(self.driver)
        actionobj.send_keys(Keys.PAGE_DOWN).perform()
        time.sleep(2)
        actionobj.send_keys(Keys.PAGE_UP).perform()
        time.sleep(2)

# click on Displayby dropdown :4
    def clickdisplayfour(self):
        ele = self.driver.find_element(*ASobj['displayvar'])
        disobj = Select(ele)
        disobj.select_by_value("https://demowebshop.tricentis.com/apparel-shoes?pagesize=4")
        time.sleep(2)
        actionobj = ActionChains(self.driver)
        actionobj.send_keys(Keys.PAGE_DOWN).perform()
        time.sleep(2)
        actionobj.send_keys(Keys.PAGE_UP).perform()
        time.sleep(2)

# click on Displayby dropdown:8
    def clickdisplayeight(self):
        ele = self.driver.find_element(*ASobj['displayvar'])
        disobj = Select(ele)
        disobj.select_by_value("https://demowebshop.tricentis.com/apparel-shoes?pagesize=8")
        time.sleep(2)
        actionobj = ActionChains(self.driver)
        actionobj.send_keys(Keys.PAGE_DOWN).perform()
        time.sleep(2)
        actionobj.send_keys(Keys.PAGE_UP).perform()
        time.sleep(2)

# click on Displayby dropdown :12
    def clickdisplaytwelve(self):
        ele = self.driver.find_element(*ASobj['displayvar'])
        disobj = Select(ele)
        disobj.select_by_index(2)
        time.sleep(2)
        actionobj = ActionChains(self.driver)
        actionobj.send_keys(Keys.PAGE_DOWN).perform()
        time.sleep(2)
        actionobj.send_keys(Keys.PAGE_UP).perform()
        time.sleep(2)


# click on View As dropdown : List
    def clickviewaslist(self):
        ele = self.driver.find_element(*ASobj['viewas'])
        viewasobj = Select(ele)
        viewasobj.select_by_visible_text('List')
        time.sleep(2)
        actionobj = ActionChains(self.driver)
        actionobj.send_keys(Keys.PAGE_DOWN).perform()
        time.sleep(2)
        actionobj.send_keys(Keys.PAGE_UP).perform()
        time.sleep(2)

# click on View As dropdown : Grid
    def clickviewasgrid(self):
        ele = self.driver.find_element(*ASobj['viewas'])
        viewasobj = Select(ele)
        viewasobj.select_by_visible_text('Grid')
        time.sleep(2)
        actionobj = ActionChains(self.driver)
        actionobj.send_keys(Keys.PAGE_DOWN).perform()
        time.sleep(2)
        actionobj.send_keys(Keys.PAGE_UP).perform()
        time.sleep(2)

# to click  on each product and open  it to see details
    def clickopenproduct(self):
        list1 = ["50's Rockabilly Polka Dot Top JR Plus Size", "Blue and green Sneaker", "Blue Jeans", "Casual Golf Belt", "Custom T-Shirt", "Denim Short with Rhinestones", "Genuine Leather Handbag with Cell Phone Holder & Many Pockets", "Men's Wrinkle Free Long Sleeve", "Sunglasses ", "Women's Running Shoe", "Wool Hat"]
        for item in list1:
            self.driver.find_element("xpath", f'''//a[text()="{item}"]''').click()
            time.sleep(3)
            self.driver.back()
            time.sleep(3)

# to click on each product's add to cart button and check it is clickable or not
    def click_eachproducts_addtocart(self):
        click_each_addtocart = self.driver.find_elements("xpath", f"//input[@value='Add to cart']")
        for x in range(2,):
            time.sleep(2)
            click_each_addtocart[x].click()
            time.sleep(2)










