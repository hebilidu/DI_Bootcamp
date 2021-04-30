# Week04 Day05 - Daily challenge - Sorting
# Created on  : 210429 by : lidu
# Modified on : 210429 by : lidu

while True:
    inp = input("\nEnter words separated with commas : ")
    if inp == '':
        print('\nEnd of program. Goodbye.\n')
        break
    wordlist = inp.split(',')
    print('\n' + ','.join(wordlist))
    wordlist.sort()
    print(','.join(wordlist) + '\n')

    # Second method
    print('Same with use of list comprehension...')
    newlist = []
    word = ''

    for letter in inp:
        if letter == ',':
            newlist.append(word)
            word = ''  
        else:
            word += letter
    newlist.append(word)
    
    print('\n' + ','.join(newlist))
    newlist.sort()
    print(','.join(newlist) + '\n')