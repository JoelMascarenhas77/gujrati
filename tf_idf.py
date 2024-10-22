import os
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer

def apply_tfidf(sentences):
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(sentences)
   
    with open('models/tfidf_vectorizer.pkl', 'wb') as vec_file:
        pickle.dump(vectorizer, vec_file)
    
    with open('models/tfidf_matrix.pkl', 'wb') as matrix_file:
        pickle.dump(tfidf_matrix, matrix_file)


with open('texts/output.txt', 'r', encoding='utf-8') as input_file:
    sentences = [line.strip() for line in input_file.readlines()]

apply_tfidf(sentences)

