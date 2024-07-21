from question_model import Questions
from data import question_data  # Assuming question_data is in question_data.py
from quiz_brain import Quizbrain

question_bank = []

for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Questions(question_text, question_answer)
    question_bank.append(new_question)

quiz = Quizbrain(question_bank)

while quiz.still_has_questions():
    quiz.next()

print("You've completed the Quiz!")
print(f"Your final score is: {quiz.score}/{quiz.question_number}")
