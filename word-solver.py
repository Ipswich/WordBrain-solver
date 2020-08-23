#!/usr/bin/python3

import sys
from array import *
    
if len(sys.argv) > 1:
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
    else:
        try:
            inputFile = open(sys.argv[1], 'r')            
        except:
            print("Error: Could not open file.")
            sys.exit(1)
        data = list(map(str.strip, inputFile.readlines()))
        inputFile.close()
else:
    print ('\nWelcome to word solver! Please read all instructions before continuing.\n')
    print ("Type each row of letters followed by a return. "
    "When you\'re done, enter an empty line.")

    count = 0
    data = list()
    while True:
        string = input("Enter row: ")
        if not string:
            break
        data.insert(count, string)
        count += 1

length = int(input("Enter your word length: "))
print("ROWS: " + str(data))
print("WORD LENGTH: " + str(length))

    