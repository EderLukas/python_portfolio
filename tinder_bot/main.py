from selenium import webdriver
from env import chrome_driver_path, FACEBOOK
import time as t


driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://tinder.com/")

# Go to login
login_button = driver.find_element_by_xpath('//*[@id="t--1032254752"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/button')
t.sleep(5)
login_button.click()
t.sleep(3)

# Click login button via facebook
facebook = driver.find_element_by_xpath('//*[@id="t-1222506740"]/div/div/div[1]/div/div[3]/span/div[2]/button')
facebook.click()
t.sleep(8)

# Login at facebook
base_window = driver.window_handles[0]
fb_window = driver.window_handles[1]

driver.switch_to.window(fb_window)

email = driver.find_element_by_id("email")
email.send_keys(FACEBOOK["email"])
password = driver.find_element_by_id("pass")
password.send_keys(FACEBOOK["password"])
t.sleep(0.5)
login_button = driver.find_element_by_name("login")
login_button.click()

driver.switch_to.window(base_window)
t.sleep(8)

# Accept location tracking
accept_location = driver.find_element_by_xpath('//*[@id="t-1222506740"]/div/div/div/div/div[3]/button[1]')
accept_location.click()
t.sleep(2)
# disable notifications
disable = driver.find_element_by_xpath('//*[@id="t-1222506740"]/div/div/div/div/div[3]/button[2]')
disable.click()
t.sleep(2)

# turn down gold edition
gold = driver.find_element_by_xpath('//*[@id="t-1222506740"]/div/div/div/div[3]/button[2]')
gold.click()
t.sleep(3)

# Like next 10 girls
like_button = driver.find_element_by_xpath('//*[@id="t--1032254752"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')

for i in range(10):
    like_button.click()
    t.sleep(1)
    try:
        dicline_super_like = driver.find_element_by_xpath('//*[@id="t-1222506740"]/div/div/button[2]')
        dicline_super_like.click()
    except:
        pass

    try:
        dicline_start_menue = driver.find_element_by_xpath('//*[@id="t-1222506740"]/div/div/div[2]/button[2]')
        dicline_start_menue.click()
    except:
        pass

