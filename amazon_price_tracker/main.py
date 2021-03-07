import requests
from bs4 import BeautifulSoup
import smtplib
from env import URL, HEADER, EMAIL
import lxml


def main():
    # Get amazon webpage
    response = requests.get(url=URL, headers=HEADER)
    response.raise_for_status()
    html_content = response.text

    # Scrap for product price
    soup = BeautifulSoup(html_content, "lxml")
    price_string = soup.select_one("#priceblock_ourprice").text
    # Formatting the price to float
    price_without_euro = price_string.split("\xa0")[0]
    string_list = list(price_without_euro)
    string_list[string_list.index(",")] = "."
    price = float("".join(string_list))

    # Send email if price is lower than 250 Euro
    if price < 250:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=EMAIL["my_email"], password=EMAIL["my_pass"])
            connection.sendmail(from_addr=EMAIL["my_email"],
                                to_addrs=EMAIL["to_email"],
                                msg="Amazon Price Check\n\nThe price of your searched product"
                                    f"is lower than 250 => {price}.\n\nBest Regards\nPrice-Bot")


if __name__ == '__main__':
    main()
