#   https://www.nltk.org/book/ch01.html

import nltk
import matplotlib.pyplot as plt
#   nltk.download()
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

#   Lists
sent1 = ['Call','me','Ishmael']
lexical_diversity(sent1)

#   Frequency distribution
fdist1 = FreqDist(text1)

#   Looking at long words
V = set(text1)
long_words = [w for w in V if len(w) > 15] #    {w | w in V & P(w)}
sorted(long_words)

'''
Functions Defined for NLTK's Frequency Distributions

Example	Description
fdist = FreqDist(samples)	create a frequency distribution containing the given samples
fdist[sample] += 1	increment the count for this sample
fdist['monstrous']	count of the number of times a given sample occurred
fdist.freq('monstrous')	frequency of a given sample
fdist.N()	total number of samples
fdist.most_common(n)	the n most common samples and their frequencies
for sample in fdist:	iterate over the samples
fdist.max()	sample with the greatest count
fdist.tabulate()	tabulate the frequency distribution
fdist.plot()	graphical plot of the frequency distribution
fdist.plot(cumulative=True)	cumulative plot of the frequency distribution
fdist1 |= fdist2	update fdist1 with counts from fdist2
fdist1 < fdist2	test if samples in fdist1 occur less frequently than in fdist2

Word Comparison Operators
s.startswith(t)	test if s starts with t
s.endswith(t)	test if s ends with t
t in s	test if t is a substring of s
s.islower()	test if s contains cased characters and all are lowercase
s.isupper()	test if s contains cased characters and all are uppercase
s.isalpha()	test if s is non-empty and all characters in s are alphabetic
s.isalnum()	test if s is non-empty and all characters in s are alphanumeric
s.isdigit()	test if s is non-empty and all characters in s are digits
s.istitle()	test if s contains cased characters and is titlecased (i.e. all words in s have initial capitals)
'''