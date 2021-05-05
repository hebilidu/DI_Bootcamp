# Week05 Day4 - OOP - Daily challenge - Text Analysis
# Created on  : 210505 by : lidu
# Modified on : 210505 by : lidu
'''
Create a class called Text that takes a string as an argument and store the text in a attribute.
Implement the following methods:
    a method to return the frequency of a word in the text (assume words are separated by whitespace) return None or a meaningful message .
    a method that returns the most common word in the text.
    a method that returns a list of all the unique words in the text.
    a classmethod that returns a Text instance but with a text file: >>> Text.from_file('my_text.txt')
Create a class called TextModification that inherits from Text.
Implement the following methods:
    a method that returns the text without any punctuation.
    a method that returns the text without any english stop-words (check out what this is !!).
    a method that returns the text without any special characters.
'''
with open('english') as f:
    content = f.read().splitlines()
    stop_words = set(content)

class Text():
    def __init__(self, text):
        self.text = text

    def word_frequency(self, word):
        result = self.text.count(word)
        # print(f"The word '{word}'' occurs {result} times in the text")
        return result

    def gen_no_duplicates(self):
        '''Generates list of all words present in text, without duplicates'''
        words = self.text.split()
        no_duplicates = []
        for word in words:
            if word not in no_duplicates:
                no_duplicates.append(word)
        return no_duplicates

    def count_words_occurrences(self):
        '''Generates list of tuples (number of occurrences, word)'''
        occurrences = []
        for word in self.gen_no_duplicates():
            occurrences.append((self.word_frequency(word), word))
        return occurrences

    def most_frequent_word(self):
        occurrences = self.count_words_occurrences()
        occurrences.sort()
        occurrences.reverse()
        return f"Most frequent word is '{occurrences[0][1]}'. It occurs {occurrences[0][0]} times.\n"

    @staticmethod
    def feed_from_file(file_name):
        with open(file_name) as f:
            text = Text(f.read())
        return text

  
class TextModification(Text):
    @staticmethod
    def feed_from_file(file_name):
        with open(file_name) as f:
            text = TextModification(f.read())
        return text

    def trim_special_char(self):
        '''Keeps only alphanumeric characters and spaces'''
        trimmed_text = ''
        for char in self.text:
            if char.isalnum():
                trimmed_text += char
            elif len(trimmed_text) == 0:
                continue
            elif trimmed_text[len(trimmed_text)-1] != ' ':
                trimmed_text += ' '
        return trimmed_text
    
    def remove_stop_words(self):
        no_stop_words_list = []
        for word in self.trim_special_char().split():
            if not word in stop_words:
                no_stop_words_list.append(word)
        return ' '.join(no_stop_words_list)
    

text = Text.feed_from_file('the_stranger.txt')

print('\n' + f"'html' occurs {text.word_frequency('html')} times.")
print(f"'this' occurs {text.word_frequency('this')} times.")
print(f"'body' occurs {text.word_frequency('body')} times.")
print(f"'doctype' occurs {text.word_frequency('doctype')} times.")
print(f"'DOCTYPE' occurs {text.word_frequency('DOCTYPE')} times.")
print(f"'rounded-1' occurs {text.word_frequency('rounded-1')} times.")

print('\n' + text.most_frequent_word() + '\n')

text_mod = TextModification.feed_from_file('the_stranger.txt')
print('Gettin rid of special characters...')
trimmed_text = text_mod.trim_special_char()
print(trimmed_text[0:1000])
print('\n' + f"'html' occurs {text.word_frequency('html')} times.\n")
print('Gettin rid of stop-words...')
no_stop_words_text = text_mod.remove_stop_words()
print(no_stop_words_text[0:1000])