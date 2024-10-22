import os
import re
from nltk.tokenize import sent_tokenize  # Correct the import


def process_files(directory_path, output_file_path):
    all_sentences = []

    # Loop through all files in the directory
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)

        # Check if it's a text file
        if os.path.isfile(file_path) and file_path.endswith('.txt'):
            with open(file_path, 'r', encoding='utf-8') as file:
                file_content = file.read()
                cleaned_content = re.sub(r'[-:`.,•\d\n\t"\'\[\]\(\)]', ' ', file_content).strip()
                all_sentences.append(cleaned_content)

    # Write all sentences to the output file, one per line
    with open("texts/to_sent.txt", 'w', encoding='utf-8') as output_file:
        for sentence in all_sentences:
            if(sentence):
                output_file.write(sentence + '\n')


# Call the function
process_files("train", "output_sentences.txt")
