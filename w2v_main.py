import pandas as pd
from gensim.models import Word2Vec
import w2v
def main():
    input_file_path = 'phrases_bert.csv'
    output_file_path = 'phrases_bert_w2v.csv'

    # Load your CSV data
    data = pd.read_csv(input_file_path)
    sentences = data["Sentence 1"].tolist() + data["Sentence 2"].tolist()

    # Train Word2Vec model
    sentences_tokenized = [sentence.split() for sentence in sentences]
    word2vec_model = Word2Vec(sentences_tokenized, vector_size=100, window=5, min_count=1, workers=4)
    w = w2v.Word2V
    sentence_vectors = [w.extract_word2vec_features(sentence, word2vec_model) for sentence in sentences]

    similarity_scores = w.calculate_similarity(sentence_vectors)
    annotation = w.automatic_annotation(similarity_scores)

    # Add Word2Vec annotation to the DataFrame
    data['word2vec_annotation'] = annotation

    # Save the DataFrame to a new CSV file
    data.to_csv(output_file_path, index=False, encoding='utf-8')

    print(f"Pairs extracted and saved to {output_file_path}")

    
if __name__ == "__main__":
    main()
    