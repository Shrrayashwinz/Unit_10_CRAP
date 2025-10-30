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

def wordFreq():

def printOut()



