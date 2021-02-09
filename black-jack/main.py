#to fix: handle 11 or 1.
#solution: define a function calculate_score()

#to fix: winner reveal when win with 2 cards
# lesson learnt:  if you need to call any functions in the main, those functions need parameters so that the varibles in the main() can be passed in as argument.

import random
from replit import clear
from art import logo

#function to draw one random card from list card and append to the chosen player's list 
def draw_one_card(which_player):
  '''
  parameter: list (computer or user)
  do: append a random card to the list
  '''
  cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
  random_card = random.choice(cards)
  which_player.append(random_card)

#function to calculate scores and handle 1 and 11 situation
def calculate_score(which_player):
  if 11 in which_player and sum(which_player) > 21:
    which_player.remove(11)
    which_player.append(1)
  return sum(which_player)

#function to reveal the final results
def reveal_final_result(user, computer):
  print(f"your cards: {user}, current scores: {calculate_score(user)}")
  print(f"computer's final hand: {computer}, current score {calculate_score(computer)}")

def reveal_result(user, computer):
  print(f"your cards: {user}, current scores: {calculate_score(user)}")
  print(f"Computer's first card: {computer[0]}")


def compare_scores(user_score, computer_score):
  if computer_score == user_score:
    print("Your score is equal to computer. Draw!")
  elif user_score == 21:
    print("you win with a Black Jack!")
  elif computer_score == 21:
    print("you lose. Computer has a Black Jack!")
  elif user_score > 21:
    print("you went over, you lose")
  #user choose to not draw more
  elif computer_score > 21:
    print("computer went over, you win")
  elif computer_score < user_score:
    print("Your score is greater than computer, you win!")
  else:

    print("Your score is less than computer, you lose.")


def main():
  play_game = input("Do you want to play Black Jack? Type 'y' or 'n': ")

  if play_game == 'y':

    user_hand =[]
    computer_hand = []


    #draw two cards for user and computer 
    draw_one_card(user_hand)
    draw_one_card(user_hand)
    draw_one_card(computer_hand)
    draw_one_card(computer_hand)
    
    clear()
    print(logo)

    reveal_result(user_hand, computer_hand)
    
    computer_score = calculate_score(computer_hand)
    user_score = calculate_score(user_hand)

    # draw card for computer if its total score is less than 1
    while user_score !=21 and computer_score < 17:
      draw_one_card(computer_hand)
      #important!!!!!! update computer_score to reflect the change!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
      computer_score = calculate_score(computer_hand)
      
    
    while computer_score !=21 and user_score < 21:
      continue_draw = input("Type 'y' to get another card, 'n' to pass: ")
      if continue_draw == 'y':#user choose to draw more
        draw_one_card(user_hand)
        #important!!!!!! update user_score to reflect the change!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        user_score = calculate_score(user_hand)
        reveal_result(user_hand, computer_hand)
      else: 
        break
    
    reveal_final_result(user_hand, computer_hand)
    compare_scores(user_score, computer_score)

    #when game finishes, restart main()
    main()


if __name__ == "__main__":
  main()
    




