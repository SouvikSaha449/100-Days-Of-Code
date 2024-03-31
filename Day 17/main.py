from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for dicto in question_data:
    question_text = dicto["question"]
    question_answer = dicto["correct_answer"]
    question = Question(question_text, question_answer)
    question_bank.append(question)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print("You have finished the quiz")
print(f"Your final score is {quiz.score}/{quiz.question_number}")
