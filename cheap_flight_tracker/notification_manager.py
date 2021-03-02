from env import TWILIO
from twilio.rest import Client
from env import EMAIL
import smtplib

class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO["account_sid"], TWILIO["auth_token"])

    def send_message(self, message):
        """Sends message to defined user with flight information and price tag"""
        message = self.client.messages \
            .create(
                body=message,
                from_=TWILIO["from_phone"],
                to=TWILIO["to_phone"]
            )
        print(message.status)

    def send_emails(self, respondent, flight):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=EMAIL["from_email"], password=EMAIL["password"])

            message = "Low price alert!\n" \
                      f"Only {flight.price} £ to fly from {flight.origin_city}-{flight.origin_airport}" \
                      f" to {flight.destination_city}-{flight.destination_airport}" \
                      f" from {flight.out_date}" \
                      f" to {flight.return_date}." \
                      f"\n\nhttps://www.google.co.uk/flights?hl=en#flt={flight.origin_airport}." \
                      f"{flight.destination_airport}.{flight.out_date}*{flight.destination_airport}." \
                      f"{flight.origin_airport}.{flight.return_date}".encode("utf-8")

            if flight.stop_overs > 0:
                message += f"\nFlight has {flight.stop_overs} stop over, via {flight.via_city}."

            connection.sendmail(from_addr=EMAIL["from_email"],
                                to_addrs=respondent,
                                msg=message)
