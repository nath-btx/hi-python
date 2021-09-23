import random



moves=['rock','paper','scissors']

def convert_input(move):
    if (move == "r"): return 'rock'
    elif(move == "p"): return 'paper'
    elif(move == "s"): return 'scissors'
    else: return move

def game():
    tie = True
    while tie:
        tie = False
        AI_move = random.choice(moves)
        move = convert_input(input('Do you want to play Rock, Paper, or Scissors (r or rock / p or paper / s or Scissors)'))
        convert_input(move)
        if (move == AI_move): 
            tie = True
            print(f"You both played {move}, it's a tie !")

        elif(move == "r" or move == "rock"):
            if(AI_move == "scissors"): print("Rock > Scissors, you win !")
            else: print("Rocks < Paper, you lose !")

        elif(move == "p" or move == "paper"):
            if(AI_move == "rock"): print("Paper > Rock, you win !")
            else: print("Paper < Scissors, you lose !")

        elif(move == "s" or move == "scissors"):
            if(AI_move == "paper"): print("Scissors > Paper, you win !")
            else: print("Scissors < Rock, you lose !")

        else: 
            tie = True
            print("Please select a valid input")


if __name__ == "__main__":
    while True:
        game()
        play_again = input("Do you want to play again ? (y/n)")
        if(play_again == "y"):continue
        else: exit()
