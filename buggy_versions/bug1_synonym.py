# bug1_synonym.py

def find_best_match(query, questions, model):
    # Forces exact match only
    query = query.lower().strip()

    if query in questions:
        return questions.index(query), 1.0

    return 0, 0.0
