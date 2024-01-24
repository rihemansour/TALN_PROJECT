import torch
from sklearn.metrics.pairwise import cosine_similarity
import model
class Bert(model.Model):
    @staticmethod
    def extract_bert_features(text, model, tokenizer):
        encoded_input = tokenizer(
            text, return_tensors="pt", padding=True, truncation=True
        )
        with torch.no_grad():
            model_output = model(**encoded_input)
            return model_output["last_hidden_state"]

    