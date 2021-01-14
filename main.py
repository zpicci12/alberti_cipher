import sys 
import random

disk = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "I": 8, "J": 9, "K": 10, "L": 11, "M": 12, "N": 13, "O": 14, "P": 15, "Q": 16, "R": 17, "S": 18, "T": 19, "U": 20, "V": 21, "W": 22, "X": 23, "Y": 24, "Z": 25} #reference disk to store letters and their indexes, will be used to match up shifted letters

numToChar = {0: "A", 1: "B", 2: "C", 3: "D", 4: "E", 5: "F", 6: "G", 7: "H", 8: "I", 9: "J", 10: "K", 11: "L", 12: "M", 13: "N", 14: "O", 15: "P", 16: "Q", 17: "R", 18: "S", 19: "T", 20: "U", 21: "V", 22: "W", 23: "X", 24: "Y", 25: "Z"}

#function to shift letters 
  #input: start position uppercase letter
def shift_index(outer_disk_key, inner_disk_key):
  outer_disk_letters = list(disk.keys())
  outer_index = disk[outer_disk_key] 
  inner_index = disk[inner_disk_key] 
  shift_i = inner_index - outer_index
  return shift_i

print(shift_index("S", "K"))
#function to match up letters after shift 
def shift_letter(shift_index, letter):
  shifted_letter_i = disk[letter] + shift_index 
  disk_letters = list(disk.keys())
  if shifted_letter_i > 25: 
    shifted_letter_i = shifted_letter_i % 26 
  if shifted_letter_i < 0: 
    shifted_letter_i = 26 + shifted_letter_i
  shifted_letter = disk_letters[shifted_letter_i]
  return(shifted_letter.lower())
  
#function to keep track of matching 
  #add uppercase letter to indicate new shift change 
  #determine new shift change with random number from 0-25
def begin(text, period_length, outer_disk_key): #once completed, add shift_interval and randomize new shifts and delete spaces from words! 
#find shift_index using k (Alberti's starting place): 
  text = text.replace(" ", "") #delete all whitespace
  shift_num = shift_index(outer_disk_key, "K") #note: make lowercase eventually
  cipher = "K" #start each shift with the key of the shift
  num = 0 #position of letter to recognize when to shift
  for letter in text:
    #if letter != " ":
    if num != period_length:
      cipher += shift_letter(shift_num, letter.upper())
      num += 1
    else: #if num = period_length
      randNum = random.randint(0, 24) #don't include 25 because that wouldn't shift it
      #shift_num = shift_index(numToChar.get(randNum), outer_disk_key)
      shift_num = shift_index(outer_disk_key, "L")
      cipher += shift_letter(shift_num, letter.upper())
  print(cipher)

#random testing: 
begin("hello world", 5, "S")

#python3 alphatext period_length key_letter
  #period_length = after period_length letters, shift
  #key_letter = the outer disk's letter that will match with every shift

''''
shift_index = shift_index("K", "S")
shift_letter(shift_index, "H")
shift_letter(shift_index, "E")
shift_letter(shift_index, "L")
shift_letter(shift_index, "L")
shift_letter(shift_index, "O")
shift_letter(shift_index, "W")
shift_letter(shift_index, "O")
shift_letter(shift_index, "R")
shift_letter(shift_index, "L")
shift_letter(shift_index, "D")

'''
'''
if __name__ == "__main__": 
text = sys.argv[1]
lower_disk_key = sys.argv[2]  #letter for start position (uppercase) (for the first shift, this will get matched with k because that's what Alberti did)
shift_interval = sys.argv[3] #interval at which shift setting changes (every n letters)   
'''
