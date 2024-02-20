import time
import pytest
import os
import logging
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException

def test_open_login():
    driver = webdriver.Chrome()
    driver.get("https://www.amazon.in/")

    assert driver.current_url == "https://www.amazon.in/"

    search_box = driver.find_element(By.XPATH, "//input[@id='twotabsearchtextbox']")

    search_box.send_keys("16 gb")

    search_btn = driver.find_element(By.XPATH, "//input[@id='nav-search-submit-button']")
    search_btn.click()

    list_results = driver.find_elements(By.XPATH,"//span[@role='heading']")
    for i in list_results:
        print(i.text)


driver = webdriver.Chrome()
LOGGER = logging.info(__name__)

def waitForElements(waitInSeconds):
    wait = WebDriverWait(driver, waitInSeconds)
    return wait

def test_deviceNameListTest():

    driver.get("https://www.amazon.in/s?k=mobile+under+10000+128gb+storage&i=electronics&rh=n%3A1389432031%2Cp_89%3Arealme%2Cp_36%3A-500000&dc&crid=17THE8HJH9KC6&qid=1708421853&rnid=1318502031&sprefix=mobile+under+10000+1%2Caps%2C221&ref=sr_nr_p_36_1")

    waitForElements(15).until(EC.presence_of_element_located((By.CLASS_NAME, "a-size-medium")))
    devicesList = driver.find_elements(By.XPATH, "//div[@class='a-size-medium']")

    for device in devicesList:
        print(device.text)

    time.sleep(15)
    driver.quit()