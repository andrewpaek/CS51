import os
import pickle

# function returns number of files in a directory
def numFiles (directory):
    ctr = 0
    for name in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, name)):
            ctr += 1
    return ctr

rootDir = os.getcwd() + os.sep + "copy" + os.sep
authors = ["Dickens","Twain"]
num_files = {}

for author in authors:
    num_files[author] = numFiles(rootDir + author)

bfile=open(r'C:\num_files.pkl','wb')
pickle.dump(num_files,bfile)
bfile.close()
