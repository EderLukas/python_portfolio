from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    lbl_action.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    lbl_progress_bar.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        lbl_action.config(text="Break", fg=RED)
        count_down(10)
    elif reps % 2 == 0:
        lbl_action.config(text="Break", fg=PINK)
        count_down(2)
    else:
        lbl_action.config(text="Work", fg=GREEN)
        count_down(5)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        if reps % 2 == 0 and reps != 0:
            m = math.floor(reps / 2)
            checks = ""
            for i in range(m):
                checks += "✔"
            lbl_progress_bar.config(text=checks)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Action label
lbl_action = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 32, "bold"))
lbl_action.grid(column=1, row=0)

# Canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# buttons
btn_start = Button(text="Start", command=start_timer)
btn_start.grid(column=0, row=2)
btn_reset = Button(text="Reset", command=reset_timer)
btn_reset.grid(column=2, row=2)

# process bar
lbl_progress_bar = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 14, "bold"))
lbl_progress_bar.grid(column=1, row=3)

# window loop
window.mainloop()

