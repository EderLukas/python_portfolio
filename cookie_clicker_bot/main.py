from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from env import chrome_driver_path
import time as t

SLEEP = 0.1


driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("http://orteil.dashnet.org/experiments/cookie/")
cookie = driver.find_element_by_id("cookie")
upgrade_bar = driver.find_element_by_id("store")

timeout = t.time() + 60 * 5
five_second = t.time() + 5
while True:
    cookie.click()

    if t.time() > five_second:
        # reset timer for 5 seconds to check upgrades
        five_second = t.time() + 5

        # Make a list of upgrades
        upgradeable_ids = []
        for upgrade in upgrade_bar.find_elements_by_css_selector("div"):
            if not upgrade.get_attribute("class") == "grayed" and not upgrade.get_attribute("class") == "amount":
                upgradeable_ids.append(upgrade.get_attribute("id"))
        # go through list of possible upgrades and click them if they
        # are affordable (reverse order of list)
        for i in range(len(upgradeable_ids) - 1, -1, -1):
            t.sleep(SLEEP)
            upgrade_price_tag = driver.find_element_by_css_selector(f"#{upgradeable_ids[i]} b").text
            price_string = upgrade_price_tag.split(" ")[2]
            try:
                if price_string.index(","):
                    price_string = price_string.replace(",", "")
            except ValueError:
                pass
            price = int(price_string)

            money = int(driver.find_element_by_id("money").text)
            if money > price:
                t.sleep(SLEEP)
                driver.find_element_by_id(upgradeable_ids[i]).click()

    # end while loop after 5 minutes
    if t.time() > timeout:
        print(driver.find_element_by_id("cps").text)
        break

driver.quit()
