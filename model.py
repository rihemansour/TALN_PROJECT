from sklearn.metrics.pairwise import cosine_similarity

class Model:
    @staticmethod
    def calculate_similarity(sentence_vectors):
        similarity_scores = []
        for i in range(len(sentence_vectors) - 1):
            similarity = cosine_similarity(
                sentence_vectors[i][:, 0, :], sentence_vectors[i + 1][:, 0, :]
            ).item()
            similarity_scores.append(similarity)
        return similarity_scores

    @staticmethod
    def automatic_annotation(similarity_scores):
        annotations = []
        for score in similarity_scores:
            if score >= 0.8:
                annotations.append(5)
            elif 0.6 <= score < 0.8:
                annotations.append(4)
            elif 0.4 <= score < 0.6:
                annotations.append(3)
            elif 0.2 <= score < 0.4:
                annotations.append(2)
            else:
                annotations.append(1)
        return annotations

    @staticmethod
    def aggregate_paragraph_scores(similarity_scores, sentence_boundaries):
        paragraph_scores = []
        start_index = 0
        for end_index in sentence_boundaries:
            paragraph_score = sum(similarity_scores[start_index:end_index]) / (end_index - start_index)
            paragraph_scores.append(paragraph_score)
            start_index = end_index
        return paragraph_scores

    @staticmethod
    def aggregate_between_paragraph_scores(similarity_scores, sentence_boundaries):
        between_paragraph_scores = []
        for i in range(len(sentence_boundaries) - 1):
            # Utilize the index of the last sentence of the current paragraph - 1
            index = sentence_boundaries[i] - 1
            if index < len(similarity_scores):
                score = similarity_scores[index]
                between_paragraph_scores.append(score)
            else:
                print(f"Index {index} out of range for similarity_scores")
        return sum(between_paragraph_scores) / len(between_paragraph_scores) if between_paragraph_scores else 0

    @staticmethod
    def aggregate_overall_score(similarity_scores):
        overall_score = sum(similarity_scores) / len(similarity_scores)
        return overall_score

