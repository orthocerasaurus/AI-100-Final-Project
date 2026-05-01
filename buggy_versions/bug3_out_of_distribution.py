# bug3_out_of_distribution.py

def get_answer(query):
    best_index, score = find_best_match(query, questions, embeddings)
    
    # Removed threshold check
    return answers[best_index]
