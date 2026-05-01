# AI-100 Final Project

This project is a simple AI question-answering system that uses sentence embeddings to match user queries with the most similar question in a dataset.

## How it works
- Questions are encoded using Sentence Transformers
- User input is compared using cosine similarity
- The closest match is returned as the answer

## Files
- app.py: Main application
- model.py: Embedding and similarity logic
- preprocessing.py: Input cleaning
- data.json: Dataset

## How to run
1. Install dependencies:
   pip install -r requirements.txt

2. Run the app:
   python app.py
