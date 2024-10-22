import os
from inltk.inltk import remove_foreign_languages
from nltk.tokenize import sent_tokenize  # Ensure proper import of sent_tokenize

def remove_fl(sentence):
    tokens = remove_foreign_languages(sentence, 'gu')  
    filtered_tokens = []

    for token in tokens:
        if token.startswith("▁"):
            cleaned_token = token.strip("▁")  # Clean token
            if cleaned_token != "▁":
                filtered_tokens.append(cleaned_token)

    cleaned_string = " ".join(filtered_tokens)
    return cleaned_string

with open('texts/to_sent.txt', 'r', encoding='utf-8') as input_file:
    sentences = input_file.readlines()

with open('texts/remove_fl.txt', 'w', encoding='utf-8') as output_file:
    for sentence in sentences:
        if sentence.strip():
            cleaned_sentence = remove_fl(sentence.strip())  
            output_file.write(cleaned_sentence + '\n')  
