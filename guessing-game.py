import random
import math 


#Taking Inputs
lower = int(input("Enter Lower bound: "))

#Taking Inputs 

upper = int(input("Enter upper bound: "))


#generating random number between #the lower and upper 

x = random.randint(lower, upper)

print("\n\tYou've only ", round(math.log(upper - lower + 1, 2)), " chances to guess the integer!\n")

#Initializing the number of guesses: 
count = 0 

#for calculation of minimum number of guesses depends on range 

while count < math.log(upper- lower + 1, 2): 
    count += 1

    #taking guessing number as input
    guess = int(input("Guess a number:- "))

    #Condition testing 
    if x == guess: 
        print("Congratulations you did it in ", count,  " try")
        #once guessed, the loop will break 
        break 
    elif x > guess: 
        print ("You guessed too small!")
    elif x < guess: 
        print("You Guessed Too High!!")

#If Guessing is more than required guesses, 
# shows this output

if count >= math.log(upper - lower + 1, 2): 
    print("\nThe number is %d"%x)
    print("\tBetter luck Next time!")



