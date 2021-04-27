# Week04 Day03 - Timed challenge 1 - Perfect number
# Created on  : 210427 by : lidu
# Modified on : 210427 by : lidu
# 
# A perfect number is a positive integer that is equal to the sum of its divisors.
# However, the number itself is not included in the sum.
# 
#     Ask the user for a number and print whether or not it is a perfect number. If yes, print True else False.
#     Hint: Google perfect numbers
# 
# Example
# Input -- Enter the number:6
# Output -- True
# 
# Input -- Enter the number:10
# Output --  False

def main():
    while True:
        input_txt = input("Please enter a number (nothing or 0 will end the program): ")
        if input_txt in ["", "0"]:
            break
        try:
            n = int(input_txt)
        except ValueError:
            print("That's not an int!")
            continue

        dividers = []
        for i in range(1, n // 2 + 1):
            if n % i == 0:
                dividers.append(i)
        print(dividers)
        output = False
        if sum(dividers) == n:
            output = True

        print("\nInput  --", n)
        print("Output --", output, "\n")


if __name__ == "__main__":
    main()
