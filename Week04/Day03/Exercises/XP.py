# Week04 Day03 - XP - Exercises
# Created on  : 210427 by : lidu
# Modified on : 210427 by : lidu

def main():
    #  Exercise 1 : Convert lists into dictionaries
    print('\nExercise 1\n==========')
    # Convert the two following lists, into dictionaries.
    # Hint: Use the zip method
    keys = ['Ten', 'Twenty', 'Thirty']
    values = [10, 20, 30]
    # Expected output:
    # {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
    new_dic = dict(zip(keys, values))
    print(new_dic)

    #  Exercise 2 : Cinemax #2
    print('\nExercise 2\n==========')
    # “Continuation of Exercise Cinemax from Week4Day2 XP”
    #     A movie theater charges different ticket prices depending on a person’s age.
    #         if a person is under the age of 3, the ticket is free.
    #         if they are between 3 and 12, the ticket is $10.
    #         if they are over the age of 12, the ticket is $15.
    #     Given the following object:
    #     family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
    # 
    #     How much does each family member have to pay ?
    #     Print out the family’s total cost for the movies.
    #     Bonus: Ask the user to input the names and ages instead of using the provided family variable 
    #     (Hint: ask the user for names and ages and add them into a family dictionary that is initially empty).
    # names = input('Enter names separated with spaces : ').split() 
    
    # ages = []
    # for name in names:
    #     age = 0
    #     while age == 0:
    #         age_txt = input('Enter age for {} : '.format(name))
    #         try:
    #             age = int(age_txt)
    #         except ValueError:
    #             print("That's not an int!")
    #         ages.append(age)

    # family = dict(zip(names, ages))
    # print(family)
        
    # total = 0
    # num1, num2, num3 = 0, 0, 0
    # for name, age in family.items():
    #     if int(age) < 3:
    #         num1 += 1
    #         print("{} pays nothing.".format(name))
    #     if 3 <= int(age) < 12:
    #         num2 += 1
    #         total += 10
    #         print("{} pays $10.".format(name))
    #     elif int(age) >= 12:
    #         num3 += 1
    #         total += 15
    #         print("{} pays $15.".format(name))

    # print ('So: {} under 3, {} between 3 and 12, {} over 12 makes ${}'.format(num1, num2, num3, total))

   
    #  Exercise 3: Zara
    print('\nExercise 3\n==========')
    # 1. Here is some information about a brand.
    brand = {
        'name': 'Zara', 
        'creation_date': 1975, 
        'creator_name': 'Amancio Ortega Gaona', 
        'type_of_clothes': ['men', 'women', 'children', 'home'], 
        'international_competitors': ['Gap', 'H&M', 'Benetton'],
        'number_stores': 7000, 
        'major_color': {
            'France': 'blue', 
            'Spain': 'red', 
            'US': ['pink', 'green'],
        }
    }
    print("brand =", brand)
    # 2. Create a dictionary called brand which value is the information from part one (turn the info into keys and values).
    # 3. Change the number of stores to 2.
    brand["number_stores"] = 2
    # 4. Print a sentence that explains who Zaras clients are.
    print("\nZara clients are {} who may also visit {}".format(', '.join(brand["type_of_clothes"]), ', '.join(brand["international_competitors"])))
    # 5. Add a key called country_creation with a value of Spain.
    # 6. Check if the key international_competitors is in the dictionary. If it is, add the store Desigual.
    # 7. Delete the information about the date of creation.
    # 8. Print the last international competitor.
    # 9. Print the major clothes colors in the US.
    # 10. Print the amount of key value pairs (ie. length of the dictionary).
    # 11. Print the keys of the dictionary.
    # 12. Create another dictionary called more_on_zara with the following details:

    # creation_date: 1975 
    # number_stores: 10 000

    # 13. Use a method to add the information from the dictionary more_on_zara to the dictionary brand.
    # 14. Print the value of the key number_stores. What just happened ?

  
    # Exercise 4: 
    print('\nExercise 4\n==========')
    users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]
    # #1/
    # >>> print(disney_users_A)
    # {"Mickey": 0, "Minnie": 1, "Donald": 2, "Ariel": 3, "Pluto": 4}
    # #2/
    # >>> print(disney_users_B)
    # {0: "Mickey",1: "Minnie", 2: "Donald", 3: "Ariel", 4: "Pluto"}
    # #3/ 
    # >>> print(disney_users_C)
    # {"Ariel": 0, "Donald": 1, "Mickey": 2, "Minnie": 3, "Pluto": 4}
    # Use a for loop to recreate the 1st result. Tip : don’t hardcode the numbers.
    # Use a for loop to recreate the 2nd result. Tip : don’t hardcode the numbers.
    # Use a method to recreate the 3rd result. Hint: The 3rd result is sorted alphabetically.
    # Only recreate the 1st result for:
    #     The characters, which names contain the letter “i”.
    #     The characters, which names start with the letter “m” or “p”.
    disney_users_A = dict(zip(users, list(range(len(users)))))
    print(disney_users_A)
    disney_users_B = dict(zip(list(range(len(users))), users))
    print(disney_users_B)
    users.sort()
    disney_users_C = dict(zip(users, list(range(len(users)))))
    print(disney_users_C)
    new_list = [user for user in users if (user.find('i') and (user.index('m') == 0 or user.index('p') == 0))]
    disney_users_D = dict(zip(new_list, list(range(len(users)))))
    print(disney_users_D)

if __name__ == "__main__":
    main()
