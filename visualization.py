import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

input_file_path = 'phrases_bert_w2v.csv'
# Load your CSV data
d = pd.read_csv(input_file_path)
# Extract the relevant columns
auto_annotation_counts = d['Automatic Annotation'].value_counts().sort_index()
word2vec_annotation_counts = d['word2vec_annotation'].value_counts().sort_index()

# Plotting
plt.figure(figsize=(10, 6))
sns.countplot(x='value', hue='variable', data=pd.melt(d[['Automatic Annotation', 'word2vec_annotation']], value_name='value'))
plt.title('Comparison of Automatic Annotation and Word2Vec Annotation')
plt.xlabel('Annotation Value')
plt.ylabel('Count')
plt.show()