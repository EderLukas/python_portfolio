from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from env import chrome_driver_path

driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("http://secure-retreat-92358.herokuapp.com/")
first_name_field = driver.find_element_by_name("fName")
first_name_field.send_keys("Lukas")
last_name_field = driver.find_element_by_name("lName")
last_name_field.send_keys("Eder")
email_field = driver.find_element_by_name("email")
email_field.send_keys("eder.lukas@bluewin.ch")
sign_up_button = driver.find_element_by_xpath('/html/body/form/button')
sign_up_button.send_keys(Keys.ENTER)