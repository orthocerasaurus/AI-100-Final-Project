import json
from model import encode_questions, find_best_match
from preprocessing import clean_text

with open("../data.json", "r") as f:
    data = json.load(f)

questions = [item["question"] for item in data]
answers = [item["answer"] for item in data]

question_embeddings = encode_questions(questions)

def get_answer(query):
    query = clean_text(query)

    if len(query.split()) < 2:
        return "Please provide more details."

    best_index, score = find_best_match(query, questions, question_embeddings)

    if score < 0.5:
        return "I don't know the answer to that."

    return answers[best_index]
