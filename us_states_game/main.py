import turtle
import pandas

FONT = ("Arial", 8, "normal")

# setup screen
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# global Variables
right_guessed_states = 0
data = pandas.read_csv("50_states.csv")
correct_guesses = []

# game loop
while right_guessed_states < 50:
    # get user input
    answer_state = screen.textinput(title=f"{right_guessed_states}/50 States Correct",
                                    prompt="What's another state's name?").title()

    # Stop game and make list of missing states
    if answer_state == "Exit":
        missing_states = {
            "state": [],
            "x": [],
            "y": []
        }

        for state in data.state.to_list():
            if state not in correct_guesses:
                missing_states["state"].append(state)
                missing_states["x"].append(data[data.state == state].x.item())
                missing_states["y"].append(data[data.state == state].y.item())

        df = pandas.DataFrame(missing_states)
        df.to_csv("Missing_States.csv")

        break

    # check if user input is in data
    elif answer_state in data.state.to_list():
        right_guessed_states += 1
        correct_guesses.append(answer_state)

        # get screen coordinates of answer state
        state_data = data[data.state == answer_state]
        state_position = (state_data.x.item(), state_data.y.item())

        # Create writing on map
        state_writing = turtle.Turtle()
        state_writing.hideturtle()
        state_writing.penup()
        state_writing.goto(state_position)
        state_writing.write(arg=answer_state, align="center", font=FONT)

screen.exitonclick()
