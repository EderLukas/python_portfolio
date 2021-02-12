from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        # Window setup
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Score
        self.lbl_score = Label(text="Score: 0", fg="white", bg=THEME_COLOR, highlightthickness=0)
        self.lbl_score.grid(column=1, row=0)

        # Canvas with questions
        self.canvas = Canvas(height=250, width=300, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=200,
            text="Question",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        # Buttons
        img_false = PhotoImage(file="images/false.png")
        img_right = PhotoImage(file="images/true.png")
        self.btn_false = Button(image=img_false, command=self.false_pressed)
        self.btn_false.grid(column=0, row=2)
        self.btn_right = Button(image=img_right, command=self.true_pressed)
        self.btn_right.grid(column=1, row=2)

        self.get_next_question()

        # Mainloop
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.lbl_score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.btn_right.config(state="disabled")
            self.btn_false.config(state="disabled")

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        elif not is_right:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
