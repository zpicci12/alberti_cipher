print("hello")
import sys 
import random

disk = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "I": 8, "J": 9, "K": 10, "L": 11, "M": 12, "N": 13, "O": 14, "P": 15, "Q": 16, "R": 17, "S": 18, "T": 19, "U": 20, "V": 21, "W": 22, "X": 23, "Y": 24, "Z": 25} #reference disk to store letters and their indexes, will be used to match up shifted letters

#function to shift letters 
  #input: start position uppercase letter
def shift_index(upper_disk_key, lower_disk_key):
  upper_disk_letters = list(disk.keys())
  upper_index = disk[upper_disk_key] 
  print(upper_index)
  lower_index = disk[lower_disk_key] 
  print(lower_index)
  shift_index = upper_index - lower_index 
  return shift_index

#function to match up letters after shift 
def shift_letter(shift_index, letter):
  shifted_letter_i = disk[letter] + shift_index 
  disk_letters = list(disk.keys())
  if shifted_letter_i > 25: 
    shifted_letter_i = shifted_letter_i % 26 
  if shifted_letter_i < 0: 
    shifted_letter_i = 26 + shifted_letter_i
  shifted_letter = disk_letters[shifted_letter_i]
  print(shifted_letter.lower())
  
#function to keep track of matching 
  #add uppercase letter to indicate new shift change 
  #determine new shift change with random number from 0-25

#testing shift_letter() and shift_index()
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

if __name__ == "__main__": 
text = sys.argv[1]
lower_disk_key = sys.argv[2]  #letter for start position (uppercase) (for the first shift, this will get matched with k because that's what Alberti did)
shift_interval = sys.argv[3] #interval at which shift setting changes (every n letters)   
'''
