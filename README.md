# Py1x Web Automation Repo

## Install the Import lib
- selenium ( > 4)
- Pytest
- Allure Pytest
- Pytest HTML
- xdist - Run Parallel Execution
- logging - Logging (API lib)
- openpyxl - CSV, Excel
- Faker lib (Fake data generation)

pip install selenium pytest pytest-html allure-pytest 

## To Push the Git
1. git add .
2. git commit -m "Message"
3. git push
4. git pull ( if You have added somehting on Github.com)

## To run your Testcase Parallellyy

pip install pytest-xdist pytest -n auto code/8_JAN_2024/test_Lab14.py -s -v


## How Selenium works
-> Below displayed code will be converted to HTTP request(API) by using w3c protocol

from selenium import webdrivers

def test_open_login():                  ##request1

drover = webdriver.Chrome()              ##request2 (https://www.w3.org/TR/webdriver2/#new-session)

driveer.get("https://google.com") print(driver.title) ##request3

-> Here for all the request there is a POST request to selenium 4 server which creates a new session(Fresh browser)
https://www.w3.org/TR/webdriver2/#new-session

# code -> (Selenium 4 server) API request -> Brwoser Drivers -> Browsers