import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter:row.code for (index, row) in data.iterrows()}

name = input("What's the name you want to spell? ").upper()
print([phonetic_dict[letter] for letter in name])

