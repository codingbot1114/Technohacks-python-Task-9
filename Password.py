import string
import random
import array
# import tkinter
# from tkinter import *

# What this Program does!!!!

# This is an Random password generated program....

# alpha = ["a" ,"b", "c", "d", "e" "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]  #-- This is comment section so you can ignore this [Para]....

# This is Symbols signs....... I just add all this Symbols in one [Var]
SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>', 
           '*', '(', ')', '<']

# This is Randomize Function(Code)
rand_symbol = random.choice(SYMBOLS)
ab = random.shuffle(rand_symbol)

# This is Number var's for calling/performing an given tasks 
a = ("1")
b = ("2")
c = ("3")
d = ("4")
e = ("5")
g = ("6")

# While True means:-- Run this Code whenver the entered task is true 
while True:
    print("\nWelcome to the Random Password generator by Prathamesh Rajapurkar\n")
    # print("\n")
    print("1. Alphabetical Password")
    print("2. Numerical Password")
    print("3. Special Characters Password")
    print("4. Random suffle Password")
    print("5. Manually Entered Password")
    print("6. Exit the Program\n")
    slc = input("Enter the Following Digit : ")
    if slc == a:
        print("\n1. CAPITAL LETTERS ONLY")
        print("2. SMALL LETTERS ONLY")
        print("3. Mix Letters\n")
        diff = (input("Enter the folloing choice : "))
        if diff == a:
            asklen = int(input("Enter the Length of Password : "))
            
            # I just comment it out.... Just because i found the other way to do this task easily
            # askrev = input("Want to print in Revserse String ?")
            # if askrev == a:
            #     resrev = ''.join(random.choices(string.ascii_uppercase, k = asklen))
            #     print(resrev[::-1])
            # else:
            #     print("WARNING : Enter the ABOVE OPTIONS")
            
            res = ''.join(random.choices(string.ascii_uppercase, k = asklen))
            print("The generated random Alphabet : " + str(res))
        elif diff == b:
            asklen2 = int(input("Enter the Length of Password : "))
            res = ''.join(random.choices(string.ascii_lowercase, k = asklen2))
            print("The generated random Alphabet : " + str(res))
        elif diff == c:
            asklen3 = int(input("Enter the Length of Password : "))
            res = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k = asklen3))
            print("The generated random Alphabet : " + str(res))
        else:
            print("$WARNING$ - Please enter the following selection\n")
        # print result
    elif slc == b:
        asklen2 = int(input("Enter the Length of Password : "))
        res2 = ''.join(random.choices(string.digits, k = asklen2))
        # print result
        print("The generated random Number : " + str(res2))
    elif slc == c:
        MAX_LEN = int(input("Enter the Length of Characters : "))
        COMBINED_LIST = SYMBOLS
        rand_symbol = random.choice(SYMBOLS)
        temp_pass = rand_symbol
        for x in range(MAX_LEN - 1):
            temp_pass = temp_pass + random.choice(COMBINED_LIST)
            temp_pass_list = array.array('u', temp_pass)
            random.shuffle(temp_pass_list)
        password = ""
        for x in temp_pass_list:
                password = password + x
        print("The generated random Characters : " + str(password))
    elif slc == d:
        MAX_LEN = int(input("Enter the Length of Password : "))
        DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                            'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                            'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                            'z']
        UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                            'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q',
                            'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                            'Z']
        SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
                '*', '(', ')', '<']
        COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS
        rand_digit = random.choice(DIGITS)
        rand_upper = random.choice(UPCASE_CHARACTERS)
        rand_lower = random.choice(LOCASE_CHARACTERS)
        rand_symbol = random.choice(SYMBOLS)
        temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol
        for x in range(MAX_LEN - 4):
            temp_pass = temp_pass + random.choice(COMBINED_LIST)
            temp_pass_list = array.array('u', temp_pass)
            random.shuffle(temp_pass_list)
        password = ""
        for x in temp_pass_list:
                password = password + x
        print("The generated random Password : " + str(password))
    elif slc == e:
        usrask = input("Enter the desire characters : ")
        print("\n")
        print("1. Want to shuffle it ?")
        print("2. Want to Reverse it ?")
        custask = input("Enter the following Options : ")
        if custask == a:
            usrask = ''.join(random.sample(usrask,len(usrask)))
            print("Your Manually modified password is ", usrask)
        elif custask == b:
            print("Your Manually Reversed password is " + usrask[::-1])
        # else:
        #     print("$WARNING --Invalid selection\nPlease Enter the given value from list")    
    elif slc == g:
        print("Thank you for Choosing")
        quit()
    else:
        print("$WARNING --Invalid selection\nPlease Enter the given value from list")
