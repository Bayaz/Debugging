#corrected_pdb_ex.py

import sys
import pdb
from random import choice

random1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
random2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

while True:
    print("To exit this game type: 'exit'")
    num1 = choice(random2)
    num2 = choice(random1)
    #debugging trace where you can begin tracing through the code
    #pdb.set_trace()
    raw_answer = input("What is {} times {}? :" .format(num1,\
        num2))

    try:
        answer = int(raw_answer)

        if answer == num1 * num2:
            print("Correct Choice!")
        else:
            print("WRONG")

    except ValueError:
        if raw_answer == 'exit':
            print("Now exiting the game")
            sys.exit()
        else:
            print("that answer is not valid try again")



 

