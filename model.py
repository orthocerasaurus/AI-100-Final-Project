from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')

def encode_questions(questions):
    return model.encode(questions)

def find_best_match(query, questions, question_embeddings):
    query_embedding = model.encode([query])
    scores = cosine_similarity(query_embedding, question_embeddings)[0]
    
    best_index = np.argmax(scores)
    best_score = scores[best_index]
    
    return best_index, best_score
