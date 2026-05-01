# bug6_similarity.py
import random

def find_best_match(query, questions, embeddings):
    scores = [0.5 for _ in questions]  # fake scores
    return random.randint(0, len(questions)-1), 0.5
