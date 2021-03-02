from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager


def main():
    flight_search = FlightSearch()
    data_manager = DataManager()
    notification_manager = NotificationManager()
    data = data_manager.get_data()["prices"]

    # Get IATA Codes for cities in spreadsheet.
    if data[0]["iataCode"] == "":
        city_ids = [(elem["id"], elem["city"]) for elem in data]

        for elem in city_ids:
            iata = flight_search.get_iata_code_by_city(elem[1])
            body = {
                "price": {
                    "iataCode": iata,
                }
            }
            data_manager.put_data(body, elem[0])

    # Get Cheap flights from LON (London) to destinations in spread sheet.
    for destination in data:
        flight = flight_search.search_a_flight(destination["iataCode"])

        if flight is None:
            continue

        # Notify if cheap flight is found.
        if destination["lowestPrice"] > flight.price:
            message = "Low price alert!\n" \
                     f"Only {flight.price} to fly from {flight.origin_city}-{flight.origin_airport}" \
                     f" to {flight.destination_city}-{flight.destination_airport}" \
                     f" from {flight.out_date}" \
                     f" to {flight.return_date}."

            if flight.stop_overs > 0:
                message += f"\nFlight has {flight.stop_overs} stop over, via {flight.via_city}."

            # Notify me on phone
            notification_manager.send_message(message)

            #notify customers via mail
            customers = data_manager.get_users()["users"]
            notification_manager.send_emails(customers[0]["email"], flight)


if __name__ == '__main__':
    main()
