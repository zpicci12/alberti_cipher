print("hello")
import sys 
import random

lower_disk = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7, "i": 8, "j": 9, "k": 10, "l": 11, "m": 12, "n": 13, "o": 14, "p": 15, "q": 16, "r": 17, "s": 18, "t": 19, "u": 20, "v": 21, "w": 22, "x": 23, "y": 24, "z": 25} #reference disk to store letters and their indexes, will be used to match up shifted letters

#function to shift letters 
  #input: start position uppercase letter, 

#function to match up letters after shift 

#function to keep track of matching 
  #add lowercase letter after each shift change (use random number from 0-25 to determine which letter will match up with the uppercase letter)


if __name__ == "__main__": 
text = sys.argv[1]
lower_disk_key = sys.argv[2]  #letter for start position (uppercase) (for the first shift, this will get matched with k because that's what Alberti did)
shift_interval = sys.argv[3] #interval at which shift setting changes (every n letters)   

