import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter:row.code for (index, row) in data.iterrows()}


def get_name():
    name = input("What's the name you want to spell? ").upper()
    try:
        print([phonetic_dict[letter] for letter in name])
    except KeyError:
        print("Your input contained a letter which was not an asci")
        get_name()


get_name()
