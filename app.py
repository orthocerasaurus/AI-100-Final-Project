import json
from model import encode_questions, find_best_match
from preprocessing import clean_text

# Load dataset
with open("data.json", "r") as f:
    data = json.load(f)

questions = [item["question"] for item in data]
answers = [item["answer"] for item in data]

# Precompute embeddings
question_embeddings = encode_questions(questions)

def get_answer(query):
    query = clean_text(query)

    # Handle very short queries
    if len(query.split()) < 2:
        return "Please provide more details."

    best_index, score = find_best_match(query, questions, question_embeddings)

    # Confidence threshold
    if score < 0.5:
        return "I don't know the answer to that."

    return answers[best_index]


# Simple CLI test
if __name__ == "__main__":
    while True:
        user_input = input("Ask a question: ")
        print(get_answer(user_input))
