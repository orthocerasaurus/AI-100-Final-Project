# bug4_ambiguity.py

def get_answer(query):
    # Removed short query handling
    best_index, score = find_best_match(query, questions, embeddings)
    return answers[best_index]
