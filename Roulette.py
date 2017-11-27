bet_amount = 1
reds = "Red,"*18
reds = reds[:-1] #removes the ',' for the list conversion
red_list = reds.split(',')

black = "Black,"*18
black = black[:-1]
black_list = black.split(',')

zero = ["0"]
zeros = ["0","0"]
values_norm = zero + red_list + black_list
values_double = zeros + red_list + black_list
rounds = 1000
zero_choice = input("Single zero or double zero? (single or double)")

#bringing in random
import random
#guess = "Red"
#guess = "Black"
guess = "random"

lost = 0
won = 0
count = 0
while True:
    if zero_choice == "single":
        answer = random.randint(0, 36)
        repeat = "no"
        if guess == "random":
            pull_guess = random.randint(0, 36)
            guess = values_norm[pull_guess]
            repeat = "yes"
            print("Your guess: " + guess + "\n")
        else:
            print("Your guess: " + guess + "\n")
        print("Roulette wheel: " + values_norm[answer])
        if values_norm[answer] == guess:
            print('You win $' + str(bet_amount) + ' dollar(s)!')
            won = won + bet_amount
        else:
            print('You lose $' + str(bet_amount) + ' dollar(s).')
            lost = lost + bet_amount
        count+=1
        if repeat == "yes":
            guess = "random"
        else:
            guess = guess
        if count >= rounds:
            print("\nYou won $" + str(won) + " dollars after " + str(rounds) + " rounds however, you lost $" + str(lost)
                  + " dollars after " + str(rounds) + " rounds.")
            winnings = won - lost
            print("So you won a total of $" + str(winnings) + "!")
            break
    else:
        answer = random.randint(0, 37)
        repeat = "no"
        if guess == "random":
            pull_guess = random.randint(0, 37)
            guess = values_double[pull_guess]
            repeat = "yes"
            print("Your guess: " + guess + "\n")
        else:
            print("Your guess: " + guess + "\n")
        print("Roulette wheel: " + values_double[answer] + "\n")
        if values_double[answer] == guess:
            print('You win $' + str(bet_amount) + ' dollar(s)!')
            won = won + bet_amount
        else:
            print('You lose $' + str(bet_amount) + ' dollar(s).')
            lost = lost + bet_amount
        count+=1
        if repeat == "yes":
            guess = "random"
        else:
            guess = guess
        if count >= rounds:
            print("\nYou won $" + str(won) + " dollars after " + str(rounds) + " rounds however, you lost $" + str(lost)
                  + " dollars after " + str(rounds) + " rounds.")
            winnings = won - lost
            print("So you won a total of $" + str(winnings) + "!")
            break

Simulations for 5 rounds:
    single 0:
        Red: You won $3 dollars after 5 rounds however, you lost $2 dollars after 5 rounds.
            So you won a total of $1!

        Black: You won $4 dollars after 5 rounds however, you lost $1 dollars after 5 rounds.
            So you won a total of $3!

        Random:You won $4 dollars after 5 rounds however, you lost $1 dollars after 5 rounds.
                So you won a total of $3!

    double 0:
        Red: You won $2 dollars after 5 rounds however, you lost $3 dollars after 5 rounds.
            So you won a total of $-1!

        Black: You won $1 dollars after 5 rounds however, you lost $4 dollars after 5 rounds.
                So you won a total of $-3!

        Random:You won $3 dollars after 5 rounds however, you lost $2 dollars after 5 rounds.
                So you won a total of $1!

Simulations for 100 rounds:
    single 0:
        Red: You won $49 dollars after 100 rounds however, you lost $51 dollars after 100 rounds.
                So you won a total of $-2!

        Black:You won $50 dollars after 100 rounds however, you lost $50 dollars after 100 rounds.
                So you won a total of $0!

        Random:You won $46 dollars after 100 rounds however, you lost $54 dollars after 100 rounds.
                    So you won a total of $-8!

    double 0:
        Red: You won $47 dollars after 100 rounds however, you lost $53 dollars after 100 rounds.
                So you won a total of $-6!

        Black:You won $45 dollars after 100 rounds however, you lost $55 dollars after 100 rounds.
                So you won a total of $-10!

        Random: You won $48 dollars after 100 rounds however, you lost $52 dollars after 100 rounds.
                So you won a total of $-4!

Simulations for 1000 rounds:
    single 0:
        Red: You won $518 dollars after 1000 rounds however, you lost $482 dollars after 1000 rounds.
                So you won a total of $36!

        Black:You won $499 dollars after 1000 rounds however, you lost $501 dollars after 1000 rounds.
                So you won a total of $-2!

        Random:You won $452 dollars after 1000 rounds however, you lost $548 dollars after 1000 rounds.
                    So you won a total of $-96!

    double 0:
        Red: You won $501 dollars after 1000 rounds however, you lost $499 dollars after 1000 rounds.
                So you won a total of $2!

        Black:You won $455 dollars after 1000 rounds however, you lost $545 dollars after 1000 rounds.
                So you won a total of $-90!

        Random:You won $447 dollars after 1000 rounds however, you lost $553 dollars after 1000 rounds.
                So you won a total of $-106!