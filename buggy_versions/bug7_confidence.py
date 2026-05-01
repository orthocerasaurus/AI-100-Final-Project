# bug7_confidence.py

def get_answer(query):
    best_index, score = find_best_match(query, questions, embeddings)
    
    # Always returns answer
    return answers[best_index]
