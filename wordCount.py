#modified version of original code by Dr. Freudenthal
#! /usr/bin/env python3

import sys        # command line arguments
import re         # regular expression tools


textFname = sys.argv[1]
outputFname = sys.argv[2]

# will contain all words in a list
dictionary = []

# SUPER USEFUL dynamic list/hashtable or dict()
listOfWords = {}

# attempt to open input file
with open(textFname, 'r') as inputFile:
    for line in inputFile:
        # get rid of newline characters
        line = line.strip().split()
        
        # add all words to dictionary list
        for i in line:
            dictionary.append( str(i).lower() )




for i in range(0, len(dictionary)):
    # check if word in dictionary, assign count value for word
    if dictionary[i] not in listOfWords:
        listOfWords[ dictionary[i] ] = 1
    elif dictionary[i] in listOfWords:
        listOfWords[ dictionary[i] ] += 1  




# listOfWords contains the values for dictionary() as a hash table, and includes their total count for each word

outputFile = open(outputFname, 'w')

for word,number in sorted(listOfWords.items()):
# 'too many values to unpack' error without '.items()' 
    outputFile.write("%s %d\n" %(word, number) )

outputFile.close()






#Sources:
#https://developers.google.com/edu/python/dict-files
#https://stackoverflow.com/questions/16922214/reading-a-text-file-and-splitting-it-into-single-words-in-python
#Several other stackoverflow links, but not as relevant as these
