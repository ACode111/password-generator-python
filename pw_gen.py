import random
import string
import sys

def password_gen():
    
    while True:
        pw_length = input("Enter password length(q for exit): ")

        if pw_length.lower() == "q":
            sys.exit()
        else:
            try:
                pw_length = int(pw_length)
            except ValueError:
                print("Please enter a valid number or 'q'")
                continue
        
        if pw_length < 8:
            print("Password length must be at least 8 characters")
            continue

        symbol_chars = string.punctuation
        number_chars = string.digits
        letter_chars = string.ascii_letters

        question_letter = input("Do you want to include letters?(Default is only numbers)(y/n): ")
        question_symbol = input("Do you want to include symbols?(Default is only numbers)(y/n): ")

        ingredients = (number_chars)

        if question_letter == "y":
            ingredients += letter_chars

        if question_symbol == "y":
            ingredients += symbol_chars

        pw = ""

        for i in range(pw_length):
            pw += random.choice(ingredients)

        printquestion = input("Do you want to print the password?(y/n)")

        if printquestion.lower() == "y":
            print(pw)
        else:
            return pw

password_gen()
