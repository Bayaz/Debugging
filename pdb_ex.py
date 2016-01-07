import sys
import pdb
from random import choice

random1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
random2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

while True:
    print("To exit this game type: 'exit'")

    #debugging trace where you can begin tracing through the code

    pdb.set_trace()

    answer = input("What is {} times {}? :" .format(choice(random2),\
        choice(random1)))

    test = choice(random2) * choice(random1)

    if answer == "exit":
        print("Now exiting the game")
        sys.exit()


    #determine if the answer if correct
    elif answer == choice(random2) * choice(random1):
        print("Correct Choice!")

    else:
        print("WRONG")


