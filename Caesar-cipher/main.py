from art import logo
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# define caesar function
def caesar(plain_text, shift_amount, direction_input):
    cipher_text = ""
    for char in plain_text:
      if char >= "a" and char <= "z":
        position = alphabet.index(char)

        if direction_input == "encode":
          new_position = position + shift_amount
        elif direction_input == "decode":
          new_position = position - shift_amount
        else:
          print("wrong direction")
          return

        if new_position > 25 or new_position < 0:
          new_position = new_position % 26

        cipher_text += alphabet[new_position]

      else:
        cipher_text += char

    print(f"The {direction_input}d text is {cipher_text}")

# the above function combines the below both

# def encrypt(plain_text, shift_amount):
#   cipher_text = ""
#   for letter in plain_text:
#     position = alphabet.index(letter)
#     new_position = position + shift_amount
#     cipher_text += alphabet[new_position]
#   print(f"The encoded text is {cipher_text}")

# def decrypt(cipher_text, shift_amount):
#   plain_text = ""
#   for letter in cipher_text:
#     position = alphabet.index(letter)
#     new_position = position - shift_amount
#     plain_text += alphabet[new_position]
#   print(f"The decoded text is {plain_text}")

# if direction == "encode":
#   encrypt(plain_text=text, shift_amount=shift)
# elif direction == "decode":
#   decrypt(cipher_text=text, shift_amount=shift)


def main():
  keep_play = True

  while keep_play:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    #TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 
    caesar(text, shift, direction)
    keep_play_option = input("Continue to play?").lower()
    if keep_play_option == "no":
      keep_play = False
      print("Goodbye!")

if __name__ == "__main__":
  main()
