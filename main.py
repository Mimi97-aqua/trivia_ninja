from script import generate_question
from storage.to_csv import store_as_csv

questions_and_answers = generate_question("Python", 5)
store_as_csv(questions_and_answers, 'storage/python.csv')