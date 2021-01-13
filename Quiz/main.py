from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


def main():
    question_bank = []
    for elem in question_data:
        question_bank.append(Question(elem["question"], elem["correct_answer"]))

    quiz = QuizBrain(question_bank)

    while quiz.still_has_questions():
        quiz.next_question()

    print("You've completed the quiz")
    print(f"Your final score was: {quiz.score}/{quiz.question_number}.")


if __name__ == "__main__":
    main()
