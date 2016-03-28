import math
import splitData as sd
import nGram as n
from scipy.stats import poisson

# num_works is a dictionary where keys = authors names, values = num of text files of data i.e.,- (8,6)
# ngram_dict is a dictionary of dictionaries

def gensum(dictionary):
    summation=0
    for key in dictionary:
        summation+=dictionary[key]
    return summation

def calculateClassProbability(num_works,ngram_dict,testdata):
    prob = {"Dickens":0.0,"Twain":0.0}
    for author in prob:
        author_dict = ngram_dict[author]
        log_product = 0.0
        denom = num_works[author]
        totaldict=gensum(author_dict)
        totalvec=gensum(testdata)
        for ngram in testdata:
            if ngram in author_dict:
                lamb = author_dict[ngram]/9
                pmf = poisson.pmf(testdata[ngram],mu=lamb)
                if pmf > 0:
                    log_product += math.log(poisson.pmf(testdata[ngram],mu=lamb))
        prob[author] = log_product
    return prob

