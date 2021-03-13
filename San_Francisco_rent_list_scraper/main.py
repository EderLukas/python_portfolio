from env import google_form_url, chrome_driver_path, headers
from bs4 import BeautifulSoup
from selenium import webdriver
from env import chrome_driver_path
import requests
import time as t

ZILLOW_SEARCH = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22San%20Francisco%2C%20CA%22%2C%22mapBounds%22%3A%7B%22west%22%3A-122.80371703449832%2C%22east%22%3A-122.18321836330192%2C%22south%22%3A37.374622164491186%2C%22north%22%3A37.9913912031945%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22min%22%3A0%2C%22max%22%3A872627%7D%2C%22mp%22%3A%7B%22min%22%3A0%2C%22max%22%3A3000%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A11%7D"


def main():
    # Get Zillow webpage with the San Francisco search for apartments
    response = requests.get(url=ZILLOW_SEARCH, headers=headers)
    response.raise_for_status()
    webpage = response.text

    # Load webpage into BeautifulSoup and parse for the apartment listings
    soup = BeautifulSoup(webpage, "html.parser")
    rental_listings = soup.find(name="ul", class_="photo-cards")
    rental_listings_li = rental_listings.find_all(name="li")

    rental_estates = []

    # Create a info dictionary for every apartment with its link, price and address
    for estate in rental_listings_li:
        estate_info = {}
        try:
            estate_info["link"] = estate.find(name="a").get("href")
        except AttributeError:
            continue

        if "/" in estate.find(name="div", class_="list-card-heading").getText():
            estate_info["price"] = estate.find(name="div", class_="list-card-heading").getText().split("/")[0]
        elif "+" in estate.find(name="div", class_="list-card-heading").getText():
            estate_info["price"] = estate.find(name="div", class_="list-card-heading").getText().split("+")[0]
        else:
            estate_info["price"] = estate.find(name="div", class_="list-card-heading").getText()
        estate_info["address"] = estate.find(name="address", class_="list-card-addr").text,

        if estate_info["link"][0] == "/":
            estate_info["link"] = "https://www.zillow.com" + estate_info["link"]

        rental_estates.append(estate_info)

    # instantiate selenium
    driver = webdriver.Chrome(executable_path=chrome_driver_path)
    driver.get(google_form_url)
    t.sleep(0.5)

    # Fill in questions
    for estate in rental_estates:
        address = driver.find_element_by_xpath(
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
        address.send_keys(estate["address"])

        price = driver.find_element_by_xpath(
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
        price.send_keys(estate["price"])

        link = driver.find_element_by_xpath(
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
        link.send_keys(estate["link"])
        t.sleep(0.5)

        send_button = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span/span')
        send_button.click()
        t.sleep(1)

        another_form_link = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
        another_form_link.click()
        t.sleep(1)


if __name__ == '__main__':
    main()
