#Natural Language Processing

#Import the key libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import re

#Importing the dataset
dataset = pd.read_csv('Restaurant_Reviews.tsv', delimiter='\t', quoting = 3)

#Cleaning the texts
review1 = dataset['Review'][0]
review = re.sub(r'[^\w]', r' ' ,review1)
review = review.lower()
