#Natural Language Processing

#Import the key libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer


#Importing the dataset
dataset = pd.read_csv('Restaurant_Reviews.tsv', delimiter='\t', quoting = 3)

#Cleaning the texts
corpus = []
for i in range(0,len(dataset)):
    review = re.sub(r'[^\w]', r' ' ,dataset['Review'][i])
    review = review.lower()
    review = review.split()
    ps = PorterStemmer()
    review = [ps.stem(w) for w in review if not w in stopwords.words('english')]
    review = ' '.join(review)
    corpus.append(review)
