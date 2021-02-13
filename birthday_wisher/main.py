import smtplib
import datetime as dt
import pandas
import random
from env import my_email, my_pass, to_email


def main():
    # get data from CSV
    data = pandas.read_csv("birthdays.csv")
    data_sets = data.to_dict(orient="records")
    # check if today is a birthday
    for data_set in data_sets:
        if dt.datetime.now().month == data_set["month"] \
                and dt.datetime.now().day == data_set["day"]:
            # prepare letter
            rnd = random.randint(1, 3)
            with open(f"letter_templates/letter_{rnd}.txt", "r") as letter:
                default_letter = letter.read()
            letter = default_letter.replace("[NAME]", data_set["name"])
            # send email
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=my_email, password=my_pass)
                connection.sendmail(from_addr=to_email,
                                    to_addrs=f"{data_set['email']}",
                                    msg="Subject:Happy-Birthday!\n\n"
                                        f"{letter}")


if __name__ == '__main__':
    main()
