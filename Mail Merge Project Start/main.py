def main():
    with open("./Input/Letters/starting_letter.txt", mode="r") as letter:
        letter_lines = letter.readlines()

    with open("./Input/Names/invited_names.txt", mode="r") as names:
        names = names.readlines()

    for name in names:
        new_name = name.strip("\n")
        greeting = letter_lines[0].replace("[name]", new_name)

        with open(f"./Output/ReadyToSend/letter_for_{new_name}.txt", mode="w") as new_letter:
            for i in range(len(letter_lines)):
                if 0 == i:
                    new_letter.write(greeting)
                else:
                    new_letter.write(letter_lines[i])


if __name__ == '__main__':
    main()
