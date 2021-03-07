from selenium import webdriver
from env import chrome_driver_path

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.python.org/")
dates = [time.text for time in driver.find_elements_by_css_selector(".event-widget time")]
print(dates)
events = [event.text for event in driver.find_elements_by_css_selector(".event-widget li a")]
print(events)

calendar = {}

for i in range(len(dates)):
    calendar[i] = {
        "date": dates[i],
        "name": events[i]
    }

print(calendar)

driver.close()
driver.quit()
