#!/usr/bin/python3

import sys
import copy
from array import *

foundWords = list()

def searchFromLocation(currentWord, letterIndex, rowIndex, columnIndex, length, matrix, dictionary):
    upperBound = len(matrix[0]) - 1
    # rowIndex is out of bounds - wrap
    if rowIndex == -1:
        rowIndex = upperBound
    elif rowIndex > upperBound:
        rowIndex = 0
    # columnIndex is out of bounds - wrap
    if columnIndex == -1:
        columnIndex = upperBound
    elif columnIndex > upperBound:
        columnIndex = 0
    # Location has been visited - end
    elif matrix[rowIndex][columnIndex] is '0':
        return
    # Filter dictionary by letterIndex value
    filteredDictionary = list(filter(lambda x: x[letterIndex] == matrix[rowIndex][columnIndex], dictionary))
    # Update currentWord to include the current location's character
    currentWord = currentWord + matrix[rowIndex][columnIndex]
    # Deep copy, then update the copy with a tombstone at current location
    copiedMatrix = copy.deepcopy(matrix)
    copiedMatrix[rowIndex][columnIndex] = '0'
    # If we've reached length, end.
    if letterIndex == length - 1:
        # If word is in dictionary, add to found words.
        if currentWord in filteredDictionary:
            # print(currentWord)
            foundWords.append(currentWord)
        return        
    else:
        # Recurse!
        searchFromLocation(currentWord, letterIndex + 1, rowIndex - 1, columnIndex + 1, length, copiedMatrix, filteredDictionary)
        searchFromLocation(currentWord, letterIndex + 1, rowIndex - 1, columnIndex, length, copiedMatrix, filteredDictionary)
        searchFromLocation(currentWord, letterIndex + 1, rowIndex - 1, columnIndex - 1, length, copiedMatrix, filteredDictionary)
        searchFromLocation(currentWord, letterIndex + 1, rowIndex, columnIndex + 1, length, copiedMatrix, filteredDictionary)
        searchFromLocation(currentWord, letterIndex + 1, rowIndex, columnIndex - 1, length, copiedMatrix, filteredDictionary)
        searchFromLocation(currentWord, letterIndex + 1, rowIndex + 1, columnIndex + 1, length, copiedMatrix, filteredDictionary)
        searchFromLocation(currentWord, letterIndex + 1, rowIndex + 1, columnIndex, length, copiedMatrix, filteredDictionary)
        searchFromLocation(currentWord, letterIndex + 1, rowIndex + 1, columnIndex - 1, length, copiedMatrix, filteredDictionary)



def searchMatrix(dictionary, matrix, length):
    size = len(matrix)
    # Deep copy to preserve original
    copiedMatrix = copy.deepcopy(matrix)
    for r in range(size):
        for c in range(size):
            # Starting point
            searchFromLocation('', 0, r, c, length, copiedMatrix, dictionary)

# If arguments...
if len(sys.argv) > 1:
    # Display help info
    if sys.argv[1] == 'help':
        print ("\nWelcome to word solver!\n"
        "This script finds words of the supplied length in the letter matrix.")
        print ("This script may be used in two ways:\n")
        print ("1) Run the program without any arguments: \n"
        "Type each row of letters followed by a return. " 
        "When you've entered each row, enter an empty line.\n"
        "You will then be prompted for the length of the word; enter this, and press return.\n")
        print ("2) Run the program with a text file as an argument: \n"
        "This text file MUST contain an (N x N) matrix of letters, "
        "Where N is equal to both the number of letters in each row and the number of rows."
        "\nFor example:\n\n"
        "     abcd\n"
        "     efgh\n"
        "     ijkl\n"
        "     mnop\n\n"
        "You will then be prompted for the length of the word; enter this, and press return.")
        sys.exit(0)
    # Try to parse entered file
    else:
        try:
            inputFile = open(sys.argv[1], 'r')            
        except:
            print("Error: Could not open input file.")
            sys.exit(1)
        data = list(map(str.strip, inputFile.readlines()))
        inputFile.close()
# No arguments...
else:
    print ('\nWelcome to word solver! Please read all instructions before continuing.\n')
    print ("Type each row of letters followed by a return. "
    "When you\'re done, enter an empty line.")
    count = 0
    data = list()
    # Get input from user
    while True:
        string = input("Enter row: ")
        if not string:
            break
        data.insert(count, string)
        count += 1

# Format data to all upper case
data = list(map(str.upper, data))
data = list(map(lambda x: list(x), data))

# Get length of word to search for (steps to take)
length = int(input("Enter your word length: "))

# Open dictionary
try:
    dictionaryFile = open('./words_alpha.txt', 'r')            
except:
    print("Error: Could not open dictionary.")
    sys.exit(1)
# Create list from dictionary file
dictionary = list(map(str.strip, dictionaryFile.readlines()))
dictionary = list(map(str.upper, dictionary))
# dictionary = list(map(lambda x: list(x), dictionary))
dictionaryFile.close()

# Shorten dictionary to only words of expected length
dictionary = list(filter(lambda x : len(x) == length, dictionary))

searchMatrix(dictionary, data, length)

cleanedList = []
[cleanedList.append(x) for x in foundWords if x not in cleanedList]
cleanedList.sort()

print(cleanedList)
    