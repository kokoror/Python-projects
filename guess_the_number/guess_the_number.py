#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).


def set_difficulty():
  difficulty = input("Please choose a difficulty. Type 'easy' or 'hard'. ")
  if difficulty == 'easy':
    return 10
  else:
    return 5

def main():
  import random
  from art import logo
  
  print(logo)
  print("Welcome to the number-gussing game!")
  print("Guess a number between 1 - 100.")

  # difficulty = input("Choose a difficulty. Type 'easy' or 'hard'. ")

  # while difficulty != 'easy' and difficulty != 'hard':
  #   difficulty = input("Please choose a difficulty. Type 'easy' or 'hard'. ")

  # if difficulty == 'easy':
  #   attempt = 10
  # else:
  #   attempt = 5

  attempt = set_difficulty()


  print(f"You have {attempt} attempts remaining to guess the number.")
  guess = int(input("Make a guess: "))
  correct_number = random.randint(1, 100)


  while guess != correct_number and attempt != 1:
    if guess < correct_number:
      print("Too low")
    else:
      print("Too high")
    attempt -= 1
    print(f"You have {attempt} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))

  if guess == correct_number:
    print(f"You got it. The answer is {correct_number}")
  else:
    print(f"You have no attempts. You lose. Correct number is {correct_number}")   

main()
