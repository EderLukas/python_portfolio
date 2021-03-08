from selenium import webdriver
from env import chrome_driver_path, LINKED_IN
import time as t


URL = "https://www.linkedin.com/jobs/search?keywords=Python%20Entwickler&location=Schweiz&geoId=&trk=public_jobs_jobs-search-bar_search-submit&redirect=false&position=1&pageNum=0"

# Get Job list from url
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(URL)

# Click on save button of first listed job opportunity
t.sleep(3)
save_button = driver.find_element_by_css_selector(".save-job-modal-outlet")
save_button.click()
t.sleep(1)

# Enter email to go to login process
input = driver.find_element_by_id("public_jobs_save-job_email-input")
input.send_keys(LINKED_IN["email"])
t.sleep(0.5)
proceed_button = driver.find_element_by_css_selector(".save-job-form__button")
proceed_button.click()

# Click Login link
t.sleep(1)
login_link = driver.find_element_by_css_selector(".main__sign-in-link")
login_link.click()
t.sleep(1)

# Login
username = driver.find_element_by_id("username")
username.send_keys(LINKED_IN["email"])
password = driver.find_element_by_id("password")
password.send_keys(LINKED_IN["password"])
login_button = driver.find_element_by_css_selector(".login__form_action_container button")
login_button.click()
t.sleep(3)

# Save job description / set to tracking
save_job = driver.find_element_by_css_selector(".jobs-save-button")
save_job.click()
