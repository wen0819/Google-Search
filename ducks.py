from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
page = ("https://www.google.com")

class ducks_search():

    def __init__(self,driver):
        self.driver = driver

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(page)

    def ducks():

        print("TC#1_launch Google and print out page title")
        driver.get(page)
        print("*** Google page title: " + driver.title)
        print("\n")

        print("TC#2_Enter search keyword 'ducks' and submit search request: ")
        search = driver.find_element_by_name("q")
        search.clear()
        search.send_keys("ducks")
        search.submit()
        print("*** Successful submitted the search request. \n ")

        print("TC#3_List the search results for 'ducks':")
        for element in driver.find_elements_by_xpath('//div[@class="yuRUbf"]'):
            print(element.text)
        print("*** Successful display google search results for 'ducks'. \n")


        print("TC#4_List the search results for 'People also ask' and 'See results about:'")
        for element in driver.find_elements_by_xpath('//div[@class="ifM9O"]'):
            print(element.text)
        print("*** Successful list 'People also ask' and 'See results about' articles above. \n")

        print("TC#5_Verify redirect URL: link from ducks result page to Wikipedia page: ")
        driver.find_element_by_link_text("Wikipedia").click()
        time.sleep(3)
        print("*** Successful redirects to Wikipedia page: \n" + driver.current_url)
        print("\n")
        driver.back()

        print("TC#6_View ducks search result via 'View all' link: ")
        Link = driver.find_element_by_link_text("View all")
        Link.click()
        print("***  Successful redirect ducks related info on 'View all' page:: \n " + driver.current_url)
        driver.back()
        print("\n")

        print("TC#7_Verify redirect via 'Images' menu item, open ducks image page: ")
        Link = driver.find_element_by_link_text("Images")
        Link.click()
        print("*** Successful redirects to ducks 'Images' page: \n " + driver.current_url)
        driver.back()
        print("\n")

        print("TC#8_Verify redirect via 'Videos' menu item, open ducks video page: ")
        Link = driver.find_element_by_link_text("Videos")
        Link.click()
        print("*** Successful redirects to ducks videos page: \n " + driver.current_url)
        driver.back()
        print("\n")

        print("TC#9_Verify redirect via 'Shopping' menu item, open ducks shopping page: ")
        Link = driver.find_element_by_link_text("Shopping")
        Link.click()
        print("*** Successful redirects to ducks shopping page: \n " + driver.current_url)
        driver.back()
        print("\n")

        print("TC#10_Verify redirect via 'News' menu item, open ducks news page: ")
        Link = driver.find_element_by_link_text("News")
        Link.click()
        print("*** Successful redirects to ducks related news page: \n " + driver.current_url)
        driver.back()
        print("\n")

        print("TC#11_Verify navigation bar at bottom of page, ensure 'Next' & 'Previous' keys are working fine: ")
        Link = driver.find_element_by_link_text("Next")
        Link.click()
        print("*** Successful go to the next page_2: \n " + driver.current_url)
        Link = driver.find_element_by_link_text("Previous")
        Link.click()
        print("*** Successful go back previous page_1: \n " + driver.current_url)
        print("\n")

    ducks()
    driver.quit()
