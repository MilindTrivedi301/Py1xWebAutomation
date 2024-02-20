import time

from selenium import webdriver
from selenium.webdriver.common.by import By

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


    time.sleep(5)
    driver.quit()