from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from env import chrome_driver_path

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://en.wikipedia.org/wiki/Main_Page")
english_article_count = driver.find_element_by_css_selector("#articlecount a")
#english_article_count.click()

search = driver.find_element_by_name("search")
search.send_keys("python")
search.send_keys(Keys.ENTER)

# driver.quit()