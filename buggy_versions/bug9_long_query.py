# bug9_long_query.py

def get_answer(query):
    # No length handling
    best_index, score = find_best_match(query, questions, embeddings)
    return answers[best_index]
