import pickle
import numpy as np
from similarity import euclidean_distance, cos_similarity, manhattan_distance
from prepro import tokenize_and_filter

# Load TF-IDF vectorizer and matrix once
with open('models/tfidf_vectorizer.pkl', 'rb') as vec_file:
    vectorizer = pickle.load(vec_file)

with open('models/tfidf_matrix.pkl', 'rb') as matrix_file:
    tfidf_matrix = pickle.load(matrix_file)

def calculate_similarity(sent1, sent2):
    # Preprocess the sentences
    sent1 = tokenize_and_filter(sent1)
    sent2 = tokenize_and_filter(sent2)

    # Transform the new sentences to the same TF-IDF space
    new_sentences = [sent1, sent2]
    new_tfidf_matrix = vectorizer.transform(new_sentences)

    # Compute similarity and distances
    cosine_similarity = cos_similarity(new_tfidf_matrix[0].toarray(), new_tfidf_matrix[1].toarray())
    euclidean_dist = euclidean_distance(new_tfidf_matrix[0].toarray(), new_tfidf_matrix[1].toarray())
    manhattan_dist = manhattan_distance(new_tfidf_matrix[0].toarray(), new_tfidf_matrix[1].toarray())

    similarity_scores = {
     "cosine":  cosine_similarity,
    "euclidean": euclidean_dist,
    "manhatan":  manhattan_dist,
    }

    return  similarity_scores
