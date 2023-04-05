import random

def play():
    player = input("Rock(R), Paper(P), scissor (S) : ")
    computer = random.choice(['r','p','s'])

    if player == computer:
        print("Tie")

    if is_win(player, computer):
        print("Yow win")
    else:
        print("You lose")
        
#r > s , p > r, s > p


def is_win(player, computer):
    if (player == 'r' and computer == 's') or (player == 'p' and computer == 'r') or (player == 's' and computer == 'p'):
        return True
    else:
        return False

play()
