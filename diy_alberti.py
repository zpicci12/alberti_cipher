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
def shift_index(outer_disk_key, inner_disk_key):
    outer_index = disk[outer_disk_key]
    inner_index = disk[inner_disk_key]
    shift_i = inner_index - outer_index
    return shift_i

#function to match up letters after shift; match outside disk (plaintext letter) to inside disk (ciphertext letter)
def encode_letter(shift_index, letter):
    shifted_letter_i = disk[letter] + shift_index
    disk_letters = list(disk.keys())
    if shifted_letter_i > 25:
        shifted_letter_i = shifted_letter_i % 26
    if shifted_letter_i < 0:
        shifted_letter_i = 26 + shifted_letter_i
    shifted_letter = disk_letters[shifted_letter_i]
    return (shifted_letter.lower())

#function to choose a random letter and shift the disk
def encode_shift(outer_disk_key): 
  randNum = random.randint(0, 25)
  disk_letters = list(disk.keys())
  inner_disk_key = disk_letters[randNum]
  print("The inner disk key is: " + inner_disk_key)
  shift_num = shift_index(outer_disk_key, disk_letters[randNum])
  return(inner_disk_key, shift_num)

#decode plaintext
#add uppercase letter to indicate new shift change
#determine new shift change with random number from 0-25
def encode(text, outer_disk_key, period_length):
  print("Starting! \nYour plaintext is: " + text + "\nThe outer disk key is: " + outer_disk_key + "\n----------------")
    #text = text.replace(" ", "")  #delete all whitespace 
  cipher = ""
  num = 0 #position of letter to recognize when to shift
  for letter in text:
    if num == 0 or num == period_length: #the disk needs to be shifted
        num = 0
        print("Beginning new shift. The cipher is currently: " + cipher)
        inner_disk_key, shift_num = encode_shift(outer_disk_key) #begin new shift
        print("Encoding in progress...")
        cipher += inner_disk_key #start each shift with the key of the shift
    cipher += encode_letter(shift_num, letter.upper())
    num += 1
  print("--------------- \nFINAL CIPHER: " + cipher)

def create_inner_disk():
  print("Create your inner disk! \n*Must be single-character slots and no slot must be the same.* \n---------------- ")
  inner_disk = {} #inner disk to be created by user
  for i in range (0, 26):
    if i == 0 or i == 20:
      slot = input(str(i + 1) + "st slot character: ") 
    elif i == 1 or i == 21:
      slot = input(str(i + 1) + "nd slot character: ")
    elif i == 2 or i == 22:
      slot = input(str(i + 1) + "rd slot character: ")
    else: 
      slot = input(str(i + 1) + "th slot character: ")
    while slot == "":
      slot = input("Blank slot. Please try again: ")
    while slot in inner_disk: 
      slot = input("Repeat character. Please try again: ")
    inner_disk[slot] = i
  print("----------------\nYour inner disk is:")
  for i in range(0, 26):
    inner_disk_keys = list(inner_disk.keys())
    if i == 25:
      print(inner_disk_keys[i] + "\n----------------")
    else: 
      print(inner_disk_keys[i] + ", ", end="")  

if __name__ == "__main__":
  inner_disk = create_inner_disk()
  method = input("encode or decode? Type one: ")
  if method == "encode": 
    text = input("Insert plaintext: ")
  elif method == "decode":
    text = input("Insert plaintext: ")
  else:  
    method = input("Invalid method type. Please incidate \"encode\" or \"decode\": ")
  outer_disk_key = input("Insert outer disk key: ").upper()
  period_length = int(input("Insert period length: "))
  while period_length > len(text):
    period_length = input("Period length is longer than text length. Please try again.")
  if method == "encode":
     encode(text, outer_disk_key, period_length)
  