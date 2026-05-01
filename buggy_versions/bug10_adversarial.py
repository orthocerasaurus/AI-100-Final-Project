# bug10_adversarial.py

def get_answer(query):
    # No validation
    best_index, score = find_best_match(query, questions, embeddings)
    return answers[best_index]
