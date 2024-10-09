from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
import os
import time
load_dotenv("C:/Python/Environmental variables/.env")
username = os.getenv("email")
password = os.getenv("password")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()

URL = "https://www.linkedin.com/?original_referer="
driver.get(URL)
time.sleep(2)
sign_in = driver.find_element(By.XPATH,value="/html/body/nav/div/a[1]")
sign_in.click()
time.sleep(1)
email_field = driver.find_element(By.ID,value="username")
password_field = driver.find_element(By.ID,value="password")
submit = driver.find_element(By.TAG_NAME,value="button")
time.sleep(2)
email_field.send_keys(username)
password_field.send_keys(password)
submit.click()

time.sleep(5)

jobs = driver.find_element(By.LINK_TEXT,value="Jobs")
jobs.click()

job_title = driver.find_element(By.CSS_SELECTOR,value=".jobs-search-box__inner")
location = driver.find_element(By.XPATH,value='//*[@id="jobs-search-box-location-id-ember226"]')

job_title.send_keys("Python Developer")
location.send_keys("Chennai",Keys.ENTER)
