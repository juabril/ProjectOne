import random

#This function finds the minimum value in a list
def find_min(any_list):
    low = any_list[0]
    i=0
    for element in any_list:
        if element < low:
            low = any_list[i]
            i+=1
        else:
            i+=1
    return(low)        


def start_game():
    LOWER = 1
    UPPER = 10
    print("""
    \n***********************************************
    \n****Welcome to the number guessing game!!******
    \n***********************************************
    """)
    user_scores = []
    proceed_answer = "y"
    lowest_score = 0
    while proceed_answer.lower() == "y":                  
        right_answer = random.randint(LOWER,UPPER)
        attempts = 0
        if lowest_score == 0:
            print("")
        else:
            print("\nYour current best score is {} attempts, good luck ! ".format(lowest_score))
        try:
            user_guess = int(input("\nPlease enter your guess, must be an integer between {} and {}: ".format(LOWER,UPPER)))
            while user_guess < LOWER or user_guess > UPPER:
                print("\nYour input is outside the valid range, please try again")
                user_guess = int(input("\nPlease enter your guess, must be an integer between {} and {}: ".format(LOWER,UPPER)))    
            attempts += 1                                  
        except ValueError:
            print("\nThat's not a valid input, please enter an integer between {} and {}".format(LOWER, UPPER))         
        else:
            while user_guess != right_answer:
                if user_guess > right_answer:
                    print("\nThe right number is lower than your guess")
                    try:
                        user_guess = int(input("\nWhat is your new, lower guess? "))
                        while user_guess < LOWER or user_guess > UPPER:
                            print("\nYour input is outside the valid range, please try again")
                            user_guess = int(input("\nPlease enter your guess, must be an integer between {} and {}: ".format(LOWER,UPPER)))    
                        attempts += 1
                    except ValueError:
                        print("\nThat's not a valid input, please enter an integer between {} and {}".format(LOWER, UPPER)) 
                        print("We won't count this input towards your number of attempts")
                        print("Your current guess is {} ".format(user_guess))
                        print("Your current number of attempts is {}".format(attempts))                        
                elif user_guess < right_answer:
                    print("\nThe right number is higher than your guess")
                    try:
                        user_guess = int(input("\nWhat is your new, higher guess? "))
                        while user_guess < LOWER or user_guess > UPPER:
                            print("\nYour input is outside the valid range, please try again")
                            user_guess = int(input("\nPlease enter your guess, must be an integer between {} and {}: ".format(LOWER,UPPER)))
                        attempts += 1
                    except ValueError:
                        print("\nThat's not a valid input, please enter an integer between {} and {} ".format(LOWER, UPPER))
                        print("We won't count this input towards your number of attempts ")
                        print("Your current guess is {} ".format(user_guess))
                        print("Your current number of attempts is {}".format(attempts))               
            print("\n***** Good job! you guessed it in {} attempts *****".format(attempts))      
            user_scores.append(attempts)
            lowest_score = find_min(user_scores)
            print("\nYou have played {} times and your current best score is {} attempts".format(len(user_scores),lowest_score))
            proceed_answer = input("\nWould you like to play another game (y/n)? ")
    print("\nGood bye ! come back soon !\n")            
start_game()
