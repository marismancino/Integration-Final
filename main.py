# Maris Mancino
# First, you go to play mini golf with your friends
# Afterwards, you enter a bakery looking to buy some pastries
# import time and time.sleep() are used to delay the next time of code
# this allows for the user to have time to read
# https://www.geeksforgeeks.org/python-time-module/


# add parameters from golf to bakery-incorporate the two scenarios

import time


# allows for the predefined function 'time.sleep()' to be used
def greeting():
    """
    # function definition
    print("Hello and welcome to the Putt Palace Mini Golf!")
    # prints phrase inside of quotations
    time.sleep(1.5)
    # 1.5 second pause before next line is printed
    print("How many players are on your team?")
    time.sleep(1)
    # 1 second pause before next line is printed

def assign_players():
    # function definition
    players = int(input("number of players: "))
    # allows input for the number of players turns in into an integer
    print(players, ", great! What are the names of your players?")
    # prints the number inputted above with the phrase inside the quote
    for x in range(players):
        # for is used as a loop with a definite set of outputs
        # range() defines the amount of times the loop will run
        name = input("Player's name: ")
        # allows a name to be inputted
    print("Alright, here are your clubs and balls. There are", players, " of each.")
    # prints phrase inside of quotations and the number previously inputted
    time.sleep(1.5)
    # 1.5 second pause before next line is printed


def enter_bakery():
    # function definition
    print("Hello and welcome to the Maris' Munchies Bakery!")
    # prints phrase inside of quotations
    time.sleep(2)
    # 2 second pause before next line is printed
    print("Our menu today features cake, cookies, and macaroons.")
    # prints phrase inside of quotations
    time.sleep(1.5)
    # 1.5 second pause before next line is printed
    cake = "red velvet cakes"
    # assigns variable cake to the phrase inside the quotations
    cookies = "chocolate chip cookies"
    # assigns variable cookies to the phrase inside the quotations
    macaroons1 = "strawberry macaroons"
    # assigns variable macaroon1 to the phrase inside the quotations
    print("How many of each would you like?")
    # prints phrase inside of quotations
    time.sleep(2)
    # 2 second pause before next line is printed
    cake = int(input("number of " + cake + ": "))
    # allows for an input in the number of cakes
    # uses a + to combine phrase inside of quotes and the assigned variable
    # + concatenates two strings
    cookies = input("number of " + cookies + ": ")
    # allows for an input in the number of cookies
    # uses a + to combine phrase inside of quotes and the assigned variable
    macaroons1 = input("number of " + macaroons1 + ": ")
    # allows for an input in the number of cookies
    # uses a + to combine phrase inside of quotes and the assigned variable
    print("I will package those right up for you.")
    # prints phrase inside of quotations
    time.sleep(1.5)
    # 1.5 second pause before next line is printed
    num1 = int(cake)
    # assigns a new variable to the user entered number
    # number is from the previous input of the prior assigned variable, cake
    num2 = int(cookies)
    # assigns a new variable to the user entered number
    # number is from the previous input of the prior assigned variable, cookies
    num3 = int(macaroons1)
    # assigns a new variable to the user entered number
    # number is from previous input of the prior assigned variable, macaroons1
    cost1 = (num1 * 15.99)
    # assigns a new variable to represent the product
    # product is the previous variable multiplied by a number, representing cost
    # * multiplies the two values
    cost2 = (num2 * 1.99)
    # assigns a new variable to represent the product
    # product is the previous variable multiplied by a number, representing cost
    cost3 = (num3 * 0.99)
    # assigns a new variable to represent the product
    # product is the previous variable multiplied by a number, representing cost
    print("Okay, your prices today break down like this:")
    # prints phrase inside of quotations
    time.sleep(1.5)
    # 1.5 second pause before next line is printed
    print("The cakes cost $", format(cost1, '0.2f'), sep='')
    # prints phrase inside of quotations
    # formats the cost to round 2 decimal places
    # sep='' removes the space between the number and the dollar sign
    time.sleep(0.5)
    # 0.5 second pause before next line is printed
    print("The cookies cost $", format(cost2, '0.2f'), sep='')
    # prints phrase inside of quotations
    # formats the cost to round 2 decimal places
    # sep='' removes the space between the number and the dollar sign
    time.sleep(0.5)
    # 0.5 second pause before next line is printed
    print("The macaroons cost $", format(cost3, '0.2f'), sep='')
    # prints phrase inside of quotations
    # formats the cost to round 2 decimal places
    # sep='' removes the space between the number and the dollar sign
    time.sleep(0.5)
    # 0.5 second pause before next line is printed
    total1 = (cost1 + cost2 + cost3)
    # assigns a new variable to represent the addition of all 3 cost variables
    # + adds the values
    time.sleep(1)
    # 1 second pause before next line is printed
    print("Your total will be $", format(total1, '0.2f'), sep='')
    # prints phrase inside of quotations
    # formats the total to round 2 decimal places
    # sep='' removes the space between the number and the dollar sign
    total2 = (total1 - cost3)
    # assigns a new variable to remove the third cost from the total
    # - removes the value
    time.sleep(2)
    # 2 second pause before next line is printed
    print("I see, you don't want the macaroons anymore? ", end='')
    # prints phrase inside of quotations
    # end='' ends the output with a space
    print("Sure thing. Your new total is $", format(total2, '0.2f'), sep='')
    # prints phrase inside of quotations
    # formats the total to round 2 decimal places
    # sep='' removes the space between the number and the dollar sign
    time.sleep(3.5)
    # 3.5 second pause before next line is printed
    print("Can I offer you a different macaroon flavor? ", end='')
    # prints phrase inside of quotations
    # end='' ends the output with a space
    print("We also have pistachio and vanilla.")
    # prints phrase inside of quotations
    time.sleep(2)
    # 2 second pause before next line is printed
    macaroons2 = "pistachio macaroons"
    # assigns variable macaroons2 to the phrase inside of quotations
    macaroons3 = "vanilla macaroons"
    # assigns variable macaroons3 to the phrase inside of quotations
    macaroons2 = input("number of " + macaroons2 + ": ")
    # allows for an input in the number of cookies
    # uses a + to combine phrase inside of quotes and the assigned variable
    macaroons3 = input("number of " + macaroons3 + ": ")
    # allows for an input in the number of cookies
    # uses a + to combine phrase inside of quotes and the assigned variable
    num4 = int(macaroons2)
    # assigns a new variable to the user entered number
    # number is from the previous input of the prior assigned variable, macaroons2
    num5 = int(macaroons3)
    # assigns a new variable to the user entered number
    # number is from the previous input of the prior assigned variable, macaroons3
    cost4 = (num4 * 0.99)
    # assigns a new variable to represent the product
    # product is the previous variable multiplied by a number, representing cost
    cost5 = (num5 * 0.99)
    # assigns a new variable to represent the product
    # product is the previous variable multiplied by a number, representing cost
    total3 = (total2 + cost4 + cost5)
    # assigns a new variable to represent new total
    # addition of the previous total and 2 new cost variables

    if total3 > 100:
        # condition if the total is greater than 100
        # if statement allows for a conditional output based on the value of an expression
        # > greater than conditional operator
        total6 = (total3 * 0.85)
        # assigns a new variable to represent the product
        # product is the previous total by a number, representing a new total
        print("It's your lucky day! ", end='')
        # prints phrase inside of quotations
        # end='' ends the output with a space
        time.sleep(1)
        # 1 second pause before next line is printed
        print("Since you are spending more than $100, we will give you 15% off your order.")
        # print phrase inside of quotations
        time.sleep(2)
        # 2 second pause before next line is printed
        print("Your final total will be $", format(total6, '0.2f'), sep='')
        # prints phrase inside of quotations
        # formats the total to round 2 decimal places
        # sep='' removes the space between the number and the dollar sign
    elif total3 <= 100 or total3 > 30:
        # condition if the total is equal to or less than 100 but greater than 30
        # elif is a python keyword to test multiple options
        # <= less than or equal to conditional operator
        # or operator is a disjunction
        total5 = (total3 * 0.90)
        # assigns a new variable to represent the product
        # product is the previous total by a number, representing a new total
        print("It's your lucky day! ", end='')
        # prints phrase inside of quotations
        # end='' ends the output with a space
        time.sleep(1)
        # 1 second pause before next line is printed
        print("Since you are spending between $30-$100, we will give you 10% off your order.")
        # print phrase inside of quotations
        time.sleep(2)
        # 2 second pause before next line is printed
        print("Your final total will be $", format(total5, '0.2f'), sep='')
        # prints phrase inside of quotations
        # formats the cost to round 2 decimal places
        # sep='' removes the space between the number and the dollar sign
    elif total3 > 30:
        # condition if the total is greater than 30
        total4 = (total3 * 0.95)
        # assigns a new variable to represent the product
        # product is the previous total by a number, representing a new total
        print("It's your lucky day! ", end='')
        # prints phrase inside of quotations
        # end='' ends the output with a space
        time.sleep(1)
        # 1 second pause before next line is printed
        print("Since you are spending more than $30, we will give you 5% off your order.")
        # print phrase inside of quotations
        time.sleep(2)
        # 2 second pause before next line is printed
        print("Your final total will be $", format(total4, '0.2f'), sep='')
        # prints phrase inside of quotations
        # formats the cost to round 2 decimal places
        # sep='' removes the space between the number and the dollar sign
    else:
        # no conditions are met
        # else output if all other conditions fail
        print("Your final total will be $", format(total3, '0.2f'), sep='')
        # prints phrase inside of quotations
        # formats the cost to round 2 decimal places
        # sep='' removes the space between the number and the dollar sign
    time.sleep(2)
    # 2 second pause before next line is printed
    print("Cash or card?")
    # print phrase inside of quotations
    time.sleep(1)
    # 1 second pause before next line is printed
    print("Alright, you're all set! Have a great day!")
    # print phrase inside of quotations
    time.sleep(1.5)
    # 1.5 second pause before next line is printed


def demonstration():
    # function definition
    # extra operations not used in project
    firstNumber = input("Enter a number: ")
    # allows for input and assigns it to a variable
    secondNumber = input("Enter another number: ")
    # allows for input and assigns it to a variable
    num1 = int(firstNumber)
    # makes the input an integer and reassigns the variable
    num2 = int(secondNumber)
    # makes the input an integer and reassigns the variable
    division = num1 / num2
    # divides the two numbers
    # / division operator
    power = num1 ** num2
    # put the first number to the power of the second number
    # ** power operator
    num1 *= num2
    # *= power shortcut operator
    floor = num1 // num2
    # // floor division rounds to a whole number
    modulus = num1 % num2
    # % modulus operation returns the remainder
    num1 += num2
    # += addition shortcut operator
    num1 -= num2
    # -= subtraction shortcut operator
    num1 == num2
    # == equal to shortcut operator
    num1 != num2
    # != not equal to shortcut operator
    print("First, divide the two numbers: ", division)
    # prints phrase inside of quotations
    # adds division variable
    print("Then, put the first number to the power of the second number: ", power)
    # prints phrase inside of quotations
    # adds power variable
    print("Next, floor divide the first number to the second number: ", floor)
    # prints phrase inside of quotations
    # adds floor variable
    print("Finally, modulus the first number to the second number: ", modulus)
    # prints phrase inside of quotations
    # adds modulus variable
    print("Puppy" * 5)
    # prints phrase inside of quotations as many times as the value of the number
    # * in a string prints the word that many times
    number = 11
    # assigns variable to equal 11
    while number <= 10:
    # condition if number is less than or equal to 10
        print(number)
        #prints variable
        number = number + 1
        # adds one to variable
    # while loop allows for a block of code to be repeated multiple times

    (age >= 18) and (can_vote)
    # and operator is a conjunction
    not (credits > 120)
    # not operator is a negation

    number = int(input("Enter a number: ")
    x=1
    while (x <= number):
    # parameter passing
        if(x% 10 == 0):
            print(x)
        else:
            print(x, end=" ")
        x = x + 1


def main():
# function definition
    greeting()
    assign_players()
    enter_bakery()
    demonstration()

main()
# call to all function definitions
# call to main
"""