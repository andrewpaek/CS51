import probability as p
import pickle
import math
import sys

def predict(ngram_dict,testdata):
    f_ = open(r'C:\num_files.pkl','rb')
    num_files = pickle.load(f_)
    f_.close()

    ## generating prior probabilities
    # calculating total number of files
    total_files = 0
    for author in num_files:
        total_files += num_files[author]

    prob_prior = {}
    for author in num_files:
        prob_prior[author] = num_files[author]/float(total_files)

    # generating conditional probabilities
    prob_cond = p.calculateClassProbability(num_files,ngram_dict,testdata)

    """
    # generating denominator for bayes theorem
    # use law of total probability
    denom = 0
    for key in prob_cond:
        denom += prob_prior[key]*prob_cond[key]
    """

    # generating final probabilities using bayes theorem formula
    probabilities = {}
    for key in prob_cond:
        probabilities[key] = prob_cond[key] + math.log(prob_prior[key])

    bestclass = None
    bestprob = -sys.maxint - 1
    for key in probabilities:
        if probabilities[key] > bestprob:
            bestprob = probabilities[key]
            bestclass = key

    # returns prediction
    return bestclass
