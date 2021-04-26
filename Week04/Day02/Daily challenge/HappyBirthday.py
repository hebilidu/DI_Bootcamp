# Week04 Day02 - Daily Challenge - Happy birthday
# Created on  : 210426 by : lidu
# Modified on : 210426 by : lidu

from datetime import datetime

def main():
    # Ask the user for their birthdate (specify the format, for example: DD/MM/YYYY).
    # Display a little cake as seen below:
    #       ___iiiii___
    #      |:H:a:p:p:y:|
    #    __|___________|__
    #   |^^^^^^^^^^^^^^^^^|
    #   |:B:i:r:t:h:d:a:y:|
    #   |                 |
    #   ~~~~~~~~~~~~~~~~~~~
    # The number of candles on the cake should be the last number of the users age, if they are 53, then add 3 candles.
    # Bonus : If they were born on a leap year, display two cakes !

    layers = [
        '    ___iiiii___    ',
        '   |:H:a:p:p:y:|   ',
        ' __|___________|__ ',
        '|^^^^^^^^^^^^^^^^^|',
        '|:B:i:r:t:h:d:a:y:|',
        '|                 |',
        '~~~~~~~~~~~~~~~~~~~']
    birthdate = input('What is your birthdate (dd/mm/yyyy) ? ')
    year = int(birthdate[6:10])
    age = 2021 - int(year)
    candles = int(age) % 10
    # Rebuild top layer
    unders = 11 - candles
    if unders % 2 == 0:
        layers[0] = '    ' + '_' * (unders // 2) + 'i' * candles + '_' * (unders // 2) + '    '
    else:
        layers[0] = '    ' + '_' * (unders // 2) + 'i' * candles + '_' * (unders // 2 +1) + '    '

    # Check leap year
    is_leap = False
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                is_leap = True
            else:
                is_leap = False
        else:
            is_leap = True
    else:
        is_leap = False

    for layer in layers:
        print(layer + is_leap * layer)

if __name__ == "__main__":
    main()