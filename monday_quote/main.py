import datetime as dt
import smtplib
import random
from env import my_email, my_pass, to_email


def main():
    weekday = dt.datetime.now().weekday()
    if 0 == weekday:
        with open("quotes.txt", "r") as file:
            quotes = file.readlines()

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_pass)
            connection.sendmail(from_addr=my_email,
                                to_addrs=to_email,
                                msg="Subject:Monday-Motivator\n\n"
                                    f"{random.choice(quotes)}"
                                    "\nBest wishes\nMotivator-Bot")


if __name__ == '__main__':
    main()
