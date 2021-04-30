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
    