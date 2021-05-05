# Week05 Day4 - OOP - XP exercises
# Created on  : 210505 by : lidu
# Modified on : 210505 by : lidu

# Exercise 1 : Random Sentence Generator
print('\nExercise 1 : \n=================')
'''
Description: In this exercise we will create a random sentence generator. We will do this by asking the user how long the sentence should be and then printing the generated sentence.

Hint : The generated sentences do not have to make sense.

    Create a function called get_words_from_file. This function should read the file’s content and return the words as a collection. What is the correct data type to store the words?

    Create another function called get_random_sentence which takes a single parameter called length. The length parameter will be used to determine how many words the sentence should have. The function should:
        use the words list to get your random words.
        the amount of words should be the value of the length parameter.

    Take the random words and create a sentence (using a python method), the sentence should be lower case.

    Create a function called main which will:
    Print a message explaining what the program does.

    Ask the user how long they want the sentence to be. Acceptable values are: an integer between 2 and 20. Validate your data and test your validation!
        If the user inputs incorrect data, print an error message and end the program.
        If the user inputs correct data, run your code.

'''
import random  # multiple choices with possible duplicates (sample, otherwise)

with open('sowpods.txt') as f:
   thesaurus = f.read().splitlines()

def get_words_from_file(num):
   '''Returns num words from thesaurus, as a list'''
   return random.choices(thesaurus, k = num)

def get_random_sentence(length):
   return (' '.join(get_words_from_file(length))).lower()

def main():
   '''This program builds a sentence with a number of words extracted randomly from a thesaurus.
   The number is specified by the user.'''
   while True:
      input_str = input("Please enter an integer between 2 and 20 (Just press <Enter> to stop the program): ")
      if len(input_str) == 0: 
         print("End of program. Thanks for playing.")
         return
      try:
         if 1 < int(input_str) < 21:
            print(get_random_sentence(int(input_str)))
      except:
         print("Invalid input")
         continue

if __name__ == "__main__":
   main()      

# Exercise 2 : Working with JSON
print('\nExercise 2 : \n=================')
'''
Access the nested “salary” key from the JSON-string above.
Add a key called “birth_date” to the JSON-string at the same level as the “name” key.
Save the dictionary as JSON to a file.
'''
import json

sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

my_dict = json.loads(sampleJson)
print("salary = " + str(my_dict['company']['employee']['payable']['salary']))
my_dict['company']['employee']['birth_date'] = None
print(my_dict)

with open('a_file.json', 'w') as f:
   json.dump(my_dict, f)
