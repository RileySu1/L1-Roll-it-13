# functions go here

def yes_no(question):

     """Checks user response to a question is yes/ no (y/n). returns 'yes' or 'no' """

     while True:

        response = input(question).lower()

        #check the user says yes / no / y / n
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("please enter yes / no")

def instructions():
    """Prints instructions"""

    print("""
*** Instructions ****

Roll the dice and try to win!
    """)



def int_checker():
    """Checks users enter an integer more than / equal to 13"""

    error ="Please enter am integer more than / equal to 13."

    while True:
        try:
            response = int(input("What is your goal? "))

            if response < 13:
                print(error)
            else:
                return response

        except ValueError:
            print(error)

# Main routine

# ask the user if they want instructions (check they say yes / no)
want_instructions = yes_no("Do you want to see the instructions? ")

# Display the instructions if the user wants to see them...
if want_instructions == "yes":
    instructions()

print()
game_goal = int_checker()
print(game_goal)


import random

# Intialise rounds points
user_points = 0
comp_points = 0
double_user = "no"

# Roll the dice for the user and note if they got a double
user_one =  random.randint(1, 6)
user_two =  random.randint(1, 6)

if user_one == user_two:
    double_user = "yes"


# roll the dice for the computer
comp_one =  random.randint(1, 6)
comp_two =  random.randint(1, 6)

# Update the user / computer points
user_points += user_one + user_two
comp_points += comp_one + comp_two


# Output the results
print("\nInitial Points")
print(f"User        - Roll 1: {user_one} \t| Roll 2: {user_two} \t| Total: {user_points} ")
print(f"Computer    - Roll 1: {comp_one} \t| Roll 2: {comp_two} \t| Total: {comp_points} ")

# Let the user know if they qualify for double points
if double_user == "yes":
    print("Great news - if you win, you will earn double points!")
