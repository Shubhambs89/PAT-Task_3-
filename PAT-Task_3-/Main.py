# 1. Guess the Number 

import random
number = random.randint(1, 100)
print(number)
attepts = 0

print ("Welcome to the Guess the Number Game!");
while True:
    guess = int(input("Enter your guess: "))
    attepts += 1
    
    if guess < number:
        print("Too low! Try again.")
    elif guess > number:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You've guessed the number {number} in {attepts} attempts.")
        break

# 2. Word Scramble 
import random 

words =['python','javascript','java','automation','pytest','guvi','selenium']
word = random.choice(words)

Jumbled_word = ''.join(random.sample(word, len(word)))

print('The Jumble word is :',Jumbled_word)

guess = None
num_guesses=0

while guess != word:
    guess = input("Enter yuor Guess:")
    num_guesses += 1

    if guess == word:
        print("Your guessed word is correct")
    else:
        print('Incorrect try again')
print("thanks for playing")