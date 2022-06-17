import csv
import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from tqdm import tqdm
import numpy as np
csvfile = open('IndieGames.csv', encoding="utf8")
csvreader = csv.reader(csvfile)
docs = []
for row in csvreader:
    docs.append(row[2])
words = []
for d in docs:
    words.extend(d.split())
vocab = np.array(words)
vocab = np.unique(vocab)
vectorizer = TfidfVectorizer(lowercase=True)
x = vectorizer.fit(docs)
tfidf_docs = vectorizer.fit_transform(docs)
y = vectorizer.vocabulary_
docs_tfidf = vectorizer.transform(docs)
type(docs_tfidf), docs_tfidf.shape
z = docs_tfidf[0].A
def QueryFinder(query):
    tfidf_query = vectorizer.transform([query])[0]
    cosines = []
    for d in tqdm(tfidf_docs):
        cosines.append(float(cosine_similarity(d, tfidf_query)))
    k = 10
    sorted_ids = np.argsort(cosines)
    for i in range(k):
        cur_id = sorted_ids[-i-1]
        print(docs[cur_id])
        print(f"______________________score :{cosines[cur_id]} ")
while True:
    print('Enter Yout Query')
    query = input()
    QueryFinder(query)
    print('____________________________________ TOP 10 DOCS ____________________________________')