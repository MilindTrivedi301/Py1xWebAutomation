import time

from selenium import webdriver


# Chrome -> # Chrome Options
# Edge -> Edge Options
# Firefox -> Firefox Options

def test_open_login():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com")
    time.sleep(5)
    driver.quit()