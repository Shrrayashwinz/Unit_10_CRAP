"""
Author: Shrrayash Srinivasan
Purpose: The program's purpose is to read a text chosen by the user and count how much each word appears. It 
eliminates punctuation, ignores differences, and handles files gracefully.
Date: October 27, 2025
"""

import string

def main():
    try:
        filename = input("Enter filename to analyze:")
        with open(filename, 'r') as file:
            word_data = wordFreq(file)
    
    except FileNotFoundError:
        print(f'ERROR: You have asked for the file, {filename}. Sadly {filename} does not exist. Please try again!')

    
    else:
        printOut(word_data)

def wordFreq(file):
    word_count = {}
    for line in file:
        #Remove punctuation and normalize case
        line = line.translate(str.maketrans('', '', string.punctuation)).lower()
        words = line.split()
        for word in words:
            word_count[word] = word_count.get(word, 0) + 1
    return word_count
  
def printOut(word_data):
    print("Word frequency report:")
    for word in sorted(word_data):
        print(f"{word:<15} : {word_data[word]}")
       
# Now we just run the program
if __name__ == "__main__":
    main()



