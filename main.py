import splitData as split
import probability as pn
import predict as pr
import nGram as ng

# n is the size of the ngrams
# k is k-fold validation
def main(n,k):

    # cleaning up the input vec wordlist
    # takes in input and removes punctuation
    # then converts to ngrams
    #inpt = ng.nGrams(n,split.punctRemove(vec))

    # converts author x's text files into list of string lists
    # each list in the parent list is a text file
    # e.g., class1dickens is a list of string lists
    # class1dickens[0] = list of strings in 1.txt in Dickens

    class1dickens = split.wordList("Dickens")
    class2twain = split.wordList("Twain")

    classes = {"Dickens":class1dickens,"Twain":class2twain}

    # getting rid of punctuation in authors lists
    for key in classes:
        lst_of_lsts = classes[key]
        for i in range(0,len(lst_of_lsts)):
            lst_of_lsts[i] = split.punctRemove(lst_of_lsts[i])
        classes[key] = lst_of_lsts

    # splitting the data
    # traintest is a dictionary
    # each value is a list of tuples of training/testing data
    # each tuple = (train, test) represents one fold
    # train = a list of strings (across all docs by that author)
    # test = a list of lists of strings (each list corresp. to a doc)
    traintest = {}
    for key in classes:
        traintest[key] = split.crossValidAll(classes[key],k)

    ctr = 0
    correct = 0
    top = 50
    for x in range (0,k): # for each fold
        training_perfold = {}
        (train_d,test_d) = traintest["Dickens"][x]
        (train_t,test_t) = traintest["Twain"][x]
        training_perfold["Dickens"] = train_d
        training_perfold["Twain"] = train_t
        ngrams = {}
        ngrams["Dickens"] = ng.nGram(n,training_perfold["Dickens"])
        ngrams["Twain"] = ng.nGram(n,training_perfold["Twain"])
        # dict_of_dict = ng.intersectDict(ngrams["Dickens"],ngrams["Twain"])
        dict_of_dict = {}
        dict_of_dict["Dickens"] = ng.topDict(top,ngrams["Dickens"])
        dict_of_dict["Twain"] = ng.topDict(top,ngrams["Twain"])

        testing_perfold = {}
        testing_perfold["Dickens"] = test_d
        testing_perfold["Twain"] = test_t

        for author in testing_perfold:
            for text in testing_perfold[author]:
                ngram_text = ng.nGram(n,text)
                # passing in ONE dictionary of ngrams for ONE fold for ONE author; ONE ngrammed text by same author
                ctr += 1
                print str(ctr) + ") Predict: " + str(pr.predict(dict_of_dict,ngram_text)) + " | Actual: " + author
                if pr.predict(dict_of_dict,ngram_text) == author:
                    correct += 1
    print "Fraction correct: " + str(correct) + "/" + str(ctr)

"""
    for key in traintest:
        ngrams = {}
        for tup in traintest[key]:
            ctr = 0
            (train,test) = tup
            ngrams["Dickens"] = ng.nGram(n,train)
            ngrams["Twain"] = ng.nGram(n,train)

            # generate intersecting dictionaries. intersectDict
            dict_of_dict = ng.intersectDict(ngrams["Dickens"],ngrams["Twain"])
            for t in test:
                testgram = ng.nGram(n,t)
                ctr += 1
               # print str(ctr) + author + ": " + str(pr.predict(dict_of_dict,testgram))


    # generate the ngrams
    # ngrams = dictionary of dictionaries where key is author name
    # the value of parent dict is a dict with ngram as key and frequency as value

    ngrams = {}
    for key in traintest:
        lst_of_tup = traintest[key]
        for tup in lst_of_tup:
            (train,test) = tup
            ngrams[key] = ng.nGram(n,train)

    # generate intersecting dictionaries. intersectDict
    dict_of_dict = ng.intersectDict(ngrams["Dickens"],ngrams["Twain"])
    print dict_of_dict
    ctr = 0
    for key in traintest:
        lst_of_tup = traintest[key]
        for tup in lst_of_tup:
            (train,test) = tup
            for t in test:
                testgram = ng.nGram(n,t)
                ctr += 1
                print str(ctr) + ": " + str(pr.predict(dict_of_dict,testgram))

    #pr.predict(dict_of_dict,vec)
"""
main(2,10)
