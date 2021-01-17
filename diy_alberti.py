#DIY Alberti cipher: create your own inner disk and encode messages 
#take inputs to fill each slot of inner disk
#store in dictionary
#same encode process as main.py
import sys 

if __name__ == "__main__":
  print("Create your inner disk!")
  inner_disk = {} #inner disk to be created by user
  for i in range (0, 26):
    if i == 0 or i == 20:
      slot = input(str(i + 1) + "st character: ") 
    elif i == 1 or i == 21:
      slot = input(str(i + 1) + "nd character: ")
    elif i == 2 or i == 22:
      slot = input(str(i + 1) + "rd character: ")
    else: 
      slot = input(str(i + 1) + "th character: ")
    while slot == "":
      slot = input("Please try again: ") 
    inner_disk[slot] = i
  print(inner_disk)


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

