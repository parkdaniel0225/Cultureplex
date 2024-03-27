import os
import spacy
import json
from pathlib import Path

# Load spaCy's English language model
nlp = spacy.load("en_core_web_sm")

# Directories
txt_directory = r"C:\Users\parkd\OneDrive\Desktop\cultureplex\TXT"
json_directory = r"C:\Users\parkd\OneDrive\Desktop\cultureplex\JSON"

# Creating the JSON directory if it doesn't exist
os.makedirs(json_directory, exist_ok=True)

# Function to tokenize text into sentences using spaCy
def tokenize_to_sentences(text):
    doc = nlp(text)
    return [sent.text for sent in doc.sents]

# Processing each .txt file
txt_files = [f for f in os.listdir(txt_directory) if f.endswith('.txt')]
for file_name in txt_files:
    file_path = os.path.join(txt_directory, file_name)
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    sentences = tokenize_to_sentences(text)
    uuid = Path(file_path).stem.split('_')[-1]
    json_data = [{"sentence": s, "sentence_id": f"{uuid}_{i}"} for i, s in enumerate(sentences, 1)]

    json_filename = f"{Path(file_path).stem}.json"
    json_path = os.path.join(json_directory, json_filename)
    
    with open(json_path, 'w', encoding='utf-8') as json_file:
        json.dump(json_data, json_file, indent=4)
    
    print(f"Created JSON file: {json_filename}")

print("All JSON files have been created successfully.")
