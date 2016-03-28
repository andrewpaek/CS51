# function returns a dict
# key is the ngram string; value is the number of occurrences
# wordList is a list of strings

def nGram (n,wordList):
    end_index = len(wordList)-n+1
    dict = {}

    for i in range (0,end_index):
        ngram = ""
        # creates ngram string
        for word in wordList[i:i+n]:
            if len(ngram) == 0:
                ngram = word
            else:
                ngram = ngram + " " + word
        # seeing if ngram already exists
        if ngram in dict:
            dict[ngram] = dict[ngram] + 1
        else:
            dict[ngram] = 1
    return dict

# returns top n entries in dict
def topDict (n,dict):
    lowest = ("",1)
    newD = {}
    size = 0
    for key in dict:
        if size < n:
            if dict[key] <= lowest[1]:
                lowest = (key,dict[key])
            newD[key] = dict[key]
            size += 1
        elif dict[key] > lowest[1]:
            del newD[lowest[0]]
            newD[key] = dict[key]
            newLowKey = min(newD, key=newD.get)
            lowest = (newLowKey, newD[newLowKey])
    return newD

# returns a dictionary of dictionaries
def intersectDict (d1,d2):
    commonKeys = d1.viewkeys() & d2.viewkeys()
    common_d1 = {}
    common_d2 = {}
    big_dict = {}
    for key in commonKeys:
        common_d1[key] = d1[key]
        common_d2[key] = d2[key]
    big_dict["Dickens"] = common_d1
    big_dict["Twain"] = common_d2
    return big_dict

