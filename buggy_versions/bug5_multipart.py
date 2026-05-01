# bug5_multipart.py

def get_answer(query):
    # Does not split multi-part queries
    return answers[find_best_match(query, questions, embeddings)[0]]
