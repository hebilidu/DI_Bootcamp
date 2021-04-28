# Week04 Day03 - Daily Challenge - Caesar Cypher
# Created on  : 210427 by : lidu
# Modified on : 210428 by : lidu
#
# In cryptography, a Caesar cipher is one of the simplest and most widely known encryption techniques.
# It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some
#  fixed number of positions down the alphabet.

# For example, with a left shift of 3, D would be replaced by A, E would become B, and so on. 
# The method is named after Julius Caesar, who used it in his private correspondence.

# Create a python program that encrypts and decrypts messages with ceasar cypher, 
# the user entries the program, and then the program asks him if he wants to encrypt or decrypt, 
# and then execute encryption/decryption on a given message and a given shift. 

sample_txt = "abcde fghij ;:0908 klmn opqr stuvw xyz ABCDE RSTUVW-XYZ"

def main():
    while True:
        input_action = input("C for Cypher / D for Decypher / S for Stop : ")
        
        if input_action in ["S","s"]:
            break
        if input_action in ["D", "d"]:
            cypher = -1
        elif input_action in ["C", "c"]:
            cypher = 1
        else:
            continue

        cypher_text = ""
        input_txt = input("Enter a text, please (empty string stops the program): ")
        if input_txt == "":
            break

        # for letter in input_txt:
        #     if is_alpha(letter):
        #         if cypher == 1 and ((ord(letter) > 119) or (87 < ord(letter) < 91)):
        #             cypher_text += chr(ord(letter) - 23)
        #         elif cypher == -1 and ((ord(letter) < 68) or (96 < ord(letter) < 100)):
        #             cypher_text += chr(ord(letter) + 23)
        #         else:
        #             cypher_text += chr(ord(letter) + 3 * cypher)
        #     else:
        #         cypher_text += letter

        # Version using modulo
        for letter in input_txt:
            if letter.isalpha():
                if ord(letter) > 96:    # start of lowercase range (codes from 97 to 122)
                    cypher_text += chr((ord(letter) + (3 * cypher) - 97) % 26 + 97)
                else:                   # we are in uppercase range (codes from 65 to 90)
                    cypher_text += chr((ord(letter) + (3 * cypher) - 65) % 26 + 65)
            else:
                cypher_text += letter

        print("\n" + input_txt + "\n" + cypher_text + "\n")

if __name__ == "__main__":
    main()