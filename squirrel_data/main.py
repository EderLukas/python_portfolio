import pandas


def main():
    data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

    # colors_list = data["Primary Fur Color"].to_list()
    # gray_count = colors_list.count("Gray")
    # black_count = colors_list.count("Black")
    # red_count = colors_list.count("Cinnamon")
    gray_count = len(data[data["Primary Fur Color"] == "Gray"])
    red_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
    black_count = len(data[data["Primary Fur Color"] == "Black"])

    data_dict  = {
        "Fur Color": ["gray", "red", "black"],
        "Count": [gray_count, red_count, black_count]
    }

    data_frame = pandas.DataFrame(data_dict)
    data_frame.to_csv("squirrel_count.csv")


if __name__ == '__main__':
    main()
