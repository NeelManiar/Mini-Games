import random
import datetime
with open('wordlist.txt', 'r') as n:
    words = n.readlines()

word = random.choice(words)[:-1]
allowed_errors = 7
guesses = []
done = False

while not done:
    for letter in word:
        if letter.lower() in guesses:
            print(letter, end=" ")
        else:
            print("_", end=" ")
    print("")

    time = datetime.datetime.now().second
    i = 60
    t = 60 - time
    guess = input(f'Allowed Errors Left {allowed_errors}, Guess: ')
    guesses.append(guess.lower())
    if guess.lower() not in word.lower():
        allowed_errors -= 1
        if time == 0:
            print('Time Up')
        if allowed_errors == 0:
            break
    done = True
    for letter in word:
        if letter.lower() not in guesses:
            done = False
if done:
    print(f'You found the word! It was {word}!!')
else:
    print(f'Game Over! The word was {word}!!')