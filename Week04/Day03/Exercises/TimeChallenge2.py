# Week04 Day03 - Reverse the Sentence
# Created on  : 210427 by : lidu
# Modified on : 210427 by : lidu
# 
# Write a program to reverse the sentence wordwise.
# 
# Input:
# You have entered a wrong domain
# Output:
# domain wrong a entered have You

import re # required for a version of split with multiple concurrent separators

def split_multiple_separators(text):                                  
    strings = re.split('[:,\s]{1}', text)                                          
    return strings

def main():
    while True:
        input_txt = input('Enter a sentence (nothing will stop the program): ')
        if input_txt == "":
            break        
        words_list = split_multiple_separators(input_txt)
        words_list.reverse()
        output_txt = " ".join(words_list)
        print("Input:\n", input_txt)                                                     
        print("Output:\n", output_txt)   

if __name__ == "__main__":
    main()
