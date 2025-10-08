#   https://www.nltk.org/book/ch01.html

import nltk
import matplotlib.pyplot as plt
nltk.download()
from nltk.book import *

#   A concordance view shows every occurrance of a single given word
text1.concordance("monstrous")

#   similar() shows "similar" words for a given word
text1.similar("monstrous")

#   common_contexts() lets us look at contexts shared by 2 or more words
text2.common_contexts(["monstrous", "very"])

#   dispersion_plot() to visualize word occurances
text4.dispersion_plot(["citizens", "democracy", "freedom", "duties", "America"])
plt.show(block=True) #  had to add this...block=True means script will be paused until plot window is closed

#   generate() prints random text, generated using a trigram language model
text3.generate()

#   look at the set of unique words
sorted(set(text3))

#   count() number of word occurrences
text3.count("smote")

#   make a function
def lexical_diversity(text):
    return len(set(text)) / len(text)

lexical_diversity(text3)
