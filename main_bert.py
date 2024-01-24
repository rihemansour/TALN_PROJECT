import pandas as pd
from transformers import BertTokenizer, BertModel
import bert_model 

def main_bert():
    input_file_path = 'Phrases.csv'
    output_file_path = 'phrases_bert.csv'

    # Load your CSV data
    data = pd.read_csv(input_file_path)
    sentences = data["Sentence 1"].tolist() + data["Sentence 2"].tolist()

    # Load pre-trained BERT model and tokenizer
    tokenizer = BertTokenizer.from_pretrained('bert-base-multilingual-cased')
    model = BertModel.from_pretrained('bert-base-multilingual-cased')
    bert = bert_model.Bert
    sentence_vectors = [bert.extract_bert_features(sentence, model, tokenizer) for sentence in sentences]

    similarity_scores = bert.calculate_similarity(sentence_vectors)
    annotation = bert.automatic_annotation(similarity_scores)

    # Add BERT annotation to the DataFrame
    data['bert_annotation'] = annotation

    # Save the DataFrame to a new CSV file
    data.to_csv(output_file_path, index=False, encoding='utf-8')

    print(f"Pairs extracted and saved to {output_file_path}")

    
if __name__ == "__main__":
    main_bert()