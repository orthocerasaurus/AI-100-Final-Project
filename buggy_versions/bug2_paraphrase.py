# bug2_paraphrase.py

def similarity(q1, q2):
    return len(set(q1.split()) & set(q2.split()))

def find_best_match(query, questions):
    scores = [similarity(query, q) for q in questions]
    best_index = scores.index(max(scores))
    return best_index, max(scores)
