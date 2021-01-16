import sys
import random

disk = {
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
    outer_disk_letters = list(disk.keys())
    outer_index = disk[outer_disk_key]
    inner_index = disk[inner_disk_key]
    shift_i = inner_index - outer_index
    return shift_i

#function to match up letters after shift
def shift_letter(shift_index, letter):
    shifted_letter_i = disk[letter] + shift_index
    disk_letters = list(disk.keys())
    if shifted_letter_i > 25:
        shifted_letter_i = shifted_letter_i % 26
    if shifted_letter_i < 0:
        shifted_letter_i = 26 + shifted_letter_i
    shifted_letter = disk_letters[shifted_letter_i]
    return (shifted_letter.lower())

#function to choose a random letter and shift the disk
def shift(outer_disk_key): 
  randNum = random.randint(0, 25)
  disk_letters = list(disk.keys())
  inner_disk_key = disk_letters[randNum]
  print("The inner disk key is: " + inner_disk_key)
  shift_num = shift_index(outer_disk_key, disk_letters[randNum])
  return(inner_disk_key, shift_num)


#function to keep track of matching
#add uppercase letter to indicate new shift change
#determine new shift change with random number from 0-25
def begin(text, outer_disk_key, period_length):
  print("Starting! \nYour text is: " + text + "\nThe outer disk key is: " + str(outer_disk_key) + "\n----------------")
    #text = text.replace(" ", "")  #delete all whitespace 
  cipher = ""
  num = 0 #position of letter to recognize when to shift
  for letter in text:
    if num == 0 or num == period_length: #the disk needs to be shifted
        print("Beginning new shift. the cipher is currently: " + cipher)
        inner_disk_key, shift_num = shift(outer_disk_key) #begin new shift
        print("Encoding in progress...")
        cipher += inner_disk_key #start each shift with the key of the shift
    cipher += shift_letter(shift_num, letter.upper())
    num += 1
  print("--------------- \nFINAL CIPHER: " + cipher)

#note: text must be ONE WORD (no whitespace), unless we changed it to a file input
if __name__ == "__main__": 
  text = sys.argv[1] #text to encode
  outer_disk_key = sys.argv[2].upper()  #letter for outer disk position (uppercase)
  period_length = sys.argv[3] #interval at which shift setting changes (every period_length letters) 
  begin(text, outer_disk_key, int(period_length))
