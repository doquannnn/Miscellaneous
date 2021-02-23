from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
from collections import defaultdict, Counter

import nltk
import numpy as np
import os
import re

MAXFILE = 1400  # number of documents
MAXQUERY = 100  # test set
N = 1400  # MAXFILE


def preprocess(doc):
    # remove punctuations
    doc = re.sub(r'[^\w\s]', '', doc)
    # convert to lowercase + tokenization
    doc = map(lambda x: x.lower(), word_tokenize(doc))
    # remove stopwords
    stop_words = stopwords.words('english')
    filtered_words = filter(lambda x: x not in stop_words, doc)
    # stemming
    ps = PorterStemmer()
    stemmed_words = [ps.stem(word) for word in filtered_words]
    return stemmed_words


def invertedIndex():
    n_docs = defaultdict(int)
    posting_lists = defaultdict(list)
    path = os.path.join(os.getcwd(), 'Cranfield')
    empty_txt = ['471', '995']  # empty documents

    for doc in os.listdir(path):
        index, _ = os.path.splitext(doc)  # 471, 995
        if index in empty_txt:
            continue

        doc_path = os.path.join(path, doc)
        with open(doc_path, 'r') as f:
            processed_file = preprocess(f.read())
            count_terms = Counter(processed_file)
            # assign each unique term with its own frequency
            for term, freq in count_terms.items():
                n_docs[term] += 1
                posting_lists[term].append([int(index), freq])

    norm2 = [0 for _ in range(MAXFILE + 1)]
    # reloop over every term to compute its weght
    for term, posting_list in posting_lists.items():
        idf = 1 / n_docs[term]

        for index, (n, tf) in enumerate(posting_list):
            tfidf = tf * idf
            posting_list[index][1] = tfidf
            norm2[n] += tfidf ** 2
    norm2 = list(map(np.sqrt, norm2))

    for _, posting_list in posting_lists.items():
        for index, (n, __) in enumerate(posting_list):
            posting_list[index][1] /= norm2[n]
    return posting_lists, n_docs


def computeQuery(p, n_docs_id, query):
    c = Counter(query)

    # calculate each term's weight in query
    for term in c:
        idf = 1 / n_docs[term] if term in n_docs_id else 0
        c[term] = c[term] * idf

    norm_query = np.linalg.norm(list(c.values()))

    for term in c:
        c[term] = c[term] / norm_query

    rankings = {}
    for term, posting_list in p.items():
        if term in c and c[term] != 0:
            for n, weight in posting_list:
                rankings[n] = rankings.get(n, 0) + weight * c[term]
    rankings = list(rankings.items())

    # the higher, the more relevant
    return sorted(rankings, key=lambda x: x[1], reverse=True)

# get mAP score - metric to evaluate information retrieval system


def computeAveragePrecision(rankings, index):
    ranking_docs = [x[0] for x in rankings]

    file_txt = str(index) + '.txt'
    result_path = os.path.join(os.getcwd(), 'TEST/RES')
    text_path = os.path.join(result_path, file_txt)

    with open(text_path) as f:
        relevant_indices = f.readlines()

    result = set()
    for index in relevant_indices:
        result.add(int(index.split()[1]))

    average_precision, num_correct = 0.0, 0
    for i, doc in enumerate(ranking_docs, start=1):
        if doc in result:
            num_correct += 1
            average_precision += num_correct / i

    return average_precision / len(result)


p, n_docs = invertedIndex()
query_path = os.path.join(os.getcwd(), 'TEST/query.txt')
with open(query_path) as f:
    queries = f.readlines()
    processed_queries = []
    for query in queries:
        q = query.split()
        id, processed = int(q[0]), preprocess(' '.join(q[1:]))
        processed_queries.append((id, processed))


MAP = []
for index, query in processed_queries:
    rankings = computeQuery(p, n_docs, query)
    AP = computeAveragePrecision(rankings, index)
    MAP.append(AP)

print(np.mean(MAP))
