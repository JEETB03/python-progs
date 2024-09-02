from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface

# Populates the question bank with Question objects.
question_bank = []

for question in question_data:
    question_text = question["question"]  # Retrieves the question text.
    question_answer = question["correct_answer"]  # Retrieves the correct answer.
    new_question = Question(question_text, question_answer)  # Creates a new Question object.
    question_bank.append(new_question)  # Adds the Question object to the question bank.

# Initializes the QuizBrain and QuizInterface with the question bank.
quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)

# Final message after completing the quiz.
print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")