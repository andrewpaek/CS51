import re
import os, os.path
import pickle

tag_main = "PROJECT GUTENBERG EBOOK"
tag_begin = "START OF"
tag_end = "END OF"
DIR = os.getcwd() + os.sep + "copy" + os.sep

# loads author and file information
f_ = open(r'C:\num_files.pkl','rb')
num_files = pickle.load(f_)
f_.close()

# iterates through files to remove header and footer junk
for author in num_files:
    endRange = num_files[author]
    for x in range (1,endRange+1):
        tag_begin_found = False
        tag_end_found = False
        f = open(DIR + author + os.sep + str(x) + ".txt","r")
        lines = f.readlines()
        f.close()
        f = open(DIR + author + os.sep + str(x) + ".txt","w")
        for line in lines:
            if not tag_begin_found:
                tag_begin_found = re.search("(.*" + tag_begin + ".*" + tag_main + ".*)",line)
            elif tag_begin_found and not tag_end_found:
                tag_end_found = re.search("(.*" + tag_end + ".*" + tag_main + ".*)",line)
                if not tag_end_found:
                    f.write(line)
        f.close()

