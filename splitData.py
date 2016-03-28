import random
import os
import string
import pickle

"""
WordList converts all the text files in the directory
into a list of words. Includes punctuation marks. Returns
a list of word lists, where each element in the list
corresponds to the list of words for each specific text file

NOTE: make sure text files are in the same directory as this
.py file
"""

def wordList(dirName):
    f_ = open(r'C:\num_files.pkl','rb')
    num_files = pickle.load(f_)
    f_.close()
    endRange = num_files[dirName]

    wordListList = []
    for i in range(1,endRange+1):
        wordlist = []
        filename = "." + os.sep + "copy" + os.sep + dirName + os.sep + str(i) + '.txt'
        f = open(filename,'r')
        datalist = list(f.read().decode("utf-8-sig").encode("utf-8"))
        datalist.append(' ')
        chardummy = ''
        for char in datalist:
            if char != ' ' and char != '\n' and char != '\r':
                chardummy += char.lower()
            elif chardummy != '':
                wordlist.append(chardummy)
                chardummy = ''
            else:
                chardummy = ''
        wordListList.append(wordlist)
    return wordListList
#print wordList("Twain") #(used to test function)

"""
The below contains some of the split functions we experimented with but
decided not to use in favor of k-fold cross validation.

SplitData randomlysplits a list of words of a text file into a training set
and a testing set. The parameter "dataset" for splitData must
be a list of words, which can be created by the wordList
function seen above. The parameter "splitRatio" for splitData
is the proportion of training data that we want in our program
(if we want 60% training and 40% testing, we would pass in 0.6
as the "splitRatio" parameter). Returns a list containing two elements:
the training data and the testing data.

def splitData(dataset, splitRatio):
    trainSet = []
    testSet = []
    startIndex = random.randrange(int(len(dataset)*(1.0 - splitRatio)))
    endIndex = int(startIndex + len(dataset)*splitRatio)
    for i in range(startIndex, endIndex):
        trainSet.append(dataset[i])
    for i in range(0, startIndex):
        testSet.append(dataset[i])
    for i in range(endIndex,len(dataset)):
        testSet.append(dataset[i])
    return (trainSet, testSet)
#print splitData([1,2,3,4,5,6,7,8,9,0,1,2,3,4], 0.66) (used to test function)

#data is a list of lists
def word(data,splitRatio):
    training=[]
    testing=[]
    for i in range(0,len(data)):
        a,b=splitData(data[i],splitRatio)
        training.extend(a)
        testing.append(b)
    return (training,testing)
"""

#Inputs word list and removes all punctuation from each word
def punctRemove(data):
    nopunct = []
    for word in data:
        nopunct.append(word.translate(string.maketrans("",""), string.punctuation))
    return nopunct

"""crossValid takes in a string list (data),
number of subsets (k), and the specific subset
that the function will be splitting of the k subsets (n) """
def crossValid(data,k,n):
    train = []
    test = []
    testsize = len(data)/k
    start = (n-1)*testsize
    end = n*testsize
    for i in range(start,end):
        test.append(data[i])
    for i in range(0,start):
        train.append(data[i])
    for i in range(end,len(data)):
        train.append(data[i])
    return (train,test)

"""crossValidAll takes in a list of string lists (data)
and number of subsets (k) and returns a list of tuples
where the first element is the list of testing data while
the second element is the list of string lists"""
def crossValidAll(data, k):
    tuplelist = []
    for i in range(1,k+1):
        train = []
        test = []
        for j in range(0,len(data)):
            a,b = crossValid(data[j],k,i)
            train.extend(a)
            test.append(b)
        tuplelist.append((train,test))
    return tuplelist
