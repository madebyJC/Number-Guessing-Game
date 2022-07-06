import random
from time import sleep
from art import logo_1, logo_2
from replit import clear


#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
sleep(1)
print(logo_1)
sleep(2)
print(logo_2)

numbers = []
print("Welcome to the Number Guessing Game!")

for n in range(1, 101):
  numbers.append(n)

random_num = random.choice(numbers)

def check(num):
  if player_guess < random_num:
    return "low"
  elif player_guess > random_num:
    return "high"
  elif player_guess == random_num:
    return "win"

def easy():
  print(random_num)
  sleep(1)
  print(logo_1)
  sleep(2)
  print(logo_2)
  player_life = 10
  easy_game_end = True
  while easy_game_end == True:
    global player_guess
    print(f"You have {player_life} attempts remaining to guess the number.")
    player_guess = int(input("Make a guess: "))
    result_easy = check(num=player_guess)
    if result_easy == "low" or result_easy == "high":
      player_life -= 1
      print(result_easy)
      if player_life == 0:
        easy_game_end = False
        print("You have run out of guesses, you lose.")
    elif result_easy == "win":
      print(f"You got it! The answer was {random_num}")
      easy_game_end = False
    else: 
      None

def hard():
  print(random_num)
  sleep(1)
  print(logo_1)
  sleep(2)
  print(logo_2)
  player_life = 5
  hard_game_end = True
  while hard_game_end == True:
    global player_guess
    print(f"You have {player_life} attempts remaining to guess the number.")
    player_guess = int(input("Make a guess: "))
    result_easy = check(num=player_guess)
    if result_easy == "low" or result_easy == "high":
      player_life -= 1
      print(result_easy)
      if player_life == 0:
        hard_game_end = False
        print("You have run out of guesses, you lose.")
    elif result_easy == "win":
      print(f"You got it! The answer was {random_num}")
      hard_game_end = False
    else: 
      None

  
player_difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
if player_difficulty == "easy":
  clear()
  easy()
  easy_game_end = True
elif player_difficulty == "hard":
  clear()
  hard()
  hard_game_end = True
else:
  clear()
  print("Invalid")

