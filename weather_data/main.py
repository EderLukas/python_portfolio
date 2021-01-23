import csv
import pandas


def main():
    # with open("weather_data.csv", mode="r") as data_file:
    #     data = csv.reader(data_file)
    #
    #     temperatures = []
    #     for row in data:
    #         if row[1] != "temp":
    #             temperatures.append(int(row[1]))
    #
    #     print(temperatures)

    data = pandas.read_csv("weather_data.csv")
    print(data["temp"])

    data_dict = data.to_dict()
    print(data_dict)

    temp_list = data["temp"].to_list()
    print(temp_list)

    average = data["temp"].mean()
    print(f"Average: {average}")

    maximum = data["temp"].max()
    print(f"Maximum: {maximum}")

    # Get data in row
    print(data[data.day == "Monday"])

    # get data in row with max value
    print(data[data.temp == data.temp.max()])

    #get specific value of row
    monday = data[data.day == "Monday"]
    print(monday.condition)

    # convert celcius to fahrenheit
    print((monday.temp * 9/5) + 32)

    # example dict to pandas
    data_dict = {
        "students": ["Amy", "James", "Angela"],
        "scores": [76, 56, 65]
    }

    data_frame = pandas.DataFrame(data_dict)
    data_frame.to_csv("new_data.csv")


if __name__ == '__main__':
    main()
