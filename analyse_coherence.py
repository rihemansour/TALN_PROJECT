import re
import pandas as pd
# Fonction pour extraire les phrases d'un texte
def extraire_phrases(texte):
    phrases = re.split(r'\.\s*', texte)
    return [phrase for phrase in phrases if phrase]

# Fonction pour analyser la cohérence
def analyse_coherence(paragraph_scores, between_paragraph_scores, overall_score, sentences, sentence_boundaries):
    print("Analyse des Résultats de Cohérence :")

    # Cohérence au niveau des paragraphes
    for i, score in enumerate(paragraph_scores):
        print(f"Cohérence du paragraphe {i + 1} : {score:.2f}")

    # Cohérence entre les paragraphes
    print(f"Cohérence entre les paragraphes : {between_paragraph_scores:.2f}")

    # Cohérence globale du texte
    print(f"Cohérence globale du texte : {overall_score:.2f}")

    # Zones de cohérence perçue différemment
    for i in range(len(sentence_boundaries) - 1):
        start = sentence_boundaries[i]
        end = sentence_boundaries[i + 1] if i < len(sentence_boundaries) - 1 else len(sentences)
        paragraph = " ".join(sentences[start:end])
        print(f"Paragraphe {i + 1}: {paragraph}")
        print(f"Score de cohérence: {paragraph_scores[i]:.2f}\n")

# Exemple d'utilisation
df = pd.read_csv("")
for i in range(len(df)):
   texte_complet = df['Phrase'][i]
   sentences = extraire_phrases(texte_complet)

# Scores de similarité et frontières des paragraphes (à remplacer par vos propres données)
similarity_scores = df['Similarity Score'].tolist()
sentence_boundaries = [2, 4]

# Calcul des scores de cohérence
paragraph_scores = [sum(similarity_scores[:sentence_boundaries[0]]) / sentence_boundaries[0],
                    sum(similarity_scores[sentence_boundaries[0]:sentence_boundaries[1]]) / (sentence_boundaries[1] - sentence_boundaries[0])]
between_paragraph_scores = sum(similarity_scores) / len(similarity_scores)
overall_score = sum(similarity_scores) / len(similarity_scores)

# Analyse des résultats
analyse_coherence(paragraph_scores, between_paragraph_scores, overall_score, sentences, sentence_boundaries)
