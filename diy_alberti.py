#DIY Alberti cipher: create your own inner disk and encode messages 
#take inputs to fill each slot of inner disk
#store in dictionary
#same encode process as main.py
import sys 
import random

outer_disk = {
    "A": 0,
    "B": 1,
    "C": 2,
    "D": 3,
    "E": 4,
    "F": 5,
    "G": 6,
    "H": 7,
    "I": 8,
    "J": 9,
    "K": 10,
    "L": 11,
    "M": 12,
    "N": 13,
    "O": 14,
    "P": 15,
    "Q": 16,
    "R": 17,
    "S": 18,
    "T": 19,
    "U": 20,
    "V": 21,
    "W": 22,
    "X": 23,
    "Y": 24,
    "Z": 25
}  #reference disk to store letters and their indexes, will be used to match up shifted letters

#function to determine amount to shift disk
#input: start position uppercase letter
def shift_index(outer_disk_key, inner_disk_key, inner_disk):
    outer_index = outer_disk[outer_disk_key]
    inner_index = inner_disk[inner_disk_key.lower()] 
    shift_i = inner_index - outer_index
    return shift_i

#function to match up letters after shift; match outside disk (plaintext letter) to inside disk (ciphertext letter)
def encode_letter(shift_index, letter, inner_disk):
    shifted_letter_i = outer_disk[letter.upper()] + shift_index #maybe just disk and not inner?
    inner_disk_letters = list(inner_disk.keys())
    if shifted_letter_i > 25:
        shifted_letter_i = shifted_letter_i % 26
    if shifted_letter_i < 0:
        shifted_letter_i = 26 + shifted_letter_i
    shifted_letter = inner_disk_letters[shifted_letter_i]
    return (shifted_letter.lower())

def decode_letter(shift_index, letter, inner_disk):
    shifted_letter_i = inner_disk[letter.lower()] - shift_index
    outer_disk_letters = list(outer_disk.keys())
    if shifted_letter_i > 25:
        shifted_letter_i = shifted_letter_i % 26
    if shifted_letter_i < 0:
        shifted_letter_i = 26 + shifted_letter_i
    shifted_letter = outer_disk_letters[shifted_letter_i]
    return(shifted_letter.lower())

#function to choose a random letter and shift the disk
def encode_shift(outer_disk_key, inner_disk): 
  randNum = random.randint(0, 25)
  inner_disk_letters = list(inner_disk.keys())
  inner_disk_key = inner_disk_letters[randNum]
  print("The inner disk key is: " + inner_disk_key)
  shift_num = shift_index(outer_disk_key, inner_disk_letters[randNum], inner_disk)
  return(inner_disk_key, shift_num)

def decode_shift(outer_disk_key, inner_disk_key): 
  shift_num = shift_index(outer_disk_key, inner_disk_key, inner_disk)
  return(shift_num)

#decode plaintext
#add uppercase letter to indicate new shift change
#determine new shift change with random number from 0-25
def encode(text, outer_disk_key, period_length, inner_disk):
  print("----------------\nStarting! \nYour plaintext is: " + text + "\nThe outer disk key is: " + outer_disk_key + "\n----------------")
    #text = text.replace(" ", "")  #delete all whitespace 
  cipher = ""
  num = 0 #position of letter to recognize when to shift
  for letter in text:
    if num == 0 or num == period_length: #the disk needs to be shifted
        num = 0
        print("Beginning new shift. The cipher is currently: " + cipher)
        inner_disk_key, shift_num = encode_shift(outer_disk_key, inner_disk) #begin new shift
        print("Encoding in progress...")
        cipher += inner_disk_key.upper() #start each shift with the key of the shift
    cipher += encode_letter(shift_num, letter, inner_disk)
    num += 1
  print("--------------- \nFINAL CIPHER: " + cipher)

#decode ciphertext
def decode(text, outer_disk_key, period_length, inner_disk): 
  print("----------------\nStarting! \nYour ciphertext is: " + text + "\nThe outer disk key is: " + outer_disk_key + "\n----------------")
  plain_txt = ""
  n = 0  
  for letter in text: 
    if n == 0:
      print(letter + " is the start of a shift. The plaintext is currently: " + plain_txt)
      print("Decoding in progress...")
      shift_num = decode_shift(outer_disk_key, letter)
      n += 1
      continue
    if n == period_length + 1: 
      n = 0 
      print(letter + " is the start of a shift. The plaintext is currently: " + plain_txt)
      print("Decoding in progress...")
      shift_num = decode_shift(outer_disk_key, letter)
      n += 1
      continue
    plain_txt += decode_letter(shift_num, letter,inner_disk)
    n += 1
  print("--------------- \nFINAL PLAINTEXT: " + plain_txt)

def create_inner_disk():
  print("Step 1: create your inner disk! \n*Must be single-character slots, and no slot can be the same.* \n---------------- ")
  inner_disk = {} #inner disk to be created by user
  for i in range (0, 26):
    if i == 0 or i == 20:
      slot = input(str(i + 1) + "st slot character: ")
      slot = slot.lower() 
    elif i == 1 or i == 21:
      slot = input(str(i + 1) + "nd slot character: ")
      slot = slot.lower() 
    elif i == 2 or i == 22:
      slot = input(str(i + 1) + "rd slot character: ")
      slot = slot.lower() 
    else: 
      slot = input(str(i + 1) + "th slot character: ")
      slot = slot.lower() 
    while len(slot) != 1 or (slot in inner_disk) or (slot == ""):
      if len(slot) != 1:
        slot = input("You can only input one character per slot. Please try again: ")
      if slot in inner_disk: 
        slot = input("Repeat character. Please try again: ")
      if slot == "":
        slot = input("Blank slot. Please try again: ")
    inner_disk[slot] = i
  print("----------------\nYour inner disk is:")
  for i in range(0, 26):
    inner_disk_keys = list(inner_disk.keys())
    if i == 25:
      print(inner_disk_keys[i] + "\n----------------")
    else: 
      print(inner_disk_keys[i] + ", ", end="")
  return inner_disk  

def take_inputs(inner_disk):
  method = input("encode or decode? Type one: ")
  while method != 'encode' and method != 'decode':
     method = input("Invalid method type. Please incidate \"encode\" or \"decode\": ")
  if method == 'encode': 
    text = input("Insert plaintext: ")
  elif method == 'decode':
    text = input("Insert ciphertext: ") 
  outer_disk_key = input("Insert outer disk key: ").upper()
  while outer_disk_key not in outer_disk: 
    outer_disk_key = input("Outer disk key must be a letter. Please try again: ").upper()
  period_length = int(input("Insert period length: "))
  if method == "encode":
    encode(text.replace(" ", ""), outer_disk_key, period_length, inner_disk)
  elif method == "decode":
    decode(text, outer_disk_key, period_length, inner_disk)
if __name__ == "__main__":
  print("DIY ALBERTI CIPHER       \n~~~~~~~~~~~~~~~~~~")
  inner_disk = create_inner_disk()
  take_inputs(inner_disk)
  repeat = input("----------------\nWould you like to encode or decode something else? (y/n) ") 
  while repeat == "y":
    take_inputs(inner_disk)
    repeat = input("----------------\nWould you like to encode or decode something else? (y/n) ") 
  if repeat == "n":
    print("\nCongrats, you used your own Alberti cipher! Hope you had fun!")

