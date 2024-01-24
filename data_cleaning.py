import re
import csv
import random

# This file is used to clean the data we collected and construct our dataset
# The dataset has 3 columns : sentence1, sentence2 and human annotation


def clean_text(text):
    # Remove numbers
    text = re.sub(r'\d+', '', text)
    
    # Remove square brackets
    text = text.replace('[', '').replace(']', '')

    return text.strip()

def main():
    input_file_path = 'arabicData.txt'
    output_file_path = 'Phrases.csv'

    with open(input_file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Clean the text
    cleaned_text = clean_text(content)

    # Split into sentences
    sentences = re.split(r'[\n.!?]', cleaned_text)

    # Remove empty sentences
    sentences = [sentence.strip() for sentence in sentences if sentence.strip()]

    # Create pairs of consecutive sentences
    consecutive_pairs = list(zip(sentences, sentences[1:]))

    # Create random pairs of sentences
    random_pairs = random.sample(list(zip(sentences, random.sample(sentences, len(sentences)))), min(len(sentences), 10000))

    # Write to CSV file
    with open(output_file_path, 'w', encoding='utf-8', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['Sentence 1', 'Sentence 2', 'Human Annotation'])

        # Write consecutive pairs with human annotation 5
        for pair in consecutive_pairs:
            csv_writer.writerow([pair[0], pair[1], 5])

        # Write random pairs with human annotation 1
        for pair in random_pairs:
            csv_writer.writerow([pair[0], pair[1], 1])

    print(f"Pairs extracted and saved to {output_file_path}")

if __name__ == "__main__":
    main()