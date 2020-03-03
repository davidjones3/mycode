#!/usr/bin/env python3

import sys
import random

ans = True

while ans:
    question = input("Ask the magic 8 ball a question (type exit to end): ")
    
    answers = random.randint(1,8)
    
    if question == "":
        print("\n Nothing? Oh come on... \n\n")
    	
    elif question == "exit":
       # sys.exit()
        break
    elif answers == 1:
        print("It is certain")
    
    elif answers == 2:
        print("Outlook good")
    
    elif answers == 3:
        print("You may rely on it")
    
    elif answers == 4:
        print("Ask again later")
    
    elif answers == 5:
        print ("Concentrate and ask again")
    
    elif answers == 6:
        print ("Reply hazy, try again")
    
    elif answers == 7:
        print ("My reply is no")
    
    else:
        print ("My sources say no")


print("The End!")
