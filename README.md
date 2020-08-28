# word-solver
Not so much a solver as a helper, this script is for the WordBrain mobile app. WordBrain is a variation on traditional word searches, where the user is challenged to find words hidden in a grid of seemingly random letters. However, unlike a traditional word search, words are not strictly linear. When searching for a word, the next letter in a given sequence may be in any direction, with the caveat of not being able to reuse visited tiles. Additionally, upon completion of the expected word, the tiles "above" the used tiles fall down to fill in hole. As such, the state of the board changes after the correct word is found. Each board has only one solution, yet some words may be found in multiple ways, leading to unwinnable states.

WordBrain is structured so that at the start of a round a new board of NxN letter tiles is presented with a series of word lengths at the bottom. The user is given the order in which the words must be found, but only the lengths of the words that must be found. There is no indication of what the starting letter might be, unless the user uses a freemium hint.

This script functions by either taking in a file or input that describes the current state of the board, and a number for the length of the word to be searched for. It then supplies a list of ALL of the words that are of the correct length that can be found on the supplied board.

Proper input data is defined as:
- N x N in shape (only square inputs)
- Contains alphabetical characters, using non-alphabetical characters to mark empty spaces (i.e. '-').

Example:

   ---e-  
   --ls-  
   d-rr-  
   o-lo-  
   obeh-  
