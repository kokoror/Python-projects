from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.

print(logo)
print("Welcome to the secret auction program.")
auction_dictoionary = {}
keep_enter = True

while keep_enter == True:
  name = input("What is your name? ")
  bid = int(input("What is your bid? $"))
  auction_dictoionary[name] = bid

  keep_enter_message = input("Are there other bidders? Type 'yes' or 'no'.").lower()
  if keep_enter_message == "no":
    keep_enter = False
  clear() #clear the screen

print(auction_dictoionary)

# the below can be written in a function

winner_name = ""
winner_bid = 0

for person in auction_dictoionary:
  if auction_dictoionary[person] > winner_bid:
    winner_name = person
    winner_bid = auction_dictoionary[person] 

print(f"The winner is {winner_name} with a bit of ${winner_bid}.")
   





