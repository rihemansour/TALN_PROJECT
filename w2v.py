import torch
from sklearn.metrics.pairwise import cosine_similarity
import model
class Word2V(model.Model):
    @staticmethod
    def extract_word2vec_features(text, word2vec_model):
        words = text.split()
        word_vectors = [word2vec_model.wv[word] for word in words if word in word2vec_model.wv]
        return torch.tensor(word_vectors)
    