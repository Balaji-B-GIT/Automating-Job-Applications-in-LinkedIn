from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from dotenv import load_dotenv
import os
import time
# We are waiting for a specific time, because the page can load.
load_dotenv("C:/Python/Environmental variables/.env")
username = os.getenv("email")
password = os.getenv("password")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

linkedin = webdriver.Chrome(options=chrome_options)
linkedin.maximize_window()

URL = "https://www.linkedin.com/"
linkedin.get(URL)

time.sleep(2)

sign_in = linkedin.find_element(By.LINK_TEXT,value="Sign in")
sign_in.click()

time.sleep(2)

email_field = linkedin.find_element(By.ID,value="username")
password_field = linkedin.find_element(By.ID,value="password")
# submit = linkedin.find_element(By.CSS_SELECTOR,value=".login__form_action_container button")

email_field.send_keys(username)
password_field.send_keys(password,Keys.ENTER)
# submit.click()

time.sleep(2)

# jobs = driver.find_element(By.LINK_TEXT,value="Jobs")
# jobs.click()

# The below url is the url of linkedin with job filters applied to it.
# You might think we can go to this page after logged in but we cant. Because, after logged in we cant find job filters in job section.
# So, here i just opened new linkedin page with applied job filters after logged in, so it doesnt ask to log in again.
jobs_url = "https://www.linkedin.com/jobs/search/?currentJobId=4039135429&distance=100&f_AL=true&geoId=105214831&keywords=python%20intern&origin=JOB_SEARCH_PAGE_KEYWORD_AUTOCOMPLETE&refresh=true"
linkedin.get(jobs_url)

time.sleep(5)

jobs_ul = linkedin.find_element(By.CLASS_NAME,value = "scaffold-layout__list-container")
list_of_jobs = jobs_ul.find_elements(By.CLASS_NAME,value="ember-view.jobs-search-results__list-item.occludable-update.p0.relative.scaffold-layout__list-item")
list_of_job_applied = set()

for job in list_of_jobs:
    try:
        title = job.find_element(By.TAG_NAME,value="strong").text
        # The below line of code is to scroll down
        linkedin.execute_script("arguments[0].scrollIntoView(true);", job)
        job.click()

        time.sleep(2)

        save = linkedin.find_element(By.CLASS_NAME,value="jobs-save-button")
        save_text = save.text.lower()
        if "saved" in save_text or "unsave" in save_text:
            print("Job already saved, skipping.")
        else:
            save.click()
            print(f"A job for the role {title} has saved")

            time.sleep(2)

        list_of_job_applied.add(title)
    except NoSuchElementException:
        print("No application button, skipped.")
        continue
print(list_of_job_applied)