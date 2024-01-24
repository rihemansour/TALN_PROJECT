# Projet TALN

## Titre du Projet : Analyse de la Cohérence Inter-phrastique en langue arabe à travers la similarité des paires de phrases

Développer une analyse approfondie de la cohérence inter-phrastique à l'intérieur des paragraphes, entre les paragraphes, et dans l'ensemble du texte en évaluant la cohérence deux à deux entre les phrases.
### Exemples :
***2 phrases incohérentes:***

"الفتاة تمشي في حديقة الزهور، والطيور تغني بصوت عالي."

"المطار يعلن عن إلغاء الرحلات، والرياح تعصف بقوة. "

***2 phrases cohérentes:***

"الطلاب يستعدون للاحتفال بتخرجهم، والجامعة تكرمهم في حفل كبير."

"العائلات تحضر للمشاركة في الاحتفال، والفرح يملأ الهواء"

### Collecte de Données :

Rassemblez un corpus de texte varié comprenant des paragraphes et des sections plus larges.

### Annotation Humaine :

Marquez la cohérence inter-phrastique pour chaque paire de phrases à l'intérieur des paragraphes, entre les paragraphes, et pour l'ensemble du texte. Utilisez une échelle numérique pour représenter le degré de cohérence entre chaque paire. (Exemple: 1->5)

### Prétraitement des Données :

Nettoyez et prétraitez les données textuelles en éliminant les éléments non pertinents.

### Extraction de Caractéristiques :

Utilisez un modèle de langage pré-entraîné (par exemple, BERT) pour générer des représentations vectorielles des phrases.

### Mesure de Similarité Inter-phrastique :

Calculez la similarité entre les vecteurs de représentation des phrases pour chaque paire de phrases. Utilisez des métriques telles que la similarité cosinus.

### Annotation Automatique :

Comparez les résultats de la mesure automatique avec les annotations humaines pour évaluer la performance de la similarité inter-phrastique.

### Agrégation des Scores :

Agrégez les scores de similarité inter-phrastique pour obtenir des mesures de cohérence au niveau du paragraphe, entre les paragraphes, et pour l'ensemble du texte.

### Analyse des Résultats :

Identifiez les zones où la cohérence est perçue différemment à différents niveaux d'analyse. Analysez les résultats pour comprendre les nuances de la cohérence dans le texte.

### Réajustement du Modèle :

En fonction des résultats de l'analyse, ajustez le modèle ou explorez d'autres modèles de langage pour améliorer la capture de la cohérence inter-phrastique.

### BONUS:

Utilisation des techniques d'apprentissage automatique pour automatiser l’attribution de la note de cohérence
