from src.database import setup_and_populate_db
from src.generator import compile_quiz_data

setup_and_populate_db()

quiz, context = compile_quiz_data(
    "Football",
    "Easy"
)

print(quiz)