import random

def play():
    user = input('What is your choice? "r" for rock, "p" for paper, "s" for scissor\n')
    user = user.lower()

    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'You and the computer have both chosen {}. It is a tie.'.format(computer)

    if is_win(user, computer):
        return "You have chosen {} and the computer has chosen {}. You won".format(UserWarning, computer)
    return "You have chosen {} and the computer has chosen {}. You lost :(".format(user, computer)
def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True

if __name__ == '__main__':
    print(play())
